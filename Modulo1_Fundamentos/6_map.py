def myfunc(a,b):
  return (a,b)

x = map(myfunc,('apple','banana','cherry'),('orange','lemon','pineapple'))


for i in x:
  print(i)