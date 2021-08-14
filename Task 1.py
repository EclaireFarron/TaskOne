#!/usr/bin/env python
# coding: utf-8

# Import excel into Python

# In[1]:


import pandas as pd
df = pd.read_excel (r'data.xlsx')
print (df)


# In[2]:


display(df)


# View all the data

# In[3]:


pd.set_option('display.max_rows', None)
display(df)


# Find out how many regions are in the data set.

# In[13]:


df.Region.unique()


# The regions in the data set are East and West.

# Find out the cities in the data set.

# In[14]:


df.City.unique()


# The countries in the data set are Boston, Los Angeles, New York and San Diego.

# Find out the categories in the data set.

# In[15]:


df.Category.unique()


# The categories in the data set are Bars, Crackers, Cookies and Snacks.

# Find out the products in the data set.

# In[16]:


df.Product.unique()


# The types of product in the data set are Carrot, Whole Wheat, Chocolate Chip, Arrowroot, Potato Chips, Oatmeal Raisin, bran, Pretzels and Banana.

# Comparing the total value from each region.

# In[23]:


EastTotalValue = df.loc[df['Region'] == 'East', 'TotalPrice'].sum()
print(EastTotalValue)


# In[24]:


WestTotalValue = df.loc[df['Region'] == 'West', 'TotalPrice'].sum()
print(WestTotalValue)


# In[41]:


RegionValueData = pd.DataFrame({'Region':['East', 'West'], 'TotalPrice':[EastTotalValue, WestTotalValue]})
RegionValueChart = RegionValueData.plot.bar(x='Region', y='TotalPrice', rot=0)


# In[42]:


BostonTotalValue = df.loc[df['City'] == 'Boston', 'TotalPrice'].sum()
print("Boston Total Value = " + str(BostonTotalValue))
LosAngelesTotalValue = df.loc[df['City'] == "Los Angeles", 'TotalPrice'].sum()
print("Los Angeles Total Value = " + str(LosAngelesTotalValue))
NewYorkTotalValue = df.loc[df['City'] == "New York", 'TotalPrice'].sum()
print("New York Total Value = " + str(NewYorkTotalValue))
SanDiegoTotalValue = df.loc[df['City'] == "San Diego", 'TotalPrice'].sum()
print("San Diego Total Value = " + str(SanDiegoTotalValue))
print("Total Price Combined = " + str(SanDiegoTotalValue + NewYorkTotalValue + LosAngelesTotalValue + BostonTotalValue))


# In[43]:


CityValueData = pd.DataFrame({'City':['Boston', 'Los Angeles','New York','San Diego'], 'TotalPrice':[BostonTotalValue, LosAngelesTotalValue,NewYorkTotalValue,SanDiegoTotalValue]})
CityValueChart = CityValueData.plot.bar(x='City', y='TotalPrice', rot=0)


# In[40]:


BarsTotalValue = df.loc[df['Category'] == 'Bars', 'TotalPrice'].sum()
print("Bars Total Value = " + str(BarsTotalValue))
CrackersTotalValue = df.loc[df['Category'] == "Crackers", 'TotalPrice'].sum()
print("Crackers Total Value = " + str(CrackersTotalValue))
CookiesTotalValue = df.loc[df['Category'] == "Cookies", 'TotalPrice'].sum()
print("Cookies Total Value = " + str(CookiesTotalValue))
SnacksTotalValue = df.loc[df['Category'] == "Snacks", 'TotalPrice'].sum()
print("Snacks Total Value = " + str(SnacksTotalValue))
print("Total Price Combined = " + str(SnacksTotalValue + CookiesTotalValue + CrackersTotalValue + BarsTotalValue))


# In[44]:


CategoryValueData = pd.DataFrame({'Category':['Bars', 'Crackers','Cookies','Snacks'], 'TotalPrice':[BarsTotalValue, CrackersTotalValue,CookiesTotalValue,SnacksTotalValue]})
CategoryValueChart = CategoryValueData.plot.bar(x='Category', y='TotalPrice', rot=0)


# In[45]:


BarsTotalQuantity = df.loc[df['Category'] == 'Bars', 'Quantity'].sum()
print("Bars Total Value = " + str(BarsTotalQuantity))
CrackersTotalQuantity = df.loc[df['Category'] == "Crackers", 'Quantity'].sum()
print("Crackers Total Value = " + str(CrackersTotalQuantity))
CookiesTotalQuantity = df.loc[df['Category'] == "Cookies", 'Quantity'].sum()
print("Cookies Total Value = " + str(CookiesTotalQuantity))
SnacksTotalQuantity = df.loc[df['Category'] == "Snacks", 'Quantity'].sum()
print("Snacks Total Value = " + str(SnacksTotalQuantity))


# In[50]:


