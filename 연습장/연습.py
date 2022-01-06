#n = int(input())
#a = list(map(int,input().split()))


#sum =[a[0]]


# import sys
# n = int(input())
# for i in range(n):
#     i = list(map(int,sys.stdin.readline().strip().split()))
#     avg = sum(i[1:])/i[0]
#     cnt=0
#     for j in range(1,len(i)):
#         if i[j] > avg:
#             cnt+=1
#     print("{:.3f}%".format(cnt/(len(i)-1)*100))

# a= []
# sets = set(range(1,10001))
# for i in range(1,10001):
#     i = str(i)
#     b = int(i)
#     for j in range(len(i)):
#         b += int(i[j])
#     a.append(b)
# for i in sorted(sets-set(a)):
#     print(i)

# n = int(input())
# cnt = 0
# for i in range(1,n+1):
#     if i <100:
#         cnt+=1
#     else:
#         i = str(i)
#         if int(i[2])-int(i[1]) == int(i[1]) - int(i[0]):
#             cnt+=1
#         else:
#             pass
# print(cnt)


# n = int(input(''))
# n2 = input('')
# a=[]
# for i in range(len(n2)):
#     a.append(int(n2[i]))
#
# print(sum(a))


# n = input('')
# b = ['-1'] * 26
#
# a = [chr(x) for x in range(97,123)]
# for i in n:
#     b[a.index(i)] = str(n.index(i))
#
# print(' '.join(b))


# n = int(input())
#
# for i in range(n):
#     s = ''
#     a,b = input().split()
#     for j in range(len(b)):
#         s += b[j]*int(a)
#     print(s)

# n = input().upper()
# alp = []
# num = []
# for i in list(set(n)):
#     alp.append(i)
#     num.append(list(n).count(i))
# if num.count(max(num)) >= 2:
#     print('?')
# else:
#     a = num.index(max(num))
#     print(alp[a])

# n = input().split()
# print(len(n))

# a,b = input().split()
# a = int(a[2]+a[1]+a[0])
# b = int(b[2]+b[1]+b[0])
# if a>b:
#     print(a)
# else:
#     print(b)

# n = input()
# a = list(map(int,input().split()))
# d=[]
# for i in a:
#     if i == 1:
#         d.append(i)
#     elif i ==2:
#         pass
#     else:
#         for j in range(2,i):
#             if i % j == 0:
#                 d.append(i)
#                 break
#
# print(len(list(set(a)-set(d))))

# n = input()
# cnt = 0
# for i in n:
#     if i in ['A','B','C']:
#         cnt += 3
#     elif i in ['D','E','F']:
#         cnt += 4
#     elif i in ['G','H','I']:
#         cnt += 5
#     elif i in ['J','K','L']:
#         cnt += 6
#     elif i in ['M','N','O']:
#         cnt += 7
#     elif i in ['P','Q','R','S']:
#         cnt += 8
#     elif i in ['V','T','U']:
#         cnt += 9
#     elif i in ['Y','W','X','Z']:
#         cnt += 10
#     else:
#         cnt +=2
# print(cnt)

# l = ['c=','c-','dz=','d-','lj','nj','s=','z=']
# n = input()
# cnt = 0
# for i in l:
#     if i in n:
#         cnt += n.count(i)
#         n = n.replace(i,',')
#     else:
#         pass
# print(len(n.replace(',',''))+cnt)

# n = int(input())
# cnt = 0
#
# for i in range(n):
#     w = input()
#     if len(w) == 1 or len(w) == 2:
#         cnt +=1
#         continue
#     wr = list(set(w)) #각 알파벳
#     for j in wr:
#         a=[] #인덱스
#         b=[] #인덱스 간 차이
#         if w.count(j) == 1:
#             if wr.index(j) == len(wr) - 1:
#                 cnt += 1
#             else:
#                 continue
#         else:
#             index = -1
#             while True:
#                 index = w.find(j,index+1)
#                 if index == -1:
#                     break
#                 a.append(index)
#         for x in range(1,len(a)):
#             b.append(a[x]-a[x-1])
#         if len(wr) == 1:
#             cnt += 1
#             break
#         if len(set(b)) != 1:
#             break
#         if len(set(b)) == 1 and b[0] !=1:
#             break
#         if len(set(b)) == 1 and b[0] == 1:
#             if wr.index(j) == len(wr)-1:
#                 cnt+=1
#             else:
#                 continue
# print(cnt)

