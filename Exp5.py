import pandas as pd
import matplotlib.pyplot as plt

# Historical stock trading volume data for Alphabet Inc.
data = {
    "Date": [
        "2023-01-02",
        "2023-01-03",
        "2023-01-04",
        "2023-01-05",
        "2023-01-06",
        "2023-01-09",
        "2023-01-10"
    ],
    "Volume": [
        28000000,
        31000000,
        29500000,
        33000000,
        31500000,
        34000000,
        32500000
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Convert Date column to datetime format
df["Date"] = pd.to_datetime(df["Date"])

# Select data between two specific dates
start_date = "2023-01-03"
end_date = "2023-01-09"

filtered_df = df[(df["Date"] >= start_date) & (df["Date"] <= end_date)]

# Display filtered data
print("Trading Volume of Alphabet Inc.")
print(filtered_df)

# Create Bar Plot
plt.figure(figsize=(8, 5))
plt.bar(filtered_df["Date"].dt.strftime("%Y-%m-%d"),
        filtered_df["Volume"],
        color="skyblue",
        edgecolor="black")

# Chart Title and Labels
plt.title("Alphabet Inc. Trading Volume")
plt.xlabel("Date")
plt.ylabel("Trading Volume")
plt.xticks(rotation=45)
plt.grid(axis="y")

# Display the chart
plt.tight_layout()
plt.show()