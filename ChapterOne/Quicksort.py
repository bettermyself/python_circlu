# def sum(arr):
#     total = 0
#     for i in arr:
#         total +=i
#     return  total
#
# print(sum([1,2,3,4,5]))


#练习4.1：请编写前述sum函数的代码

# def sum_total(arr):
#     length = len(arr)
#     if length==1:
#         return arr[0]
#     else:
#         total = arr.pop(0)+sum_total(arr)
#     return total
#
# print(sum_total([1,2,3,4,5]))

#练习4.2：编写一个递归函数来计算列表包含的元素数
# def count_total(arr):
#
#     if not arr:
#         return 0
#     else:
#         arr.pop()
#         total= 1 + count_total(arr)
#
#     return total
#
# print(count_total([1,2,3,4,5]))

# def max_num(arr):
#     length = len(arr)
#     max_number = arr[0]
#     if  length==1:
#         return max_number
#     else:
#         if arr[0]>arr[1]:
#             arr.pop(1)
#         else:
#             arr.pop(0)
#         return max_num(arr) #此处一定要加上return，不然函数返回None;
#
# print(max_num([1, 2, 3, 4, 7]))


def quick_sort(arr):
    if len(arr)<2:  #基线条件
        return arr
    else:
        pivot = arr[0]  #递归条件
        less = [i for i in arr if i < pivot] #Q&C
        greater = [i for i in arr if i > pivot]
        return quick_sort(less)+[pivot]+quick_sort(greater)

print(quick_sort([10,5,2,3]))