# a,b,c = map(int,input().split())
#
# if b >= c:
#     print(-1)
# else:
#    print(int(a/(c-b)+1))

# n = int(input())
# a = 1
# cnt = 1
# while n > a:
#     a += 6*cnt
#     cnt += 1
# print(cnt)

# up = 1
# down = 1
# cnt = 1
# count = 1
# n = int(input())
#
# while True:
#     u1 = up
#     d1 = down
#     if n == 1:
#         break
#     for i in range(cnt):
#         if n == count:
#             break
#         if cnt == 1:
#             down = down+1
#             cnt += 1
#             count += 1
#             break
#         if i == cnt -1:
#             if up > down:
#                 up = up+down
#                 count+=1
#                 cnt+=1
#             else:
#                 down = up+down
#                 count += 1
#                 cnt+=1
#         else:
#             if u1/d1 < 1 :
#                 down = down-1
#                 up = up +1
#                 count+=1
#             else:
#                 down = down+1
#                 up = up-1
#                 count+=1
#
#     if n == count:
#         break
# print('{}/{}'.format(up,down))

# import math
# a,b,c = map(int,input().split())
# print(math.ceil((c - a) / (a - b))+1)

# c = int(input())
#
# for i in range(c):
#     h,w,n = map(int,input().split()) # h층수 w방수 n몇번째 손님
#
#     if n % h == 0: # 층수 구하기
#         floor = h
#         room = n // h
#     else:
#         floor = n % h
#         room = n//h + 1
#
#     print(floor*100 + room)

# n = int(input())
# for s in range(n):
#     k = int(input()) #층수
#     r = int(input()) #호수
#     p = [i for i in range(1,r+1)]
#     for j in range(k):
#         for i in range(len(p)):
#             if i == 0:
#                 p[i] = p[i]
#             else:
#                 p[i] = p[i-1] + p[i]
#     print(p[-1])

# m = int(input())
# n = int(input())
# c =[]
# for i in range(m,n+1):
#     if i == 1:
#         c.append(1)
#         continue
#     elif i == 2:
#         continue
#     for j in range(2,i):
#         if i % j == 0:
#             c.append(i)
#             break
# d = [i for i in range(m,n+1)]
# an = list(set(d)-set(c))
# if len(an) == 0:
#     print(-1)
# else:
#     print(sum(an))
#     print(min(an))
# print(an)

# a = int(input())
# b = []
#
# def so(a):
#     for i in range(2,a+1):
#         if a % i == 0:
#             b.append(i)
#             a = int(a/i)
#             so(a)
#             break
# so(a)
# for j in b:
#     print(j)

# m,n = map(int,(input().split()))
#
# c =[]
# for i in range(m,n+1):
#     if i == 1:
#         c.append(1)
#         continue
#     elif i == 2:
#         continue
#     for j in range(2,int(i**0.5)+1):
#         if i % j == 0:
#             c.append(i)
#             break
# d = [i for i in range(m,n+1)]
# an = list(set(d)-set(c))
# an = sorted(an)
# for i in an:
#
#     print(i)
# li = list(range(2,246912))
#
# while True:
#     a = int(input())
#
#     c = 0
#     if a == 0:
#         break
#     for i in range(a+1,2*a+1):
#         if i == 1:
#             c +=1
#             continue
#         elif i == 2:
#             continue
#         for j in range(2,int(i**0.5)+1):
#             if i % j == 0:
#                 c+=1
#                 break
#
#
#     print(a-c)
# c = []
# for i in range(2,10001):
#     if i == 2:
#       continue
#     for j in range(2,int(i**0.5)+1):
#         if i % j ==0:
#             c.append(i)
#             break
# li = list(range(2,10001))
# d = list(set(li)-set(c))
# n1 = int(input())
# for s in range(n1):
#     n = int(input())
#     a = int(n/2)
#     b = int(n/2)
#     while True:
#         if a in d:
#             if b in d:
#                 break
#             else:
#                 a -= 1
#                 b += 1
#         else:
#             a -= 1
#             b += 1
#     print(a,b)

# x,y,w,h = map(int,input().split())
# a= []
# a.append(x-0)
# a.append(y-0)
# a.append(w-x)
# a.append(h-y)
# print(min(a))

