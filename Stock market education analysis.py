#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd


# In[13]:


stock_Edu = pd.read_csv("stock_market_education_analysis_sample.csv")


# In[14]:


stock_Edu


# In[15]:


stock_Edu.isna().sum()


# In[16]:


stock_Edu.dtypes


# In[17]:


stock_Edu.info()


# # Market Segmentation Criteria

# In[18]:


def Age_Segmentation(Age):
    if Age >= 18 and Age <=25:
        return "Young Adults"
    if Age > 25 and Age <=35:
        return "Early Career Professionals"
    if Age > 36 and Age <=50:
        return "Mid-Career Professionals"
    if Age > 50:
        return "Late-Career and Retirees"


# In[19]:


stock_Edu["Age_Segment"]=stock_Edu.apply(lambda x:Age_Segmentation(x["Age"]), axis=1)


# In[20]:


stock_Edu


# In[21]:


stock_Edu['ID'] = range(1, len(stock_Edu) + 1)


# In[22]:


stock_Edu


# In[23]:


stock_Edu.groupby(by=["Age_Segment"])["ID"].count()


# Age Level Segments:

# 
# Early Career Professionals (192 individuals)
# This segment typically includes individuals aged 25-35 who are at the beginning of their professional careers. They are often looking to establish financial stability and are motivated by career advancement and financial independence. Early career professionals might prefer flexible learning options, such as online or blended courses, to balance work and education. They are keen on gaining practical skills that can quickly translate into better job opportunities or salary increases.
# 
# Late-Career and Retirees (289 individuals)
# This segment includes individuals aged 50 and above, many of whom are either approaching retirement or are already retired. Their primary motivations might include securing their financial future, managing their retirement funds, or pursuing personal interests. They may have more time to dedicate to learning and might prefer in-person or longer-term courses. This group values the reputation and quality of the course highly, as they are looking for reliable and trustworthy education to manage their investments effectively.
# 
# Mid-Career Professionals (322 individuals)
# Mid-career professionals are typically aged 35-50 and are established in their careers. They may have higher disposable incomes and are likely motivated by income diversification, financial independence, and career advancement. This segment might seek advanced courses to deepen their knowledge and skills in stock market investing. They prefer courses that offer flexibility, such as online or blended formats, to fit into their busy schedules. The cost and reputation of the course are significant factors for this group.
# 
# Young Adults (177 individuals)
# Young adults, typically aged 18-24, are either in college or just starting their professional journeys. They are often driven by personal interest and the desire to build a solid financial foundation early on. This group might prefer short-term courses that provide a broad overview of stock market basics. They may favor lower-cost or free online courses due to limited financial resources. Young adults are likely to be influenced by reviews and testimonials and value the accessibility and flexibility of online learning platforms.

# In[24]:


stock_Edu.groupby(by=["Education_Level"])["ID"].count()



# High School (344 individuals)
# This segment includes individuals whose highest level of education is a high school diploma. They might be students, young adults entering the workforce, or individuals who chose not to pursue higher education. Their motivations for stock market education could range from personal interest to financial independence and basic investment knowledge. They may prefer accessible, beginner-friendly, and cost-effective courses, often opting for online or short-term formats to get started with investing without significant financial or time commitments. Practical examples and easy-to-understand content are crucial for engaging this group.
# 
# Postgraduate (307 individuals)
# This segment consists of individuals who have completed postgraduate education, such as a master's degree or Ph.D. They are likely to be in professional careers and have a higher level of disposable income. Their motivations might include career advancement, income diversification, and advanced investment strategies. This group values in-depth, comprehensive courses with a strong reputation and high-quality content. They may prefer medium to long-term courses that provide advanced knowledge and practical applications. Blended learning formats that offer both online convenience and in-person networking opportunities could be attractive to this segment.
# 
# Undergraduate (349 individuals)
# Individuals in this segment have completed an undergraduate degree. They are typically early to mid-career professionals or recent graduates. Their motivations for stock market education include career advancement, financial independence, and building investment skills. They might prefer flexible learning methods, such as online or blended courses, that allow them to balance work and learning. Cost and course reputation are important considerations for this group, and they may seek courses that offer certifications to enhance their resumes. Practical, application-oriented content that can be directly implemented in their financial planning is highly valued by this segment.

# # Consumer Behaviour Analysis

# # Early Career Professionals (26-35)

# In[25]:


Early_Career_Professionals = stock_Edu[(stock_Edu["Age"] >= 26) & (stock_Edu["Age"] <=35)]
Early_Career_Professionals


# In[26]:


Learning_Methods = Early_Career_Professionals["Preferred_Learning_Method"].value_counts()
Learning_Methods


# In[27]:


key_Motivator = Early_Career_Professionals["Primary_Motivator"].value_counts()
key_Motivator


# # Influence factor Analysis

# Cost:

# In[28]:


Cost_Distribution = Early_Career_Professionals["Course_Cost"].value_counts()
Cost_Distribution


# Reputation:

# In[29]:


Reputation = Early_Career_Professionals["Course_Reputation"].value_counts()
Reputation


# Content Quality:

# In[30]:


Content_Quality_distribution = Early_Career_Professionals["Content_Quality"].value_counts()
Content_Quality_distribution


# Reviews and Testimonials:

# Reviews_Distribution:

# In[31]:


Reviews_Distribution = Early_Career_Professionals["Reviews_and_Testimonials"].value_counts()
Reviews_Distribution


# Visual Representation of Consumer behavior Analysis

# In[45]:


import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


# In[47]:


methods = Learning_Methods.index
counts = Learning_Methods.values

# Set the figure size
plt.figure(figsize=(10, 6))

# Create the bar plot
plt.bar(methods, counts, color=['blue', 'green', 'red'])

# Add title and labels
plt.title('Preferred Learning Methods')
plt.xlabel('Learning Method')
plt.ylabel('Count')

# Display the plot
plt.show()


# In[49]:


methods = key_Motivator.index
counts = key_Motivator.values

# Set the figure size
plt.figure(figsize=(10, 6))

# Create the bar plot
plt.bar(methods, counts, color=['blue', 'green', 'red','yellow'])

# Add title and labels
plt.title('key_Motivator')
plt.xlabel('Primary_Motivator')
plt.ylabel('Count')

# Display the plot
plt.show()


# In[ ]:




