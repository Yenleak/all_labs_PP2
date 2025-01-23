x = "zhylan"

def myfunc():
  print("Python is " + x)

myfunc()


a = "zhylan"

def myfunc():
  a = "fantastic"
  print("Python is " + a)

myfunc()

print("Python is " + a)


def myfunc():
  global c
  c = "fantastic"

myfunc()

print("Python is " + c)


b = "zhylan"

def myfunc():
  global b
  b = "fantastic"

myfunc()

print("Python is " + b)