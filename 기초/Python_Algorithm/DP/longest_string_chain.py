"""
https://leetcode.com/problems/longest-string-chain/solution/

DP, DFS 

TODO : refactoring 
 
"""

"""
sample code

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key = len)
        
        path_len = {}
        res = 1
        
        for word in words:
            path_len[word] = 1
            
            for i in range(len(word)):
                candidate = word[:i] + word[i + 1:]
                
                if candidate in path_len:
                    path_len[word] = path_len[candidate] + 1
                    res = max(res, path_len[word])
                    
        return res


# 스터디원 풀이
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        chain_length = {w: 1 for w in words}
        
        words.sort(key=lambda x: -len(x)) # 길이가 긴 순
        
        for i, w in enumerate(words):
            for w2 in words[i+1:]:
                if len(w2) == len(w): continue
                    
                if len(w2) < len(w) - 1: break
                    
                for i in range(len(w)):
                    if w[:i] + w[i+1:] == w2:
                        chain_length[w2] = max(chain_length[w2], chain_length[w] + 1)
                        break
        
        return max(chain_length.values())
    

    


"""


class Solution:
    
    def longestStrChain(self, words: List[str]) -> int:
        len_idx = [None for _ in range(17)] # 0 index : len=0 element
        words_depth = [0 for _ in range(len(words))]
        words = sorted(words,key=len)     
        # get len_idx
        cur_len = 1
        for idx, ele in enumerate(words):
            if(len(ele)>cur_len):
                len_idx[len(ele)] = idx
                cur_len = len(ele)
        
        def check_predecessor(pre,cval):
            c_ptr = 0
            for idx, char in enumerate(pre):
                if(char!=cval[idx+c_ptr]):
                    c_ptr += 1 
                    if(c_ptr>1 or char!=cval[idx+c_ptr]):
                        print(pre,cval,'no')
                        return False
            print(pre,cval,'yes')
            return True
                            
        def dfs(idx):
            print(idx)
            depth = 1
            max_depth = 1
            val = words[idx]
            cl = len(val)
            if(cl==16 or len_idx[cl+1]==None):
                return depth
            c_idx = len_idx[cl+1]
            while(len(words[c_idx])==cl+1):
                if(words_depth[c_idx]>0):
                    max_depth = max(max_depth,depth+words_depth[c_idx])
                elif(check_predecessor(val,words[c_idx])):
                    words_depth[c_idx] = 1  
                    max_depth = max(max_depth,depth+dfs(c_idx))
                    print()
                c_idx += 1
                if(c_idx>=len(words)):
                    break
            words_depth[idx] = max_depth
            return  max_depth
        for idx in range(len(words)):
            if(words_depth[idx]>0):
                continue
            else : 
                dfs(idx)
        return max(max(words_depth),1)
        
        
    
    

    


