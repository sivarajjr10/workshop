def right(list1,n):
    temp=list1[0]
    for i in range(n-1):
        list1[i]=list1[i+1]
    list[n-1]=temp
def rot(list,k,n):
    for i in range(k):
        right(list1,n)
n=int(input())
list1=[]
for i in range(n):
    ele=int(input())
    list1.append(ele)
k=int(input())
rot(list1,k,n)
print[list1]
