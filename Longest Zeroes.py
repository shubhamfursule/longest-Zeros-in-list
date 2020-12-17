def count_zero(zlist):
    count=[]
    if 0 in zlist:
        for i in range(len(zlist)):
            if zlist[i]==0:
                zero = 0
                while zlist[i]!=1:
                    zero+=1
                    i+=1
                    if i>=len(zlist):
                        i-=1
                        break
                count.append(zero)
        return max(count)
    else:
        return 0
Lones=[1,1,1,1,1,1,1]
Lzero_list= [randint(0,1) for i in range(10)]
print(f"Given List is : {Lzero_list}")
print(f"max count of Zeros are : {count_zero(Lzero_list)}")