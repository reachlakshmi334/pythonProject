# Finding the maximum number of a list
#

def maximum(nums):
   Max = 0
   for item in nums:
       if item > Max:
           Max=item
   return Max

List = [5,8,50,39,59,43,29,40,59,79,100,50]
maxList = maximum(List)
print ("Highest value in the list is:", maxList)


