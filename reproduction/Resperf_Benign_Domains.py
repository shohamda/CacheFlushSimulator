with open('Benign_domains.txt', 'w') as f:
    DOMAINS_NUM = 100000
    for i in range(DOMAINS_NUM):
        print(f'benign{i}.fun.lan. A', file=f)
