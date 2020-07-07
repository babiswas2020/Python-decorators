def missing_letters(s1):
   s2=''
   s1.strip().lower()
   l=list('abcdefghijklmnopqrstuvwxyz')
   for i in l:
      if i not in list(s1):
         s2+=i
   print(s2)

if __name__=="__main__":
   missing_letters("welcome to geeksforgeeks")

   
   