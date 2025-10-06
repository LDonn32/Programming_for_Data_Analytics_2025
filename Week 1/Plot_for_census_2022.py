import numpy as np
import pandas as pd
import os

import matplotlib.pyplot as plt

# Find the first .xlsx file in the current directory
folder = os.path.dirname(__file__)
files = [f for f in os.listdir(folder) if f.endswith('.xlsx')]
if not files:
    raise FileNotFoundError("No .xlsx file found in the current folder.")
excel_file = os.path.join(folder, files[0])

# Read the first sheet of the Excel file
df = pd.read_excel(excel_file)

# Try to find two numeric columns for plotting
numeric_cols = df.select_dtypes(include=[np.number]).columns
if len(numeric_cols) < 2:
    raise ValueError("Not enough numeric columns to plot.")

x = df[numeric_cols[0]].to_numpy()
y = df[numeric_cols[1]].to_numpy()

plt.scatter(x, y)
plt.xlabel(numeric_cols[0])
plt.ylabel(numeric_cols[1])
plt.title('Simple Point Plot from CSO Census 2022 Data')
plt.show()

# If you are getting a "Permission denied" error in the terminal, it is likely due to one of the following reasons:
# 1. The script file does not have execute permissions. Run: chmod +x Plot_for_census_2022.py
# 2. You are trying to run the script with ./Plot_for_census_2022.py but the shebang (#!/usr/bin/env python3) is missing at the top.
# 3. You do not have permission to access the Excel file or the directory. Check file permissions with: ls -l
# 4. You are not the owner of the file or directory. You may need to use sudo or change ownership with chown.
# 5. If running with python Plot_for_census_2022.py, make sure you have read permissions for the script and the Excel file.

# To fix, try:
# chmod +r Plot_for_census_2022.py
# chmod +r <your_excel_file.xlsx>
# If needed, add a shebang line at the top: #!/usr/bin/env python3