import numpy as np
import typing

def fromCSVtoNumpy() -> np.array:
    with open(file="./data/bedtime_screentime_sleep_debt.csv",mode="r") as f:
        lines = f.readlines()
        input_matrice = np.zeros((len(lines),len(lines[0])))
        features = lines[0]
        # for index,line in enumerate(lines):
        #     curr_line = line
        #     curr_line = line.split(",")
        #     input_matrice[index] 
        print(features)
    return input_matrice

print(fromCSVtoNumpy().shape)