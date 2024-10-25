#!/usr/bin/env python
# coding: utf-8

# In[137]:


import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[138]:


#get_ipython().system('ls')


# In[139]:


df=pd.read_csv('student_performance_data.csv')


# In[140]:


df=pd.DataFrame(df)
df


# In[141]:


df.dtypes


# In[142]:


df.describe()


# In[143]:


#To show missing data
df.isnull().sum()


# In[ ]:





# In[144]:


df['Gender'].value_counts().plot(kind='pie', title= 'Frequency of Gender')


# In[145]:


df['Major'].value_counts().plot(kind='pie', title= "Frequency of Majors", autopct='%1.1f%%')


# In[146]:


gpa_stats = df.groupby('Gender')['GPA'].agg(['max', 'min', 'mean']).reset_index()
gpa_stats.columns = ['Gender', 'Max GPA', 'Min GPA', 'Mean GPA']
gpa_stats


# In[150]:


gpa_stats = df.groupby('Major')['GPA'].agg(['max', 'min', 'mean']).reset_index()
gpa_stats.columns = ['Major', 'Max GPA', 'Min GPA', 'Mean GPA']
gpa_stats


# In[148]:




# Sample data for demonstration
data = {
    'Major': ['Math', 'Science', 'Arts', 'Engineering', 'Business'],
    'GPA': [3.5, 3.7, 3.2, 3.8, 3.6]
}
df = pd.DataFrame(data)

# Calculate mean GPA per Major
mean_gpa = df.groupby('Major')['GPA'].mean().reset_index()
mean_gpa = mean_gpa.sort_values('Major')

# Streamlit app
st.title('Mean GPA per Major')

# Create a plot
plt.figure(figsize=(10, 6))
plt.plot(mean_gpa['Major'], mean_gpa['GPA'], marker='o')
plt.title('Mean GPA per Major')
plt.xlabel('Major')
plt.ylabel('Mean GPA')
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()

# Display the plot in Streamlit
st.pyplot(plt)

# Optionally display the data in a table
st.write('Mean GPA Data:', mean_gpa)


# In[149]:


#crosstab_gender_major = pd.crosstab(df['Gender'], df['Major'])
#print(crosstab_gender_major)


# In[ ]:




