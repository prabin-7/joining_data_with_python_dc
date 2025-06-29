import pandas as pd 
import os 

grand_parent_path = os.path.abspath(os.path.join(os.path.dirname(__file__),'../..'))
data_folder = 'data'

file1_name = 'ward.p'
file2_name = 'licenses.p'
file3_name = 'financials.p'
file4_name = 'zip_demo.p'
path1 = os.path.join(grand_parent_path,data_folder,file1_name)
path2 = os.path.join(grand_parent_path,data_folder,file2_name)
path3 = os.path.join(grand_parent_path,data_folder,file3_name)
path4 = os.path.join(grand_parent_path,data_folder,file4_name)


ward = pd.read_pickle(path1)
license = pd.read_pickle(path2)
grants = pd.read_pickle(path3)
zip_demo = pd.read_pickle(path4)
print('ward: \n', ward.head(),'\n')
print('license: \n', license.head(),'\n')
print('grants: \n',grants.head(),'\n')
print('zip_demo: \n',zip_demo.head(),'\n')

licenses_zip_ward = license.merge(zip_demo, on = 'zip') \
    .merge(ward, on = 'ward' )
    
# print(licenses.cip.r                                                                                        ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd)
print(licenses_zip_ward.head())
print(licenses_zip_ward.shape)
print(licenses_zip_ward.info())