class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        allow = defaultdict(list)
        for word in allowed:
            allow[word[:2]].append(word[2])
        start = list(bottom)

        def build(i, level, next_row):
            if i == len(level) - 1:
                return dfs(next_row)
            block = level[i] + level[i + 1]
            if block not in allow:
                return False
            for complement in allow[block]:
                next_row.append(complement)
                if build(i + 1, level, next_row):
                    return True
                next_row.pop()
            return False

        memo = {}
        def dfs(cur):
            if len(cur) == 1:
                return True
            current = "".join(cur)
            if current in memo:
                return memo[current]
            memo[current] = build(0, cur, [])
            return memo[current]
        return dfs(start)
