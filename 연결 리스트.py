# class Node:
#     def __init__(self,data,next=None):
#         self.data = data
#         self.next = next
#
# def init_list():
#     global node_A
#     node_A = Node("A")
#     node_B = Node("B")
#     node_C = Node("C")
#     node_D = Node("D")
#     node_A.next = node_B
#     node_B.next = node_C
#     node_C.next = node_D
#
# def print_list():
#     global node_A
#     node = node_A
#     while node:
#         print(node.data)
#         node = node.next
#
# if __name__ =='__main__':
#     init_list()
#     print_list()

# aud = []
# char = input('')
# length = len(char)
# cur = len(char)
# l = int(input(''))
# for i in range(l):
#     aud.append(input(''))
#
# for j in aud:
#     if j == 'L':
#         if cur == 0:
#             pass
#         else:
#             cur -= 1
#     elif j == 'D':
#         if cur == len(char):
#             pass
#         else:
#             cur += 1
#     elif j == 'B':
#         if cur == 0:
#             pass
#         else:
#             char = char[0:cur-1] + char[cur:length]
#             cur -= 1
#     else:
#         ad = j.split(" ")[1]
#         if cur == 0:
#             char = ad + char
#             cur += 1
#         else:
#             char = char[0:cur] + ad + char[cur:]
#             cur += 1
#
# print(char)


import sys

a = list(sys.stdin.readline().strip())
print(a)
b = sys.stdin.readline()
print(b)