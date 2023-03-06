class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum = []
        sum = 0
        for i in nums:
            sum += i
            runningSum.append(sum)
        return runningSum
