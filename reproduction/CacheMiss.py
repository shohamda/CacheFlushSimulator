import pandas as pd

def parse_tshark_file(file_path):
    columns = ['frame.number', 'frame.time', 'ip.src', 'ip.dst', 'tcp.srcport', 'tcp.dstport', 'udp.srcport', 'udp.dstport', 'dns.id', 'dns.qry.name', 'dns.flags.rcode']
    df = pd.read_csv(file_path, delimiter='\t', header=None, names=columns)
    return df

def find_cache_miss(benign_client_file, authoritative_file):
    benign_df = parse_tshark_file(benign_client_file)
    auth_df = parse_tshark_file(authoritative_file)
    
    cache_misses = {}
    
    for domain in benign_df['dns.qry.name'].unique():
        benign_queries = benign_df[benign_df['dns.qry.name'] == domain]
        auth_queries = auth_df[auth_df['dns.qry.name'] == domain]
        
        if auth_queries.empty:
            cache_misses[domain] = 1
            continue
        
        cache_miss_count = 0
        for _, row in benign_queries.iterrows():
            if row['ip.dst'] in auth_queries['ip.src'].values:
                continue
            else:
                cache_miss_count += 1
        
        cache_misses[domain] = cache_miss_count
    
    return cache_misses

def write_cache_miss_csv(cache_misses, output_file):
    df = pd.DataFrame(cache_misses.items(), columns=['Domain', 'Cache Misses'])
    df.to_csv(output_file, index=False)
    
    avg_cache_miss = df['Cache Misses'].mean()
    with open(output_file, 'a') as f:
        f.write(f'\nAverage Cache Miss,{avg_cache_miss}')

benign_client_file = '/env/reproduction/tshark_benign_client.txt'
authoritative_file = '/env/reproduction/tshark_auth.txt'
output_file = '/env/reproduction/cache_misses.csv'

cache_misses = find_cache_miss(benign_client_file, authoritative_file)
write_cache_miss_csv(cache_misses, output_file)
print("Cache Misses CSV file generated successfully.")

