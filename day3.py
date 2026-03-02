# # # # # # stack = []
# # # # # # stack.append(10)
# # # # # # stack.append(20)
# # # # # # stack.append(30)
# # # # # # stack.pop()
# # # # # # print(stack)

# # # # # class node:
# # # # #     def __init___(self,data):
# # # # #         self.data = data
# # # # #         self.next = None
# # # # # class LinkedList:
# # # # #     def __init__(self):
# # # # #         self.head = None
# # # # #     def push(self,data):
# # # # #         new = Node(data)
# # # # #         if self.head is None:
# # # # #             self.head=new
# # # # #             return
# # # # #         new.next=self.head
# # # # #         self.head=new
# # # # #     def pop(self):
# # # # #         if self.head is None:
# # # # #             return "underflow"
# # # # #         temp=self.head
# # # # #         self.head=self.head.next
# # # # #         temp=None
# # # # #     def is_empty(self):
# # # # #         print(self.head is None)
# # # # #     def peek(self): 
# # # # #         print(self.head.data)
# # # # #     def size(self):
# # # # #         temp=self.head
# # # # #         c=0
# # # # #         while temp:
# # # # #             c+=1
# # # # #             temp=temp.next
# # # # #         print("size of stack is:",c)
# # # # # s=LinkedList

# # # # # s.push(10)           
# # # # # s.push(20)
# # # # # s.push(30)
# # # # # s.peek()


# # # # #bubblesort
# # # # def bubble_sort(arr):
# # # #     n = len(arr)
# # # #     for i in range(n):
# # # #         for j in range(0,n-i-1):
# # # #             if arr[j]< arr[j+1]:
# # # #                 arr[j], arr[j+1] = arr[j+1], arr[j]
# # # #     return arr
# # # # nums = [64,32,58,12,55,90,74,11]
# # # # print(bubble_sort(nums))

 

# # # class Apple:
# # #     def __init__(self,name,age):
# # #         self.name = name
# # #         self.age = age
# # #     def details(self):
# # #         __salary = 100000
# # #         print("This is a normal method of a class")
# # #         print(self.age)
# # #         print(self.name)
# # #         print(__salary)
# # # obj = Apple("Tarun", 21)
# # # obj.details()

# # class Student:
# #     def __init__(self):
# #         self.name = "your name"
# # s = Student()
# # print(s.name)

# class Student:
#     def __init__(self):
#         self._marks = 90
# s = Student()
# print(s._marks)


class Student:
    def __init__(self):
        self.__salary = 170000
    def __result(self):
        print("marks are:")

s = Student()
print(s._Student__salary)
s._Student__result()

 

