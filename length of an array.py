n=input()
c1=0
c2=0
c3=0
for i in range(len(n)):
    if(n[i]>='A' and n[i]<='Z') or (n[i]>='a' and n[i]<='z'):
        c1+=1
    elif(n[i]>='0' and n[i]<='9'):
            c2+=1
    else:
            c3+=1
print(c1,c2,c3)
