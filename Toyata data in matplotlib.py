#!/usr/bin/env python
# coding: utf-8

# In[2]:


import  pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


df = pd.read_csv('D:\\Toyota.csv')
df


# In[4]:


df.head()


# In[5]:


df = pd.read_csv('D:\\Toyota.csv', index_col=0, na_values=["??", "???"])
df


# In[6]:


df_cleaned = df.dropna(axis = 0)


# In[7]:


df_cleaned


# In[8]:


plt.scatter(df['Age'],df['Price'],c='r')


# In[9]:


df.head()


# In[10]:


# To apply different colors


# In[11]:


data = {'Age': [23, 23, 26, 30, 32],
        'Price': [13500,13750,14950,13750,12950],
        'Color': ['r', 'g', 'b', 'y', 'm'],
       'Marker': ['o', 's', '^', 'D', '*']}  # List of colors
df = pd.DataFrame(data)

plt.scatter(df['Age'], df['Price'], c=df['Color'],cmap='viridis')
plt.title("Scatter plot of Price vs Age")


# #Horizontal

# In[12]:


plt.axhline(y=200, color='r', linestyle='--')


# In[13]:


plt.axhline(y=200, color='r', linestyle=':')


# In[14]:


plt.axhline(y=200, color='r', linestyle='-.')


# In[15]:


plt.axhline(y=200, color='r', linestyle='-')


# In[16]:


plt.axvline(x=35, color='g', linestyle='--')


# In[17]:


plt.axvspan(xmin=30, xmax=40, color='yellow', alpha=0.3)


# In[18]:


plt.axhspan(ymin=150, ymax=250, color='blue', alpha=0.3)


# In[19]:


color_map = {'r': 0, 'g': 1, 'b': 2, 'y': 3, 'm': 4}
df['ColorNum'] = df['Color'].map(color_map)


# In[20]:


# Create a color list and a custom color map
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

# Data
data = {'Age': [23, 23, 26, 30, 32],
        'Price': [13500,13750,14950,13750,12950],
        'Color': ['r', 'g', 'b', 'y', 'm'],
       'Marker': ['o', 's', '^', 'D', '*']}
df = pd.DataFrame(data)

# Map colors to numbers
color_map = {'r': 0, 'g': 1, 'b': 2, 'y': 3, 'm': 4}
df['ColorNum'] = df['Color'].map(color_map)

# Create a color list and a custom color map
colors = ['r', 'g', 'b', 'y', 'm']
cmap = mcolors.ListedColormap(colors)

# Plot
sc = plt.scatter(df['Age'], df['Price'], c=df['ColorNum'], cmap=cmap)

# Add color bar
cbar = plt.colorbar(sc, ticks=[0, 1, 2, 3, 4])
cbar.ax.set_yticklabels(['r', 'g', 'b', 'y', 'm'])

plt.title("Scatter plot of Price vs Age")
plt.xlabel("Age")
plt.ylabel("Price")
plt.show()


# In[21]:


#Histogram


# In[22]:


import  pandas as pd
import matplotlib.pyplot as plt


# In[23]:


df = pd.read_csv('D:\\Toyota.csv')
df


# In[24]:


plt.hist(df['Age'], bins=20)  


# In[25]:


plt.hist(df['Price'], bins=20) 


# In[26]:


df = df.dropna(subset=['Age'])
df


# In[27]:


plt.hist(df['Price'],bins =20)


# In[31]:


sns.regplot(x=df['Age'],y=df['Price'])


# In[ ]:





# In[ ]:




