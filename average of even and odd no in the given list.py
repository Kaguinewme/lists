elements=[23,14,56,12,19,9,15,25,31,42,43]
even=0
odd=0
sum_even=0
sum_odd=0
avg_even=0
avg_0dd=0
i=0
while i<len(elements):
  if elements[i]%2==0:
      even=even+1
      sum_even=sum_even+elements[i]
      avg_even=sum_even/even
  else:
      odd=odd+1
      sum_odd=sum_odd+elements[i]
      avg_odd=sum_odd/odd
  i=i+1
print("avg of even=",even)
print("avg of odd=",odd)
        
        