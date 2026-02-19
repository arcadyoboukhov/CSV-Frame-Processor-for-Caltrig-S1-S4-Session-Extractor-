from tkinter import Tk, filedialog
import pandas as pd

root = Tk()
root.withdraw()

csv_file = filedialog.askopenfilename(
    title="Select CSV file",
    filetypes=[("CSV files", "*.csv")],
    initialfile=""
)

print(f"File Selected: {csv_file}") 

session = input("Select session (S1 or S4): ").upper()
if session not in ["S1", "S4"]:
    print("Invalid selection. Please enter S1 or S4.")
    exit()

#remove all columns except "Global Frame Number" and "Frame Timestamp (s)"
df_filtered = pd.read_csv(csv_file)[["Global Frame Number", "Frame Timestamp (s)"]]
print(df_filtered.head())
#convert second to ms
df_filtered["Frame Timestamp (s)"] = df_filtered["Frame Timestamp (s)"] * 1000
#convert absolute timestamps to relative (starting at 0 ms)
df_filtered["Frame Timestamp (s)"] = df_filtered["Frame Timestamp (s)"] - df_filtered["Frame Timestamp (s)"].iloc[0]
#it should change names to Frame Number and Time Stamp (ms) to meet Caltrig docs
df_filtered.rename(columns={"Global Frame Number": "Frame Number", "Frame Timestamp (s)": "Time Stamp (ms)"}, inplace=True)

#S1 (first 15 min) vs S4 (last 15 min)
fifteen_min_ms = 15 * 60 * 1000
if session == "S1":
    df_filtered = df_filtered[df_filtered["Time Stamp (ms)"] <= fifteen_min_ms]
else:
    df_filtered = df_filtered[df_filtered["Time Stamp (ms)"] >= df_filtered["Time Stamp (ms)"].max() - fifteen_min_ms]

#Now saved as Behavior.csv
df_filtered.to_csv("Behavior.csv", index=False)

#I did not add any error handling so it is very important not to break the script.
#This script is under GNU General Public License v3.0 (GPL-3.0) and is provided "as is" without any warranty. Use at your own risk.
#Made by Arcady Oboukhov. Source: https://github.com/arcadyoboukhov/CSV-Frame-Processor-for-Caltrig-S1-S4-Session-Extractor-?