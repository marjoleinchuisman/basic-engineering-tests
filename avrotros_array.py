# Function 'findClosestValues' 
def findClosestValues(array, needle, number):
    # Empty list to store the closest values
    closest_values = []

    # Check if the input array is empty, if so, return an empty list
    if not array:
        return closest_values

    # Initialize left and right pointers for binary search
    left, right = 0, len(array) - 1

    while len(closest_values) < number and left <= right:
        left_diff = abs(array[left] - needle)
        right_diff = abs(array[right] - needle)
        if left_diff <= right_diff:
            closest_values.append(array[left])
            left += 1
        else:
            closest_values.append(array[right])
            right -= 1

    # Sort the closest values in ascending order
    closest_values.sort()

    # Return the list of closest values
    return closest_values