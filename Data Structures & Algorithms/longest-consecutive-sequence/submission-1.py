class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        if not nums:
            return 0
        max_len = 1
        for n in nums:
            if n-1 not in num_set:
                k = n
                s_len = 1
                while(k+1 in num_set):
                    k += 1
                    s_len += 1
                if max_len < s_len:
                    max_len = s_len

        return max_len
        