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

# n,m,v = map(int,input().split()) # n-노드수, m-간선수, v-시작노드
# li = [[0]*(n+1) for _ in range(n+1)] # (n+1)x(n+1) 2차원 리스트 생성(인덱스 0이 들어가는 것은 무시 -> 실제로 사용하는 2차원리스트는 nxn
# for i in range(m):
#     a,b = map(int,input().split())
#     li[a][b] = li[b][a] = 1 # 양방향이기 때문에 연결된 부분 양쪽 모두 1로 설정
#
# visit = [0] * (n+1) # 인덱스 = 이미 방문한 노드라면 1, 방문하지 않은 노드는 0 (초기엔 0으로 설정)
#
# def dfs(v):
#     visit[v] = 1 # v번 노드를 방문 -> 0을 1로변경
#     print(v,end=' ')
#     for i in range(1,n+1):
#         if visit[i] == 0 and li[v][i] == 1:
#             dfs(i)
#
# def bfs(v):
#     visit[v]= 0
#     visit2 =[v]
#     while visit2:
#         a = visit2.pop(0)
#         print(a,end=' ')
#         for i in range(1,n+1):
#             if visit[i] == 1 and li[a][i]:
#                 visit2.append(i)
#                 visit[i] = 0
#
# answer = 0
# for i in range(1,n+1):
#     if visit[i] == 0:
#         dfs(i)
#         answer += 1
# print(answer)
#
#
#
#
#
#
#
#
# a, b = map(int,input().split())
# n= []
# for i in range(a):
#     n.append(int(input()))
# n.sort(reverse=True)
# cnt = 0
# while True:
#     if b == 0:
#         break
#     for i in range(len(n)):
#         if n[i] <= b:
#             cnt += b//n[i]
#             b = b-(n[i]*(b//n[i]))
#             n = n[i+1:]
#             break
# print(cnt)

# import sys
# n = int(input())
# m = int(input())
# #n,m, = map(int,input().split()) # n-노드수, m-간선수,
# li = [[0]*(n+1) for _ in range(n+1)] # (n+1)x(n+1) 2차원 리스트 생성(인덱스 0이 들어가는 것은 무시 -> 실제로 사용하는 2차원리스트는 nxn
# for i in range(m):
#     a,b = map(int,sys.stdin.readline().strip().split())
#     li[a][b] = li[b][a] = 1 # 양방향이기 때문에 연결된 부분 양쪽 모두 1로 설정
#
# visit = [0] * (n+1) # 인덱스 = 이미 방문한 노드라면 1, 방문하지 않은 노드는 0 (초기엔 0으로 설정)
# def bfs(v):
#     visit[v]= 1
#     visit2 =[v]
#     while visit2:
#         a = visit2.pop(0)
#         for i in range(1,n+1):
#             if visit[i] == 0 and li[a][i]:
#                 visit2.append(i)
#                 visit[i] = 1
# bfs(1)
# cnt =0
# for i in visit:
#     if i == 1:
#         cnt += 1
# print(cnt-1)

# n = int(input())
# li = []
# for i in range(n):
#     a, b = map(int,sys.stdin.readline().strip().split())
#     li.append([a,b])
#
# li = sorted(li, key=lambda a: a[0])
# li = sorted(li, key=lambda a: a[1])
#
# finish = 0
# cnt = 0
# for i in li:
#     if finish <= i[0]:
#         finish = i[1]
#         cnt += 1
# print(cnt)

# import heapq
# n = int(input())
# li = list(int(input()) for _ in range(n))
# heapq.heapify(li)
# ans = 0
# while len(li) != 1:
#     a = heapq.heappop(li)
#     b = heapq.heappop(li)
#     sum = a+b
#     ans += sum
#     heapq.heappush(li,sum)
#
# print(ans)

# n = int(input())
# ans = []
# top = list(map(int,input().split()))
#
# a = True
# for i in range(n):
#     if i == n-1:
#         ans.append(0)
#         break
#     top1 = top[:n-i]
#     loc = len(top1) - 1
#     now = top1.pop()
#     while loc != 0:
#         past = top1.pop()
#         if now < past:
#             ans.append(loc)
#             a = False
#             break
#         else:
#             loc -= 1
#     if a == False:
#         a = True
#         continue
#     else:
#         ans.append(0)
# ans.reverse()
# print(*ans)

# from collections import deque
# n = int(input())
# for i in range(n):
#     a = sys.stdin.readline().strip()
#     stack = deque()
#     li = deque()
#
#     for i in a:
#         if i == '<':
#             if stack :
#                 li.appendleft(stack.pop())
#         elif i == '>':
#             if li:
#                 stack.append(li.popleft())
#         elif i =='-':
#             if stack:
#                 stack.pop()
#         else:
#             stack.append(i)
#     print(''.join(list(stack)+list(li)))

# n = int(input())
# from collections import deque
# bil = []
# for i in range(n):
#     bil.append(int(sys.stdin.readline().strip()))
# stack =[]
# cnt = 0
# for i in range(n):
#     while stack and stack[-1] <= bil[i]:
#         stack.pop()
#     stack.append(bil[i])
#     cnt += len(stack)-1
# print(cnt)

# a,b = map(int,input().split())
# poket = {}
# for i in range(a):
#     name = sys.stdin.readline().strip()
#     poket[i+1] = name
#     poket[name] = i+1
# for i in range(b):
#     a = sys.stdin.readline().strip()
#     try:
#         print(poket[int(a)])
#     except:
#         print(poket[a])



# n = int(input())
# a = deque([i for i in range(1,n+1)])
# while len(a) != 1:
#     a.popleft()
#     if len(a) == 1:
#         break
#     a.append(a.popleft())
#
# print(a[0])

# n = int(input())
# li = list(map(int,input().split()))
# a = {}
# for i in li:
#     try:
#         if a[i]:
#             a[i] += 1
#     except:
#
#         a[i] = 1
# m = int(input())
# li2 = list(map(int,input().split()))
# ans = []
# for i in li2:
#     try:
#         ans.append(a[i])
#     except:
#         ans.append(0)
#
# print(*ans)

# a,b = map(int,input().split())
# def wa(a):
#     c = 1
#     if a == 0:
#         return c
#     while a != 1 :
#         c *= a
#         a -= 1
#     return c
# def wa2(a,b):
#     c = 1
#     while b != 0:
#         c *= a
#         a -= 1
#         b -= 1
#     return c
#
# print(int(wa2(a,b)/wa(b)))

# a,b = map(int,input().split())
# stack = deque([i for i in range(1,a+1)])
# ans =[]
# count = 1
# while stack:
#     if count == b:
#         ans.append(stack.popleft())
#         count = 1
#         continue
#     stack.append(stack.popleft())
#     count += 1
#
# print(str(ans).replace('[','<').replace(']','>'))


# a = int(input())
# b= input()
#
# ans = 0
# for i in range(a):
#     ans += (ord(b[i])-96) * (31**i)
# print(ans % 1234567891)

# n = int(input())
# ans = []
# for i in range(n):
#     a = int(sys.stdin.readline().strip())
#     if a != 0:
#         ans.append(a)
#     else:
#         ans.pop()
#
# if len(ans) == 0:
#     print(0)
# else:
#     print(sum(ans))


# while True:
#     stack = []
#     a = sys.stdin.readline().rstrip()
#     if a == '.':
#         break
#     for i in a:
#         if i == '(' or i == '[':
#             stack.append(i)
#         elif i ==')':
#             if stack and stack[-1] == '(':
#                 stack.pop()
#             else:
#                 stack.append(i)
#                 break
#         elif i ==']':
#             if stack and stack[-1] == '[':
#                 stack.pop()
#             else:
#                 stack.append(i)
#                 break
#     if not stack:
#         print('yes')
#     if stack:
#         print('no')

# n = int(input())
# li = [1,1,1]
# for i in range(n):
#     a = int(input())
#     leng = len(li)
#     if leng >= a:
#         print(li[a-1])
#     else:
#         for j in range(leng,a+1):
#             li.append(li[j-2]+li[j-3])
#         print(li[a-1])

# import heapq
# n = int(input())
# qu = []
# heapq.heapify(qu)
# for i in range(n):
#     a = int(sys.stdin.readline().strip())
#     if a != 0:
#         heapq.heappush(qu,a)
#     else:
#         if qu:
#             print(heapq.heappop(qu))
#         else:
#             print(0)

# a,b = map(int,input().split())
# j = {}
# for i in range(a):
#     url,password = sys.stdin.readline().strip().split()
#     j[url] = password
#
# for i in range(b):
#     want = sys.stdin.readline().strip()
#     print(j[want])
# n = int(input())
# for i in range(n):
#     a,b = map(int,sys.stdin.readline().strip().split())
#     c = list(map(int,sys.stdin.readline().strip().split()))
#     li = deque()
#     idx = 0
#     for i in c:
#         li.append([i,idx])
#         idx+=1
#
#     idx1 = 0
#     ans = []
#     while True:
#         if idx1 == a:
#             break
#         s = True
#         for i in range(1,len(li)):
#             if li[0][0] < li[i][0] :
#                 li.append(li.popleft())
#                 s = False
#                 break
#         if s == True:
#             idx1 += 1
#             ans.append(li.popleft())
#     cc = 0
#     for j in ans:
#         if j[1] == b:
#             print(cc+1)
#         else:
#             cc += 1

# n, m =map(int,input().split())
# li = list(map(int,input().split()))
# sum_list =[0]
# c_sum = 0
# for i in li:
#     c_sum += i
#     sum_list.append(c_sum)
# for i in range(m):
#     a,b = map(int,sys.stdin.readline().strip().split())
# #     print(sum_list[b]-sum_list[a-1])
# n = int(input())
# for i in range(n):
#     a = sys.stdin.readline().strip()
#     b = int(sys.stdin.readline().strip())
#     c = sys.stdin.readline().strip()
#     if len(c) != 2:
#         c = c[1:-1].split(',')
#         c = deque(c)
#     else:
#         c = deque()
#     try:
#         front = True
#         for i in a:
#             if i =='R':
#                 if front == True:
#                     front = False
#                 else:
#                     front = True
#             else:
#                 if front == True:
#                     c.popleft()
#                 else:
#                     c.pop()
#         if front == False:
#             c.reverse()
#         print('['+",".join(c)+']')
#     except:
#         print('error')

# n = int(sys.stdin.readline().strip())
# ans = []
# top = deque(map(int,sys.stdin.readline().strip().split()))
# s = {}
# top.reverse()
# ans = deque()
# while top:
#     now = top.popleft()
#     s = 0
#     x = True
#     for i in top:
#         if i > now:
#             ans.appendleft(len(top)-s)
#             x = False
#             break
#         s += 1
#     if x:
#         ans.appendleft(0)
# print(*ans)

# n = int(input())
# li = list(map(int,input().split()))
# dp = [0] * n
# dp[0] = li[0]
# for i in range(1,n):
#     dp[i] = max(li[i],li[i]+dp[i-1])
#
# print(max(dp))

# a,b = map(int,input().split())
# n = list(map(int,input().split()))
# left,right = 1,max(n) # left: 가장짧은 나무의 길이, right: 가장긴 나무의 길이
#
# while left <= right:
#     mid = (left+right) // 2  # 자를 톱의 높이 설정
#     meter = 0                # 자르고 가져갈 수 있는 나무의 미터
#     for i in n:              # 반복문을 돌며 나무가 톱의 높이 보다 클경우
#         if i > mid:          # (현재 나무높이 - 톱의 높이)값을 현재 가지고 있는 나무의 미터와 더하여 갱신
#             meter += i-mid
#             if meter >= b:   # 자른 나무의 길이가 b 이상이면 더이상 반복 X
#                 break
#     if meter >= b:           # 자른 나무의 길이가 b 이상일 때
#         left = mid+1         # 가장 짧은 나무의 길이를 톱의 높이(mid) +1 한값으로 설정
#     else:                    # 자른 나무의 길이가 b 미만일 때
#         right = mid-1        # 가장 긴 나무의 길이를 톱의 높이(mid) -1 값으로 설정
# print(right)

# a, b = map(int,input().split())
# li = [int(input()) for _ in range(a)]
# start = 1
# end = max(li)
# while start <= end:
#     mid = (start+end) // 2
#     cnt = 0
#     for i in li:
#         cnt += i//mid
#         if cnt >=b:
#             break
#     if cnt >= b:
#         start = mid+1
#     else:
#         end = mid-1
# print(end)

# n = int(input())
# m = int(input())
# bb = []
# cc = []
# x = []
# for i in range(m):
#     a,b = map(int,sys.stdin.readline().split())
#     x.append([a,b])
# x.sort(key=lambda x:x[1])
# x.sort(key=lambda x:x[0])
# for i in x:
#     if i[0] == 1:
#         bb.append(i[1])
#     elif i[1] == 1:
#         bb.append(i[0])
#     elif i[0] in bb:
#         cc.append(i[1])
#     elif i[1] in bb:
#         cc.append(i[0])
#
# print(len(set(bb+cc)))

# n = input()
# a = [0] * 10
# for i in n:
#     i = int(i)
#     if i == 6 and a[i] >= a[9]:
#         a[9] += 1
#     elif i == 9 and a[i] >= a[6]:
#         a[6] += 1
#     else:
#         a[i] += 1
# print(max(a))

# a,b = map(int,input().split())
# n = 1
# c = []
# while n <= b:
#     for i in range(n):
#         c.append(n)
#     n += 1
# print(c)
# print(sum(c[a-1:b]))
#
# n = int(input())
# ans = [0] * 21
#
# for i in range(n):
#     a = input().split()
#     if a[0] == 'add':
#         if ans[int(a[1])] == 0:
#             ans[int(a[1])] = 1
#     elif a[0] == 'remove':
#         if ans[int(a[1])] == 1:
#             ans[int(a[1])] = 0
#     elif a[0] == 'check':
#         if ans[int(a[1])] == 1:
#             print(1)
#         else:
#             print(0)
#     elif a[0] == 'toggle':
#         if ans[int(a[1])] == 1:
#             ans[int(a[1])] = 0
#         else:
#             ans[int(a[1])] = 1
#     elif a[0] == 'all':
#         ans = [1 for i in range(21)]
#     else:
#         ans = [0] * 21

# n = input()
# a = [0,9,99,999,9999,99999,999999,9999999,99999999]
# print(int(n)*len(n) - sum(a[:len(n)]))

# n = int(input())
# a = [-1] * 11
# b = [0] * 11
# for i in range(n):
#     x,y = map(int,input().split())
#     if a[x] !=0 and a[x] != 1:
#         a[x] = y
#     elif a[x] != y:
#         a[x] = y
#         b[x] += 1
#
# print(sum(b))

# a,b = map(int,input().split())
# li = [0]
# def wa():
#     if len(li) == b+1:
#         return print(*li[1:])
#     for i in range(1,a+1):
#         if i in li or i < li[-1]:
#             continue
#         li.append(i)
#         wa()
#         li.pop()
#
# wa()

# n,m,b = map(int,sys.stdin.readline().strip().split())
# li = []
# for i in range(n):
#     li.extend(list(map(int,sys.stdin.readline().strip().split())))
# count = []
# compare = list(set(li))
# if len(compare) == 1:
#     print(0,compare[0])
# else:
#     for j in compare:
#         a = True
#         cnt = 0
#         for i in li:
#
#             if i == j:
#                 continue
#             if i > j:
#                 a = False
#                 b += i-j
#                 cnt += 2
#             elif i < j and b >= j-i:
#                 a = False
#                 b -= j-i
#                 cnt += 1
#
#         count.append(cnt)
#     x = []
#     for i in range(len(count)):
#         if count[i] == 0:
#             continue
#         x.append([count[i],compare[i]])
#     x.sort(key=lambda x:x[1])
#     x.sort(key=lambda x:x[0])
#     print(*x[0])
# a,b = map(int,input().split())
# com = deque(map(int,input().split()))
# li = [i for i in range(1,a+1)]
# li = deque(li)
# c = 0
# for i in list(com):
#     while True:
#         if li[0] == i:
#             li.popleft()
#             com.popleft()
#             break
#         if li.index(i) < len(li)/2:
#             li.append(li.popleft())
#             c+=1
#         else:
#             li.appendleft(li.pop())
#             c+= 1
# print(c)


# n = int(input())
# li =[]
# for i in range(n):
#     li.append(list(map(int,input().split())))
# visit = [[False]*n for _ in range(n)]
#
# def dfs(a,b):
#     if a <= -1 or a >= n or b <= -1 or b >= n:
#         return False
#     now = li[a][b]
#     if now == -1:
#         print('HaruHaru')
#         exit(0)
#
#     if visit[a][b] == False:
#         visit[a][b] = True
#         dfs(a+now,b)
#         dfs(a,b+now)
#
# dfs(0,0)
# print('Hing')

# genres =['a','b','c','d','a','d','d','d','a','a','c','c']
# plays =  [100,300,400,150,100,300,200,600,700,110,900,9000]
# def a(generes,plays):
#     a = {}
#     b = []
#     ans = []
#     for i in range(len(plays)):
#         try:
#             b.append([genres[i],plays[i],i])
#             a[genres[i]] += plays[i]
#         except:
#             a[genres[i]] = plays[i]
#     a1 = sorted(a.items(), key=lambda x: x[1], reverse=True)
#     b2 = sorted(b,key=lambda x: x[1], reverse=True)
#     for i in a1:
#
#         c=0
#         for j in b2:
#             if c == 2:
#                 break
#             if i[0] == j[0]:
#                 ans.append(j[2])
#                 c += 1
#     return ans
# print(a(['a','b','c','d','a','d','d','d','a','a','c','c'],[100,300,400,150,100,300,200,600,700,110,900,9000]))
# from collections import defaultdict
# dic = defaultdict(int)
# total = 0
# while True:
#     a = sys.stdin.readline().strip()
#     if not a:
#         break
#     dic[a] +=1
#     total += 1
# key_list = sorted(list(dic.keys()))
#
# for i in key_list:
#     print('%s %.4f' % (i,(dic[i]/total*100)))

import heapq
#
# n = int(input())
# l = []
# for i in range(n):
#     a = list(map(int,input().split()))
#     for j in a:
#         heapq.heappush(l, j)
#         if len(l) > n:
#             heapq.heappop(l)
#
# print(l[0])

# n = int(input())
# dic = {}
# for i in range(n):
#     a,b,c = sys.stdin.readline().strip().split()
#     dic[a] = [b,c] # [left,right]
#
# def inorder(node):
#     if node != '.':
#         inorder(dic[node][0]) #left
#         print(node,end='')            #middle
#         inorder(dic[node][1]) #right
#
# def preorder(node):
#     if node != '.':
#         print(node,end='')
#         preorder(dic[node][0]) #left
#         preorder(dic[node][1]) #right
#
# def postorder(node):
#     if node != '.':
#         postorder(dic[node][0]) #left
#         postorder(dic[node][1]) #right
#         print(node,end='')
# preorder('A')
# print()
# inorder('A')
# print()
# postorder('A')

# n = int(input())
# li = [[] for _ in range(n+1)]
#
#
# ans = [0 for _ in range(n+1)]
#
# for i in range(n-1):
#     a, b = map(int, sys.stdin.readline().strip().split())
#     li[a].append(b)
#     li[b].append(a)
#
# def bfs(node):
#     q = deque()
#     q.append(node)
#     while q:
#         root = q.popleft()
#         for j in li[root]:
#             if ans[j] == 0:
#                 ans[j] = root
#                 q.append(j)
#
# bfs(1)
# for i in range(2,n+1):
#     print(ans[i])

# n = int(input())
# q = deque()
# for i in range(n):
#     a = sys.stdin.readline().strip().split()
#     if a[0] == 'push':
#         q.append(a[1])
#     elif a[0] == 'front':
#         if len(q) == 0:
#             print(-1)
#         else:
#             print(q[0])
#     elif a[0] == 'back':
#         if len(q) == 0:
#             print(-1)
#         else:
#             print(q[-1])
#     elif a[0] == 'size':
#         print(len(q))
#     elif a[0] == 'pop':
#         if len(q) == 0:
#             print(-1)
#         else:
#             print(q.popleft())
#     elif a[0] == 'empty':
#         if len(q) == 0:
#             print(1)
#         else:
#             print(0)

# a,b = map(int,input().split())
# rel = [[] for _ in range(a+1)]
# for i in range(b):
#     x,y = map(int,sys.stdin.readline().strip().split())
#     rel[y].append(x)
# def bfs(start):
#     visit = [0] * (a + 1)
#     q = deque()
#     q.append(start)
#     visit[start] = 1
#     cnt = 1
#     while q:
#         node = q.popleft()
#         for i in rel[node]:
#             if visit[i] == 0:
#                 q.append(i)
#                 visit[i] = 1
#                 cnt += 1
#     return cnt
# ans = []
# for i in range(1,a+1):
#     ans.append(bfs(i))
#
# ma = max(ans)
#
# for i in range(len(ans)):
#     if ans[i] == ma:
#         print(i+1, end=' ')

# n = int(input())
# for i in range(n):
#     a,b = map(int,sys.stdin.readline().strip().split())
#
#     if  a % 10 == 1 or a % 10 == 5 or a % 10 == 6:
#         print(a%10)
#     elif a % 10 == 0:
#         print(10)
#     else:
#         if b % 4 == 0:
#             c = 4
#         else:
#             c = b % 4
#         x = str(a**c)
#         print(x[-1])
# from collections import defaultdict
# name = defaultdict(int)
# n = int(input())
# for i in range(n):
#     file = sys.stdin.readline().strip().split('.')
#     name[file[1]] += 1
# new = sorted(name.items())
#
# for i in new:
#     print(i[0],i[1])

# n = int(input())
# a = list(map(int,input().split()))
# b = list(map(int,input().split()))
# a = sorted(a)
# b = sorted(b,reverse=True)
# ans = 0
# for i in range(len(a)):
#     ans += (a[i]*b[i])
# print(ans)

# d,n = map(int,input().split())
# oven = list(map(int,input().split()))
# dow = list(map(int,input().split()))
#
# for i in range(1,d):
#     oven[i] = min(oven[i],oven[i-1])
#
# now = 0
# ans = 0
# for i in reversed(range(d)):
#     if oven[i] >= dow[now]:
#         now += 1
#         ans = i+1
#     if now >= n:
#         print(ans)
#         sys.exit(0)
# print(0)

# n,m = map(int,input().split())
# dic = {}
# for i in range(n):
#     name = sys.stdin.readline().strip()
#     dic[name] = 1
# ans = []
# for i in range(m):
#     name = sys.stdin.readline().strip()
#     try:
#         dic[name] += 1
#         ans.append(name)
#     except:
#         continue
# ans.sort()
# print(len(ans))
# for i in ans:
#     print(i)

# from itertools import combinations_with_replacement
# num = [1,5,10,50]
# c = int(input())
# result =[]
#
# for a in combinations_with_replacement(num, c):
#     sum = 0
#     for i in a:
#         sum += i
#     result.append(sum)
#
# print(len(set(result)))
import math
# n,k = map(int,input().split())
# li = deque()
# for i in range(n):
#     li.append(float(input()))
# li = sorted(li)
# def sol1(li):
#     li1 = deque(li)
#     for i in range(k):
#         li1.popleft()
#         li1.pop()
#     re = sum(li1) / len(li1)
#     return re
#
# def sol2(li):
#     li1 = deque(li)
#     for i in range(k):
#         li1.popleft()
#         li1.pop()
#     for i in range(k):
#         li1.append(li1[-1])
#         li1.appendleft(li1[0])
#     return sum(li1) / len(li1)
#
# print('%.2f'%(sol1(li)+0.00000001))
# print('%.2f'%(sol2(li)+0.00000001))

# n, k = map(int,input().split())
# s = list(map(int,input().split()))
# d = list(map(int,input().split()))
#
# for i in range(k):
#     ans = [0] * n
#     for j in range(n):
#         ans[d[j]-1] = s[j]
#     s = ans
#
# print(*ans)
# import copy
# t = int(input())
# for i in range(t):
#     n,d = map(int,sys.stdin.readline().split())
#     array = []
#     for i in range(n):
#         array.append(list(map(int,sys.stdin.readline().split())))
#     ans = copy.deepcopy(array)
#     idx = n // 2
#     if d % 360 == 0:
#         pass
#     elif d < 0:
#         for j in range(int(-d/45)%4):
#             for i in range(n):
#                 ans[i][i] = array[i][idx]
#                 ans[idx][i] = array[i][i]
#                 ans[i][idx] = array[i][n-1-i]
#                 ans[n-1-i][i] = array[idx][i]
#                 array = copy.deepcopy(ans)
#     elif d > 0:
#         for j in range(int(d/45)%4):
#             for i in range(n):
#                 ans[i][i] = array[idx][i]
#                 ans[idx][i] = array[n-1-i][i]
#                 ans[i][idx] = array[i][i]
#                 ans[n-1-i][i] = array[n-1-i][idx]
#                 array = copy.deepcopy(ans)
#
#     for i in ans:
#         print(*i)

# 10 000 000
# n, k = map(int,input().split())
# cnt = 0
#
# while True:
#     if str(bin(n)[2:]).count('1') <= k:
#         print(cnt)
#         break
#     else:
#         n += 1
#         cnt += 1
# li =[0]
# dp = [0]
# n = int(input())
# for i in range(n):
#     li.append(int(input()))
# if n == 1:
#     dp.append(li[1])
# elif n == 2:
#     dp.append(li[1])
#     dp.append(li[1]+li[2])
#
# else:
#     dp.append(li[1])
#     dp.append(li[1] + li[2])
#
#     for i in range(3,n+1):
#         dp.append(max(dp[i-1],li[i]+li[i-1]+dp[i-3],li[i]+dp[i-2]))
#
#
# print(dp[-1])
# board =[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
# moves =[1,5,3,5,1,2,1,4]
# answer = 0
# st = []
# print(len(board))
# for i in moves:
#     for j in range(len(board)):
#         if board[i-1][j] != 0:
#             if st:
#                 if st[-1] == st.append(board[i][j]):
#                     board[i][j] = 0
#                     st.pop()
#                     break
#         st.append(board[i][j])
#         board[i][j] = 0
# print(st)

# n,s = map(int,input().split())
# li = list(map(int,input().split()))
# left = 0
# right = 0
# a_sum = 0
# ans = 100001
#
# while True:
#     if a_sum >= s:
#         ans = min(ans,right-left)
#         a_sum -= li[left]
#         left += 1
#
#     elif right == n:
#         break
#     else:
#         a_sum += li[right]
#         right += 1
#
#
# if ans == 100001:
#     print(0)
# else:
#     print(ans)

# n = int(input())
# time = [] # 전체 강의시간표
# classroom = [] # 강의실의 끝나는 시간 담는 리스트 , 해당 리스트의 길이가 곧 강의실 갯수
# for i in range(n):
#     s, t = map(int,sys.stdin.readline().strip().split())
#     time.append([s,t])
# time.sort(key=lambda x: x[0])
# heapq.heappush(classroom,time[0][1])
#
# for i in range(1,n):
#     if time[i][0] < classroom[0]:
#         heapq.heappush(classroom, time[i][1])
#     else:
#         heapq.heappop(classroom)
#         heapq.heappush(classroom, time[i][1])
# print(len(classroom))

# n,m = map(int,input().split())
# num = []
# for i in range(n):
#     num.append(int(input()))
# num.sort()
# start, end =0,0
# ans = sys.maxsize
#
# while start < n and end < n:
#     if num[end]-num[start] >= m:
#         ans = min(num[end]-num[start],ans)
#         start += 1
#     else:
#         end += 1
# print(ans)

# 4 7 44 47 74 77 444 447 474 477 744
# 1 2 3  4  5  6  7   8
# n = int(input())
# f = '47'
# f1 = '74'
# def sol(x):
#     if x <= 2:
#         return f[x-1]
#     else:
#         a = (x-1) // 2
#         b = x % 2
#         return sol(a) + f1[b]
#
# print(sol(n))

# n = input()
# a = input()
# ans = ''
# for i in n:
#     try:
#         int(i)
#     except:
#         ans += i
# if a in ans:
#     print(1)
# else:
#     print(0)

# n = int(input())
# a = list(map(int,input().split()))
# b,c = map(int,input().split())
# ans = 0
# for i in a:
#     if i-b <= 0:
#         continue
#     if abs(i-b) % c == 0:
#         ans += (abs(i - b) // c)
#     else:
#         ans += (abs(i-b) // c) +1
#     print(ans)
# print(ans+len(a))

# n = int(input())
# if n % 2 == 0:
#     print('CY')
# else:
#     print('SK')

# n,m = map(int,input().split())
# miro =[]        # 미로 n*m 배열
# for i in range(n):
#     miro.append(list(map(int,input())))
#
# dx = [1,-1,0,0] # 상,하,좌,우
# dy = [0,0,1,-1]
#
# q = deque()     # 현재 위치 담을 데크
# q.append([0,0]) # 맨 처음 위치인 0,0 대입
#
# while q:              # bfs
#     x,y = q.popleft() #
#
#     for i in range(4):  # 상 하 좌 우 -> 4번 반복
#         nx = x + dx[i]
#         ny = y + dy[i]
#
#         if nx < 0 or nx >= n or ny < 0 or ny >= m: # x,y 위치가 기존 미로범위보다 작거나 커지면 continue
#             continue
#         if miro[nx][ny] == 0:   # 미로의 위치의 값이 0이면 벽이므로 continue
#             continue
#
#         if miro[nx][ny] == 1:             # 이동하는 미로의 위치 값이 1인경우 (아직 방문 하지 않았다는 뜼)
#             miro[nx][ny] = miro[x][y] + 1 # 이동하는 미로의 위치 값 = 현재 위치의 값 + 1
#             q.append([nx,ny])             # 데크에 이동하는 위치의 x,y 값 추가
#
# print(miro[n-1][m-1])

# t = int(input())
# for i in range(t):
#     n,m,k = map(int,input().split())
#     ground = [[0]*n for _ in range(m)]
#
#     for i in range(k):
#         x,y = map(int,input().split())
#         ground[y][x] = 1
#     dx = [-1,1,0,0]
#     dy = [0,0,-1,1]
#     def bfs(a,b):
#         q = deque()
#         q.append([a,b])
#         ground[a][b] = 0
#         while q:
#             x,y = q.popleft()
#             for i in range(4):
#                 nx = x + dx[i]
#                 ny = y + dy[i]
#
#                 if nx < 0 or ny < 0 or nx >= m or ny >= n:
#                     continue
#                 if ground[nx][ny] == 0:
#                     continue
#
#                 if ground[nx][ny] == 1:
#                     q.append([nx,ny])
#                     ground[nx][ny] = 0
#
#     c = 0
#     for i in range(m):
#         for j in range(n):
#             if ground[i][j] == 1:
#                 bfs(i,j)
#                 c += 1
#     print(c)

# a,p = map(int,input().split())
# li = [a]
# while True:
#     num = 0
#     for i in range(len(str(li[-1]))):
#         num += int(str(li[-1])[i]) ** p
#     if num in li:
#         idx = li.index(num)
#         print(len(li[:idx]))
#         break
#     else:
#         li.append(num)
#
# n = int(input())
# call = list(map(int,input().split()))
# def y(c):
#     s = 0
#     for i in c:
#         s += 10 * (i // 30 + 1)
#     return s
#
# def m(c):
#     s = 0
#     for i in c:
#         s += 15 * (i // 60 + 1)
#     return s
#
# if y(call) > m(call):
#     print('M',m(call))
# elif y(call) < m(call):
#     print('Y', y(call))
# else:
#     print('Y M',y(call))

# n = int(input())
# home = []
# for i in range(n):
#     home.append(list(map(int,input().split())))
#
# for i in range(1,n):                                                # 2번째 집부터 이전의 R,G,B 중 현재 색과 다른 두개 중 작은 비용과 현재 비용을 더한값을 현재 값으로 설정
#     home[i][0] = min(home[i-1][1],home[i-1][2])+home[i][0]          # 현재 색상 R
#     home[i][1] = min(home[i - 1][0], home[i - 1][2]) + home[i][1]   # 현재 색상 G
#     home[i][2] = min(home[i - 1][1], home[i - 1][0]) + home[i][2]   # 현재 색상 B
#
# print(min(home[n-1]))

