def removeDuplicates(nums):
    i1 = 0
    i2 = i1 +1
    cnt = 0
    while i1 < i2 < len(nums):
        if nums[i1] == nums[i2]:
            i2+=1
        else:
            nums = nums[:i1] + nums[i2-1:]
            cnt+=1
            i1 = cnt
            i2 = i1+1
    return nums


if __name__ == '__main__':
    print(removeDuplicates([1,1,2]))
    print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))