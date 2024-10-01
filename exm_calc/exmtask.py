# #to create a text file
# f=open("exm/adm.txt",'x')

#to read a sentence
# print(f.write("evng\nwelcome\nhiii"))

#return the longest word in the sentence
# f=open("exm/adm.txt",'r')
# l=len(f.readlines())
# f.seek(0)
# longest_word=''
# for i in range(l):
#     a=f.readline().strip()
#     s=a.split(' ')
#     for j in s:
#         if j!='':
#          if len(longest_word)<len(j):
#             longest_word=j
# print("longest word :",longest_word)

#create a dictionary retrns a new dictionary with key and values swapped
# d={1:"one",2:"two",3:"three"}
# def num(d):
#     return{value:key for key,value in d.items()}
# print(num(d))    



#duplicates in a list

# l=[1,34,1,1,4,34]
# l1=[]
# for i in l:
#   if i not in l1:
#     l1.append(i)
# print(l1)

#to find a factorial of number
# import math
# print (math.factorial(5))
# def factorial():
#     a=int(input("enter a number"))
#     factorial=1
#     for i in range(1,a+1):
#         factorial*=i
#     print(factorial)
# factorial()        

#writing a python program to print the following pattern
#A
#BA
#CBA
#DCBA

# no=4
# for i in range(no):
#     for j in range(i,-1,-1):
#         print(chr(65+j),end='')
#     print()        
