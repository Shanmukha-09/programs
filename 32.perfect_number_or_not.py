def my(n):
  sum=0
  for i in range(1,n):
    if(n%i==0):
      sum=sum+i
    if(sum==n):
        return 'perfect number'
    else:
       return 'not a perfect number'
print(my(6))
