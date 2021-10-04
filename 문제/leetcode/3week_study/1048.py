class Solution:
    def longestStrChain(self, words: List[str]) -> int:
      words_ = sorted(words,key=len)
      for pivot_idx, pivot_value in enumerate(words_[:-1]):
        for comp_value in range(pivot_idx+1,len(words_)):
            

