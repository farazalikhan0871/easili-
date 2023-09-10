#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pymysql


# In[7]:


connection = pymysql.connect(host = 'localhost',
                              user = 'root',
                            password = 'Faraz@12345',
                            database = 'library')


# In[8]:


cursor = connection.cursor()


# In[10]:


sql1 = '''
create table table1(
col1 int primary key,
col2 int,
col3 int);
'''


# In[11]:


cursor.execute(sql1) ## executing the table


# In[34]:


col1_val = int(input("enter the first value"))    ## giving value dynamic values
col2_val = int(input("enter the secound value"))
col3_val = int(input("enter the third value"))


# In[ ]:





# In[ ]:





# In[35]:


sql2 = "insert into table1 values (%s,%s,%s)"     ## inserting the value into the table 
cursor.execute(sql2,(col1_val,col2_val,col3_val))
cursor.execute("commit")


# In[47]:


sql3 = "select * from table1"
cursor.execute(sql3)
result = cursor.fetchall()
print(result)


# In[48]:


for i in result:
    print(i)


# In[45]:


sql4 = "delete from table1 where col1=5"    
cursor.execute(sql4)
cursor.execute("commit")


# In[ ]:


del1 = int(input('enter the row you need to  delete: '))


# In[50]:


search = int(input('enter the column you want to select :'))
sql5 = 'select * from table1 where col1 = %s'
cursor.execute(sql5,(search,))
result = cursor.fetchone()
print(result)


# In[53]:


sql3 = " select * from table1"
cursor.execute(sql3)
result = cursor.fetchall()
print(result)


# In[54]:


for i in result:
    print(i)


# In[56]:


del1 = int(input('Enter the row you want to delete:'))
sql6 = "delete from table1 where col1=%s"
cursor.execute(sql6,(del1,))
cursor.execute('commit')


# In[57]:


sql3 = " select * from table1"
cursor.execute(sql3)
result = cursor.fetchall()
print(result)


# In[ ]:




