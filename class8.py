#--------------------------------------------------------------------
#d691
'''
a=list(map(int,input().split()))
b=list(map(int,input().split()))
A=set(a)
B=set(b)
C=set()
print(A,B)

if A==B:
    print('A equals B')
elif B<=A:
    print('B is a proper subset of A')
elif A<=B:
    print('A is a proper subset of B')
elif A.intersection(B)==C:
    print('A and B are disjoint')
elif A.intersection(B)!=C:
    print("I'm confused!")
'''
#--------------------------------------------------------------------
#e283
'''
N=int(input())
d={
    "0 1 0 1":"A",
   "0 1 1 1":"B",
   "0 0 1 0":"C",
   "1 1 0 1":"D",
   "1 0 0 0":"E",
   "1 1 0 0":"F",
   }
for i in range(N):
    s=input()
    print(d[s],end='')
'''
#--------------------------------------------------------------------
#greedy
'''
money=int(input())
change=100-money
while 0<money<100:
    if change-50>=0:
        change=change-50
        print('50',end='  ')
    elif change-10>=0:
        change=change-10
        print('10',end='  ')
    elif change-5>=0:
        change=change-5
        print('5',end='  ')
    elif change-1>=0:
        change=change-1
        print('1',end='  ')
else:
    print('False')
'''
#--------------------------------------------------------------------
#e788
'''
N=int(input())
students=[]
for i in range(N):
    stuID,stuName=input().split()
    students.append( [ stuID[-1] , stuID[0] , i , stuName ] )
for i in range(N-1):
    for j in range(N-1-i):
        if students[j][0]>students[j+1][0]:
            students[j],students[j+1]=students[j+1],students[j]
        elif students[j][0]==students[j+1][0]:
            if students[j][1]>students[j+1][1]:
                students[j],students[j+1]=students[j+1],students[j]
            elif students[j][1]==students[j+1][1]:
                if students[j][2]>students[j+1][2]:
                    students[j],students[j+1]=students[j+1],students[j]
for college,_,_,name in students:
    print(college+':',name)
'''
#--------------------------------------------------------------------
#a539
'''
N=int(input())
nums=list(map(int,input().split()))
times=0
for i in range(N-1):
    for j in range(N-1-i):
        if nums[j]>nums[j+1]:
            nums[j],nums[j+1]=nums[j+1],nums[j]
            times+=1

print('Minimum exchange operations',':',times)
'''
#--------------------------------------------------------------------
