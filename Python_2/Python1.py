#PROGRAM 1
# list1=[23,45,12,67,23,11,3,88]
# list1.sort()
# print(list1)

# print("The minimum Value is: ",list1[0])
# print("The maximum Value is: ",list1[-1])

#PROGRAM 2
# list2=[3,5,1,6,7,88,65,34,564]
# print(list2[::-1])

#PROGRAM 3
# list3=[33,4,2,5,66,7,3]
# print(sum(list3))

#PROGRAM 4
def containsDuplicate(nums):
    num_set = set()
    for i in nums:
        if i in num_set:
            return True
        num_set.add(i)
    print(num_set)
    return False

nums = [1, 1, 3, 4, 5]  # Example array

if containsDuplicate(nums):
    print("Duplicates found")
else:
    print("No duplicates")
    


