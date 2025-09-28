max_num = 20000
is_prime = [True] * (max_num + 1)
is_prime[0] = is_prime[1] = False 
for i in range(2, int(max_num**0.5) + 1):
    if is_prime[i]:
        is_prime[i*i : max_num+1 : i] = [False] * len(is_prime[i*i : max_num+1 : i])

count = 0
for num in range(1, max_num + 1):
    if is_prime[num]:
        print(num, end=" ")
        count += 1
        if count % 5 == 0:
            print()