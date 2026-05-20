# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data.csv")

# Display dataset
print(df)

# -----------------------------
# LINE CHART
# -----------------------------
plt.figure(figsize=(8,5))

plt.plot(df["Name"], df["Marks"])

plt.title("Student Marks Line Chart")
plt.xlabel("Student Name")
plt.ylabel("Marks")

plt.show()

# -----------------------------
# BAR CHART
# -----------------------------
plt.figure(figsize=(8,5))

plt.bar(df["Name"], df["Marks"])

plt.title("Student Marks Bar Chart")
plt.xlabel("Student Name")
plt.ylabel("Marks")

plt.show()

# -----------------------------
# SCATTER PLOT
# -----------------------------
plt.figure(figsize=(8,5))

sns.scatterplot(x=df["Hours"], y=df["Marks"])

plt.title("Study Hours vs Marks")
plt.xlabel("Hours")
plt.ylabel("Marks")

plt.show()

# -----------------------------
# PIE CHART
# -----------------------------
plt.figure(figsize=(7,7))

plt.pie(
    df["Marks"],
    labels=df["Name"],
    autopct='%1.1f%%'
)

plt.title("Marks Percentage")

plt.show()

# -----------------------------
# HEATMAP
# -----------------------------
plt.figure(figsize=(6,4))

sns.heatmap(
    df.corr(numeric_only=True),
    annot=True
)

plt.title("Correlation Heatmap")

plt.show()

print("Visualization Completed Successfully")