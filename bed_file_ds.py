import sys
import numpy as np
import pandas as pd

input_data = sys.argv[1]
output_data = sys.argv[2]

data = pd.read_csv(input_data, "\t", header = None)

##### Create bed-files from various positions

data[2] = data[2].add(500)

data.to_csv(output_data, "\t", index = False, header = None)

