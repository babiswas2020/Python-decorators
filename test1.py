def mycopy(s1,s2):
   for i in list(s2):
     s1.append(i)

if __name__=="__main__":
   s2="GEEKSFORGEEKS"
   s1=['']*(len(s2))
   mycopy(s1,s2)
   print(''.join(s1))