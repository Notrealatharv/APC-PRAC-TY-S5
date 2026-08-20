# # text="programming"
# # for i in text:
# #     if i not in new:
# #         new=new+i
# # print (new)


# # anagram
# # s1="silent"
# # s2="listen"
# # if sorted(s1)==sorted(s2):
# #     print("true")
# # else:
# #     print("false")
    
# # eventhough strings s and t find the smallest substring of s that contains all charchters of the including duplicates
# # s="ADOBECODEBANC"
# # t="ABC"

# #  a library has books with pages[12,34,67,90] assign them to two students such that the max pages 
# # assigned to any student is minimized

# pages = [12, 34, 67, 90]


# def can_allocate(pages, students, limit):
#     student_count = 1
#     current_sum = 0

#     for page in pages:
#         if current_sum + page <= limit:
#             current_sum += page
#         else:
#             student_count += 1
#             current_sum = page
#             if student_count > students:
#                 return False
#     return True


# def minimize_max_pages(pages, students):
#     low = max(pages)
#     high = sum(pages)

#     while low < high:
#         mid = (low + high) // 2
#         if can_allocate(pages, students, mid):
#             high = mid
#         else:
#             low = mid + 1

#     return low


# print("Minimum possible maximum pages per student:", minimize_max_pages(pages, 2))


# koko eating bananas 
# coco loves to eat abnanas there are n piles of bananas where the ith pie contains the guard will return in h hours koko can decide her eating speed of k babanas per hour each hour she chooses 1pile of bananas and eats k bananas from that pile , if the pile has fewer than k babanas she eats all of them and will not eats anymore bananas that hour, kokolikes to eat slowly but still wants to eat all the bananas before the guard returns , return the minimum integer k such that koko can eat all the bananas in h hours 
# 8262067986

# given a list off roll and a target roll determine wether tget exist in the list using linear  search return the index of the target if it is found otherwise return -1
# roll=[101,105,109,112,120]
# target=109
# def search():
#     for i in range (0, len(roll)):
#         if roll[i]==target:
#             print(i)
#     return -1
# search()
    


# a supermarket maintqians a list of products names currently avalaible in its inventory given a list of product names and a target product determine wether a target product exist in the inventory using linear search return thr index of the product if its found 
# list1=["milk","butter","eggs","rice"]
# target="eggs"
# def search():
#     for i in range (0, len(list1)):
#         if list1[i]==target:
#             return(i)
#     return -1
# print(search())

# a shopping mall stores the payment ststements of its customers , each element is represented as paid it eans customer has completed a payment , pending is customer not paid , given a list payments return the index of the first customer whos payment is pending
# list1=["paid","paid","pending","paid"]
# target="pending"
# def search():
#     for i in range (0, len(list1)):
#         if list1[i]==target:
#             return(i)
#     return -1
# print(search())

