This project simulates reconciliation process. The aim is to compare internal sales registration with external report from payment provider - which allows to identify discrepancies, missing payments and errors in prices.
At this stage it's important to talk about reconciliation stages:
1. Data Collection - data gathering from various source systems. 
2. Data Validation - validation process to ensure integrity, completeness and consistency. 
3. Comparison - data comparison to identify any discrepancies or differences. Can be done by matching key fields or variables that should be consistent across the datasets.
4. Error Detection - after comparison, any discrepancies or differences will be flagged as error. This step involves analysis of reasons of discrepancies. 
5. Resolution - taking corrective actions to align the data to ensure consistency. Depending of the nature of discrepancies, it can include manual adjustments, data transformations, system updates or communication with stakeholders to rectify the errors. 
6. Verification - rechecking and revalidating the data to ensure that the errors have been resolved and datasets now are aligned. 
7. Documentation - helps reconciliation activities, maintain audits etc.


Step 1: 
Data Collection
I downloaded .csv file from Kaggle (https://www.kaggle.com/datasets/carrie1/ecommerce-data?resource=download) and in generate_noise.py file I generated copy of the following file, to simulate data from another providor, allowing me to run entire recocniliation process. 

Step 2: Exploratory Data Analysis (EDA)
In this step, before I'll move to Valdiation process, it's necessary understand the structure and characteristics of the datasets. The objective is to identify potential anomalies, inconsistencies, and structural differences between the files.

This step include:
- dataset shape check - to verify if both files have same rows numbers, if not - differences in the number of records may indicate potential discrepancies between the systems.
- data type overview - reviewing the data types assigned to each column in order to identify potential inconsistencies (e.g., numerical values stored as strings or incorrect date formats).
- missing value identification - detecting null values
- unique values analysis - analyzing the number of unique values in key columns (e.g. order identifiers). Repeated values may indicate duplicate records or non-unique keys.
- descriptive statistics - generating summary statistics for numerical variables (mean, average, median, min, max, etc.).

! The purpose of EDA is to explore and understand the data, identify irregularities, and detect potential data quality issues before further processing.


Step 3: 
Validation
After the initial exploration, the next step is to prepare the datasets for comparison. Data validation focuses on ensuring that the datasets are technically consistent and properly formatted before conducting reconciliation.

This step include: 
- missing data verification - identifying gaps in the data and assessing whether they may affect the comparison process
- data type verification and standatization - ensuring that variables representing the same information in both files use consistend data types
- formatting standarization - detecting formatting inconsistencies, such as hidden spaces, inconsistent capitalization or irregular delimiters
- duplicates detection - identifying duplicate records that could distort the comparison results.