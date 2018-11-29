

import time
import numpy as np
from sklearn import datasets, linear_model
import pandas
import openpyxl
import utils
import statistics
import numpy
import xlrd

TCP_IP = "192.168.61.27"
#TCP_IP = "192.168.49.161"
TCP_PORT = 20121


class Calibration:
    log_path_preffix = 'calibrationLog_'
    log_path_suffix = '.xlsx'
    sheet_name = 'CalibrationArray'
    trials_amount = 9;
    test_index = 0;
    current_VAS = -1;
    initial_tmp_array = [41.0,44.0,47.0]
    amount_of_initial_trials = 3;

    def __init__(self, subId):
        self.log_path = self.log_path_preffix + subId + self.log_path_suffix;
        self.tmp_array = np.array([])
        self.rating_array = np.array([])
        wb = xlrd.open_workbook('C:\Users\Noa\Noam_cloned\calibrationOrder.xlsx')
        self.tmps_order = wb.sheet_by_index(0)

    def round_of_rating(self, number):
        return round(number)

    def runVAS(self, x):
        if self.test_index < self.amount_of_initial_trials:
            y = self.initial_tmp_array[self.test_index]
        else:
            y = self.predictTmp(self.tmps_order.cell_value(self.test_index, 0))
        self.current_VAS = y
        if y > 48:
            self.current_VAS = 48.0
        elif y < 39:
            self.current_VAS = 39.0
        if utils.pain_machine_connected:
            utils.initPain(str(self.current_VAS), False, True)



    def updateRating(self, rating):
        if rating == "space":
            rating = 10;
        elif rating == []:
            rating = None
        else:
            rating = int(rating)
        self.rating_array = np.insert(self.rating_array, self.test_index, rating)
        self.tmp_array = np.insert(self.tmp_array, self.test_index, self.current_VAS)
        self.test_index += 1;
        if self.test_index == self.trials_amount:
            self.finish()

    def predictTmp(self, targetRating):
        regr = linear_model.LinearRegression()
        regr.fit(self.tmp_array.reshape(-1, 1), self.rating_array.reshape(-1, 1))
        residuals = abs(regr.predict(self.tmp_array.reshape(-1, 1)) -
                                                 self.rating_array.reshape(-1, 1))
        residuals_median = statistics.median(residuals);
        mask = np.array(residuals) <= 3*residuals_median;
        tmp_array_no_outlier = self.tmp_array.reshape(-1, 1)[mask]
        rating_array_no_outlier = self.rating_array.reshape(-1, 1)[mask]
        regr.fit(tmp_array_no_outlier.reshape(-1, 1), rating_array_no_outlier.reshape(-1, 1))

        coef = regr.coef_
        intercept = regr.intercept_
        y = (targetRating - intercept) / coef
        y = self.round_of_rating(y)
        return y

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


