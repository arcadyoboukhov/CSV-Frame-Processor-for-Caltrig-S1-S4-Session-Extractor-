CSV Frame Processor for Caltrig (S1 / S4 Session Extractor)
Overview

This Python script processes CSV files containing frame timing data and converts them into a Caltrig-compatible format. It extracts either the first 15 minutes (S1) or the last 15 minutes (S4) of a session, converts timestamps from seconds to milliseconds, adjusts them to start at 0 ms, renames columns according to documentation, and saves the result as Behavior.csv.

Features

Graphical File Selection: Easy CSV selection using a Tkinter file dialog.

Session Extraction: Extract either the first 15 minutes (S1) or the last 15 minutes (S4) of data.

Data Filtering & Processing:

Keeps only Global Frame Number and Frame Timestamp (s).

Converts timestamps from seconds → milliseconds.

Converts absolute timestamps → relative timestamps starting at 0 ms.

Renames columns to Frame Number and Time Stamp (ms) for Caltrig compatibility.

Output: Saves processed data as Behavior.csv.

Requirements

Python 3.x

Libraries:

pandas

tkinter (usually included with Python)

Install missing packages using:

pip install pandas

Usage

Clone or download the repository.

Run the script:

python script_name.py


A file dialog will appear. Select the CSV file containing frame data.

Enter the session to extract:

S1 → First 15 minutes

S4 → Last 15 minutes

The processed CSV will be saved in the same directory as Behavior.csv.

Example

Input CSV (example.csv):

Global Frame Number	Frame Timestamp (s)	Other Column
1	0.0	...
2	0.033	...
3	0.067	...

Output (Behavior.csv) for S1:

Frame Number	Time Stamp (ms)
1	0
2	33
3	67
Notes

No error handling implemented: The script may break if:

CSV is missing required columns (Global Frame Number, Frame Timestamp (s)).

File dialog is canceled.

Invalid session is entered.

Ensure CSV contains valid frame timing data before running.
