"""
k largest(or smallest) elements in an array | added Min Heap method
https://www.geeksforgeeks.org/k-largestor-smallest-elements-in-an-array/

"""
#User function Template for python3
from heapq import heappop,heapify



class Solution:
    #Function to return k largest elements from an array.
    
    def maxHeapify(self,li):
        n = len(li)
        for i, ele in enumerate(li):
            for j, in range(1,3):
                if(li[2*i+j] is None):
                    break
                if(ele<li[2*i+1]) : #left
                    li[i], li[2*i+j] = li[2*i+j],li[i]       
    def kLargest(self,li,n,k):
        # code her
        heapify(li)
        for _ in range(n) :
          print(li[0])
          li.heapop()