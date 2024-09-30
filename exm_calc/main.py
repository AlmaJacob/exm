# import python.exm_calc.inputtt as inputtt
from number import *
from add import *
from div import *
from mul import *
from mod import *
from sub import *
while True:
 print("""
1.add
2.sub
3.mul
4.div
5.mod""")

 ch=int(input("enter ur choice"))
 if ch==1:
    a,b=number.number()
    c.add(a,b)
 elif ch==2:
  sub()
 elif ch==3:
  mul()
 elif ch==4:
  div()
 elif ch==5:
  mod()
  break
 else:
  print("invalid choice")
