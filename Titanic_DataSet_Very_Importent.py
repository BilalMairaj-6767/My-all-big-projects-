#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import matplotlib.pyplot as plt


# In[6]:


xyz = pd.read_csv(r"C:\Titanic-Dataset.csv")


# In[7]:


xyz


# In[8]:


xyz.mode


# In[9]:


xyz.head(5)


# In[10]:


xyz.tail(891)


# In[11]:


xyz['age_group' ] = pd.cut(xyz['Survived'],
bins=[0,12,18,35,60,100],
labels=['Child','Teen', 'Adult', 'Middle', 'Senior'])


# In[12]:


xyz


# * ***Overall survival rate:***
# 
# xyz['survived'].mean()
# 
# * **Survival by gender:**
# 
# xyz.groupby('sex')['survived'].mean()
# 
# * **Survival by passenger class:**
# 
# xyz.groupby('pclass')['survived'].mean()
# 
# * **Survival by age group:**
# 
# xyz.groupby('age_group')['survived'].mean()
# 
# * **Survival by embark town:**
# 
# xyz.groupby('embark_town')['survived'].mean()

# In[13]:


xyz['Survived'].mean()


# In[14]:


xyz.groupby('Sex')['Survived'].mean()


# In[15]:


xyz.groupby('Sex')['Survived'].mean() * 100


# In[16]:


xyz.groupby('PassengerId')['Survived'].mean() 


# In[17]:


xyz.groupby('Age')['Survived'].mean()


# In[18]:


xyz.groupby('Embarked')['Survived'].mean()


# ### **Distribution Analysis**
#  1.age distribution
#  
#  2.fare distribution

# ## 1.Age distribution

# In[19]:


import matplotlib.pyplot as plt
xyz['Age'].plot(kind='hist', bins=20)
plt.title("Age Distribution")
plt.show()


# In[20]:


import matplotlib.pyplot as plt
xyz['Age'].plot(kind='hist', bins=60)
plt.title("Age Distribution")
plt.show()


# In[21]:


plt.scatter(xyz.index, xyz['Age'])
plt.title("Age Distribution")
plt.show()


# ### 2.Fare distribution

# In[22]:


import matplotlib.pyplot as plt
xyz['Fare'].plot(kind='hist', bins=20)
plt.title("Fare Distribution")
plt.show()


# In[23]:


import matplotlib.pyplot as plt
xyz['Fare'].plot(kind='hist', bins = 16)
plt.title("Fare Distribution")
plt.show()


# ### ***gender ditribution***

# In[24]:


import matplotlib.pyplot as plt
xyz.groupby('Sex')['Survived'].mean().plot(kind='bar', color = ['pink', 'lightblue'])
plt.title("Survival Rate by Sex")
plt.show()


# In[25]:


xyz.isnull()


# In[26]:


xyz['Age' ].value_counts().head(10)


# In[27]:


xyz['Age'].fillna(xyz['Age'].median())


# In[28]:


xyz['Embarked'].head(891)


# In[29]:


xyz['Survived'].mean()


# In[30]:


xyz['Age'].head(10)


# In[31]:


xyz.groupby('Embarked')['PassengerId'].mean().plot(kind = 'bar', color = ['pink', 'lightblue', 'yellow'])
plt.grid()
plt.legend()
plt.show()


# In[32]:


xyz.groupby('Sex')['Survived' ].mean().plot(kind = 'bar', color = ['pink', 'lightblue'])
plt.title("Survival Rate by Gender")
plt.show()


# In[33]:


xyz.groupby('Sex')['Survived' ].value_counts().plot(kind = 'bar', color = ['pink', 'pink', 'lightblue', 'lightblue'])
plt.title("Survival by Gender")
plt.grid()
plt.show()


# In[34]:


xyz[xyz["Fare"] > xyz["Fare"].mean() + 2 * xyz["Fare"].std()]


# In[35]:


xyz.groupby(['Sex','PassengerId'])['Survived' ].mean(),pd.pivot_table(xyz, values='Survived', index='Sex', columns='PassengerId')


# In[36]:


xyz.groupby(['Sex', 'Age'])['Survived'].mean(),pd.pivot_table(xyz, values = 'Survived', index = 'Sex', columns = 'Age')


# In[37]:


xyz.groupby(['Sex', 'Embarked'])['Survived' ].mean()

pd.pivot_table(xyz,
values = 'Survived',
index = 'Sex',
columns = 'Embarked')


# In[38]:


xyz.to_csv("titanic_cleaned.csv", index=False)


# # ***finally machine learning is started now***

# In[39]:


datatoexcel = pd.ExcelWriter('titanic_data_cleaned_newexcel.xlsx')
xyz.to_excel(datatoexcel)
datatoexcel.close()
print('DataFrame is written to Excel File successfully. ')


# In[40]:


xyz_ml = pd.get_dummies(xyz, drop_first = True)


# In[41]:


xyz_ml.head(4)


# In[42]:


xyz_ml.tail(798)


# ### ***Pandas Important Functions***
# 
# 1. strf.time()
# 2. to_excel()
# 3. isin()
# 4. isna()
# 5. to_datetime()
# 6. aggfunc()
# 7. apply()
# 8. .agg
# 9. str.len
# 10. replace
# 11. extract()
# 12. get_dummies()
# 13. .boundary()

# In[43]:


from datetime import datetime
abc = datetime.now()
print(abc)


# In[44]:


import pandas as pd
date = pd.Timestamp.now()
print(date.strftime('%d-%m-%Y %H %M %S'))


# In[45]:


import pandas as pd
date = pd.Timestamp.now()
print(date.strftime('%d-%m-%y %H %M %S'))


# In[46]:


df = pd.DataFrame ({
'City':['Lahore', 'Karachi', 'Islamabad']

})


# In[47]:


df['City'].isin(['Lahore','Karachi'])


# In[48]:


xyz.isna


# In[49]:


xyz


# In[50]:


xyz.head(891)


# In[51]:


xyz.tail(1)


# ### ***18. Advanced Group Analysis***
# 
# * df.groupby(['sex','pclass'])['survived'].mean()
# * pd.pivot_table(df,
#     * values='survived',
#     * index='sex',
#     * columns='pclass')

# In[54]:


xyz.groupby(['Sex','PassengerId'])['Survived'].mean()
pd.pivot_table(xyz,
values='Survived',
index='Sex',
columns='PassengerId')


# In[ ]:




