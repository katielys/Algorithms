# Bubble Sort is a sorting algorithm that can be applied to Arrays and Dynamic Lists.
# Time complexity : O(n^2)
# Space complexity: O(1) 
def bubblesort(vec):
    for iter_num in range(len(vec)-1,0,-1):
        for i in range(iter_num):
            if vec[i]>vec[i+1]:
                temp = vec[i]
                vec[i] = vec[i+1]
                vec[i+1] = temp


vec = [19,2,31,45,6,11,32,27,66,-2]
bubblesort(vec)
print(vec)