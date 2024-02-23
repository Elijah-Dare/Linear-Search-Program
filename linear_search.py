def linear_search(arr, target):
    """This function takes in the array of elements and the target element
       It then iterated over the array of elements and returns the index of the element or
       It returns -1 to indicate the elements is not available"""
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Print a new line
print()


# Take the input of the user of the elements to store
elements = input("Enter the elements of the list (space - seperated): ").split()
my_list = [] # This can also be written as :
             # my_list = [int(a) for a in elements]


# Iterate over each element in elements (For begineers)
for a in elements:
    # convert the sting elements to an integer and append it to my_list
    int_element = int(a)
    my_list.append(int_element)

# Take the input of the target elements from the user and convert it to an integer
target = int(input("Enter the element to search for: "))

# Call the linear_search function and pass in the necessary arguments and strore it in the index variable
index = linear_search(my_list, target)


# A loop to check the index variable whether the returned value is valid or not
if index != -1:
    print(f"The element {target}, found at index, {index}")
else:
    print(f"The element {target} cannnot be found in the list")
    

    
    
    
    
    
