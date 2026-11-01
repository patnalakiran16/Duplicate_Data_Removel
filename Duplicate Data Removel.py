import pandas as pd

# Creating an employee dataset with some duplicate records
employees = {
    "Name": ["Kiran", "Ravi", "Priya", "Suresh", "Kiran", "Anu", "Ravi"],
    "Age": [23, 24, 22, 25, 23, 21, 24],
    "Department": ["IT", "HR", "Finance", "IT", "IT", "HR", "HR"],
    "Salary": [30000, 35000, 40000, 32000, 30000, 28000, 35000]
}

# Converting the data into a DataFrame
df = pd.DataFrame(employees)

print("Original Employee Dataset:")
print(df)

# Checking the total number of records
original_count = len(df)
print("\nTotal records before cleaning:", original_count)

# Finding duplicate records
duplicate_records = df[df.duplicated()]

print("\nDuplicate Records Found:")
print(duplicate_records)

# Counting the duplicate records
total_duplicates = df.duplicated().sum()
print("\nTotal Duplicate Records:", total_duplicates)

# Removing duplicate records from the dataset
cleaned_data = df.drop_duplicates()

# Checking the records after removing duplicates
cleaned_count = len(cleaned_data)
print("\nTotal records after cleaning:", cleaned_count)

# Displaying the final cleaned dataset
print("\nFinal Cleaned Employee Dataset:")
print(cleaned_data)

# Saving the cleaned data into a CSV file
cleaned_data.to_csv("cleaned_dataset.csv", index=False)

print("\nDataset cleaned and saved successfully!")
