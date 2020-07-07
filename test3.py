def is_panagram(s1):
   l=[False]*26
   s1.strip().lower()
   for i in list(s1):
     if ord(i)-ord('a')>=0 and ord(i)-ord('a')<26:
       l[ord(i)-ord('a')]=True
   if False not in l:
      print(f"{s1} is a panagram")
   else:
      print(f"{s1} is not a panagram")

if __name__=="__main__":
   is_panagram("The quick brown fox jumps over the little lazy dog")
   
        