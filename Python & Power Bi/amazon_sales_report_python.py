# -*- coding: utf-8 -*-
"""Amazon Sales Report Python.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1S_xnsJPxmMzazbpmS_n0I5I-Sa0h92L3
"""

from google.colab import files
uploaded=files.upload()

import pandas as pd
import numpy as np
df=pd.read_excel('/content/Amazon Sales.xlsx') #read excel file
df
df.head(10) #first row
df.tail(10) #last row
df.loc[0:10,'product_id':'discounted_price']
df['rating']
new=df.fillna("TBD")
new
df.shape # Display the first few rows and shape of the DataFrame