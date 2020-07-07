class A:
  def __init__(self,a,b):
     self.a=a
     self.b=b

  def __str__(self):
     return f"{self.a} and {self.b}"

  def __call__(self,fun):
      def wrapper(*args):
          return fun(*args)
      return wrapper

#*args is tuple
#**kwargs is dictionary

@A(2,4)
def func(*args):
  print(args)
  for i in args:
     print(i)

def test1(**kwargs):
   print(kwargs)
   for i,j in kwargs.items():
      print(i,j)

if __name__=="__main__":
  func(1,2,3,4)
  a=A(5,6)
  print(a.__dict__)
  print(a)
  test=a(func)
  test(1,2,3,4,5,6)
  test1(hello="Bapan",hi="Rosy",bello="Mello")



   
   