# a1,b1 = map(int,input().split())
# # a2,b2 = map(int,input().split())
# # a3,b3 = map(int,input().split())
# # a4,b4 = 0,0
# # if a1 == a2:
# #     a4 = a3
# # elif a1 == a3:
# #     a4 = a2
# # else:
# #     a4 = a1
# # if b1 == b2:
# #     b4 = b3
# # elif b1 == b3:
# #     b4 = b2
# # else:
# #     b4 = b1
# # print(a4,b4)

# while True:
#     d =[]
#     a,b,c = map(int,input().split())
#     if a ==0 and b ==0 and c == 0:
#         break
#     d.append(a)
#     d.append(b)
#     d.append(c)
#     maxx = max(d)
#     del d[d.index(maxx)]
#     if d[0]**2 + d[1]**2 == maxx**2:
#         print('right')
#     else:
#         print('wrong')

# import math
# r = int(input())
# a = r*r*math.pi
# b = 2*r*r
# print(round(a,6))
# print('{:.6f}'.format(b))
# n = int(input())
# for i in range(n):
#     x1,y1,r1,x2,y2,r2 = map(int,input().split())
#
#     r = ((x2-x1)**2 + (y2-y1)**2)**0.5
#
#     if r == 0:
#         if r1 == r2:
#             print(-1)
#         else:
#             print(0)
#     else:
#         if r==r1+r2 or abs(r2-r1) == r:
#             print(1)
#         elif abs(r2-r1) > r or r > r1+r2:
#             print(0)
#         else:
#             print(2)

# a = int(input())
#
# def fac(a,n,b):
#
#     if n == a+1 or a == 0:
#         print(b)
#     else:
#         b *= n
#         n+=1
#
#         fac(a,n,b)
# n = 1
# b = 1
# fac(a,n,b)

# n,m = map(int,input().split())
# a = list(map(int,input().split()))
# sum =[]
# c = 1
# for i in range(len(a)):
#     if i == len(a) - 2:
#         break
#     for j in range(i+1,len(a)):
#         if j == len(a)-1:
#             break
#         for k in range(j+1,len(a)):
#             if a[i]+a[j]+a[k] <= m:
#                 #print(a[i],a[j],a[k])
#                 sum.append(a[i]+a[j]+a[k])
#             else:
#                 continue
# print(max(sum))

# n = int(input())
# c = []
# for i in range(n):
#     a = int(input())
#     c.append(a)
# for i in sorted(c):
#     print(i)

# n = int(input())
# b = []
# for i in range(n):
#     c = 0
#     for j in range(len(str(i))):
#         i = str(i)
#         c += int(i[j])
#         i = int(i)
#
#     if i+c == n:
#         b.append(i)
# try:
#     print(min(b))
# except:
#     print(0)

# n = input() # 첫번째 문자열
# n2 = input() # 찾고자하는 문자열
# count = 0 # 첫번째 출력(몇번 나타나는지)
# c = [] # 어느 인덱스에서 나타나는지
# repeat = n2 #
# for i in range(1,len(n2)):
#
#     if n2[0:i] in n2[i:]:
#         repeat = n2[0:i]
#         continue
#     else:
#         break
#
# index = -1
# while True:
#     index = n.find(repeat, index+1)
#     if index == -1:
#         break
#     c.append(index)
#
# for i in c:
#     if n[i:i+len(n2)] == n2:
#         count += 1
#
#
# print(count)
# print(" ".join(str(i) for i in c))
# print(c)

# a = int(input())
#
# rank_list =[]
# list = []
# for i in range(a):
#     w,h = map(int,input().split())
#     list.append([w,h])
# for i in range(len(list)):
#     rank = 1
#     for j in range(len(list)):
#         if list[i][0] < list[j][0] and list[i][1] < list[j][1]:
#             rank +=1
#
#         else:
#             pass
#     rank_list.append(str(rank))
#
# print(" ".join(rank_list))

# n,m = map(int,input().split())
# board = []
# li = []
# for i in range(n):
#     board.append(list(input()))
#
# for i in range(n-7):
#     for j in range(m-7):
#         count1 = 0
#         count2 = 0
#         for a in range(i,i+8):
#             for b in range(j,j+8):
#                 if (a+b) % 2 ==0:
#                     if board[a][b] == 'W':
#                         count1 += 1
#                     else:
#                         count2 += 1
#                 else:
#                     if board[a][b] == 'B':
#                         count1 += 1
#                     else:
#                         count2 += 1
#         li.append(count1)
#         li.append(count2)
# print(min(li))

