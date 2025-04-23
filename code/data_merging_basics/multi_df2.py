import pandas as pd
import os 

g_path = os.path.abspath(os.path.join(os.path.dirname(__file__),'../..'))
data_folder = 'data'

file1_name = 'cta_ridership.p'
file2_name = 'cta_calendar.p'
file3_name = 'stations.p'

path1 = os.path.join(g_path,data_folder,file1_name)
path2 = os.path.join(g_path,data_folder,file2_name)
path3 = os.path.join(g_path,data_folder,file3_name)

rider = pd.read_pickle(path1)
cal = pd.read_pickle(path2)
stations = pd.read_pickle(path3)

# print(rider.head())
# print(cal.head())
# print(stations.head())

ridership_cal_stations = rider.merge(cal, on  = ['year','month','day']) \
    .merge(stations, on = 'station_id')

# print(ridership_cal_stations.head())

filter = ((ridership_cal_stations['station_name'] == 'Wilson') \
    & (ridership_cal_stations['day_type'] == 'Weekday') \
    & (ridership_cal_stations['month'] == 7))

# print(type(filter))

# print(ridership_cal_stations.loc[filter,'rides'])  #print the df with 1 column of rides 

print(type(ridership_cal_stations.loc[filter,'rides'].sum()))  # type = numpy.int64
