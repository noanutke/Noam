

import time
import numpy as np
from sklearn import datasets, linear_model
import pandas
import openpyxl
import utils

TCP_IP = "192.168.0.1"
TCP_PORT = 20121


class Calibration:
    log_path_preffix = 'calibrationLog_'
    log_path_suffix = '.xlsx'
    sheet_name = 'CalibrationArray'
    trials_amount = 6;
    test_index = 0;
    current_VAS = -1;
    initial_tmp_array = [39.0,42.0,46.0]
    amount_of_initial_trials = 3;

    def __init__(self, subId):
        self.log_path = self.log_path_preffix + subId + self.log_path_suffix;
        self.tmp_array = np.array([])
        self.rating_array = np.array([])

    def round_of_rating(self, number):
        return round(number * 2) / 2

    def runVAS(self, x):
        if self.test_index < self.amount_of_initial_trials:
            y = self.initial_tmp_array[self.test_index]
        else:
            regr = linear_model.LinearRegression()
            regr.fit(self.rating_array.reshape(-1,1), self.tmp_array.reshape(-1,1))
            y = regr.predict(np.array([x]).reshape(-1,1))
            y = self.round_of_rating(y)
        self.current_VAS = y if y <= 48 else 48;
        if utils.pain_machine_connected:
            utils.initPain(str(self.current_VAS), False, True)



    def updateRating(self, rating):
        if rating == "space":
            rating = 10;
        self.rating_array = np.insert(self.rating_array, self.test_index, int(rating))
        self.tmp_array = np.insert(self.tmp_array, self.test_index, self.current_VAS)
        self.test_index += 1;
        if self.test_index == self.trials_amount:
            self.finish()

    def finish(self):
        workbook = openpyxl.Workbook();
        workbook.save(self.log_path)

        writer = pandas.ExcelWriter(self.log_path, engine='openpyxl')
        ar = np.array([self.rating_array, self.tmp_array])
        new_data = pandas.DataFrame(ar.T)
        new_data.to_excel(writer, sheet_name=self.sheet_name, startcol=0, header=False, index=False)
        writer.save();

        regr = linear_model.LinearRegression()
        regr.fit(self.rating_array.reshape(-1,1), self.tmp_array.reshape(-1,1))
        y2 = regr.predict(np.array([2]).reshape(-1,1))
        y2 = self.round_of_rating(y2)

        y8 = regr.predict(np.array([8]).reshape(-1,1))
        y8 = self.round_of_rating(y8)

        writer = pandas.ExcelWriter(utils.results_file, engine='xlsxwriter')

        new_data = pandas.DataFrame({'VAS2': [y2], 'VAS8': [y8]})
        new_data.to_excel(writer, sheet_name=utils.results_file_sheet_name, startcol=0, header=False, index=False,  startrow=1)

        workbook = writer.book
        worksheet = writer.sheets[utils.results_file_sheet_name]

        # Add a header format.
        header_format = workbook.add_format({
            'bold': True,
            'text_wrap': True,
            'valign': 'top',
            'fg_color': '#D7E4BC',
            'border': 1})

        # Write the column headers with the defined format.
        for col_num, value in enumerate(new_data.columns.values):
            worksheet.write(0, col_num, value, header_format)

        # Close the Pandas Excel writer and output the Excel file.
        writer.save()
