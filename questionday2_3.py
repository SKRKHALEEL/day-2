'''
30) Boring Arrays
You are given an array A of size N. In one operation you can select any two elements
from it, add their absolute difference in your score.
Your task is to find and return an integer value, representing the maximum score.
Note:
Assume 1 based indexing
The elements on which operation has been performed cannot be selected again.
Input Specification:
Input1: An integer value N, representing the size of array A
input2: An integer array A
Output Specification:
Return an integer value, representing the maximum score
Sample Input:
4
1 2 3 4
Sample Output:
4
'''

 

def find_maximum_score(N, A):
    A.sort()  
    max_score = 0

    for i in range(N - 1):
        max_score += abs(A[i] - A[i + 1]) 

    return max_score


input_N = 4
input_A = [1, 2, 3, 4]

output_max_score = find_maximum_score(input_N, input_A)
print(output_max_score)  







