# # def players(bat,bowl,keeper,all='dube'):
# #     return {'batsman': bat,'bowler': bowl,'keeper': keeper,'allrounder': all}
# #
# #
# #
# #
# #
# # def print_args(*args):
# #     print('Positional argument tuple:', args)
# #
# #
# # print_args(2,5)
# #
# # def print_args(a,b,*args):
# #     print('Positional argument tuple:', a,b,args)
# #     print(a,b,*args)
# #
# # print_args(2,3,4)
# #
# # def print_kwargs(**kwargs):
# #     print('Keyword arguments:',kwargs)
# #
# #
# # print_args(1,2,3,4,5,6,7,8,9,10)
# # print_kwargs(a=2,b=3,c=4,d=5,e=6,f=7,g=8)
# # print_kwargs(bat='sachin',bol='arshdeep',keep='klrahul',all='dube')
#
# # A list of numbers
# numbers = [1, 2, 3, 4, 5, 6]
#
# # Using lambda with filter() to get only even numbers
# evens = list(filter(lambda x: x % 2 == 0, numbers))
#
#
# # Using lambda with map() to square each number
# squared = list(map(lambda x: x**2, numbers))
#
# print(f"Evens: {evens}")     # Output: [2, 4, 6]
# print(f"Squared: {squared}") # Output: [1, 4, 9, 16, 25, 36]
from importlib.metadata import files

# points = [(1, 2), (3, 1), (5, 0)]
# # Sort by the second element of each tuple
# sorted_points = sorted(points, key=lambda x: x[1]) # [(5, 0), (3, 1), (1, 2)]
# print(sorted_points)
#
# k=lambda a:a*a
# print(k(10))
#
# tex=''' hi this is shivanandreddy today class file operation '''
#
# len(tex)
#
# file_handle=open('my_first_file.txt','wt')
#
# file_bytes=file_handle.write(tex)
# file_handle.close()
#
#
# print(file_bytes)
#
# sance=''' hi this is shivanandreddy today class file operation '''
#
# fine=open('my_first_file.txt','rt')
#
# ftex=fine.read()
#
# fine.close()
# print(len(ftex))
#
# fout=open('python.txt','xt')
# fout.write('python librar


# my_data=''' hi this is shivanandreddy today class file operation corently i am under sails training '''
#
# file_handle=open('my_new_file.txt','wt')
#
# file_byt=file_handle.write(my_data)
# file_handle.close()
#
# fout=open('my_new_file.txt','xt') # we cant over writ on file
# fout.close()

# fin=open('fileop.txt','rt')
# f_tex=fin.read()
# fin.close()
# print(f_tex)


# ftext=''
# fin=open('fileop.txt','rt')
# while True:
#     line=fin.readline()
#     if not line:
#         break
#     ftext+=line
#     print(ftext)
#     print(len(ftext))
# fin.close()
#
# print(ftext)
#
import pandas as pd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
#
# n = np.linspace(0, 2, 8)
# print(n)
# x = np.linspace(0, 2 * np.pi, 100)
# print(x)
# f = np.sin(x)
# print(f)
# m=np.arange(0,2,8)
# print(m)
# b = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
# print(b)
# c = np.array([[1, 2], [3, 4]], dtype=complex)
# print(c)
# a = np.arange(6)
# print(a)
# c = np.arange(12).reshape(4, 3)
# print(c)
# a = np.array([20, 30, 40, 50])
# b = np.arange(4)
# c = a - b
# d = b ** 2
# print(d)
# print(c)
# A = np.array([[1, 1],
#                   [0, 1]])
# B = np.array([[2, 0],
#                   [3, 4]])
# C = A * B  # element wise
# print(C)
# D = A @ B
# print(D)
# D = A.dot(B)
# print(D)
# rg = np.random.default_rng(3)
# print('m',rg.random((2,3)))
# rg = np.random.default_rng(3)
# print('n',rg.random((2,3)))
# a = rg.random((2, 3))
# print(a[0].sum())
# print(a.min())
# print(a.max())
# b = np.arange(12).reshape(3, 4)
# print(b)
# print(b.sum(axis=0))  # sum column-wise
# print(b.min(axis=1))  # min of each row)
# print('k',b.cumsum(axis=1))

