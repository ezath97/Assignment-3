# Write a Python function to sum all the numbers in a list.

# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20


def sum1(list):
    sum=0
    i=0
    while i < len(list):
        sum = sum + list[i]
        i = i+1
    return sum

list = (8, 2, 3, 0, 7)
print('Sample list: ',list)
print("Expected Output: ", sum1(list))
   
