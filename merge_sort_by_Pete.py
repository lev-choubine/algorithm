def merge(arr1, arr2):
    output =[]
    
    while len(arr1)>0 or len(arr2)>0:

        if len(arr1) == 0:
            output += arr2
            arr2 = []
        elif arr1 [0] < arr2[0]:
            output.append(arr1[0])
            arr1 == arr1[1:]        
        
        elif arr1[0]<arr2[1]:
            output.append(arr1[0])
        else: output.append(arr2[0])

    return output


def split(arr):
    midpoint = len // 2
    arr1 = arr[:midpoint]
    arr1 = arr[midpoint:]

    if len(arr1) <= 1 and len(arr2) <= 2:
        return megre(arr1, arr2)

    split_arr1 = split(arr1)   
    split_arr2 = split(arr2)  

    return merger(split_arr1, split_arr2)


