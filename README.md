
Add files via upload
##Number Sum and Sorting Script
This script takes a list of numbers input by the user, calculates their sum, sorts them in ascending order, and finds the second largest number. It also handles errors related to non-numeric input and informs the user of any invalid entries.

##Features
1. Sum Calculation:

Prompts the user to enter numbers separated by spaces.
Converts these strings to floats.
Calculates and prints the sum of the numbers.
2. Sorting and Second Largest Number:

Sorts the numbers in ascending order.
Prints the sorted list.
Finds and prints the second largest number.
3. Error Handling:

Catches ValueError if the input contains non-numeric values.
Informs the user if any input values are not numbers.
Displays the invalid inputs.
##Usage
Run the Script:

Execute the script in a Python environment.
Enter numbers separated by spaces when prompted.

##Example:
Enter the numbers you want to find their sum separated by spaces: 1 2 3 4 5
Total is:  15.0
Order from smallest to largest is: [1.0, 2.0, 3.0, 4.0, 5.0]
Second largest is:  4.0

##Error Handling Example:
Enter the numbers you want to find their sum separated by spaces: 1 2 a 4 5
Only integer or float values are allowed.
['a'] are neither integers nor floats.
Code Explanation
The script is structured as follows:

Input Handling: Prompts the user to input numbers separated by spaces and splits the input into a list of strings.
Sum Calculation: Converts each string to a float and calculates the total sum.
Sorting: Converts the strings to floats again (to ensure numerical sorting) and sorts them in ascending order.
Second Largest Number: Identifies and prints the second largest number from the sorted list.
Error Handling: Catches ValueError exceptions for invalid inputs, identifies non-numeric entries, and lists them.

##Code:
try:
    number_list = input("Enter the numbers you want to find their sum separated by spaces: ")
    # Creates a list of strings from the input received
    numbers = number_list.split(' ')
    sum = 0
    for num in numbers:
        # Convert the strings in the list to integer
        num = float(num)
        sum += num 
        
    print("Total is: ", sum)
