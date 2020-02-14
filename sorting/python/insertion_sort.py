#Insertion sort is a simple sorting algorithm that works the way we sort playing cards in our hands.
# Time complexity : O(n^2)
# Space complexity: O(1) 
def insertion_sort(vec): 
    for i in range(1, len(vec)): 
        pivot = vec[i] 
        j = i-1
        while (j >= 0 and pivot < vec[j]) : 
                vec[j + 1] = vec[j] 
                j -= 1
        vec[j + 1] = pivot 

vec = [12, 11, 13, 5, 6,58,9898,6,1,854,9] 
insertion_sort(vec) 
print(vec)