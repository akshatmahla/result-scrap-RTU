#!/usr/bin/env python
# coding: utf-8

# In[1]:


from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests


# In[2]:


def getRes(roll):
    url = "https://www.rjlive.in/rtu/show-result?examno=4492&key=A035EB72743C885C28F7E9E557A82C643168DE15&no="
    url += roll
    html = requests.get(url)
    soup = BeautifulSoup(html.content,'lxml')
    #print(soup.prettify())
    My_table = soup.find('div',{'class':'rtu_Result'})
    res = My_table.prettify()
    roll += ".html"
    with open(roll, "w") as text_file:
        text_file.write(res)


# In[9]:


roll = input("start roll number")
rollend = input("end roll number")
rollint = int(roll[7:])
rollendint = int(rollend[7:])
#temproll = roll[:7] + str(rollint)
#print(temproll)
#getRes(temproll)
while rollint <= rollendint:
    temproll = roll[:7] + str(rollint)
    #print(temproll)
    getRes(temproll)
    rollint+=1


# In[ ]:




