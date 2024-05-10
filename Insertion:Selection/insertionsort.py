# 1. Implement the following algo insertion sort and salrction sort
def insertionSort(array):

    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        

        # For descending order, change key<array[j] to key>array[j].        
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        
        # Place key at after the element just smaller than it.
        array[j + 1] = key
    
    return array