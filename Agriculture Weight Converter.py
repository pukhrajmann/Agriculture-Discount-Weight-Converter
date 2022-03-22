#!/usr/bin/env python
# coding: utf-8

# In[18]:


#Inputs
cost = 15
rate = 0.075

#Define Function
def converter(cost,rate):
    
    '''Determine the sell prices of a crop based on the base and discount rate for bulk purchase Input: int,float Output list'''
    
    #Intitalize lists and values
    cost_list = []
    disc_list = []
    grams_ounce = 28.35
    conversation = [.125,.25,.5,1]
    
    #Loop to convert grams to ounces
    for x in range(len(conversation)):
        adj_cost = grams_ounce*cost*conversation[x]
        cost_list.append(adj_cost)
    
    #Loop to discount bulk purchase
    for x in range(len(cost_list)):
        disc = round(cost_list[x]*(1-(rate*(x+1))),2)
        disc_list.append(disc)
    
    #Return Discount list
    return(disc_list)

#Function Call
converter(cost,rate)


# In[ ]:




