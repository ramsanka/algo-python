
from typing import List


def findMaxOnes(nums: List[int]) -> int:
    len1 = len(nums)
    max_value = 0
    count = 0
    for i in range(0,len1):
        if nums[i] == 1:
            count += 1
            if (count > max_value):
                max_value = count
        else:
            count = 0

    return max_value        
    
        

def findMaxConsecutiveOnes(nums):
  ram1 = map(str,nums)
  
  ram2 = list(ram1)
  print(ram2)

  print(''.join(ram2))

  print(''.join(ram2).split('0'))

  ram3 = (map(len,''.join(ram2).split('0')))
  
  print("final")
  print(max(list(ram3)))

  return max(map(len, ''.join(map(str, nums)).split('0')))

rams = [0,1,1,1,0,1,1,1,1,0,1,1,1,1,1,1]
ret = findMaxOnes(rams)

ret_new = findMaxConsecutiveOnes(rams)
print(ret_new)
print("old technique")
print(ret)