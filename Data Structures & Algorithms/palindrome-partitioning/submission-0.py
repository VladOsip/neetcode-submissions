class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def isPali(string,start,end):
            while start < end:
                if string[start] != string[end]:
                    return False
                start+=1
                end-=1
            return True

        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return
            for j in range(i,len(s)):
                if isPali(s,i,j):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()
        
        dfs(0)
        return res