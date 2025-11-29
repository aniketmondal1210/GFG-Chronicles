# Function to create dictionary
# arr is list of tuple. tuple contain name and marks.


def create_dict(arr):
    dict = {}
    # Iterate through each tuple in arr
    for name, marks in arr:
        dict[name] = marks
    return dict
