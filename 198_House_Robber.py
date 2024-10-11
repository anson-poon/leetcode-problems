def rob(nums) -> int:
    n = len(nums)

    if n == 0:
        return 0
    elif n == 1:
        return nums[0]

    # dp[i] stores the maximum money that can be rob from the first i houses
    dp = [0] * n
    dp[0] = nums[0]                     # one house, can only rob this house
    dp[1] = max(nums[0], nums[1])       # two houses, rob the house with more money

    for i in range(2, n):
        # Save the max of two options to dp[i]:
        # 1. Rob the current house plus max from non-adjacent houses
        # 2. Skip current house and rob the previous house
        dp[i] = max(dp[i-2] + nums[i], dp[i-1])

    return dp[-1]


houses = [2, 7, 9, 3, 1]
print(rob(houses))
