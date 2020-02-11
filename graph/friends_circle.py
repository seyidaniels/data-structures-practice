class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        visited = [0] * len(M)
        count = 0
        for person in range(len(M)):
            if visited[person] == 0:
                self.dfs(M, visited, person)
                count += 1
        return count

    def dfs(self, N, visited, i):
        for j in range(len(N)):
            if (N[i][j] == 1 and visited[j] == 0):
                visited[j] = 1
                self.dfs(N, visited, j)
