import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("covid_grouped.csv")

print("Dataset Loaded Successfully")

print("\nFirst 5 Rows")
print(df.head())

print("\nLast 5 Rows")
print(df.tail())

print("\nShape")
print(df.shape)

print("\nColumns")
print(df.columns)

print("\nDataset Information")
print(df.info())

print("\nStatistical Summary")
print(df.describe())

print("\nMissing Values")
print(df.isnull().sum())

print("\nDuplicate Records")
print(df.duplicated().sum())

df.drop_duplicates(inplace=True)

print("\nDataset Shape After Cleaning")
print(df.shape)

# Question 1 How many rows and columns are present?

print("\nQuestion 1")
print("Rows and Columns :", df.shape)

# Question 2 Top 10 countries with highest confirmed cases

top_confirmed = (
    df.groupby("Country/Region")["Confirmed"]
    .max()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Countries with Highest Confirmed Cases")
print(top_confirmed)

plt.figure(figsize=(10,5))

plt.bar(top_confirmed.index, top_confirmed.values)

plt.title("Top 10 Countries by Confirmed Cases")
plt.xlabel("Country")
plt.ylabel("Confirmed Cases")
plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("Q2_Top10_Confirmed.png", dpi=300)

plt.show()

# Question 3 Country with Highest Deaths

top_deaths = (
    df.groupby("Country/Region")["Deaths"]
    .max()
    .sort_values(ascending=False)
)

print("\nCountry with Highest Deaths")
print(top_deaths.head(1))

# Question 4 Worldwide Totals

latest = df.sort_values("Date").groupby("Country/Region").tail(1)

total_confirmed = latest["Confirmed"].sum()
total_deaths = latest["Deaths"].sum()
total_recovered = latest["Recovered"].sum()

print("\nWorldwide Totals")
print("Confirmed :", total_confirmed)
print("Deaths :", total_deaths)
print("Recovered :", total_recovered)

# Question 5 Unique WHO Regions

print("\nUnique WHO Regions")

print(df["WHO Region"].nunique())

# Question 6 Bar Chart

plt.figure(figsize=(10,5))

sns.barplot(
    x=top_confirmed.index,
    y=top_confirmed.values
)

plt.title("Top 10 Countries by Confirmed Cases")

plt.xlabel("Country")

plt.ylabel("Confirmed Cases")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("Q6_BarChart.png", dpi=300)

plt.show()

# Question 7 Pie Chart by WHO Region

who_region = (
    latest.groupby("WHO Region")["Confirmed"]
    .sum()
)

plt.figure(figsize=(7,7))

plt.pie(
    who_region,
    labels=who_region.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Confirmed Cases by WHO Region")

plt.tight_layout()

plt.savefig("Q7_PieChart.png", dpi=300)

plt.show()


# Question 8 Line Chart Showing Confirmed Cases Over Time

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Total confirmed cases for each date
date_cases = (
    df.groupby("Date")["Confirmed"]
    .sum()
    .reset_index()
)

plt.figure(figsize=(14,6))

plt.plot(
    date_cases["Date"],
    date_cases["Confirmed"],
    color="blue",
    linewidth=2
)

plt.title("Worldwide Confirmed COVID-19 Cases Over Time", fontsize=14)

plt.xlabel("Date")
plt.ylabel("Confirmed Cases")

# Show only one label every 15 da
plt.xticks(
    date_cases["Date"][::15],
    rotation=45
)

plt.grid(alpha=0.3)

plt.tight_layout()

plt.savefig("Q8_Confirmed_Cases_Over_Time.png", dpi=300)

plt.show()

# Question 9 Histogram

plt.figure(figsize=(8,5))

sns.histplot(
    df["Confirmed"],
    bins=30,
    kde=True
)

plt.title("Distribution of Confirmed Cases")

plt.xlabel("Confirmed Cases")

plt.tight_layout()

plt.savefig("Q9_Histogram.png", dpi=300)

plt.show()

# Question 10 Scatter Plot

plt.figure(figsize=(8,5))

sns.scatterplot(
    x="Confirmed",
    y="Deaths",
    data=df
)

plt.title("Confirmed Cases vs Deaths")

plt.tight_layout()

plt.savefig("Q10_ScatterPlot.png", dpi=300)

plt.show()

# Final Output

print("\nCountry with Highest Confirmed Cases")
print(top_confirmed.head(1))

print("\nCountry with Highest Deaths")
print(top_deaths.head(1))

print("\nAnalysis Completed Successfully")

print("All Charts Saved Successfully as PNG Images")