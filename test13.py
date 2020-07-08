def find_extra_character(s1,s2):
    s1.lower()
    s2.lower()
    if len(s1)>len(s2):
      for i in list(s1):
         if i not in s2:
            print(i)
    else:
      for i in list(s2):
        if i not in s1:
           print(i)

if __name__=="__main__":
   s1="abcd"
   s2="cbdae"
   print(s1)
   print(s2)
   find_extra_character(s1,s2)
