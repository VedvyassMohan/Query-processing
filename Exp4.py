import pandas as pd
import matplotlib.pyplot as plt

# Historical stock price data for Alphabet Inc.
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
    "Close_Price": [
        89.70,
        91.85,
        93.10,
        94.50,
        96.20,
        97.85,
        99.30
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Select data between two dates
start_date = "2023-01-03"
end_date = "2023-01-09"

filtered_df = df[(df["Date"] >= start_date) & (df["Date"] <= end_date)]

# Display filtered data
print("Historical Stock Prices of Alphabet Inc.")
print(filtered_df)

# Plot line chart
plt.figure(figsize=(8, 5))
plt.plot(filtered_df["Date"], filtered_df["Close_Price"],
         marker='o', linestyle='-', color='blue')

# Chart title and labels
plt.title("Alphabet Inc. Historical Stock Prices")
plt.xlabel("Date")
plt.ylabel("Closing Price (USD)")
plt.grid(True)

# Rotate date labels
plt.xticks(rotation=45)

# Show plot
plt.tight_layout()
plt.show()