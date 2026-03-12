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
I downloaded .csv file from Kaggle (oms_orders_places.csv)(https://www.kaggle.com/datasets/carrie1/ecommerce-data?resource=download) and in generate_noise.py file I generated copy of the following file (wms_shipped_units.csv), to simulate data from another providor, allowing me to run entire recocniliation process.

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
- duplicates detection - identifying duplicate records that could distort the comparison results. After that, duplicated records will be moved into separated files.

Step 4: 
Comparison
Having standardized the data in the Validation phase, now we perform a direct "side-by-side" analysis to pinpoint exactly where the two systems diverge.

This step includes:
- Multi-level Matching: Using composite reconciliation key (`InvoiceNo` + `StockCode` + `Quantity`) to align records across both datasets at the most granular level.
- Completeness Gap Analysis: Full Outer Join to identify orphan records:
    - OMS-only records: transactions in OMS but missing in WMS (potential lost shipments)
    - WMS-only records: transactions in WMS but missing in OMS (potential ghost records)
- Numerical Variance Calculation: Quantifying differences in UnitPrice and other metrics for matched records.
- Duplicate & Error Impact: Analyzing how flagged records (duplicates, invalid dates, missing prices) affect reconciliation results.
- Financial Impact Assessment: Aggregating variances into total Net Variance showing financial exposure.
- Root Cause Cross-Referencing: Linking discrepancies back to Validation flags to identify systematic issues.

Step 5: Error Detection and Root Cause Analysis 
After comparison identified discrepancies between OMS and WMS systems, the next critical step is understanding WHY these errors occurred and categorizing them by type and impact.

This phase transforms raw discrepancy data into structured analysis of error patterns and root causes through systematic investigation.

Key activities include:
- Error categorization by type and financial impact (Data Quality: £17,945 exposure, System Sync: 5,350 records, Business Logic: 983 records)
- Root cause investigation for each error category (ETL failures, system migration issues, message queue problems)
- Pattern analysis across products and customer segments to identify systematic vs. isolated issues
- Validation effectiveness review to identify gaps in current error detection processes (90.1% detection rate achieved)

The outcome is a comprehensive understanding of error causes and patterns that provides the foundation for the Resolution phase, where remediation strategies will be developed and prioritized.

This step is essential because knowing that errors exist is only half the battle - understanding their causes and detection effectiveness is what enables effective resolution planning.