# # B = np.arange(3)
# # print(B)
# # print(np.exp(B)) # e^0, e^1, e^2
# # print(np.sqrt(B))
# # C = np.array([2., -1., 4.])
# # print(np.add(B, C))
#
# m=np.array([[1, 2, 3], [4, 5, 6], [7, 0, 9]])
# print(m.argsort())
# print(m.argmax())
# print(m.argmin())
# # print(m[8])
# a=np.arange(10)
# print(a)
# print(a.argmax())
# a[9]
# rg = np.random.default_rng(1)
# # print(a.reshape(4, 2))
# a = np.floor(10 * rg.random((3, 4)))
# print(a)
# print(a.shape)
# print(a.ravel())  # returns the array, flattened
# print(a.reshape(6, 2))
# print(a.T)
# print(np.resize(a,(6, 6)))
# a_resha=a.reshape(2,6)
# print(a_resha.shape)
# print(a.shape)
# a_reisize=np.resize(a,(6,6))
# print(a_reisize)
# print(a_reisize.shape)
# # print(a.reshape(6,6))
# a = np.floor(10 * rg.random((2, 2)))
# print(a)
# b = np.floor(10 * rg.random((2, 2)))
# print(b)
# print('v',np.vstack((a, b)))
# print('h',np.hstack((a, b)))
# a = np.array([4., 2.])
# b = np.array([3., 8.])
# c = np.column_stack((a, b))
# print(c)
# d = np.hstack((a, b))
# print(d)
# df = pd.DataFrame(
#     {
#         "Name": [
#             "Braund, Mr. Owen Harris",
#             "Allen, Mr. William Henry",
#             "Bonnell, Miss. Elizabeth",
#         ],
#         "Age": [22, 35, 58],
#         "Pincode": [76305, 43284, 98765],
#         "Sex": ["male", "male", "female"],
#     }
# )
# print(df)
# age=df["Age"]
# print(age)
# print(type(age))
# print(age.dtype)
# print(df['Age'])
# print(df["Age"].max())
# print(df.describe())
#
data=pd.read_csv("/home/sails/shiva_sailes/saile_code/titanic.csv")
# print(data.shape)
# print(data.head())
# import openpyxl
# data.to_excel("titanic.xlsx", sheet_name="passengers", index=False)
# data_excel=pd.read_excel("titanic.xlsx", sheet_name="passengers")
# print(data_excel.head())
#
# print(data_excel[['Age',"Sex"]].head())
#
# dat_age=data_excel[data_excel["Age"]>35]
# print(dat_age)
# dat_place=data_excel[(data_excel["Pclass"]==2) | (data_excel["Pclass"]==3)]
# print(dat_place)
# dat_not=data_excel[data_excel["Age"].notna()]
# print(dat_not)
# adult_names = data.loc[data["Age"] > 35, "Name"]
# print(adult_names)
# adult=data.iloc[data["Age"] > 35]
# print(adult)
#
# print(data.iloc[2:30,2:5])
# # print(data.loc[2:30,2:5])
# # print(data[2:30,2:5])
import matplotlib.pyplot as plt

air_quality = pd.read_csv("/home/sails/shiva_sailes/data_sets/air_quality_no2.csv", index_col=0, parse_dates=True)
# print(air_quality.head())
# air_quality.plot()
# plt.show()
# air_quality["station_paris"].plot()
# plt.show()
# air_quality.plot.scatter(x="station_london", y="station_paris", alpha=0.5)
# plt.show()
air_quality.plot.box()
# plt.show()
xs = air_quality.plot.area(figsize=(12, 4), subplots=True)
# plt.show()
air_quality["london_mg_per_cubic"] = air_quality["station_london"] * 1.882
print(air_quality.head())
print(data["Age"].mean())
print(data[["Age", "Fare"]].median())
print(data[["Age", "Fare"]].describe())
print(data.agg({
    "Age": ["min", "max", "median", "skew"],
    "Fare": ["min", "max", "median", "mean"],
})
)
df = pd.DataFrame({'Animal': ['Falcon', 'Falcon', 'Parrot', 'Parrot'],
                   'Max Speed': [380., 370., 24., 26.]}
                  )
print(df)
m = df.groupby(['Animal']).mean()
print(m)
df_s = data[["Sex", "Age"]].groupby("Sex")
print('a',df_s)
print(df_s.mean())
print(df_s["Age"].mean())
df_sp = data.groupby(["Sex", "Pclass"])
print(df_sp["Fare"].mean())
print(data["Pclass"].value_counts())
titanic_sorted_age = data.sort_values(by="Age").head()
print(titanic_sorted_age)
air_quality_2 = pd.read_csv("/home/sails/shiva_sailes/data_sets/air_quality_pm25_long.csv", index_col=0, parse_dates=True)