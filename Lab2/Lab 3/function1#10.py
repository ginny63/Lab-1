x = int(input())
 nums = []
 unums = []
 for i in range(x):
     nums.append(int(input()))

 def uni_list():
     for i in range(len(nums)):
         if nums[i] != nums[i - 1]:
             unums.append(nums[i])
            
     print(unums)

 uni_list()
