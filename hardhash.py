def largestsubarr1(arr):
    for i in range(len(arr)):
        if(arr[i]==0):
            arr[i]=-1 
    commulative=0
    maximumlength=0
    endingindex=0
    mp={}
    for j in range(len(arr)):
        commulative+=arr[j]
        if(commulative==0):
            endingindex=j 
            maximumlength=j+1 
        if(commulative in mp):
            if(maximumlength<j-mp[commulative]):
                endingindex=j 
                maximumlength=j-mp[commulative] 
        else:
            mp[commulative]=j 
    for j in range(len(arr)):
        if(arr[j]==-1):
            arr[j]=0 
    print(endingindex-maximumlength+1 , endingindex) 
def largernumsubarr2(arr):
    for i in range(len(arr)):
        if(arr[i]==0):
            arr[i]=-1 
    mp={}
    cummulative=0 
    count=0
    for j in range(len(arr)):
        cummulative+=arr[j]
        if(cummulative==0):
            count+=1 
        if(cummulative in mp):
            count+=mp[cummulative] 
        mp[cummulative]=mp.get(cummulative,0)+1 
    print(count) 
def longestsub(arr):
    for i in range(len(arr)):
        if(arr[i]==0):
            arr[i]=-1 
    commulative=0
    maximumlength=0
    mp={}
    for j in range(len(arr)):
        commulative+=arr[j]
        if(commulative>=1):
            maximumlength=i+1 
        if(commulative-1 in mp):
            if(maximumlength<j-mp[commulative-1]):
                maximumlength=j-mp[commulative-1]
        else:
            mp[commulative]=j
    print(maximumlength)   
def t2slongest(arr):
    sums=0
    mp={}
    count=0 
    for i in range(len(arr)):
        if(int(arr[i])==0):
            sums-=3 
        else:
            sums+=int(arr[i])
        if(sums==0):
            count+=1 
        if(sums in mp):
            count+=mp[sums]
        if(sums not in mp):
            mp[sums]=1  
        else:
            mp[sums]+=1
        
    print(count)
                
largestsubarr1([0,0,1,1,0]) 
largernumsubarr2([1, 0, 0, 1, 0, 1, 1])
longestsub([1,1,1]) 
#t2slongest("102100211")
