def is_integer_string():
   m=input("enter the input")
   try:
       print(int(m))
   except Exception as e:
      print("The entered value is string")
   else:
      print("The value is integer")

if __name__=="__main__":
   is_integer_string()
   
  
   