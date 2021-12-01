import numpy as np
import pandas as pd
import glob

data = pd.read_csv("EuroMillions_numbers.csv",sep=";")
data = data[["N1","N2","N3","N4","N5","E1","E2","Winner"]]