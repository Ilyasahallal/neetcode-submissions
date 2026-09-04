class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=len(nums)
        if nums == [] : 
            return 0
        if len(nums) == 1 :
            return 1
        sorted_nums=sorted(nums)
        seen=[]
        seen.append(sorted_nums[0])
        result = seen
        for i in range(1,n):
            num=sorted_nums[i]
            anterior_num=sorted_nums[i-1]
            if ( num == anterior_num + 1 ) : 
                seen.append(num)
                if len(seen) > len(result):
                    result = seen
            elif num == anterior_num :
                if len(seen) > len(result):
                    result = seen
                continue
            else : 
                seen = [num]
        return len(result)

