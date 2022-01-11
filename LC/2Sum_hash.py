from typing import List

def twoSum_hash(num: List, target: int) -> List[int]:

    hashmap = {}
    for i in range(len(num)):
        complement = target - num[i] 
        if complement in hashmap:
            return[i,hashmap[complement]]
        hashmap[num[i]] = i

ram = [3,2,4]
target = 6

output_final = twoSum_hash(ram,target)

print(output_final)


