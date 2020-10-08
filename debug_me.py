def reverse_array(input_arr):
    reversed_array = []

    # Initialize the array position
    array_position = 0
    while array_position < len(input_arr):
        # Pop the item off the old array and add it to the new one.
        reversed_array.append(input_arr.pop())
        
        # Increment the array position
        array_position += 1
    
    return reversed_array

data = [2,4,6,8,10]
print(reverse_array(data))