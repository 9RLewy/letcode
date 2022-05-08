# -*- coding: utf-8 -*-
"""
Created on Sat May  7 07:13:07 2022

@author: 93585
"""

#O(nlogn)
def quick_sort(b):
    if len(b) < 2:
        return b
     
    mid = b[len(b) // 2]
  
    left, right = [], []
  
    b.remove(mid)
    for item in b:
  
        if item >= mid:
            right.append(item)
        else:
     
            left.append(item)
     
    return quick_sort(left) + [mid] + quick_sort(right)
b = [11, 99, 33, 69, 77, 88, 55, 11, 33, 36, 39, 66, 44, 22]
print(quick_sort(b))
print(b)


#O(n^2)
def bubble_sort(array):
    for i in range(0, len(array)-1):
        for j in range(1, len(array)):
            if array[j] > array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
    return array
arrar=[5, 7, 3, 7, 2, 3, 2, 5, 9, 5, 7, 8]
print(bubble_sort(arrar))

print("******************************************")
#O(n^2)
def select_sort(lists):
    count = len(lists)
    for i in range(count):
        min = i
        for j in range(i + 1, count):
            if lists[min] > lists[j]:
                min = j
        lists[min], lists[i] = lists[i], lists[min]
    return lists
arrar=[5, 7, 3, 7, 2, 3, 2, 5, 9, 5, 7, 8]
print(select_sort(arrar))


print("_______________________________________")
#O(n^2)
def insertSort(arr):
    length = len(arr)
    for i in range(1,length):
        x = arr[i] 
        for j in range(i,-1,-1):    
            print(arr)
            if x < arr[j-1]:
                arr[j] = arr[j-1]
                print("arj1",arr[j])
            else:
                break
            
        arr[j] = x
        print("arj2",arr[j])
        

def printArr(arr):
    for item in arr:
        print(item)
arr = [4, 7 ,8 ,2]
insertSort(arr)


for j in range(3,-1,-1):
    print(j)
    
    
#O(nlogn)   
def mergeSort(nums:list):

    if len(nums) > 1:
        mid_index = len(nums) // 2
        left_nums = nums[:mid_index]  
        right_nums = nums[mid_index:]

        mergeSort(left_nums)
        mergeSort(right_nums)

        i, j = 0, 0
        while i < len(left_nums) and j < len(right_nums):
            if left_nums[i] < right_nums[j]:
                nums[i+j] = left_nums[i]
                i += 1
            else:
                nums[i+j] = right_nums[j]
                j += 1

        if i == len(left_nums):
            nums[i+j:] = right_nums[j:]

        if j == len(right_nums):
            nums[i+j:] = left_nums[i:]
    return nums

print(mergeSort(arr))


#
#for i in range(2,10):
#    print(i)
print("1111111111111111111")

def shellSort(arr): 
  
    n = len(arr)
    gap = int(n/2)
    print("gap:",gap)
    while gap > 0: 
  
        for i in range(gap,n): 
            
            temp = arr[i] 
            print("temp",temp)
            j = i 
            print("j",j)
            while  j >= gap and arr[j-gap] >temp: 
                print("j",j)
                print("arr[j]",arr[j])
                print("arr[j-gap]",arr[j-gap])
                arr[j] = arr[j-gap] 
                print("arr[j]",arr[j])
                j -= gap 
            arr[j] = temp 
        gap = int(gap/2)
  
arr = [ 12, 34, 54, 2, 3] 
shellSort(arr)
print(arr)