CategoryQuantityData = pd.DataFrame({'Category':['Bars', 'Crackers','Cookies','Snacks'], 'TotalQuantity':[BarsTotalQuantity, CrackersTotalQuantity,CookiesTotalQuantity,SnacksTotalQuantity]})
CategoryQuantityChart = CategoryQuantityData.plot.bar(x='Category', y='TotalQuantity', rot=0)


# # Overview

# East and West region total amount

# In[47]:


RegionValueData = pd.DataFrame({'Region':['East', 'West'], 'TotalPrice':[EastTotalValue, WestTotalValue]})
RegionValueChart = RegionValueData.plot.bar(x='Region', y='TotalPrice', rot=0)


# Total price by cities

# In[48]:


CityValueData = pd.DataFrame({'City':['Boston', 'Los Angeles','New York','San Diego'], 'TotalPrice':[BostonTotalValue, LosAngelesTotalValue,NewYorkTotalValue,SanDiegoTotalValue]})
CityValueChart = CityValueData.plot.bar(x='City', y='TotalPrice', rot=0)


# Total price based on category

# In[49]:


CategoryValueData = pd.DataFrame({'Category':['Bars', 'Crackers','Cookies','Snacks'], 'TotalPrice':[BarsTotalValue, CrackersTotalValue,CookiesTotalValue,SnacksTotalValue]})
CategoryValueChart = CategoryValueData.plot.bar(x='Category', y='TotalPrice', rot=0)


# Total quantity based on category

# In[51]:


CategoryQuantityData = pd.DataFrame({'Category':['Bars', 'Crackers','Cookies','Snacks'], 'TotalQuantity':[BarsTotalQuantity, CrackersTotalQuantity,CookiesTotalQuantity,SnacksTotalQuantity]})
CategoryQuantityChart = CategoryQuantityData.plot.bar(x='Category', y='TotalQuantity', rot=0)


# # Granular

# In[52]:


display(df)


# In[53]:


df_CategoryProduct = df.groupby(['Category','Product']).sum()
display(df_CategoryProduct)


# Total price of each product

# In[69]:


CategoryProductData = pd.DataFrame({'Category/Product':['Bars/Banana', 'Bars/Bran', 'Bars/Carrot', 'Cookies/Arrowroot', 'Cookies/Chocolate Chip', 'Cookies/Oatmeal Raisin', 'Crackers/Whole Wheat', 'Snacks/Potato Chips', 'Snacks/Pretzels'], 'TotalPrice':[179.33, 2945.25, 7410.99,5330.10,4572.15,7310.16,3339.93,1651.77,585.90]})
print(179.33+2945.25+7410.99+5330.10+4572.15+7310.16+3339.93+1651.77+585.90)
CategoryProductChart = CategoryProductData.plot.barh(x='Category/Product', y='TotalPrice')


# In[61]:


import matplotlib.pyplot as plt
df_CityCategoryProduct = df.groupby(['City','Category','Product']).sum()
display(df_CityCategoryProduct)


# Total price of products in the city of Boston

# In[70]:


BostonCityTotalPriceData = pd.DataFrame({'Boston/Category/Product':['Boston/Bars/Banana', 'Boston/Bars/Bran', 'Boston/Bars/Carrot', 'Boston/Cookies/Arrowroot', 'Boston/Cookies/Chocolate Chip', 'Boston/Cookies/Oatmeal Raisin', 'Boston/Crackers/Whole Wheat', 'Boston/Snacks/Potato Chips', 'Boston/Snacks/Pretzels'], 'TotalPrice':[179.33, 873.29, 2267.37,1918.40,1200.54,3362.56,2533.74,344.40,585.90]})
BostonCityTotalPriceChart = BostonCityTotalPriceData.plot.barh(x='Boston/Category/Product', y='TotalPrice')


# Total quantity of products sold in Boston

# In[71]:


BostonCityTotalQuantityData = pd.DataFrame({'Boston/Category/Product':['Boston/Bars/Banana', 'Boston/Bars/Bran', 'Boston/Bars/Carrot', 'Boston/Cookies/Arrowroot', 'Boston/Cookies/Chocolate Chip', 'Boston/Cookies/Oatmeal Raisin', 'Boston/Crackers/Whole Wheat', 'Boston/Snacks/Potato Chips', 'Boston/Snacks/Pretzels'], 'Quantity':[79, 467, 1281,880,642,1184,726,205,186]})
BostonCityTotalQuantityChart = BostonCityTotalQuantityData.plot.barh(x='Boston/Category/Product', y='Quantity')


# Total price of products in the city of Los Angeles

# In[72]:


