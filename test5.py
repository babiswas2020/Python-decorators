def function(cls):
   def wrapper(*args):
      def average(self,x,y):
          return (x+y)//2
      setattr(cls,'average',average)
      return cls(*args)
   return wrapper

@function
class A:
   def __init__(self,a,b):
       self.a=a
       self.b=b
   def __str__(self):
       return f"{self.a} and {self.b}"

if __name__=="__main__":
   a=A(3,4)
   print(a.__dict__)
   print(a)
   print(a.average(5,7))

          