class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        n = len(words)
        adj = defaultdict(set)
        for word in words:
            for char in word:
                adj[char] = set()
        for i in range (n - 1):
            len_word1, len_word2 = len(words[i]), len(words[i + 1])
            x, y = 0, 0
            while x < len_word1 and y < len_word2:
                if words[i][x] != words[i + 1][y]:
                    break
                x += 1
                y += 1
            if x == len_word1 and y == len_word2:
                continue
            elif y == len_word2:
                return ""
            elif x == len_word1:
                continue
            adj[words[i][x]].add(words[i + 1][y])
        visiting = set()
        visited = set()
        def dfs(char):
            if char in visiting:
                return False
            if char in visited:
                return True
            visited.add(char)
            visiting.add(char)
            if not adj[char]:
                ans.append(char)
                visiting.remove(char)
                return True
            for neighbor in adj[char]:
                if not dfs(neighbor):
                    return False
            visiting.remove(char)
            ans.append(char)
            return True

        ans = []
        for char in adj:
            if not dfs(char):
                return ""
        return "".join(ans[::-1])
            
        # Time compelxity: O(N + V + E) where N is the length of all words and V is the number of characters and E is the number of edges
        # Space complexity: O(V + E)
        # Topological Sort using DFS (Post order traversal)
