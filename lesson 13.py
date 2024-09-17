No 13 while loop 
# Print numbers until the user enters 0
number = int(input('Enter a number: '))

# iterate until the user enters 0
while number != 0:
    print(f'You entered {number}.')
    number = int(input('Enter a number: '))

print('The end.')

OUTPUT:
Enter a number: 5
You entered 5.
Enter a number: 45
You entered 45.
Enter a number: 0
The end.

=== Code Execution Successful ===