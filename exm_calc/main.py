# import python.exm_calc.inputtt as inputtt
from add import *
from div import *
from mul import *
from mod import *
from sub import *
a=int(input("enter first number : "))
b=int(input("enter second number : "))
while True:
 print("""
1.add
2.sub
3.mul
4.div
5.mod""")

 ch=int(input("enter ur choice"))
 if ch==1:
  add(a,b)
 elif ch==2:
  sub(a,b)
 elif ch==3:
  mul(a,b)
 elif ch==4:
  div(a,b)
 elif ch==5:
  mod(a,b)
  break
 else:
  print("invalid choice")
