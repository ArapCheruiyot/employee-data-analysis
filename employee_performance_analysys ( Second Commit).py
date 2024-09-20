# -*- coding: utf-8 -*-
"""Employee Performance Analysys

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17Xg3VrkFxfTX24tMutApJeTFHej7P_5X

## **Importing Required Libray And Reading Employee Recoreds Data**
"""

import pandas as pd

df = pd.read_excel("/content/project_2_-_employee_performance_-_final[1].xlsx")
df.info()

"""## **Inspacting the File**"""

df.head()

"""## **Checking size of the file (Rows And Columns)**"""

size = df.shape
print(f"Our File has {size[0]} Rows and {size[1]} Columns")

"""## **Getting Genreal information about the file**"""

df.info()

"""# **Step 1 Data Cleaning.** Note that All information on this file is ok and no need for alterring, but we will just demosntaret how missing values can be froped from the file if need be"""

#cleaned_df = df.dropna()
#cleaned_df

"""## **Checkiing for missing values in the file**"""

df.isnull().sum()



"""## **Checkking for duplicates in the file**"""

duplicated = df[df.duplicated()]
duplicated.sum()

"""## **Removing duplicates**"""

df = df.drop_duplicates()
df.info()