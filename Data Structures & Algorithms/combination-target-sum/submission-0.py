class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        
        def dfs(i, cur_array, total):
            if total == target:
                res.append(cur_array.copy())
                return
            if i >= len(nums) or total > target:
                return
            cur_array.append(nums[i])
            dfs(i,cur_array,total+nums[i])
            cur_array.pop()
            dfs(i+1,cur_array,total)

        
        dfs(0,[],0)
        return res