# CSV Frame Processor for Caltrig (S1 / S4 Session Extractor)  

[![Python](https://img.shields.io/badge/python-3.x-blue?logo=python&logoColor=white)](https://www.python.org/)  
[![License](https://img.shields.io/badge/license-GNU%20GPLv3-brightgreen)](https://www.gnu.org/licenses/gpl-3.0.en.html)  

---

## 📖 Overview
This Python script processes CSV files containing **frame timing data** and converts them into a **Caltrig-compatible format**.  

It allows you to extract either:  
- **S1** → First 15 minutes of the session  
- **S4** → Last 15 minutes of the session  

The script also:  
- Converts timestamps from seconds → milliseconds  
- Adjusts timestamps to start at 0 ms  
- Renames columns to match Caltrig documentation  
- Outputs a ready-to-use `Behavior.csv`

---

## ⚡ Features
- **Graphical File Selection:** Tkinter file dialog for easy CSV selection.  
- **Session Extraction:** Extract S1 or S4 (first or last 15 min).  
- **Data Processing:**  
  - Keeps only `Global Frame Number` and `Frame Timestamp (s)`  
  - Converts seconds → milliseconds  
  - Converts absolute → relative timestamps starting at 0 ms  
  - Renames columns to `Frame Number` and `Time Stamp (ms)`  
- **Output:** Saves as `Behavior.csv` in the current directory.

---

## 🛠️ Requirements
- Python 3.x  
- Libraries:
  - `pandas`  
  - `tkinter` (usually included with Python)  

Install missing packages using:

```bash
pip install pandas

🚀 Usage

    Clone or download the repository.

    Run the script:

python script_name.py

    Select a CSV file using the file dialog.

    Enter the session to extract:

Option	Description
S1	First 15 minutes
S4	Last 15 minutes

    Output saved as:

Behavior.csv

📊 Example
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
⚠️ Notes

    No error handling implemented. The script may break if:

        CSV is missing required columns (Global Frame Number, Frame Timestamp (s))

        File dialog is canceled

        Invalid session entered (S1 or S4 only)

    Ensure CSV contains valid frame timing data before running.

📂 File Structure (Example)

├── csv_frame_processor.py
├── README.md
└── Behavior.csv  # generated after running script

📝 License

This project is licensed under the GNU General Public License v3.0.
See the GNU GPLv3
for details.
