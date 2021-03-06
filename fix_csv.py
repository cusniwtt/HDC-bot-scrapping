import pandas as pd
import numpy as np
import os

df = pd.read_csv('link_csv/All_link.csv', sep='|')   #import dataframe from csv file
print(df.shape)

#Cut dataframe into single file by category
df = df.tail(-4)    #remove first 4 rows
print('----------------------------------------------------')
print(df)

df_info = df.iloc[1:7]  #create dataframe for info
print('----------------------------------------------------')
print(df_info)

df_state = df.iloc[8:15]  #create dataframe for state
df_state.iloc[2, 0] = 'สาเหตุการป่วยหรือตาย'
print('----------------------------------------------------')
print(df_state)

df_access = df.iloc[16:27]  #create dataframe for access
print('----------------------------------------------------')
print(df_access)

df_defend = df.iloc[28:36]  #create dataframe for defend\
print('----------------------------------------------------')
print(df_defend)

df_servplan = df.iloc[37:54]  #create dataframe for service plan
print('----------------------------------------------------')
print(df_servplan)

df_ministry = df.iloc[56:64]  #create dataframe for ministry
print('----------------------------------------------------')
print(df_ministry)

df_NCD = df.iloc[65:70]  #create dataframe for NCD
print('----------------------------------------------------')
print(df_NCD)

#Create csv from dataframe
list_df = [df_info, df_state, df_access, df_defend, df_servplan, df_ministry, df_NCD]   #create list of dataframe for loop
list_name = ['info', 'state', 'access', 'defend', 'servplan', 'ministry', 'NCD']        #create list of name for loop

for i in range(len(list_df)):
    list_df[i].to_csv('link_csv/{}.csv'.format(list_name[i]), sep='|', index=False, encoding='utf-8-sig')
    print('{}.csv created in link_csv'.format(list_name[i]))