from typing import List

#O(N^2)
def two_sum_v0(l: List[int], target: int) -> List[int]:
    returnedL = []
    found = False
    for i in range(len(l)-1):
        for j in range(i+1, len(l)):
            if l[i] + l[j] == target:
                returnedL.extend([i, j])
                found = True
                break
        if found:
            break
    return returnedL

#O(N)
def two_sum_v1(l: List[int], target: int) -> List[int]:
    returnedL = []
    dicMap = dict()
    for i in range(len(l)):
        complement = target - l[i]
        if complement in dicMap:
            returnedL.extend([dicMap[complement], i])
            break
        else:
            dicMap[l[i]] = i

    return returnedL

if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    t = 9
    r = two_sum_v0(nums, t)
    print(r)
    r1 = two_sum_v1(nums, t)
    print(r1)
