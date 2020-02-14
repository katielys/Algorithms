# Selection Sort 
# Time complexity : O(n^2)
# Space complexity: O(1) 
def selection_sort(vec):
    for i in range(len(vec)):
        min_id = i
        for j in range( i +1, len(vec)):
            if vec[min_id] > vec[j]:
                min_id = j
        vec[i], vec[min_id] = vec[min_id], vec[i]

vec = [19,2,31,45,30,1,1,27,0,3,63,87485,5]
selection_sort(vec)
print(vec)