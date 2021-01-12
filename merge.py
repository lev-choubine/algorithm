array = [10,9,89,15,-5,789,1,11,342,75,48,356]

'''
STEPS



create the recursive function to break the array down into it's single item arrays
start merging neighbouring while sorting them
repeat the step until there is one array

'''
def merge_sort(arr):

    # set up our recursive fintion here
    if len(arr) > 1:
    # find the middle of the array
      
        split = len(arr) //2
    # split the array into 2 arrays - left and right - accordingly
        left_array = arr[:split]
        right_array = arr[split:]
    # call the recursive function
        merge_sort(left_array)  
        merge_sort(right_array)
    # start array

        #set iterator counters
        l = 0
        r = 0
        m = 0
        #joining sorted arrays
        while l < len(left_array) and r < len(right_array):
            if left_array[l] < right_array[r]:
                arr[m] = left_array[l]
                l += 1 
            else:
                arr[m] = right_array[r]
                r += 1
            m += 1
        
        #handling remaining values
        while l < len(left_array):
            arr[m] = left_array[l]
            m += 1 
            l += 1
    
        while r < len(right_array):
            arr[m] = right_array[r]
            r += 1
            m += 1
   

merge_sort(array)
print(array)


