numbers=[12,34,56,56,23,21,34]
i=0
max=0
sec=0
while i<len(numbers):
    if numbers[i]>max:
        max=numbers[i]
    if numbers[i]<max and numbers[i]>sec:
        sec=numbers[i]
    i+=1
print(max)
print(sec)