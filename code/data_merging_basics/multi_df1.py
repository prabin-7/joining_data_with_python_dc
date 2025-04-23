import pandas as pd 
import os 

grand_parent_path = os.path.abspath(os.path.join(os.path.dirname(__file__),'../..'))
data_folder = 'data'

file1_name = 'ward.p'
file2_name = 'licenses.p'
file3_name = 'financials.p'

path1 = os.path.join(grand_parent_path,data_folder,file1_name)
path2 = os.path.join(grand_parent_path,data_folder,file2_name)
path3 = os.path.join(grand_parent_path,data_folder,file3_name)


ward = pd.read_pickle(path1)
license = pd.read_pickle(path2)
grants = pd.read_pickle(path3)
print(ward.head())
print(license.head())
print(grants.head())