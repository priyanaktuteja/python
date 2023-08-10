import pandas as pd
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
import numpy as np


# Read data from existing Excel file
df_gg = pd.read_excel("gg.xlsx")

# Separate into fact and dimension DataFrames
fact_columns = ["App Id", "Rating", "Rating Count", "Installs", "Minimum Installs", "Maximum Installs", "Price", "Size"]
fact_df = df_gg[fact_columns]

dimension_columns = [col for col in df_gg.columns if col not in fact_columns]
dimension_df = df_gg[dimension_columns]

# Save to separate Excel files
with pd.ExcelWriter("fact_table.xlsx", engine="openpyxl") as writer:
    fact_df.to_excel(writer, index=False, sheet_name="FactTable")

 # with pd.ExcelWriter("dimension_table.xlsx", engine="openpyxl") as writer:
    dimension_df.to_excel(writer, index=False, sheet_name="DimensionTable")






# Load the data into pandas DataFrames
data = [
    {
        "App Name": "Gakondo",
        "App Id": "com.ishakwe.gakondo",
        "Category": "Adventure",
        "Rating": 0.0,
        "Rating Count": 0,
        "Installs": "10+",
        "Minimum Installs": 10,
        "Maximum Installs": 15,
        "Free": True,
        # ... (other attributes)
    },
    {
        "App Name": "Ampere Battery Info",
        "App Id": "com.webserveis.batteryinfo",
        "Category": "Tools",
        "Rating": 4.4,
        "Rating Count": 64,
        "Installs": "5,000+",
        "Minimum Installs": 5000,
        "Maximum Installs": 7662,
        "Free": True,
        # ... (other attributes)
    },
    # ... (other data)
]

df = pd.DataFrame(data)
# ----------------------------------------------------------------------------------------------------
# Quality checks and transformations
# Drop rows with missing values in important columns
important_columns = ["App Name", "App Id", "Category", "Rating", "Rating Count", "Installs"]
df = df.dropna(subset=important_columns)

# Convert 'Installs' column to numerical format
df["Installs"] = df["Installs"].str.replace("+", "").str.replace(",", "").astype(int)

# Aggregation using GROUP BY
category_grouped = df.groupby("Category").agg(
    {
        "Rating": "mean",
        "Rating Count": "sum",
        "Installs": "max",
    }
)

# Load dimension data
dimension_data = [
    {
        "Category": "Adventure",
        "Description": "Explore new adventures.",
    },
    {
        "Category": "Tools",
        "Description": "Useful utility apps.",
    },
    # ... (other dimension data)
]

dimension_df = pd.DataFrame(dimension_data)

# JOIN operation
merged_data = pd.merge(category_grouped, dimension_df, on="Category", how="inner")

print(merged_data)


# -------------------------------------------------------------------------------------------------
# Create an in-memory database using a dictionary
database = {
    "transformed_data": merged_data,
}

# Access the table from the database
transformed_table = database["transformed_data"]

# Print the transformed data table
print(transformed_table)

# -------------------------------------------
# Reflection
# what can be differently done:
# Data Selection: Invest extra time in understanding the quality of the data. 
# Data Extraction: Create a easy data from multiple sources. Use the right tools to process this procedure.
# Implement extensive data cleansing and transformation procedures. Investigate strategies for  outliers.
# Data Loading: Select a suitable storage system or database for effective data loading. 

# Reflection: there is always have need a improvemnet in data. its endless work.

# Future initiatives can be handled with a more refined and informed plan after learning from these obstacles and experiences.

# Data knowing and Analysis: The need of completely comprehending the dataset before starting with any analysis was stressed in this project. Effective data manipulation requires a thorough understanding of the data's structure.

# Data Safety and Preprocessing: It is critical for accurate and relevant insights to ensure data quality through adequate preprocessing activities such as addressing missing values, changing data types, and removing inconsistencies.
