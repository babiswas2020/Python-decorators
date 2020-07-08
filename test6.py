def check_all_character(s1):
   for i in list(s1):
      if i!=list(s1)[0]:
         return False
   return True

if __name__=="__main__":
   s="aaaaaaaaaa"
   print(check_all_character(s))
   s="aaaaaaaab"
   print(check_all_character(s))
