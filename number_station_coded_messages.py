def solution(l, t):
    # Your code here
    idx = 0
    sum = 0
    for key,value in enumerate(l):
        sum=sum+value
        while(sum>t and idx<key):
            sum=sum-l[idx]
            idx+=1
        if(sum==t):
            return [idx,key]
    return [-1,-1]

if __name__ == "__main__":
    print(solution([4, 3, 10, 2, 8], 12))
