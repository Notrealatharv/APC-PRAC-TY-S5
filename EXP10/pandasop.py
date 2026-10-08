from pathlib import Path
import pandas as pd


'Pandas Series'

series = pd.Series([85, 90, 78], index=["Atharv", "prakarsh", "Charlie"])

print("Series:\n", series)
print("Value for Bob:", series["prakarsh"])
print("Values greater than 80:\n", series[series > 80])


'Read a CSV file'

data = pd.read_csv(Path(__file__).with_name("sample.csv"))

print("\nCSV data:\n", data)
print("First rows:\n", data.head())
