class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def isSimilar(a, b):
            diff = 0
            for x, y in zip(a, b):
                if x != y:
                    diff += 1
                if diff > 2:
                    return False
            return diff == 0 or diff == 2
        
        def dfs(i):
            for j in range(len(strs)):
                if not visited[j] and isSimilar(strs[i], strs[j]):
                    visited[j] = True
                    dfs(j)

        n = len(strs)
        visited = [False] * n
        groups = 0
        
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                dfs(i)
                groups += 1
        
        return groups
