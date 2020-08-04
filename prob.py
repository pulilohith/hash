class Node:
    def __init__(self,data):
        self.data=data
        self.next=None 
class LL:
    def __init__(self):
        self.head=self.tail=None 
    def add(self,data):
        N1=Node(data)
        if(self.head==None):
            self.head=N1 
            self.tail=N1
        else:
            self.tail.next=N1
            self.tail=N1 
    def display(self):
        temp=self.head
        while(temp!=None):
            print(temp.data,end=" ")
            temp=temp.next  
def union(L1,L2):
    mp=[]
    l3=LL()
    l4=LL()
    while(L1!=None):
        if(L1.data in mp):
            mp[L1.data]+=1 
        else:
            l4.add(L1.data)
            mp.append(L1.data)
        L1=L1.next 
    while(L2!=None):
        if(L2.data in mp):
            l3.add(L2.data)
        else:
            l4.add(L2.data)
        L2=L2.next
    print()
    print("intersection:",end=" ")
    l3.display()
    print()
    print("union:",end=" ")
    l4.display() 
def findpair(arr,sums): 
    mp=[]
    for i in arr:
        if(sums-i in mp):
            print(i,sums-i)
            break 
        mp.append(i) 
def minimumdeletionoper(arr):
    mp=[]
    count=0
    for i in arr:
        if(i not in mp):
            count+=1 
        mp.append(i)
    return count-1 
def maximumdistance(arr):
    mp={}
    maxim=0 
    for i in range(0,len(arr)):
        if(arr[i] in mp):
            maxim=max(maxim,i-mp[arr[i]]) 
        else:
            mp[arr[i]]=i 
    return maxim 
def maximumpointsliesonl(points):
    res=0
    for i in points:
        slope=0
        dp={}
        maximum=0
        dup=0
        for j in points:
            if(i!=j):
                if(i[0]==j[0]):
                    slope=float("infinity")
                else:
                    slope=float(j[1]-i[1])/float(j[0]-i[0]) 
                dp[slope]=dp.get(slope,0)+1 
                maximum=max(maximum,dp[slope])
            else:
                dup+=1 
        res=max(res,maximum+dup)
        
    return res
def findsubset(arr1,arr2):
    mp={}
    for i in arr1: 
        if(i in mp):
            mp[i]+=1 
        else:
            mp[i]=1  
    print(mp)
    for j in arr2:
        if(j in mp and mp[j]>=1):
            mp[j]-=1 
        else:
            return "not a subset" 
    return "yes"
print(findsubset([11,8,9,56,8,54],[8,11,9,0,11]))
L1=LL()
L1.add(11)
L1.add(10)
L1.add(8)
L1.add(2)
L2=LL()
L2.add(3)
L2.add(7)
L2.add(6)
L2.add(8) 
L1.display()
print()
L2.display()
union(L1.head,L2.head) 
print()
findpair([0,-1,2,-3,1],-2) 
print("minimum deletion oper:",minimumdeletionoper([4,3,4,4,2,4])) 
print("maximum distance btw 2 occurences:", maximumdistance([3,2,1,2,1,4,5,8,6,7,4,2]))
print("sameline:", maximumpointsliesonl([(-1, 1), (0, 0), (1, 1), (2, 2), (3, 3), (3, 4)] ))