# m,n = map(int,input().split())
# tmt =[]
# for i in range(n):
#     tmt.append(list(map(int,input().split())))
#
# queue = deque()
# for i in range(n):
#     for j in range(m):
#         if tmt[i][j] == 1:
#             queue.append([i,j]) # 맨 처음 익은 상태의 토마토만 데크에 추가
#
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]
#
# while queue:              # bfs
#     x,y = queue.popleft() # 익은 토마토의 위치
#     for i in range(4):    # 반복문 4번으로 상 하 좌 우 탐색
#         nx = dx[i]+x      # 이동한 위치의 x좌표 = nx
#         ny = dy[i]+y      # 이동한 위치의 y좌표 = ny
#         if nx < 0 or ny < 0 or nx >n-1 or ny > m-1: # 이동한 x,y가 상자 크기의 범위를 벗어날 경우 continue
#             continue
#
#         if tmt[nx][ny] == 0:            # 이동한 위치의 토마토가 익지 않은 0이라면
#             tmt[nx][ny] = tmt[x][y] + 1 # 현재 익은 토마토의 값에 +1 , 이렇게 하는 이유는 토마토가 익는 날짜를 알기 위해 +1을 해준다
#             queue.append([nx,ny])       # 이동한 좌표값 데크에 추가
#
# ans = 0
# for i in range(n):
#     for j in range(m):
#         if tmt[i][j] == 0:     # 위의 과정을 다 돌았는데도 0이 있는 경우 = 토마토가 모두 익지 못하는 상황
#             print(-1)          # -1 출력 후 종료
#             sys.exit(0)
#     ans = max(ans,max(tmt[i])) # n 개의 리스트를 반복하며 최대값 갱신
#
# print(ans-1)                   # 가장 최대값에 -1을 해줘야 경과된 날짜가 된다.

#n = input()
# s = ['a','e','i','o','u']
# def check(str):
#     ja = 0
#     mo = 0
#     mocheck = 0
#     c = deque()
#     compare = '-'
#     for i in str:
#         if i == compare and i != 'e' and i != 'o' :
#             return 0
#         else:
#             compare = i
#         if mocheck:
#             if i in s:
#                 mo +=1
#                 ja = 0
#             else:
#                 mo = 0
#                 ja += 1
#             if mo == 3 or ja == 3:
#                 return 0
#         else:
#             if i in s:
#                 mocheck = 1
#                 mo += 1
#                 ja = 0
#             else:
#                 mo = 0
#                 ja += 1
#             if mo == 3 or ja == 3:
#                 return 0
#
#     if mocheck:
#         return 1
#     else:
#         return 0
# while True:
#     n = input()
#     if n == 'end':
#         break
#     if check(n):
#         print("<"+n+"> is acceptable.")
#     else:
#         print("<"+n+"> is not acceptable.")

# s = input()
# ans = []
# for i in range(1,len(s)+1):
#     for j in range(len(s)-i+1):
#         ans.append(s[j:j+i])
# print(len(set(ans)))

# s = input()
# a = s[0]
# one = 0
# two = 0
# if a == '1':
#     one += 1
# else:
#     two += 1
#
# for i in s:
#     if i == '1':
#         if i != a:
#             one += 1
#             a = i
#     else:
#         if i != a:
#             two +=1
#             a = i
# print(min(one,two))

# s = int(input())
# for i in range(s):
#     n = int(sys.stdin.readline())
#     li = []
#     c = 0
#     for i in range(n):
#         li.append(list(map(int,sys.stdin.readline().split())))
#     li = sorted(li,key = lambda x: x[0])
#     now = 0
#     for i in li:
#         if i[0]==1 or i[1]==1:
#             c+=1
#             now = i[1]
#             continue
#         if i[1] < now:
#             c+=1
#             now = i[1]
#     print(c)
# import copy
# w, l = map(int,input().split())
# island = []
# for i in range(w):
#     island.append(list(input()))
#
# def bfs(a,b,land):
#     land[a][b] = 0
#     q = deque()
#     dx = [1,-1,0,0]
#     dy = [0,0,1,-1]
#     q.append([a,b])
#     c = 0
#     while q:
#         x,y = q.popleft()
#
#         for i in range(4):
#             nx = dx[i] + x
#             ny = dy[i] + y
#             if nx < 0 or ny < 0 or nx >= w or ny >= l:
#                 continue
#             if land[nx][ny] == 'L':
#                 land[nx][ny] = land[x][y] + 1
#                 q.append([nx,ny])
#                 c  = max(c,land[nx][ny])
#     return c
# ans = []
#
# for i in range(w):
#     for j in range(l):
#         if island[i][j] == 'L':
#             b = copy.deepcopy(island)
#             ans.append(bfs(i,j,b))
#
# print(max(ans))
# from collections import defaultdict
# dic = defaultdict(int)
# n = int(input())
# for i in range(n):
#     num = int(input())
#     dic[num] += 1
# ma = max(dic.values())
# ans = []
# for a,b in dic.items():
#     if b == ma:
#         ans.append(a)
# print(min(ans))

# from collections import deque
# import copy
#
#
# def solution(places):
#     answer = []
#
#     dx = [1, -1, 0, 0]
#     dy = [0, 0, 1, -1]
#
#     def bfs(place):
#         b = deque()
#         a = True
#         place2 = []
#         for i in place:
#             place2.append(list(i))
#         for j in range(5):
#             for s in range(5):
#                 if place2[j][s] == 'P':
#
#                     b.append([j, s])
#
#         if len(b) == 0:
#             return 1
#         for i in b:
#
#             stack = deque()
#             stack.append(i)
#             place3 = copy.deepcopy(place2)
#             place3[i[0]][i[1]] = 0
#             while stack:
#                 x, y = stack.popleft()
#                 for i in range(4):
#                     nx = dx[i] + x
#                     ny = dy[i] + y
#
#                     if nx < 0 or ny < 0 or nx >= 5 or ny >= 5:
#                         continue
#                     if place3[nx][ny] == 'X':
#                         continue
#                     if place3[nx][ny] == 'O':
#                         place3[nx][ny] = place3[x][y] + 1
#                         stack.append([nx,ny])
#                     elif place3[nx][ny] == 'P':
#                         if place3[x][y]+1 <= 2:
#                             return 0
#                         stack.append([nx,ny])
#                         place3[nx][ny] = 0
#
#
#         return 1
#
#     for i in places:
#         answer.append(bfs(i))
#
#     return answer
#
# print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))

# n = int(input())
# li = sorted(list(map(int,input().split())))
# m = int(input())
# li2 = list(map(int,input().split()))
# ans = []
#
# def binary(i, start, end):
#     mid = (start+end) // 2
#     if start > end:
#         ans.append(0)
#     elif i == li[mid]:
#         ans.append(1)
#     elif i > li[mid]:
#         binary(i,mid+1,end)
#     else:
#         binary(i,start,mid-1)
#
# for i in li2:
#     binary(i,0,len(li)-1)
# print(*ans)

# import math
#
# n,m = map(int,input().split(':'))
# gcd1 = math.gcd(n,m)
# print(str(int(n/gcd1))+':'+str(int(m/gcd1)))

