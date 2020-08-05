def duplicatekdist(arr,k):
    mp={}
    for i in range(len(arr)):
        if(arr[i] not in mp):
            mp[arr[i]]=i 
        else:
            if(i-mp[arr[i]]==k or mp[arr[i]]+k<len(arr) and arr[mp[arr[i]]+k]==arr[i]):
                return True 
            else:
                mp[arr[i]]=i  
    return False 
def duplicateel(arr):
    mp={}
    flag=0
    for i in arr:
        if(i in mp):
            flag=1
            print(i,end=" ")
        else:
            mp[i]=i
    if(not flag):
        print(-1)
def duplicatemax(arr):
    mp={} 
    maximum=0 
    ans=0
    for i in arr:
        if(i not in mp):
            mp[i]=1 
        else:
            mp[i]+=1 
            if(maximum<mp[i]):
                maximum=mp[i]
                ans=i 
    return ans 
def maximfreqsub(arr):
    mp={}
    maximum=0 
    ans=0 
    k=0
    for i in range(len(arr)):
        if(arr[i] not in mp):
            mp[arr[i]]=1 
        else:
            mp[arr[i]]+=1 
            if(maximum<mp[arr[i]]):
                maximum=mp[arr[i]]
                ans=arr[i]  
                k=i
    for j in range(len(arr)):
        if(arr[j]==ans):
            break
    print(arr[j:k+1]) 
def elementoccurktimes(arr,k):
    mp={}
    for i in range(len(arr)):
        if(arr[i] not in mp):
            mp[arr[i]]=1 
        else:
            mp[arr[i]]+=1 
    for j in arr:
        if(mp[j]==k):
            return j 
    return -1
def symmetric(arr):
    mp={}
    for i in arr:
        if(i[1] in mp and mp[i[1]]==i[0]): 
            
            print(i[0],i[1])
        else:
            mp[i[0]]=i[1] 
def si(arr):
    res=0
    for i in range(len(arr)):
        res=res^arr[i]^i 
    print(res)
        
    return sum(arr)-((len(arr)-1)*(len(arr))//2)
    
print(duplicatekdist([1,2,3,4,3,3,3,4],3)) 
duplicateel([2,10,100,11]) 
print(duplicatemax([1,3,2,1,4,1,4,4])) 
maximfreqsub([1,2,2,2,1]) 
print(elementoccurktimes([1,2,2,3,4,3],3))
symmetric([[10,30],[30,10],[5,10],[10,5],[3,90]]) 
print(si([2,3,3,1,4]))