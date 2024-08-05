
try:
    number_list = input("Enter the numbers you want to find their sum separated by spaces: ")
    #Creates a list of strings from the input received
    numbers= number_list.split(' ')
    sum = 0
    for num in numbers:
        #Convert the strings in the list to integer 
        num = float(num)

        sum += num 
        
    print("Total is: ", sum)

    sorted_num = []
    for num in numbers:
        num = float(num)
        sorted_num.append(num)
        sorted_num=sorted(sorted_num)
        
    print(f"Order from smallest to largest is: {sorted_num}")
    print("second largest is: ",sorted_num[len(sorted_num)-2])
    
except ValueError:
    print("Only integer or float values are allowed.")
    not_numbers = []
    for num in numbers:
        try:
            num=float(num)
        except ValueError:
            not_numbers.append(num)
            
            
    print(f"{not_numbers} are neither integers nor floats.")