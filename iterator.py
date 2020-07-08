class A:
   def __init__(self,a,b):
       self.a=a
       self.b=b
   def __iter__(self):
       return self
   def __next__(self):
      if self.a>self.b:
         raise StopIteration
      else:
         item=self.a
         self.a=self.a+1
         return item

if __name__=="__main__":
   a=A(0,13)
   a.__iter__()
   for i in range(13):
      print(next(a))
