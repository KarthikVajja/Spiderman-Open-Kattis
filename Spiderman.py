import math
def spiderman(n,arr,st,mini, s, maxi, state):
    if n in state:
        if state[n]<=s:
            return('IMPOSSIBLE',math.inf)
    if maxi<mini:
        return ('IMPOSSIBLE',math.inf,maxi, state)
    if n==len(arr):
        if s==0:
            return (st, mini, min(maxi,mini), state)
        else:
            return ('IMPOSSIBLE',math.inf, maxi, state)
    minus = (st, math.inf, maxi, state)
    if s-arr[n]>=0:
        minus = spiderman(n+1, arr, st+'D', max(mini,s-arr[n]), s-arr[n], maxi, state)
        maxi = min(maxi,minus[2])
    plus = spiderman(n+1, arr, st+'U', max(mini,s+arr[n]), s+arr[n], maxi, state)
    if plus[1]<minus[1]:
        return plus
    return minus

def helper(arr):
    state = dict()
    state[0]=arr[0]
    res = spiderman(1,arr,'U',arr[0], arr[0],math.inf,state)
    if res[0]=='U':
        return('IMPOSSIBLE')
    return(res[0])

ans = []
for i in range(int(input())):
    n = int(input())
    arr = tuple(map(int, input().split()))
    ans.append(helper(arr))
print('\n'.join(ans))