# n = int(input())
# a = 666
# c = 0
# while True:
#     if '666' in str(a):
#         c += 1
#     if c == n:
#         print(a)
#         break
#     a += 1

# import sys
# n = int(input())
# a = [0]* 10001
#
# for i in range(n):
#     b = int(sys.stdin.readline())
#     a[b-1] += 1
#
# for i in range(len(a)):
#     if a[i] !=0:
#         for j in range(a[i]):
#             print(i+1)

import sys

# from collections import Counter
# n = int(input())
# a = []
# for i in range(n):
#     a.append(int(sys.stdin.readline()))
# print(round(sum(a)/n))
# a.sort()
# print(a[len(a)//2])
# if n == 1:
#     print(a[0])
# else:
#     l = Counter(a).most_common(2)
#     if l[0][1] == l[1][1]:
#         print(l[1][0])
#     else:
#         print(l[0][0])
# print(max(a)-min(a))

# n = [x for x in input()]
# n.sort(reverse=True)
# print(''.join(n))
# import sys
# n = int(input())
# w =[]
# for i in range(n):
#     w.append(list(map(int,sys.stdin.readline().split())))
# for a,b in sorted(w,key=lambda x:(x[0],x[1])):
#     print(a,b)
#
# for a,b in sorted(w,key=w[0]):
#     print(a,b)
# import sys
# n = int(input())
# word = []
# for i in range(n):
#     word.append(sys.stdin.readline().strip())
# word = list(set(word))
# word.sort()
# word.sort(key=lambda x:len(x))
#
# for i in word:
#     print(i)
# import sys
# n = int(input())
# mem = []
# for i in range(n):
#     mem.append(list(sys.stdin.readline().split()))
# for i in range(len(mem)):
#     mem[i][0] = int(mem[i][0])
#     mem[i].append(i+1)
# mem.sort(key=lambda x:(x[0],x[2]))
#
# for i in mem:
#     print(i[0],i[1])
# import sys
# n = int(input())
# m = list(map(int,sys.stdin.readline().split()))
# a = sorted(set(m))
# s = {i:v for v,i in enumerate(a)}
# for i in m:
#     print(s[i])
import sys
# n = int(input())
# for k in range(n):
#     a = input()
#     for j in a.split():
#         v = ''
#         for i in range(len(j)):
#             v += j[-1-i]
#         print(v)

# n = int(input())
# for j in range(n):
#     a = sys.stdin.readline()
#     while True:
#         if '()' in a:
#             a = a.replace('()',"")
#         else:
#             break
#     if len(a) != 1:
#         print('NO')
#     else:
#         print('YES')
# import sys
#
# for i in range(3):
#     n = int(sys.stdin.readline())
#     a = 0
#     for i in range(n):
#         b = int(sys.stdin.readline())
#         a += b
#     if a == 0:
#         print(0)
#     elif a > 0:
#         print('+')
#     else:
#         print('-')

#
# n = int(input())
# c= []
# b= 0
# w = []
# t = True
# for i in range(n):
#     a = int(input())
#     while b < a:
#         c.append(b+1)
#         w.append('+')
#         b += 1
#     if c[-1] == a:
#         c.pop()
#         w.append('-')
#     else:
#         t = False
#         break
#
# if t == False:
#     print('NO')
# else:
#     print("\n".join(w))

# s1 = list(sys.stdin.readline().strip())
# s2 = []
# n = int(input())
# for i in range(n):
#     a = sys.stdin.readline().split()
#     if a[0] == 'L' and s1:
#         s2.append(s1.pop())
#     elif a[0] == 'D' and s2:
#         s1.append(s2.pop())
#     elif a[0] == 'B' and s1:
#         s1.pop()
#     elif a[0] == 'P':
#         s1.append(a[1])

# ans = s1 + list(reversed(s2))
# print("".join(ans))


