import numpy as np
import random
import time
import matplotlib.pyplot as plt

def main():
    size=[]
    
    timeIS_AC=[]
    timeSS_AC=[]
    
    # timeIS_BC=[]
    # timeSS_BC=[]
    
    # timeIS_WC=[]
    # timeSS_WC=[]
    
    for arraySize in range(500,9500,1000):
        size.append(arraySize)
        print("SIZE OF ARRAY: "+str(arraySize))
        # bestcaseArray=np.array(range(arraySize))
        # worstcaseArray=np.array(range(arraySize))
        # worstcaseArray=worstcaseArray[::-1]
        
        randomArray=np.array(random.sample(range(arraySize),arraySize))
        
         # Average case for insertion sort
        beginTimeIS_AC=time.time()
        insertionSort(randomArray)
        endTimeIS_AC=time.time()
        elapsedIS_AC=endTimeIS_AC-beginTimeIS_AC
        timeIS_AC.append(elapsedIS_AC)
                
        # Average case for selection sort
        beginTimeSS_AC=time.time()
        selectionSort(randomArray)
        endTimeSS_AC=time.time()
        elapsedSS_AC=endTimeSS_AC-beginTimeSS_AC
        timeSS_AC.append(elapsedSS_AC)
        
        # # Best case for insertion sort
        # beginTimeIS_BC=time.time()
        # insertionSort(bestcaseArray)
        # endTimeIS_BC=time.time()
        # elapsedIS_BC=endTimeIS_BC-beginTimeIS_BC
        # timeIS_BC.append(elapsedIS_BC)
                
        # Best case for selection sort
        # beginTimeSS_BC=time.time()
        # selectionSort(bestcaseArray)
        # endTimeSS_BC=time.time()
        # elapsedSS_BC=endTimeSS_BC-beginTimeSS_BC
        # timeSS_BC.append(elapsedSS_BC)
        
        # Worst case for insertion sort
        # beginTimeIS_WC=time.time()
        # insertionSort(worstcaseArray)
        # endTimeIS_WC=time.time()
        # elapsedIS_WC=endTimeIS_WC-beginTimeIS_WC
        # timeIS_WC.append(elapsedIS_WC)

        # Worst case for selection sort
        # beginTimeSS_WC=time.time()
        # selectionSort(worstcaseArray)
        # endTimeSS_WC=time.time()
        # elapsedSS_WC=endTimeSS_WC-beginTimeSS_WC
        # timeSS_WC.append(elapsedSS_WC)
        
        
    print("INSERTION SORT AVERAGE CASE"+str(timeIS_AC))
    print("SELECTION SORT AVERAGE CASE"+str(timeSS_AC))   
    # print("INSERTION SORT BEST CASE"+str(timeIS_BC))
    # print("SELECTION SORT BEST CASE"+str(timeSS_BC))
    # print("INSERTION SORT WORST CASE"+str(timeIS_WC))
    # print("SELECTION SORT WORST CASE"+str(timeSS_WC))
    
    plt.figure()
    plt.plot(size, timeIS_AC, label='Insertion Sort')
    plt.plot(size, timeSS_AC, label='Selection Sort')

    plt.xlabel('Array Size')
    plt.ylabel('Time (seconds)')
    plt.title('Sorting Algorithm performance comparison')
    plt.legend()
    plt.grid(True)
    plt.show()   
    
    # plt.figure()
    # plt.plot(size, timeIS_BC, label='Insertion Sort Best Case')
    # plt.plot(size, timeSS_BC, label='Selection Sort Best Case')
    # plt.plot(size, timeIS_WC, label='Insertion Sort Worst Case')
    # plt.plot(size, timeSS_WC, label='Selection Sort Worst Case')  
    
    # plt.xlabel('Array Size')
    # plt.ylabel('Time (seconds)')
    # plt.title('Sorting Algorithm performance comparison')
    # plt.legend()
    # plt.grid(True)
    # plt.show()   
    
       
     
# def insertionSort(A):
#     n=len(A)
#     for i in range(1,n):
#         key=A[i]
#         j=i-1
#         while(j>=0 and A[j]>key):
#             A[j+1]=A[j]
#             j=j-1
#         A[j+1]=key
#     return A
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

def selectionSort(array):
    n=len(array)
    for i in range(0,n-1):
        smallest=i
        for j in range(i+1,n):
            if array[j]<array[smallest]:
                smallest=j
        temp=array[smallest]
        array[smallest]=array[i]
        array[i]=temp
    return array
# def selectionSort(array, size):
   
#     for step in range(size):
#         min_idx = step

#         for i in range(step + 1, size):
#             # select the minimum element in each loop
#             if array[i] < array[min_idx]:
#                 min_idx = i
         
#         # put min at the correct position
#         (array[step], array[min_idx]) = (array[min_idx], array[step])
#     return array

main()    
    
    
