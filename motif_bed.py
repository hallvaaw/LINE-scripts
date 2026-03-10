#!/bin/python3

import pandas as pd
import sys

motif = sys.argv[1]

data = pd.read_csv("PATH", header = None)

chroms = list(data.iloc[0:, 0])
seq = list(data.iloc[0:, 1])

active_lines = []
inactive_lines = []

for i in range(len(chroms)):
    if motif in seq[i]:
        active_lines.append(chroms[i])
        active_lines.append(seq[i])
    else:
        inactive_lines.append(chroms[i])
        inactive_lines.append(seq[i])


with open(f"PATH{motif}.bed", "w") as file_:
    for i in active_lines:
        if ">" in i:
            string = i
            string = string.replace(">", "")
            string = string.replace(":", "\t")
#        string = string.replace("(-)", "\t-")
#        string = string.replace("(+)", "\t+")
            string = string.replace("-", "\t", 1)
            string = string.replace("(", "\tL1MdA\t0.0\t")
            string = string.replace(")", "")
            string = string.replace("x", "X")
            file_.write(string)
            file_.write("\n")

