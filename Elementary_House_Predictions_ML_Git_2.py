#!/usr/bin/env python
# coding: utf-8

# In[28]:


# sklearn.linear_model import LinearRegression is Used for predicting continuous values by fitting a straight line.
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd


# In[27]:


# Sample data: house size (sq ft) and price ($)
data = {
'size': [750, 800, 850, 900, 1000, 1200, 1500],
'price': [200000, 210000, 215000, 230000, 250000, 285000, 320000]
}
df = pd.DataFrame(data)


# In[26]:


# Spit data into features (X) and target (y)
X = df [['size']]
y = df ['price']


# In[25]:


# Create and train the model 
model = LinearRegression()
model.fit(X, y)


# In[35]:


# Make a prediction
new_house_size = pd.DataFrame({'size':[3500]})
predicted_price = model.predict(new_house_size)

print(f"Predicted price for a 3500 sq ft house: ${predicted_price[0]:,.2f} USD")


# In[ ]:




