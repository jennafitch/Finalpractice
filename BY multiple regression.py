
import pandas as pd
import statsmodels.api as sm

# Load the data from the spreadsheet
df = pd.read_excel(r"C:\Users\jenfi\OneDrive - University of Wisconsin-Whitewater\BrewersYankees.xlsx")

# Exclude data from 2020
df_filtered = df[(df["yearID"] != 2020) & (df["franchID"].isin(["NYY", "MIL"]))]

# Calculate winning percentage
df_filtered["Win_Percentage"] = df_filtered["W"] / df_filtered["G"]
# Calculate batting average
df_filtered["batting_avg"] = df_filtered["H"] / df_filtered["AB"]

# Perform multiple regression analysis for different performance metrics
performance_metrics = ["Win_Percentage", "ERA", "batting_avg"]
for metric in performance_metrics:
    X = sm.add_constant(df_filtered["attendance"])
    y = df_filtered[metric]

    model = sm.OLS(y, X).fit()
    print(f"Regression Analysis for {metric}:")
    print(model.summary())
    print("\n")
