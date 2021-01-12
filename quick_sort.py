array =[4,5,-16,100,-567,1000,345,23,10,1,7,0.75]

def quick_sort(arr):
    #Base Case
    length = len(arr)
    #Base Case
    if length < 2:
        return arr

    current_position = 0 # Position of the partitioning element

    for i in range(1, length): #Partitioning Loop
        if arr[i] <= arr [0]:
            current_position +=1
            temp = arr[i]
            arr[i] = arr[current_position]
            arr[current_position] = temp

    temp = arr[0]
    arr[0] =  arr[current_position]
    arr[current_position] = temp #Declares the position of the pivot

    left = quick_sort(arr[0: current_position])
    #Sorts the elements to the left of the pivot
    right = quick_sort(arr[current_position + 1:length])
    #sorts the elements to the right of the pivot
    arr = left + [arr[current_position]] + right
    #joins the array back togeteher
    return arr

print(quick_sort(array))