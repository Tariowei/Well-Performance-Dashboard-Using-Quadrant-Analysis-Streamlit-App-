# Well-Performance-Dashboard-Using-Quadrant-Analysis-Streamlit-App-

## Overview
This project is a simple interactive dashboard used to analyze oil field well performance.

It focuses on identifying wells that may require attention by comparing oil and water production using a quadrant analysis approach.

---

## Objectives
- Analyze well production data
- Compare performance across wells
- Identify underperforming wells (low oil, high water)
- Visualize production trends

---

## Tools Used
- Python
- Streamlit
- Pandas
- Plotly

---

## Key Concepts

### 1. Health Index (HI)
To compare wells fairly, a simple normalization approach is used:

- HI_Oil = 1 - (Oil / Average Oil)  
- HI_Water = 1 - (Water / Average Water)  

This helps identify wells performing above or below average.

---

### 2. Quadrant Analysis
Wells are plotted based on their performance:

- **Good Wells** → High oil, low water  
- **Problem Wells** → Low oil, high water  

Wells in the "low oil & high water" quadrant are flagged for further investigation.

---

## Features

- Upload production dataset
- Select a specific date for analysis
- View processed data table
- Distribution plots (Oil and Water)
- Bar chart of oil production by well
- Quadrant scatter plots
- Identification of problematic wells
- Production trend of selected wells over time

---

## How to Run

1. Install dependencies:
```bash
pip install -r requirements.txt
