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

points = [(1, 2), (3, 1), (5, 0)]
# Sort by the second element of each tuple
sorted_points = sorted(points, key=lambda x: x[1]) # [(5, 0), (3, 1), (1, 2)]
print(sorted_points)
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


ftext=''
fin=open('fileop.txt','rt')
while True:
    line=fin.readline()
    if not line:
        break
    ftext+=line
    print(ftext)
    print(len(ftext))
fin.close()

print(ftext)
print(len(ftext))