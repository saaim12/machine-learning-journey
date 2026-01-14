import pandas as pd

# =====================================================
# 1️⃣ LOAD CSV FILE INTO DATAFRAME
# =====================================================

# Reads the CSV file and converts it into a Pandas DataFrame
df = pd.read_csv('Mercedes_Company_dataset.csv')

# Common parameters of read_csv (for reference):
# pd.read_csv(
#     file,
#     sep=',',          # Column separator (default is comma)
#     header=0,         # Row index that contains column names
#     index_col=None,   # Column to be used as index
#     encoding='utf-8', # File encoding
#     na_values=['NA', 'null']  # Values treated as missing
# )

# =====================================================
# 2️⃣ QUICK DATA PREVIEW
# =====================================================

# Shows first 5 rows (default)
print("🔹 First 5 rows:")
print(df.head())

# Shows first 10 rows
print("\n🔹 First 10 rows:")
print(df.head(10))

# Shows last 5 rows
print("\n🔹 Last 5 rows:")
print(df.tail(5))

# =====================================================
# 3️⃣ DATASET STRUCTURE & MEMORY INFO
# =====================================================

print("\n🔹 Dataset Information:")
print(df.info())

# info() tells:
# - Number of rows
# - Number of columns
# - Column names
# - Data types (int, float, object, etc.)
# - Non-null values per column
# - Memory usage

# =====================================================
# 4️⃣ STATISTICAL SUMMARY (NUMERICAL COLUMNS)
# =====================================================

print("\n🔹 Statistical Summary (Numerical Columns):")
print(df.describe())

# describe() gives:
# - count : non-null values
# - mean  : average
# - std   : standard deviation
# - min   : minimum value
# - 25%   : first quartile (Q1)
# - 50%   : median
# - 75%   : third quartile (Q3)
# - max   : maximum value

# =====================================================
# 5️⃣ STATISTICS INCLUDING CATEGORICAL DATA
# =====================================================

print("\n🔹 Full Summary (Including Categorical Columns):")
print(df.describe(include='all'))
# | Metric          | How NaN is handled                 |
# | --------------- | -----------------------------------|
# | `count`         | ✅ counts **non-NaN values only** |
# | `mean`          | ❌ ignores NaN                    |
# | `std`           | ❌ ignores NaN                    |
# | `min/max`       | ❌ ignores NaN                    |
# | `25%, 50%, 75%` | ❌ ignores NaN                    |
#  describe() works column-wise
#  NaN values are ignored in all calculations
#  count tells about data completeness
#  Never assume NaN = 0
# Useful for:
# - object (string) columns
# - frequency counts
# - most common values

# =====================================================
# 6️⃣ BASIC DATA QUALITY CHECKS
# =====================================================

# Missing values per column
print("\n🔹 Missing Values Per Column:")
print(df.isnull().sum())

# Duplicate rows
print("\n🔹 Number of Duplicate Rows:")
print(df.duplicated().sum())

# =====================================================
# 7️⃣ DATAFRAME SHAPE
# =====================================================

print("\n🔹 Dataset Shape (Rows, Columns):")
print(df.shape)
