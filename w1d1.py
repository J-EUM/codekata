# 더해서 target값이 나오는 nums 안 두 수의 조합의 인덱스를 반환하는 함수를 만들어라
# ex: 
# nums = [4, 9, 11, 14]
# target = 13 일때
# [0, 1]을 return

def two_sum(nums, target):
    # 아래 코드를 작성해주세요.
  for i in range(len(nums)-1):
    for j in range(i+1, len(nums)):
      if nums[i] + nums[j] == target:
        return [i, j]
  
