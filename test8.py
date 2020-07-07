def isNumber(s):
   for i in list(s):
      if i.isdigit()!=True:
         return False
   return True

if __name__=="__main__":
  str1=input("enter your input")
  print(isNumber(str1))
  