# n = int(input())
# q = []
# for i in range(n):
#     a = sys.stdin.readline().split()
#     if a[0] == 'push':
#         q.append(a[1])
#     elif a[0] == 'pop':
#         try:
#             print(q.pop(0))
#         except:
#             print(-1)
#     elif a[0] == 'size':
#         print(len(q))
#     elif a[0] == 'empty':
#         if len(q) == 0:
#             print(1)
#         else:
#             print(0)
#     elif a[0] == 'front':
#         try:
#             print(q[0])
#         except:
#             print(-1)
#     else:
#         try:
#             print(q[-1])
#         except:
#             print(-1)

# n , m = map(int,input().split())
# l = [x for x in range(1,n+1)]
# yo = []
# a = m - 1
# while True:
#     if len(l) == 0:
#         break
#     if len(l) > a:
#         yo.append(str(l.pop(a)))
#         a += m-1
#     else:
#         a = a % len(l)
#         yo.append(str(l.pop(a)))
#         a += m-1
# print('<'+", ".join(yo)+'>')
# from collections import deque
# n = int(input())
# deq = deque()
#
# for i in range(n):
#     a = sys.stdin.readline().split()
#     if a[0] == 'push_back':
#         deq.appendleft(a[1])
#     elif a[0] == 'push_front':
#         deq.append(a[1])
#     elif a[0] == 'pop_front':
#         if len(deq) == 0:
#             print(-1)
#         else:
#             print(deq.pop())
#     elif a[0] == 'pop_back':
#         if len(deq) == 0:
#             print(-1)
#         else:
#             print(deq.popleft())
#     elif a[0] == 'size':
#         print(len(deq))
#     elif a[0] == 'empty':
#         if len(deq) == 0:
#             print(1)
#         else:
#             print(0)
#     elif a[0] == 'front':
#         if len(deq) == 0:
#             print(-1)
#         else:
#             print(deq[-1])
#
#     elif a[0] == 'back':
#         if len(deq) == 0:
#             print(-1)
#         else:
#             print(deq[0])
# n1 = int(input())
# n = list(map(int,input().split()))
#
# m1 = int(input())
# m = list(map(int,input().split()))
# n.sort()
#
# for i in m:
#     mid = 0
#     left = 0
#     right = len(n) - 1
#     while True:
#         mid = (right + left) // 2
#         if n[mid] == i:
#             print(1)
#             break
#         elif n[mid] < i:
#             left = mid+1
#         else:
#             right = mid - 1
#         if left > right:
#             print(0)
#             break

# while True:
#     a = sys.stdin.readline().strip()
#     if a == '0':
#         break
#     if len(a) == 1:
#         print('yes')
#     elif len(a) % 2 == 0:
#         for i in range(int(len(a)/2)):
#             t = True
#             if a[i] == a[-i-1]:
#                 continue
#             else:
#                 print('no')
#                 t = False
#                 break
#         if t == True:
#             print('yes')
#     elif len(a) % 2 == 1:
#         mid = len(a) // 2
#         for i in range(mid):
#             t = True
#             if a[mid-(i+1)] == a[mid+(i+1)]:
#                 continue
#             else:
#                 print('no')
#                 t = False
#                 break
#         if t == True:
#             print('yes')
#
# n = input()
# a = ''
# c = ''
# x = True
# for i in n:
#
#     if i == '<':
#         x = False
#         a += c
#         a += i
#     elif i == '>':
#         x = True
#         a += i
#         c =''
#     else:
#         if x == False:
#             a += i
#         elif x == True:
#             if i == ' ':
#                 a += c
#                 a += ' '
#                 c = ''
#             else:
#                 c = i+c
# a += c
# print(a)

# n = input()
# stack = []
# stick = 0
# for i in range(len(n)):
#     if n[i] =='(':
#         stack.append(i)
#     elif n[i] == ')':
#         stack.pop()
#         if n[i-1] == '(':
#             stick += len(stack)
#         else:
#             stick += 1
# print(stick)

# n = int(input())
# c = input()
# a = []
# s = []
# k = 0
# for j in range(n):
#     s.append(int(input()))
# for i in c:
#     if i == '*':
#         one = a.pop()
#         two = a.pop()
#         a.append(float(two) * float(one))
#     elif i == '+':
#         one = a.pop()
#         two = a.pop()
#         a.append(float(two) + float(one))
#     elif i == '-':
#         one = a.pop()
#         two = a.pop()
#         a.append(float(two) - float(one))
#     elif i == '/':
#         one = a.pop()
#         two = a.pop()
#         a.append(float(two) / float(one))
#     else:
#         a.append(s[ord(i)-ord('A')])
# print("{:.2f}".format(a[0]))

