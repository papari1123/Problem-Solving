# 1번 rotated된 수열인지 알 수가 없음
# pivot값이 

def pivot_idx_search(m_list, start, end, prev):
    if start==end or start>end:
            return start
    mid = int((start+end)/2)
    if m_list[mid]>prev:
        return pivot_idx_search(m_list, mid+1, end, m_list[mid])
    else:
        return pivot_idx_search(m_list, start, mid-1, m_list[mid])

def binary_search(m_list, start, end, ans):
    if start==end:
        if m_list[start]==ans:
            return start
        else:
            return -1
    mid = int((start+end)/2)
    if m_list[mid]<ans:
        return binary_search(m_list,mid+1,end,ans)
    elif m_list[mid]>ans:
        return binary_search(m_list,start,mid-1,ans)
    else:
        return mid

print('write key:')
key = int(input())
print('write array:')
arr = list(map(int,input().split()))
pivot_idx = pivot_idx_search(arr, 0, len(arr)-1, arr[0])
#print(pivot_idx)
if(key>arr[0]):
    index = binary_search(arr, 0, pivot_idx-1, key)
else:
    index = binary_search(arr, pivot_idx, len(arr)-1, key)   
if index!=-1:
    print('Found at index '+str(index)) 
else  :
    print('Not found')


