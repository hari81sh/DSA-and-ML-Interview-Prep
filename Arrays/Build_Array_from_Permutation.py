class Build_Array_from_permutation:
    def build_array(nums:list[int]) -> list[int]:
        #ans = [0 for _ in range(len(nums))]
        #if max(nums)<len(nums):
        #    for i in range(len(nums)):
        #        ans[i] = nums[nums[i]]
        #ans=[nums[nums[i]] for i in range(len(nums))]
        #return ans
        return [nums[nums[i]] for i in range(len(nums))]
        
    
    if __name__ =="__main__":
        nums = [0,2,1,5,3,4]
        #nums = [5,0,1,2,3,4]
        out = build_array(nums)
        print(out)