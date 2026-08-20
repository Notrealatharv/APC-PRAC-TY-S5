# two pointer problems

# the two pointer technique is a common algorithm pattern where we use two indices or pointers to traverse an arrayor string 
# usually used instead of nested loops so we can solve a problem by maintaining two positions (pointers) instead of checking every possible Pairs 

# ALGORITHM

# s1: initilize two pointers left=0 and right =n-1
# s2:create a loop continue while the pointers have not crossed ,while leftt<right
# s3:check the current elements arr[left] arr[right]
# s4:move the appropriate pointer ,if u r searching for 2 numberswhose sum is target sum=arr[l]+arr[r] 
# then if sum== target
# elif sum<target left+=1
# else right+=1

# Q) given a sorted array find wether 2 numbers have a sum equal to target
# target=int(input("ENTER NUMBER: "))
# arr=[1,2,4,6,8,9]
# left=0
# right=len(arr)-1
# while (left<right):
#     sum=arr[left]+arr[right]
#     if(sum == target):
#         print("found pair:",arr[left],"at index:",left,"and",arr[right],"at index:",right)
#         break
#     elif(sum<target):
#         left+=1
#     else:
#         right-=1


# Q)a movie theater has a list of avalaible movie ticket prizes sorted in ascending language u are given an integer array prizes containing ticket prizes
# an integer budget representing the maximum amount a customer wants to spend on two tickets your task is to find wether there are two diffrent
# tickets whos total prize is exactly equal to the given budget if sush a pair exist print the two ticket prizes otherwise print -1

# budget=int(input("ENTER NUMBER: "))
# prizes=[100,150,200,250,300,350]
# left=0
# right=len(prizes)-1
# sum=-1
# while (left<right):
#     sum=prizes[left]+prizes[right]
#     if(sum == budget):
#         print("found pair:",prizes[left],"at index:",left,"and",prizes[right],"at index:",right)
#         break
#     elif(sum<budget):
#         left+=1
#     elif(sum>budget):
#         right-=1
#     else:print("-1")


# Q)write a program to find maximum sum of sub array (window) from the given array list
# users=[100,48,82,57,34,112,65]
# days=3
# def sliding_window(users, days):
#     window_sum = 0
#     for i in range(days):
#         window_sum += users[i]

#     print("total number of users visited:", window_sum)
#     maxi[0]=window_sum
#     for i in range(1, len(users) - days + 1):
#         window_sum = window_sum - users[i - 1] + users[i + days - 1]
#         maxi[i+1]=window_sum
#         print("total number of users visited:", window_sum)
# print(max(maxi))

# sliding_window(users, days)


# Q)find the avarage of maximum sum 




arr=[2,4,6,8,10]
# prefix=[0]*len(arr)
# prefix[0]=arr[0]
# for i in range(1, len(arr)):
#     for j in range(0,i+1):
#         prefix[i]+=arr[j]

# print(prefix)  
 
# sum=0
# for i in range (1,4):
#     sum+=arr[i]
# print(sum)


# find the sum od ranges 0-1 1-3 2-4
sum=0
list1=[0,1,2]
list2=[2,4,5]

print(sum)

