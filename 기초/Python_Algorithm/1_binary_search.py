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
arr.sort()
index = binary_search(arr, 0, len(arr)-1, key)
if index!=-1:
    print('Found at index '+str(index)) 
else  :
    print('Not found')


