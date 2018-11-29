
results_file = 'VAS_values.xlsx'
results_file_sheet_name = 'Sheet1'
import socket
import time
import pandas
#TCP_IP = "10.101.30.184"
TCP_IP = "10.101.30.124"

TCP_PORT = 20121

pain_machine_connected = False

# size and position of rating scale to fit default scale
laptop7_scale_posY = -0.06
laptop7_scale_size = 1.80

laptopNoa_scale_posY = -0.04
laptopNoa_scale_size = 1.53

stimuli_comp_scale_posY = -0.06
stimuli_comp_scale_size = 2.85

cmds_calibration = {

        "39.0": bytearray([9, 0, 0, 0, 185, 223, 16, 88, 1, 32, 0, 0, 0]),  # 100000
        "40.0": bytearray([9, 0, 0, 0, 175, 166, 15, 88, 1, 34, 0, 0, 0]),  # 100010
        "41.0": bytearray([9, 0, 0, 0, 223, 164, 15, 88, 1, 36, 0, 0, 0]),  # 100100
        "42.0": bytearray([9, 0, 0, 0, 223, 164, 15, 88, 1, 53, 0, 0, 0]),  #110101
        "43.0": bytearray([9, 0, 0, 0, 17, 167, 15, 88, 1, 38, 0, 0, 0]),  # 100110
        "44.0": bytearray([9, 0, 0, 0, 196, 52, 72, 88, 1, 40, 0, 0, 0]),  # 101000
        "45.0": bytearray([9, 0, 0, 0, 196, 52, 72, 88, 1, 42, 0, 0, 0]),  # 101010
        "46.0": bytearray([9, 0, 0, 0, 196, 52, 72, 88, 1, 44, 0, 0, 0]),  # 101100
        "47.0": bytearray([9, 0, 0, 0, 196, 52, 72, 88, 1, 46, 0, 0, 0]),  # 101110s
        "48.0": bytearray([9, 0, 0, 0, 196, 52, 72, 88, 1, 48, 0, 0, 0])}  # 110000

cmd_stimuli = {"39": bytearray([9, 0, 0, 0, 185, 223, 16, 88, 1, 22, 0, 0, 0]),  # 010110
       # "39.5": bytearray([9, 0, 0, 0, 72, 166, 15, 88, 1, 19, 0, 0, 0]),  # 010011
        "40.0": bytearray([9, 0, 0, 0, 175, 166, 15, 88, 1, 20, 0, 0, 0]),  # 010100
       # "40.5": bytearray([9, 0, 0, 0, 58, 239, 194, 87, 1, 16, 0, 0, 0]),  # 010000
        "41.0": bytearray([9, 0, 0, 0, 223, 164, 15, 88, 1, 18, 0, 0, 0]),  # 010010
       # "41.5": bytearray([9, 0, 0, 0, 223, 164, 15, 88, 1, 51, 0, 0, 0]),  # 110011
        "42.0": bytearray([9, 0, 0, 0, 32, 239, 194, 87, 1, 17, 0, 0, 0]),  # 010001
       # "42.5": bytearray([9, 0, 0, 0, 17, 167, 15, 88, 1, 21, 0, 0, 0]),  # 010101
        "43.0": bytearray([9, 0, 0, 0, 52, 49, 72, 88, 1, 23, 0, 0, 0]),  # 010111
       # "43.5": bytearray([9, 0, 0, 0, 196, 52, 72, 88, 1, 24, 0, 0, 0]),  # 011000
        "44.0": bytearray([9, 0, 0, 0, 196, 52, 72, 88, 1, 25, 0, 0, 0]),  # 011001
       # "44.5": bytearray([9, 0, 0, 0, 196, 52, 72, 88, 1, 26, 0, 0, 0]),  # 011010
        "45.0": bytearray([9, 0, 0, 0, 196, 52, 72, 88, 1, 27, 0, 0, 0]),  # 011011
       # "45.5": bytearray([9, 0, 0, 0, 196, 52, 72, 88, 1, 28, 0, 0, 0]),  # 011100
        "46.0": bytearray([9, 0, 0, 0, 196, 52, 72, 88, 1, 29, 0, 0, 0]),  # 011101
       # "46.5": bytearray([9, 0, 0, 0, 196, 52, 72, 88, 1, 30, 0, 0, 0]),  # 011110
        "47.0": bytearray([9, 0, 0, 0, 196, 52, 72, 88, 1, 31, 0, 0, 0]), # 011111
       # "47.5": bytearray([9, 0, 0, 0, 196, 52, 72, 88, 1, 49, 0, 0, 0]), #110001
        "48.0": bytearray([9, 0, 0, 0, 196, 52, 72, 88, 1, 50, 0, 0, 0]),}  # 110010

cmds_general = {  "start": bytearray([5, 0, 0, 0, 216, 237, 194, 87, 2]),
        "pause": bytearray([5, 0, 0, 0, 40, 238, 194, 87, 3]),
        "trigger": bytearray([5, 0, 0, 0, 74, 238, 194, 87, 4]),
        "stop": bytearray([5, 0, 0, 0, 157, 238, 194, 87, 5]),
        "abort": bytearray([5, 0, 0, 0, 177, 238, 194, 87, 6]),
        "yes": bytearray([5, 0, 0, 0, 195, 238, 194, 87, 7]),
        "no": bytearray([5, 0, 0, 0, 216, 238, 194, 87, 8])}

def readTmpFromFile(columnName):
    xl = pandas.ExcelFile("VAS_values.xlsx")
    df = xl.parse("Sheet1")
    return df.iloc[0][columnName]

def initSocket():

    global TCP_IPa
    global TCP_PORT
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    return s

def initPain(tmp_input, read_from_file = True, is_calibration=True):
    tmp = tmp_input
    if read_from_file:
        tmp = readTmpFromFile(tmp_input)
    initSocket()
    global s
    if is_calibration:
        s.send(cmds_calibration[str(tmp)])
    else:
        s.send(cmd_stimuli[str(tmp)])
    a=initSocket()
    time.sleep(2)
    a=s.send(cmds_general["start"])