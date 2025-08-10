class Words_Containing_Character:

    def __init__(self):
         pass

    def findWordsContaining(words: list[str], x: str) -> list[int]:
        ans=[]
        for i in range(len(words)):
            if x in words[i]: ans.append(i)
        return ans
    
class Build_Array_from_permutation:

    def __init__(self):
        pass

    def build_array(nums:list[int]) -> list[int]:
        #ans = [0 for _ in range(len(nums))]
        #if max(nums)<len(nums):
        #    for i in range(len(nums)):
        #        ans[i] = nums[nums[i]]
        #ans=[nums[nums[i]] for i in range(len(nums))]
        #return ans
        #return [nums[nums[i]] for i in range(len(nums))]
        a=[nums[i] for i in nums]
        return a