# n = int(input())
# ball = list(map(int,input().split()))
# ball_count = 0
# base = [0,0,0]
#
# point = []
#
# def points():
#     if base[-1] == 0:
#         base[-1] = 1
#     elif base[-1] == 1:
#         if base[1] == 0:
#             base[1] = 1
#         elif base[1] == 1:
#             if base[0] == 0:
#                 base[0] = 1
#             else:
#                 base[0] = 1
#                 point.append(1)
# for i in ball:
#     if i == 1:
#         ball_count += 1
#         if ball_count == 4:
#             points()
#             ball_count = 0
#     elif i == 2:
#         ball_count = 0
#         points()
#
#     elif i == 3:
#         ball_count += 1
#         base.append(0)
#         point.append(base[0])
#         base = base[1:]
#         if ball_count == 4:
#             points()
#             ball_count = 0
# try:
#     print(sum(point))
# except:
#     print(0)


# n,m = map(int,input().split())
# train = [deque([0])*20 for _ in range(n)]
# ans = []
# for i in range(m):
#     command = list(map(int,input().split()))
#     if command[0] == 1:
#         if train[command[1]-1][command[2]-1] == 0:
#             train[command[1]-1][command[2]-1] = 1
#     elif command[0] == 2:
#         if train[command[1]-1][command[2]-1] == 1:
#             train[command[1]-1][command[2]-1] = 0
#     elif command[0] == 3:
#         train[command[1]-1].appendleft(0)
#         train[command[1] - 1].pop()
#     elif command[0] == 4:
#         train[command[1] - 1].append(0)
#         train[command[1] - 1].popleft()
#
#
# for i in train:
#     flag = False
#     if ans:
#         for j in ans:
#             if j == i:
#                 flag = True
#                 break
#         if flag == False:
#             ans.append(i)
#
#     else:
#         ans.append(i)
#
# print(len(ans))
# from collections import defaultdict, deque
#
# n = int(input())        # 사진틀의 개수
# m = int(input())        # 전체 학생의 총 추천 횟수
# photo = deque()         # 사진틀담을 데크
# dic = defaultdict(int)  # 학생의 추천 횟수 담을 딕셔너리
# re = list(map(int,input().split())) # 추천받은 학생을 나타내는 번호
#
# for i in re:
#     if len(photo) == n:                 # 사진틀의 개수가 꽉찼을때
#         if i in photo:                  # 사진틀에 추천받은 학생이 이미 존재할 경우
#             dic[i] += 1                 # 추천 횟수 +1
#             continue                    # 다음 학생 번호로 넘어감
#
#         re_min = min(list(dic.values())) # 추천 받은 학생중 최소의 추천 개수
#         for j in range(n):               # 모든 사진틀에 대해
#             if dic[photo[j]] == re_min:  # 해당 학생의 추천 수가 최소의 추천 개수와 같을 경우
#                 del dic[photo[j]]        # 해당 학생 추천개수 담는 딕셔너리에서 제거
#                 del photo[j]             # 해당 학생 사진틀에서 제거
#                 break                    # 반복문 종료
#
#         photo.append(i)                  # 현재 학생 추가
#         dic[i] += 1                      # 현재 학생 추천수 +1
#
#     else:                     # 사진틀이 비어있는 경우가 있을때
#         if i in photo:        # 학생이 이미 사진틀에 있는 경우
#             dic[i] += 1       # 추천수만 +1
#         else:
#             photo.append(i)   # 학생이 사진틀에 없을 경우 사진틀에 추가 후 추천수 +1
#             dic[i] += 1
#
# print(*sorted(photo))

from collections import defaultdict

# from collections import defaultdict
#
#
# def solution(fees, records):
#     incar = defaultdict(int)
#     timedict = defaultdict(int)
#     answer = []
#     fulltime = 23 * 60 + 59
#     for i in records:
#
#         number = i.split(' ')[1]
#
#         time = i.split(' ')[0].split(':')
#         minute = int(time[0]) * 60 + int(time[1])
#         if i.split(' ')[-1] == 'IN':
#             incar[number] = minute
#         else:
#
#             timedict[number] += (minute - incar[number])
#             incar[number] = -1
#     for i in incar:
#         if incar[i] != -1:
#             timedict[i] += fulltime - incar[i]
#             incar[i] = -1
#
#     for i in sorted(timedict):
#         if timedict[i] <= fees[0]:
#             answer.append(fees[1])
#         else:
#             if (timedict[i] - fees[0]) % fees[2] == 0:
#                 fee = fees[1] + int((timedict[i] - fees[0]) / fees[2]) * fees[3]
#             else:
#                 fee = fees[1] + (int((timedict[i] - fees[0]) / fees[2]) + 1) * fees[3]
#             answer.append(fee)
#     return print(answer)
#
# solution([120, 0, 60, 591],["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"])
# solution([1, 461, 1, 10],["00:00 1234 IN"])

# a = "a a a a a a a a a a "
# print(a.split(' '))
# def solution(s):
#     answer = ''
#
#     s = s.lower()
#     s = s.split(' ')
#
#     for i in s:
#         try:
#             if i[0].isdigit():
#                 answer += i + ' '
#             else:
#                 answer += i[0].upper() + i[1:] + ' '
#         except:
#             answer += ' '
#
#     return answer[:-1]
#
# print(solution("a a a a a a a a a a "))
# dic = {'a':[123]}
# print(dic['a'][0])
# def solution(tickets):
#     answer = []
#     dic = dict()
#     for (start,end) in tickets:
#         if start in dic:
#             dic[start].append(end)
#         else:
#             dic[start] = [end]
#     for i in dic.keys():
#         dic[i].sort(reverse=True)
#
#     stack =['ICN']
#
#     while stack:
#         now = stack[-1]
#         if (now not in dic) or (not dic[now]):
#             answer.append(stack.pop())
#         else:
#             stack.append(dic[now].pop())
#
#
#     return answer
#
# solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])

# import heapq
# def solution(n, works):
#     answer = 0
#     new = []
#     if sum(works) < n:
#         return 0
#     for i in works:
#         new.append(-i)
#     heapq.heapify(new)
#     for i in range(n):
#         num = heapq.heappop(new)
#         num += 1
#         heapq.heappush(new,num)
#
#     for i in new:
#         answer += i**2
#
#     return answer
#
# print(solution(99, [2, 15, 22, 55, 55]))

# n = input()
# count = 0
# def test(n):
#     global count
#     if len(n) == 1:
#         print(count)
#         if n % 3 == 0:
#             print('YES')
#         else:
#             print('NO')
#     else:
#         s = 0
#         for i in n:
#             s += int(i)
#         count += 1
#         test(str(s))
#
# test(n)

