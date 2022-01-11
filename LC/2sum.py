from typing import List


def twoSum(nums: List[int], target:int) -> List[int]:

    output = []
    flag = False
    for i in range(len(nums)):
        target_num = target - nums[i]
        for j in range(len(nums)):
            if target_num == nums[j] and j != i:
                output.append(i)
                output.append(j)
                flag = True
                break
        if flag == True:
            break

    return output


ram = [3,2,4]
target = 6

final_output = twoSum(ram,target)
print(final_output)