with open('CNAMECacheFlush_mitigation.txt', 'w') as f:
    DOMAINS_NUM = 100000
    for i in range(DOMAINS_NUM):
        if i % 8 != 0:
            print(f'attack{i} 86400 IN    CNAME attack{i + 1}',file=f)
        else:
            print(f'attack{i} 86400 IN    A 1.1.1.1',file=f)
