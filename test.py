p = 0
m = 1000
n = 0
ans = 0
while True:
    n += 1
    try:
        p = 1/(m-n)
    except:
        break

    pre_ans = 1
    for i in range(n):
        pre_ans *= (m-i)/m

    ans += n * pre_ans * p
    print(str(ans) + ' ' * 20, end='\r')
