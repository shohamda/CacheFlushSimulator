with open('Attack_domains.txt', 'w') as f:
    DOMAINS_NUM = 100000
    for i in range(DOMAINS_NUM):
        print(f'attack{i}.home.lan. A', file=f)
