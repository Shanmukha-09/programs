a=input()
if(len(a)>3):
  if('ing' in a):
    a=a+'ly'
    print(a)
  else:
    a=a+'ing'
    print(a)
else:
  print(a)
