#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt

#initializing the data
x = [10, 20, 30, 40]
y = [20, 25, 35, 55]

#plotting the data
plt.plot(x, y)
plt.show()


# In[3]:


import pandas as pd

#reading the file
data = pd.read_csv("data bank.csv")

#printing the top 10 rows
display(data.head(10))


# In[1]:


import pandas as pd
import matplotlib.pyplot as plt

#reading the file
data = pd.read_csv("data bank.csv")

#scatter plot with marital against age
plt.scatter(data['marital'], data['age'])

#adding title to the plot
plt.title("Scatter Plot Data Bank")

#setting the x dan y labels
plt.xlabel('Marital')
plt.ylabel('Age')

#saving the figure 
plt.savefig("scatter plot.jpg")

plt.show()


# In[2]:


import pandas as pd
import matplotlib.pyplot as plt

# reading the file
data = pd.read_csv("data bank.csv")

#scc
plt.scatter(data["marital"], data["age"], c=data['day'], s=data['previous'])

#judul
plt.title("Scatter Plot")

# Set labels for x and y axes
plt.xlabel('Marital')
plt.ylabel('Age')

#saving the figure 
plt.savefig("scatter plot warna.jpg")

# Display the plot
plt.show()


# In[3]:


import pandas as pd
import matplotlib.pyplot as plt

#reading the file
data = pd.read_csv("data bank.csv")

#line chart with marital against age
plt.plot(data['marital']) 
plt.plot(data['age'])

#adding title to the line chart
plt.title("Line Chart Data Bank")

#setting the x dan y labels
plt.xlabel('Age')
plt.ylabel('Marital')

#saving the figure 
plt.savefig("line chart.jpg")

plt.show()


# In[4]:


import pandas as pd
import matplotlib.pyplot as plt

#reading the file
data = pd.read_csv("data bank.csv")

#bar chart with marital against age
plt.bar(data['marital'], data['age'])

#adding title to the bar chart
plt.title("Bar Chart Data Bank")

#setting the x dan y labels
plt.xlabel('Marital')
plt.ylabel('Age')

#saving the figure 
plt.savefig("bar chart.jpg")

plt.show()


# In[6]:


import pandas as pd
import matplotlib.pyplot as plt

#reading the database
data = pd.read_csv("data bank.csv")

#histogram with marital
plt.hist(data['marital']) 

#adding title to the histogram
plt.title("Histogram Data Marital")

#saving the figure 
plt.savefig("histogram.jpg")

plt.show()


# In[7]:


import pandas as pd
import matplotlib.pyplot as plt

#reading the file
data = pd.read_csv("data bank.csv")

#initializing the data
marital = ['married', 'single', 'divorced']
age = [30, 45, 55]

#plotting the data
plt.pie(age, labels=marital)

#adding title to the car
plt.title("Car Data Bank")

#saving the figure 
plt.savefig("pie chart.jpg")

plt.show()


# In[ ]:




