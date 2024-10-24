list1=[]
n=int(input)
for i in range(n):
    ele=int(input())
    list1.append(ele)
n=len(list1)
if(n%2)==0:
    for i in range(0,int(n/2)-1):
        for j in range(0,int(n/2)-i-1):
            if(list1[j]>list1[j+1]):
                list1[j],list1[j+1]=list1[j+1],list1[j]
        for i in range(int(n/2),n-1):
            max=i
            for j in range(i+1,n):
                if(list1[max]<list1[j]):
        if max!=i:
                list1[max],list1[i]=list1[i],list1[max]
print(list1)
                

    
    
    
