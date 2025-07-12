import sys
import pandas as pd

# print(sys.argv[1])
file_loc = sys.argv[1]
# save_loc = sys.argv[2]

df = pd.read_csv(file_loc, skiprows=11)
print(df.head())


# Headless
# Headed


# pyinstaller (python file -> software (.exe))
# Virtual Environment (install pyinstaller, pandas)
# pyinstaller --one-file python-file-location/mypythonfile.py
# cp software /usr/local/bin
