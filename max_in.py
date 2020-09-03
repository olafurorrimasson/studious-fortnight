# find the maximum positive integer input by a user.

#num_int = int(input("Input a number: "))    # Do not change this line
# Fill in the missing code
numbers=[]
while True:
    num_int = int(input("Input a number: "))
    if num_int <0:
        break
    else:
        numbers.append(num_int)
    max_int = max(numbers) 
print("The maximum is", max_int)    # Do not change this line