LosAngelesCityTotalPriceData = pd.DataFrame({'LosAngeles/Category/Product':['LosAngeles/Bars/Banana', 'LosAngeles/Bars/Bran', 'LosAngeles/Bars/Carrot', 'LosAngeles/Cookies/Arrowroot', 'LosAngeles/Cookies/Chocolate Chip', 'LosAngeles/Cookies/Oatmeal Raisin', 'LosAngeles/Crackers/Whole Wheat', 'LosAngeles/Snacks/Potato Chips', 'LosAngeles/Snacks/Pretzels'], 'TotalPrice':[0,652.63,2233.74,403.30,1565.19,2076.04,146.58,609.84,0]})
LosAngelesCityTotalPriceChart = LosAngelesCityTotalPriceData.plot.barh(x='LosAngeles/Category/Product', y='TotalPrice')


# Total quantity of products sold in Los Angeles

# In[74]:


LosAngelesCityTotalQuantityData = pd.DataFrame({'LosAngeles/Category/Product':['LosAngeles/Bars/Banana', 'LosAngeles/Bars/Bran', 'LosAngeles/Bars/Carrot', 'LosAngeles/Cookies/Arrowroot', 'LosAngeles/Cookies/Chocolate Chip', 'LosAngeles/Cookies/Oatmeal Raisin', 'LosAngeles/Crackers/Whole Wheat', 'LosAngeles/Snacks/Potato Chips', 'LosAngeles/Snacks/Pretzels'], 'Quantity':[0,349,1262,185,837,731,42,363,0]})
LosAngelesCityTotalQuantityChart = LosAngelesCityTotalQuantityData.plot.barh(x='LosAngeles/Category/Product', y='Quantity')


# Total price of products in the city of New York

# In[76]:


NewYorkCityTotalPriceData = pd.DataFrame({'NewYork/Category/Product':['NewYork/Bars/Banana', 'NewYork/Bars/Bran', 'NewYork/Bars/Carrot', 'NewYork/Cookies/Arrowroot', 'NewYork/Cookies/Chocolate Chip', 'NewYork/Cookies/Oatmeal Raisin', 'NewYork/Crackers/Whole Wheat', 'NewYork/Snacks/Potato Chips', 'NewYork/Snacks/Pretzels'], 'TotalPrice':[0,1052.81,1982.40,2025.22,878.90,1297.88,492.09,529.53,0]})
NewYorkCityTotalPriceChart = NewYorkCityTotalPriceData.plot.barh(x='NewYork/Category/Product', y='TotalPrice')


# Total quantity of products in the city of New York

# In[77]:


NewYorkCityTotalQuantityData = pd.DataFrame({'NewYork/Category/Product':['NewYork/Bars/Banana', 'NewYork/Bars/Bran', 'NewYork/Bars/Carrot', 'NewYork/Cookies/Arrowroot', 'NewYork/Cookies/Chocolate Chip', 'NewYork/Cookies/Oatmeal Raisin', 'NewYork/Crackers/Whole Wheat', 'NewYork/Snacks/Potato Chips', 'NewYork/Snacks/Pretzels'], 'Quantity':[0,563,1120,929,470,457,141,326,0]})
NewYorkCityTotalQuantityChart = NewYorkCityTotalQuantityData.plot.barh(x='NewYork/Category/Product', y='Quantity')


# Total price of products in the city of San Diego

# In[78]:


SanDiegoCityTotalPriceData = pd.DataFrame({'SanDiego/Category/Product':['SanDiego/Bars/Banana', 'SanDiego/Bars/Bran', 'SanDiego/Bars/Carrot', 'SanDiego/Cookies/Arrowroot', 'SanDiego/Cookies/Chocolate Chip', 'SanDiego/Cookies/Oatmeal Raisin', 'SanDiego/Crackers/Whole Wheat', 'SanDiego/Snacks/Potato Chips', 'SanDiego/Snacks/Pretzels'], 'TotalPrice':[0,366.52,927.48,983.18,927.52,573.68,167.52,168.00,0]})
SanDiegoCityTotalPriceChart = SanDiegoCityTotalPriceData.plot.barh(x='SanDiego/Category/Product', y='TotalPrice')


# Total quantity of products in the city of San Diego

# In[88]:


SanDiegoCityTotalQuantityData = pd.DataFrame({'SanDiego/Category/Product':['SanDiego/Bars/Banana', 'SanDiego/Bars/Bran', 'SanDiego/Bars/Carrot', 'SanDiego/Cookies/Arrowroot', 'SanDiego/Cookies/Chocolate Chip', 'SanDiego/Cookies/Oatmeal Raisin', 'SanDiego/Crackers/Whole Wheat', 'SanDiego/Snacks/Potato Chips', 'SanDiego/Snacks/Pretzels'], 'Quantity':[0,196,524,451,496,202,48,100,0]})
SanDiegoCityTotalQuantityChart = SanDiegoCityTotalQuantityData.plot.barh(x='SanDiego/Category/Product', y='Quantity')