# n = int(input())
# a = list(map(int,sys.stdin.readline().strip().split()))
# if len(a) == 1:
#     print(a[0]* a[0])
# else:
#     print(max(a)*min(a))
#
from collections import deque

# n = input()
# a = [0 for _ in range(ord('z')-ord('a')+1)]
#
# for i in n:
#     idx = ord(i) - ord('a')
#     a[idx] += 1
# for i in a:
#     print(i,end=' ')


# while True:
#     n = sys.stdin.readline().rstrip('\n')
#     a=0
#     b=0
#     c=0
#     d=0
#     if not n:
#         break
#     for i in n:
#         if i.islower():
#               a+=1
#         elif i.isupper():
#               b+=1
#         elif i.isspace():
#               d += 1
#         elif i.isdigit():
#               c += 1
#     print(a,b,c,d)

#
# n = input()
# c = []
# for i in n:
#     if i.isupper():
#         if ord(i)+13 > ord('Z'):
#             a = ord('A') + 13-(ord('Z')-ord(i)) - 1
#             c.append(chr(a))
#         else:
#             c.append(chr(ord(i)+13))
#     elif i.islower():
#         if ord(i)+13 > ord('z'):
#             a = ord('a') + 13-(ord('z')-ord(i)) - 1
#             c.append(chr(a))
#         else:
#             c.append(chr(ord(i)+13))
#     else:
#         c.append(i)
#
# print("".join(c))

# a,b,c,d = map(int,input().split())
# ans1 = str(a)+str(b)
# ans2 = str(c)+str(d)
# print(int(ans1)+int(ans2))

# n = input()
# a = []
# for i in range(len(n)):
#     a.append(n[i:])
# for i in sorted(a):
#     print(i)
# n = int(input())
# for i in range(n):
#     a,b = map(int,input().split())
#     if a > b:
#         c = a
#         d = b
#     else:
#         c = b
#         d = a
#
#     while True:
#         if c % d != 0:
#             na = c%d
#             c = d
#             d = na
#         else:
#             break
#     print((a//d)*(b//d)*d)




def fac(n):
    if n == 1:
        return 1
    elif n == 0:
        return 1
    elif n == 2:
        return 2
    else:
        return n* fac(n-1)
#n = int(input())
# a = str(fac(n))
# c= 0
# for i in range(len(a)):
#     if a[-1-i] == '0':
#         c+=1
#     else:
#         break
# print(c)

# a, b = map(int,input().split())
# def count5(n):
#     a = 0
#     while n != 0:

def gcd(a,b):
    while True:
        if a % b == 0:
            return b
        else:
            e = a % b
            a = b
            b = e

# n = int(input())
# for i in range(n):
#     a = []
#     li = list(map(int,sys.stdin.readline().strip().split()))
#     li.pop(0)
#     li.sort(reverse=True)
#     for j in range(len(li)-1):
#         for k in li[j+1:]:
#             a.append(gcd(li[j],k))
#
#     print(sum(a))

# a,b = map(int,input().split())
# li = list(map(int,input().split()))
# li = [abs(x-b) for x in li]
# li.sort(reverse=True)
# li = deque(li)
# if len(li) == 1 :
#     print(li[0])
# elif len(li) == 2:
#     print(gcd(li[0],li[1]))
# else:
#     while len(li) != 1:
#         e = li.popleft()
#         r = li.popleft()
#         li.appendleft(gcd(e,r))
#     print(li[0])

# n = input()
# b= 0
# a = -1
# count = 0
# answer = ''
# for i in range(len(n)):
#     if n[a] == '0':
#         pass
#     else:
#         b += 2**count
#     a -= 1
#     count += 1
#     if count == 3 or i == len(n)-1:
#         count = 0
#         answer  =  str(b) + answer
#         b = 0
# print(answer)
# import math
# n = int(input())
# li = [0,0,1,1,2]
# for i in range(5,n+1):
#     one,two,three = math.inf, math.inf,li[i-1]
#     if i % 3 == 0:
#         one = li[i//3]
#     if i%2 ==0:
#         two = li[i//2]
#     s = 1+ min(one,two,three)
#     li.append(s)
# print(li[n])