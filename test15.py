def change_string(s):
   s.strip().lower()
   str1=""
   cset="qwertyuiopasdfghjklzxcvbnm"
   alphabet='abcdefghijklmnopqrstuvwxyz'
   m=dict(zip(list(cset),list(alphabet)))
   for i in list(s):
      str1+=m[i]
   return str1

if __name__=="__main__":
   print(change_string("utta"))
   print(change_string("egrt"))

      
