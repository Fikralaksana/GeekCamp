# a=open('tes.txt','r')
# b=a.readlines() 
# data=[] 
# for i,value in enumerate(b): 
#     i=i+1
#     if i%8!=0: 
#         s=value.replace('\n',',')
#         data.append(s)
#     else:
#         data.append(value)
# a.close()
# a=open('tes.csv','w') 
# a.writelines(data)




# # datas=['satu','dua','tiga','empat']
# # for index,data in enumerate(datas):
# #     print(data)

# i=0
# n=6
# # while i<6:
# #     i+=1
# #     if i<2:
        
# #     print(i)

# from ast import arg
# from typing_extensions import Self


# data=[["a",5],["b",3],["c",2],["d",4]]
# nama_murid = [x[0] for x in data]
# nilai_murid = [x[1] for x in data]

# nilai_murid.sort()

# # print(nilai_murid)
# terendah_nomor_dua = nilai_murid[1]

# print("".join([x[0] for x in data if x[1] == terendah_nomor_dua]))

# data.sort(reverse=True)
# print(data)
# data= sorted(data,)
# def ini(x):
#     return x[1] 
# # print("data awal: ",data)
# print(sorted(data,key = ini)[-2])


# def fungsi(**kwargs):
#     print(args)

# def fungsi_arg(a=2,b=4,c=5,d=5,):
#     print(a,b,c)
# a=0
# b=2
# c=3
# a={'a':2,'b':4,'c':6}
# fungsi_arg(**a)
# a=2,b=4,c=6

    
# class Honda():
#     def __init__(self):
#         self.merk='honda'
#     def gas(self):
#         return 10
#     def rem(self):
#         return -10

# class Motor(Honda):
#     def __init__(self):
#         super().__init__()
#         self.name=None
#         self.next=None
#         self.roda=2
#     def __repr__(self) -> str:
#         return self.name

# class Mobil(Honda):
#     def __init__(self):
#         super().__init__()
#         self.roda=4




# a=Motor()
# b=Motor()
# a.name='vario'
# b.name='revo'
# a.next=b

# print(a.next.name)

# import requests

# response=requests.get('http://www.google.com')
# print(response.text)

# response=requests.post(
#     'https://jsonplaceholder.typicode.com/posts',
#     data={
#     'title': 'foo',
#     'body': 'bar',
#     'userId': 1,
#     }
#   )

# print(response)

x=3
assert x>2,"x lebih kecil dari 2"
if x>2:
  pass
else:
  raise AssertionError('x lebih kecil dari 2')



  
print(x)
"""ssssssssssssssssssssssssss"""
2

1








