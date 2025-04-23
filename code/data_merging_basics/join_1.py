'''Instructions
100 XP
Starting with the licenses table on the left, merge it to the biz_owners table on the column account, and save the results to a variable named licenses_owners.
Group licenses_owners by title and count the number of accounts for each title. Save the result as counted_df
Sort counted_df by the number of accounts in descending order, and save this as a variable named sorted_df.
Use the .head() method to print the first few rows of the sorted_df.'''
import os 
import pandas as pd 
# import pickle              pickle.loads(single_arg) it takes single path name and loads byte strings and not pickle in string form

grandparent_path = os.path.abspath(os.path.join(os.path.dirname(__file__),'../..'))
data_dir_name = 'data'
file1_name = 'business_owners.p'
file2_name = 'licenses.p'

path1 = os.path.join(grandparent_path,data_dir_name,file1_name)
path2 = os.path.join(grandparent_path,data_dir_name,file2_name)

biz_owners = pd.read_pickle(path1)
licenses = pd.read_pickle(path2)

# print(biz_owners.head())
# Merge the licenses and biz_owners table on account
licenses_owners = licenses.merge(biz_owners, on ='account')

# Group the results by title then count the number of accounts
counted_df = licenses_owners.groupby('title').agg({'account':'count'})

# Sort the counted_df in descending order
sorted_df = counted_df.sort_values('account',ascending = False)

# Use .head() method to print the first few rows of sorted_df
print(sorted_df.head())

# print(biz_owners.head())
# print(licenses.head())