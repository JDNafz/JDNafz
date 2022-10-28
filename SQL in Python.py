# In[ ]:
import psycopg2 as pg2
conn = pg2.connect(database='dvdrental',user='postgres',password='password')
cur = conn.cursor()
cur.execute('SELECT * FROM payment')
data = cur.fetchmany(2)
cur.close()

print(data)
print('dad')

# In[]:
print('banana')

