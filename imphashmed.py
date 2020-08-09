def printarray(arr):
    mp={}
    maxim=-29294984928494849 
    for i in arr:
        mp[i]=1 
        maxim=max(maxim,i) 
    res=[]
    for i in arr:
        k=3
        j=i*2
        while(j<=maxim):
            if(j in mp and j not in res):
                res.append(j)
            j=i*k
            k+=1
    print(res)  
def threeelement(arr1,arr2,arr3,sums):
    mp={}
    for i in arr1:
        mp[i]=1
    for i in arr2:
        for j in arr3:
            
            if(sums-(i+j)  in mp):
                return "yes"
    return "No" 
def findfourelement(arr1):
    mp={}
    flag=0
    for i in range(len(arr1)): 
        for j in range(i+1,len(arr1)):
            if((arr1[i]+arr1[j]) not in mp):
                mp[arr1[i]+arr1[j]]=(arr1[i],arr1[j])
            else:
                if(arr1[i] not in mp[arr1[i]+arr1[j]] and arr1[j] not in mp[arr1[i]+arr1[j]]):
                    print(mp[arr1[i]+arr1[j]],(arr1[i],arr1[j])) 
                    flag=1
                    break
        if(flag==1):
            break
def largestsubarr(arr1):
    mp={}
    sums,maxi=0,0
    for i in range(len(arr1)):
        sums+=arr1[i] 
        if(sums==0):
            maxi=i+1 
        elif(sums in mp):
            if(i-mp[sums]>maxi):
                maxi=i-mp[sums]  
        else:
            mp[sums]=i
    print(maxi) 
def longestsubsequence(arr1):
    mp=[1 for i in range(len(arr1))] 
    maximum=0
    s=0
    e=0
    for j in range(1,len(arr1)):
        for k in range(j): 
            if(arr1[j]-arr1[k]==1 and mp[j]<=mp[k]):
                mp[j]=1+mp[k]  
                if(mp[j]>maximum):
                    maximum=mp[j]
    print(maximum) 
    res=[]
    for k in range(len(arr1)-1,-1,-1):
        if(mp[k]==maximum):
            res.append(arr1[k])
            maximum-=1
        
    for f in range(len(res)-1,-1,-1):
        print(res[f],end=" ")  
def binarysearch(arr,k):
    low=0 
    high=len(arr)-1
    while(low<high):
        mid=(low+high)//2 
        if((arr[mid]<k or arr[mid]==k) and arr[mid+1]>k):
            return mid 
        elif(arr[mid]<k):
            low=mid+1 
        else:
            high=mid-1
def longestsubsequencenlogn(arr):
    lis=[]
    for i in range(len(arr)):
        k=binarysearch(lis,arr[i])
        if(k==None):
            lis.append(arr[i]) 
        
        elif(lis[k]!=arr[i]):
            lis[k]=arr[i] 
            
            
            
            
            
    
printarray([ 2, 3, 8, 6, 9, 10]) 
print(threeelement([1 , 2 , 3 , 4 , 5 ],[ 2 , 3 , 6 , 1 , 2],[3 , 2 , 4 , 5 , 6],13)) 
findfourelement([3, 4, 7, 1, 2, 9, 8])
largestsubarr([1,0,3])  
longestsubsequence([3, 10, 3, 11, 4, 5, 6, 7, 8, 12]) 
longestsubsequencenlogn([3, 10, 3, 11, 4, 5, 6, 7, 8, 12])
