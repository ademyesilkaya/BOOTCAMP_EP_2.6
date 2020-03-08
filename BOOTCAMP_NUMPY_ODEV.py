#!/usr/bin/env python
# coding: utf-8

# In[8]:


#BOOTCAMP NUMPY SORU_1
import numpy as np
y = np.arange(2,201,2).reshape(10,10)
y


# In[3]:


#BOOTCAMP NUMPY SORU_2
import numpy as np
def yeni_dizi(satir,sutun):
    yeni_dizi=np.full((int(satir),int(sutun)),0)
    yeni_dizi[0]=[1]
    yeni_dizi[int(satir)-1]=[1]
    yeni_dizi[:,0]=[1]
    yeni_dizi[:,int(sutun)-1]=[1]
    return yeni_dizi


# In[7]:


yeni_dizi(10,14)


# In[ ]:




