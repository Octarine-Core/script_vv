from logging.config import valid_ident
import os
import fnmatch
from re import S
from statistics import mean
from traceback import print_tb


PATH= '.\\'


def do_val_err_list(values, val_err_list):
    for line in val_err_list:
                measurements = lines[line].split("   ")[-2:]
                measurements[1]=measurements[1][:-1]
                values.append({
                    "line":line,
                    "parameter":measurements[0],
                    "error":measurements[1]
                    })

def do_chi2(values, chi2_list):
    for line in chi2_list:
                measurements = lines[line].split("  ")
                
                values.append({
                    "line":line,
                    "chi2":measurements[9] #chi2 aqui
                    })
            
def do_v1v2(values):
    line_173_read=lines[173].split("  ")[5]
    line_177_read=lines[177].split("  ")[3]
    values.append(
        {
        "v1_measurement":line_173_read.split("(")[0], #value aqui
        "v2_measurement":line_177_read.split("(")[0],
        "v1_error" : line_173_read.split("(")[0][:-1],
        "v2_error" : line_177_read.split("(")[1][:-1]
        }
        )
def do_phase(values, phase_list):
    phase_1_pct = lines[phase_list[0]].split("  ")[3]
    phase_2_pct = lines[phase_list[1]].split("  ")[3]
    print("PHASE")
    print(phase_1_pct, phase_2_pct)
    values.append(
        {"phase1":phase_1_pct,
        "phase2":phase_2_pct}
    )

for dir in os.listdir(PATH):
    try:
        if dir[:3] != "HEA": 
            continue
    except Exception:
        continue
    temperature = dir[-4:-1]
    full_path_current_dir = PATH+"\\"+dir
    print(full_path_current_dir)
    print(temperature)
    sum_file = ""
    for file in os.listdir(full_path_current_dir):
        if file[-4:] == ".sum":
            sum_file = file
    print(sum_file)
    val_err_list = [
        52,53,54,62,63,64,95,97,105,106,107        
    ]
    chi2_list = [148]
    v1_list = [173]
    v2_list = [177]

    phase_list = [245,247]
    with open(full_path_current_dir + "\\" + sum_file) as s_f: #sum file opened
        lines = s_f.readlines()
        values = [{"TEMPERATURE": temperature}]
        do_val_err_list(values, val_err_list) #the simple ones with pairs of values and error, lines in val_err_list
        do_chi2(values, chi2_list) 
        do_v1v2(values)
        do_phase(values, phase_list)
        print(values)
