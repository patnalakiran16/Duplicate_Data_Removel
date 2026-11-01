Identify and Remove Duplicate Records Using Pandas

Project Overview

This project demonstrates how to identify duplicate records in a dataset and remove them using Python Pandas.

Duplicate records can affect data accuracy and lead to incorrect analysis. This program helps clean the dataset by detecting and removing repeated records.

Objective

- Identify duplicate records in a dataset.
- Count the number of duplicate records.
- Remove duplicate rows using Pandas.
- Compare the dataset size before and after cleaning.
- Save the cleaned dataset as a CSV file.

Technologies Used

- Python
- Pandas
- Jupyter Notebook

Dataset Description

The program uses a sample employee dataset containing the following columns:

Column| Description
Name| Employee name
Age| Employee age
Department| Employee department
Salary| Employee salary

The dataset contains 7 records, including 2 duplicate records.

Python Functions Used

- "pd.DataFrame()" – Creates a DataFrame.
- "duplicated()" – Identifies duplicate records.
- "drop_duplicates()" – Removes duplicate records.
- "len()" – Counts the total number of rows.
- "to_csv()" – Saves the cleaned dataset into a CSV file.

Output

Description| Count
Total records before cleaning| 7
Duplicate records found| 2
Total records after cleaning| 5

Project Files

- "duplicate_records.py" – Python source code.
- "cleaned_dataset.csv" – Cleaned employee dataset.
- "README.md" – Project documentation.

How to Run the Project

1. Install Python on your system.

2. Install Pandas:
   
   pip install pandas

3. Open Jupyter Notebook or VS Code.

4. Run the Python program.

5. Check the output and generated CSV file.

What I Learned

Through this task, I learned how to:

- Work with Pandas DataFrames.
- Detect duplicate records.
- Clean datasets using Pandas.
- Compare records before and after cleaning.
- Export cleaned data into CSV format.

Conclusion

This project helped me understand the importance of data cleaning in data analysis. Removing duplicate records improves data quality and helps produce more accurate results.

Internship: Veda Technology
Task: Identify and Remove Duplicate Records Using Pandas
Status: Completed