bin=input()
bin=bin[::-1]
dec=0
for i in range(len(bin)):
   power=2**i
  digit=int(bin[i])
  res=digit*power
  dec=dec+res
print(dec)
