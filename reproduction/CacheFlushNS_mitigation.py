with open('NSCacheFlush_mitigation.txt', 'w') as f:
    DOMAINS_NUM = 100
    for i in range(DOMAINS_NUM):
        for j in range(1,20):
            print(f'attack{i}	3600	IN	NS	auth{j}.fun.lan.', file=f)
