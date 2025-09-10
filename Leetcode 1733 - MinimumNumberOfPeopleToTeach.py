class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        need_to_teach = set()
        for friends in friendships:
            s = set()
            check = False
            for lan in languages[friends[0] - 1]:
                s.add(lan)
            for lan in languages[friends[1] - 1]:
                if lan in s:
                    check = True
                    break
            if not check:
                need_to_teach.add(friends[0] - 1)
                need_to_teach.add(friends[1] - 1)
        freq =[0]*(n+1)
        ans = 0
        for person in need_to_teach:
            for lan in languages[person]:
                freq[lan] += 1
                ans = max(ans, freq[lan])
        return len(need_to_teach) - ans
            

            