# Total price of products in the cities

# In[89]:


TotalPriceOfCitiesData = pd.DataFrame({'City/Category/Product':['Boston/Bars/Banana', 'Boston/Bars/Bran', 'Boston/Bars/Carrot', 'Boston/Cookies/Arrowroot', 'Boston/Cookies/Chocolate Chip', 'Boston/Cookies/Oatmeal Raisin', 'Boston/Crackers/Whole Wheat', 'Boston/Snacks/Potato Chips', 'Boston/Snacks/Pretzels','LosAngeles/Bars/Banana', 'LosAngeles/Bars/Bran', 'LosAngeles/Bars/Carrot', 'LosAngeles/Cookies/Arrowroot', 'LosAngeles/Cookies/Chocolate Chip', 'LosAngeles/Cookies/Oatmeal Raisin', 'LosAngeles/Crackers/Whole Wheat', 'LosAngeles/Snacks/Potato Chips', 'LosAngeles/Snacks/Pretzels','NewYork/Bars/Banana', 'NewYork/Bars/Bran', 'NewYork/Bars/Carrot', 'NewYork/Cookies/Arrowroot', 'NewYork/Cookies/Chocolate Chip', 'NewYork/Cookies/Oatmeal Raisin', 'NewYork/Crackers/Whole Wheat', 'NewYork/Snacks/Potato Chips', 'NewYork/Snacks/Pretzels','SanDiego/Bars/Banana', 'SanDiego/Bars/Bran', 'SanDiego/Bars/Carrot', 'SanDiego/Cookies/Arrowroot', 'SanDiego/Cookies/Chocolate Chip', 'SanDiego/Cookies/Oatmeal Raisin', 'SanDiego/Crackers/Whole Wheat', 'SanDiego/Snacks/Potato Chips', 'SanDiego/Snacks/Pretzels'], 'TotalPrice':[179.33, 873.29, 2267.37,1918.40,1200.54,3362.56,2533.74,344.40,585.90,0,652.63,2233.74,403.30,1565.19,2076.04,146.58,609.84,0,0,1052.81,1982.40,2025.22,878.90,1297.88,492.09,529.53,0,0,366.52,927.48,983.18,927.52,573.68,167.52,168.00,0]})
TotalPriceOfCitiesChart = TotalPriceOfCitiesData.plot.barh(x='City/Category/Product', y='TotalPrice' ,figsize=(10,20))


# Total quantity of products in the cities

# In[90]:


TotalQuantityOfCitiesData = pd.DataFrame({'City/Category/Product':['Boston/Bars/Banana', 'Boston/Bars/Bran', 'Boston/Bars/Carrot', 'Boston/Cookies/Arrowroot', 'Boston/Cookies/Chocolate Chip', 'Boston/Cookies/Oatmeal Raisin', 'Boston/Crackers/Whole Wheat', 'Boston/Snacks/Potato Chips', 'Boston/Snacks/Pretzels','LosAngeles/Bars/Banana', 'LosAngeles/Bars/Bran', 'LosAngeles/Bars/Carrot', 'LosAngeles/Cookies/Arrowroot', 'LosAngeles/Cookies/Chocolate Chip', 'LosAngeles/Cookies/Oatmeal Raisin', 'LosAngeles/Crackers/Whole Wheat', 'LosAngeles/Snacks/Potato Chips', 'LosAngeles/Snacks/Pretzels','NewYork/Bars/Banana', 'NewYork/Bars/Bran', 'NewYork/Bars/Carrot', 'NewYork/Cookies/Arrowroot', 'NewYork/Cookies/Chocolate Chip', 'NewYork/Cookies/Oatmeal Raisin', 'NewYork/Crackers/Whole Wheat', 'NewYork/Snacks/Potato Chips', 'NewYork/Snacks/Pretzels','SanDiego/Bars/Banana', 'SanDiego/Bars/Bran', 'SanDiego/Bars/Carrot', 'SanDiego/Cookies/Arrowroot', 'SanDiego/Cookies/Chocolate Chip', 'SanDiego/Cookies/Oatmeal Raisin', 'SanDiego/Crackers/Whole Wheat', 'SanDiego/Snacks/Potato Chips', 'SanDiego/Snacks/Pretzels'], 'Quantity':[79, 467, 1281,880,642,1184,726,205,186,0,349,1262,185,837,731,42,363,0,0,563,1120,929,470,457,141,326,0,0,196,524,451,496,202,48,100,0]})
TotalQuantityOfCitiesChart = TotalQuantityOfCitiesData.plot.barh(x='City/Category/Product', y='Quantity' ,figsize=(10,20))


# In[ ]:




