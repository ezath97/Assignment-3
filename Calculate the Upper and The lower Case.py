# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
# Sample String : 'The quick Brow Fox'
# Expected Output :
    # No. of Upper case characters : 3
    # No. of Lower case Characters : 12

def UL_Count(s):
    Upper = 0
    Lower = 0
    for i in s:
        if i.isupper():
           Upper = Upper + 1
        elif i.islower():
           Lower = Lower + 1
    print('Sample String: ', String)
    print('No. of Upper case characters: ', Upper)
    print('No. of Lower case characters: ', Lower)
    return ("")
    
String = 'The quick Brow Fox'
print (UL_Count(String))

