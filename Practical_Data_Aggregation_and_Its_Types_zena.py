#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd

# Step 1: Create Sample Dataset
Zena = {
    'Region': ['North', 'South', 'East', 'West', 'North', 'South', 'East', 'West'],
    'Product': ['A', 'B', 'A', 'B', 'C', 'C', 'B', 'A'],
    'Sales': [150, 200, 300, 400, 250, 180, 220, 310],
    'Quantity': [10, 15, 20, 25, 12, 14, 16, 18],

}


# In[13]:



df = pd.DataFrame(data)
print("Sample Dataset:\n", df)


# In[9]:


# Step 2: Grouping and Aggregation
# Aggregating Sales by Region (Sum Aggregation)
sales_by_region = df.groupby('Region')['Sales'].sum()
print("\nTotal Sales by Region:\n", sales_by_region)


# In[15]:



# Aggregating Sales and Quantity by Product (Mean Aggregation)
mean_by_product_zena = df.groupby('Product')[['Sales', 'Quantity']].mean()
print("\nMean Sales and Quantity by Product:\n", mean_by_product)


# In[11]:


# Aggregating Count of Sales by Region (Count Aggregation)
count_by_region_zena = df.groupby('Region')['Sales'].count()
print("\nCount of Sales Records by Region:\n", count_by_region)


# In[18]:


# Custom Aggregation: Calculate Min and Max Sales by Region
custom_aggregation_zena = df.groupby('Region')['Sales'].agg(['min', 'max'])
print("\nCustom Aggregation (Min and Max Sales by Region):\n", custom_aggregation)


# In[21]:


# Step 3: Multi-Level Aggregation
# Aggregating Sales by Region and Product
multi_level_agg_zena = df.groupby(['Region', 'Product'])['Sales'].sum()
print("\nSales by Region and Product:\n", multi_level_agg_zena)


# In[22]:


# Step 4: Reset Index for Multi-Level Aggregation
multi_level_agg_reset_zena = multi_level_agg.reset_index()
print("\nSales by Region and Product (Reset Index):\n", multi_level_agg_reset_zena)


# In[41]:


import pandas as pd

zena = {
    'Region': ['North', 'South', 'East', 'West', 'North', 'South', 'East', 'West'],
    'City': ['City1', 'City2', 'City3', 'City4', 'City1', 'City2', 'City3', 'City4'],
    'Product': ['A', 'B', 'A', 'B', 'C', 'C', 'B', 'A'],
    'Sales': [150, 200, 300, 400, 250, 180, 220, 310],
    'Quantity': [10, 15, 20, 25, 12, 14, 16, 18],
    'Date': pd.to_datetime(['2026-01-01', '2026-01-02', '2026-02-01', '2026-02-03',
                            '2026-03-01', '2026-03-02', '2026-04-01', '2026-04-03'])
}
    


# In[56]:


df = pd.DataFrame(zena)
print("Extended Dataset:\n", df)


# 

# In[57]:


df.set_index('Date', inplace=True)
monthly_sales = df.resample('M')['Sales'].sum()
print("\nTotal Sales by Month:\n", monthly_sales)


# In[58]:


quarterly_sales = df.resample('Q')['Sales'].sum()
print("\nTotal Sales by Quarter:\n", quarterly_sales)


# In[59]:


yearly_sales = df.resample('Y')['Sales'].sum()
print("\nTotal Sales by Year:\n", yearly_sales)


# In[60]:


df.reset_index(inplace=True)
sales_by_region = df.groupby('Region')['Sales'].sum()
print("\nTotal Sales by Region:\n", sales_by_region)


# In[61]:


sales_by_city = df.groupby('City')['Sales'].sum()
print("\nTotal Sales by City:\n", sales_by_city)


# In[62]:


sales_by_region_city = df.groupby(['Region', 'City'])['Sales'].sum()
print("\nTotal Sales by Region and City:\n", sales_by_region_city)


# In[63]:


sales_by_region_city_reset = sales_by_region_city.reset_index()


# In[ ]:





# In[ ]:





# In[ ]:




