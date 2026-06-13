class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
    # 아래의 code는 이제 time-limit이 발생을 한다.
    # 이제 해당 문제를 효율적으로 해결하기 위해서는 O(n)으로 작성할 필요가 있다.
        # for i in range(1, len(nums)):
        #     k = nums[i]
        #     j = i + 1
        #     for j in range(j, len(nums)):
        #         # print(j)
        #         if nums[j] == k:
        #             return True
        # return False
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False