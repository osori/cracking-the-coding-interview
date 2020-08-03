def selection_sort(arr):
    """
    Python implementation of selection sort

    - Time Complexity: O(n^2)
    - Space Complexity: O(1)
    """

    for i in range(len(arr)):
        min_value = arr[i]
        min_index = i

        # find the i+1th smallest value in arr
        for j in range(i, len(arr)):
            if arr[j] < min_value:
                min_value = arr[j]
                min_index = j

        # put the i+1th smallest value in arr[i]
        arr[min_index] = arr[i]
        arr[i] = min_value

    return arr

def test():
    inputs = [
        [4, 1, 3, 7, 9],
        [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
        [5, 0, 5, 4, 1],
        [1, 2, 3, 4, 5]
    ]

    outputs = [
        [1, 3, 4, 7, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [0, 1, 4, 5, 5],
        [1, 2, 3, 4, 5]
    ]


    for i in range(len(inputs)):
        print("==Testing #"+str(i)+"==")
        print("Input:", inputs[i])
        print("Result:", selection_sort(inputs[i]))
        print("Expected:", outputs[i])
        print()

if __name__ == "__main__":
    test()
