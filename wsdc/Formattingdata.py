import numpy as np
import pandas as pd


point_df = pd.DataFrame(columns = ['wsdc_id', 'level_points', 'allowed_level', 'required_level', \
                                   'event_level', 'event_name', 'event_location', 'event_date', \
                                   'points', 'result', 'role', 'first_name', 'last_name'])

df = pd.read_csv('DF1.csv')

# print(df.to_string())

# df.head()
# df.tail()

id = df['wsdc_id']
role = df['role']
lvl = df['event_level']
points = df['points']



print(df['first_name'],df['role'])


print("Leader Int points:", Lint,"\n","Follower Int Points:", Fint)