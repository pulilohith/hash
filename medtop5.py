def itinerary(maps):
    mp={}
    for i in maps:
        mp[maps[i]]=i  
    start=None
    for j in maps:
        
        if(j not in mp):
            start=j 
            break
    if(start!=None):
        j=len(maps)
        while(j):
            print(start+"-->"+maps[start],end=" ")
            j-=1 
            start=maps[start] 
def no_of_employee(maps):
    mp={}
    for j in maps:
        if(maps[j] not in mp):
            mp[maps[j]]=1 
        else:
            mp[maps[j]]+=1 
    for k in maps:
        if(k not in mp):
            print(str(k)+"-"+str(0)) 
        else:
            if(k==maps[k]):
                print(str(k)+'-'+str(len(maps)-1)) 
            else:
                print(str(k)+"-"+str(mp[k]))
def no_of_pair(arr):
    mp={}
    maxim=arr[0]
    for j in arr: 
        mp[j]=1
        if(j>maxim):
            maxim=j  
    ans=0
    for j in arr:
        k=1
        f=j
        while(f<=maxim): 
            f=j*k
            if(j!=f and f in mp):
                ans+=1  
            k+=1
    print(ans)
def arraypairel(arr,k):
    if(len(arr)%2):
        return False
    mp={}
    for i in arr:
        if(i%k not in mp):
            mp[i%k]=1 
        else:
            mp[i%k]+=1 
    for j in arr:
        rem=j%k 
        if(2*rem==k):
            if(mp[rem]%2):
                return False
        elif(rem==0):
            if(mp[rem]%2):
                return False
        else:
            if(mp[k-rem]!=mp[rem]):
                return False
    return True  
def Longest(arr,k):
    sums=0 
    curr=0 
    start=0 
    end=0 
    mp={} 
    mp[0]=0
    for j in range(len(arr)):
        sums+=arr[j] 
        rem=sums%k
        if(rem<0):
            rem+=k
        if(rem not in mp):
            mp[rem]=j 
        else:
            if((j-mp[rem])>curr):
                start=mp[rem] 
                end=j  
                curr=j-mp[rem]
    print(arr[start+1:end+1])      
itinerary({"Chennai":"Banglore","Bombay":"Delhi","Goa":"Chennai","Delhi":"Goa"})
print()
no_of_employee({'A':'C','B':'C','C':'F','D':'E','E':'F','F':'F'}) 
no_of_pair([1,2,3,6,7])
print(arraypairel([92, 75, 65, 48, 45, 35],10)) 
Longest([-2, 2, -5, 12, -11, -1, 7],3)