# def solution(N, stages):
#     answer = []
#     ans = []
#     stages = sorted(stages)
#     for i in range(1,N+1):
#         a = len(stages)
#         count = 0
#         if a == 0:
#             answer.append([i,0])
#         else:
#             for j in stages:
#                 if i >= j:
#                     count += 1
#                 elif i < j:
#                     break
#             for s in range(count):
#                 stages.pop(0)
#             answer.append([i,count/a])
#     answer.sort(key=lambda x: x[1],reverse=True)
#     for i in answer:
#         ans.append(i[0])
#     print(answer)
#     return ans
#
#
# print(solution(5,[1,2,2,1,3]))
# from collections import defaultdict
# n = int(input())
# li = []
# dict = defaultdict(int)
# for i in range(n):
#     li.append(input())
#
# for i in li:
#     leng = len(i)           # 현재 단어의 길이
#     for j in range(leng):
#         dict[i[j]] += 10 ** (leng-j-1)  # 현재 단어의 문자의 자리에 맞게 사전에 갱신
# ans = 0
# num = 9
# for i in sorted(dict.values(),reverse=True):    # 사전의 value를 기준으로 내림차순으로 정렬
#     ans += num*i    # 가장 큰 값부터 9부터 -1 씩하며 곱해줌
#     num -= 1
# print(ans)

# n = input()
# m = input()
# compare = ''
# ans = 0
# for i in n:
#
#     if len(compare) == len(m):
#         if m == compare:
#             ans += 1
#             compare = ''
#             compare += i
#         else:
#             compare = compare[1:]+i
#
#     else:
#         compare += i
# if compare == m:
#     ans += 1
#
# print(ans)
# from itertools import permutations, combinations
# n = int(input())
# a = [i for i in range(1,n+1)]   # 1번 부터 n 번까지 선수담는 리스트
# x = int(n/2)                    # 팀당 인원수 n/2
# b = list(combinations(a,x))     # 선수들을 x인원으로 조합한 모든 경우
# s = []                          # 각 선수들간의 능력치가 담길 이중리스트
# for i in range(n):
#     s.append(list(map(int,input().split())))    # 능력치 추가
#
# answer = 100000
# for i in range(len(b)//2):                 # 조합의 개수의 반까지만 반복
#     team1 = b[i]                           # 팀이 가능한 조합
#     team2 = b[-i-1]                        # 위의 조합에서 나머지 팀들의 조합
#     sum1 = 0                               # team1 의 능력의 합을 담을 변수
#     sum2 = 0                               # team2 의 능력의 합을 담을 변수
#     for j in list(permutations(team1,2)):  # team1에서 2명씩 짝지은 모든 순열
#         sum1 += s[j[0]-1][j[1]-1]          # 모든 순열에 대한 능력치의 합
#     for j in list(permutations(team2,2)):  # 위와 동일한 방식으로 team2 의 능력치의 합을 구함
#         sum2 += s[j[0]-1][j[1]-1]
#
#     answer = min(answer,abs(sum1-sum2))    # team1 과 team2 의 능력치의 차이의 최소값을 반복을 통해 계속 갱신
# print(answer)

# import copy
# n = int(input())
# land2 = []
# max_num = 0
# answer_list =[]
# for i in range(n):
#     a = list(map(int,input().split()))
#     max_num = max(max_num,max(a))
#     land2.append(a)
# dx = [1,-1,0,0]
# dy = [0,0,1,-1]
# def bfs(l,i,j):
#     q = deque()
#     q.append([i,j])
#     l[i][j] = 0
#     while q:
#         x,y = q.popleft()
#         for i in range(4):
#             nx = x+dx[i]
#             ny = y+dy[i]
#
#             if nx < 0 or ny < 0 or nx > n-1 or ny > n-1:
#                 continue
#             if l[nx][ny] == 0:
#                 continue
#             else:
#                 l[nx][ny] = 0
#                 q.append([nx,ny])
# for i in range(1,max_num):
#     answer = 0
#     land = copy.deepcopy(land2)
#     for j in range(n):
#         for k in range(n):
#             if land[j][k] <= i:
#                 land[j][k] = 0
#     for i in range(n):
#         for j in range(n):
#             if land[i][j] != 0:
#                 bfs(land,i,j)
#                 answer += 1
#     answer_list.append(answer)
# if len(answer_list) == 0:
#     print(1)
# else:
#     print(max(answer_list))

# n = int(input())
# from itertools import combinations
# s = list(map(int,input().split()))
# a = []
# for i in range(1,n+1):
#     for j in list(combinations(s,i)):
#         a.append(sum(j))
# com = 0
# ans = []
# for i in sorted(list(set(a))):
#     if com+1 != i:
#         ans.append(com+1)
#         break
#     com += 1
# if len(ans) == 0:
#     print(sum(s)+1)
# else:
#     print(ans[0])
# dx = [1,-1,0,0,1,1,-1,-1]
# dy = [0,0,1,-1,1,-1,1,-1]
# while True:
#     w,h = map(int,input().split())
#     if w == 0 and h == 0:
#         break
#     maps = []
#     for i in range(h):
#         maps.append(list(map(int,input().split())))
#     visit = [[0]*w for _ in range(h)]
#
#
#     answer = 0
#     def bfs(i,j):
#         q = deque()
#         q.append([i,j])
#         while q:
#             x,y = q.popleft()
#             for i in range(8):
#                 nx = dx[i] + x
#                 ny = dy[i] + y
#
#                 if nx < 0 or ny < 0 or nx > h-1 or ny > w-1 or visit[nx][ny] == 1:
#                     continue
#                 if maps[nx][ny] == 0:
#                     continue
#                 else:
#                     visit[nx][ny] = 1
#                     q.append([nx,ny])
#
#     for i in range(h):
#         for j in range(w):
#             if maps[i][j] == 1 and visit[i][j] == 0:
#                 visit[i][j] = 1
#                 bfs(i,j)
#                 answer += 1
#     print(answer)

# s = list(input())
# t = list(input())
#
# while True:
#     if len(s) == len(t):
#         break
#     if t[-1] == 'A':
#         t.pop()
#     else:
#         t.pop()
#         t = t[::-1]
#
# if s == t:
#     print(1)
# else:
#     print(0)


n = int(input())
n_li = sorted(list(map(int,input().split())),reverse=True)
m = int(input())
m_li = sorted(list(map(int,input().split())),reverse=True)

ans = 0
if m_li[0] > n_li[0]:
    print(-1)

else:
    while m_li:
        for i in n_li:
            for j in m_li:
                if i >= j:
                    m_li.remove(j)
                    break


        ans += 1
    print(ans)
