class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # get the unique sorted array nums (nlogn)
        nums_sorted = list(set(nums))
        nums_sorted.sort()

        # build a statistic array for the array nums (O(n))
        # check if a num is in nums: stat[num+10000]
        stat = [0] * 200001
        for n in nums:
            stat[n+100000] += 1


        # a nested loop to traverse all pairs in the sorted array (n^2)
            # check if -(nums[i] + nums[j]) is in nums (used stat) (O(1))
            # note: In both loop we only need to traverse the unique elements in the array
        triplets = []
        duplicate_counter = 0
        for i in range(len(nums_sorted)):
            for j in range(i+1, len(nums_sorted)):
                remain = -(nums_sorted[i] + nums_sorted[j])
                if remain>=-100000 and remain<=100000 and stat[remain + 100000]:
                    if nums_sorted[i] == remain and stat[remain+100000] == 1:
                        continue
                    if nums_sorted[j] == remain and stat[remain+100000] == 1:
                        continue

                    if nums_sorted[i] == remain or nums_sorted[j] <= remain:
                        triplet = [nums_sorted[i], nums_sorted[j], remain]
                        triplets.append(triplet)

        if stat[100000] >= 3:
            triplets.append([0,0,0])

        return triplets


                    

        