# DNS-CacheFlushSimulator

## Overview

**DNS-CacheFlushSimulator** is an Inner-Emulator environment for DNS protocol, developed as part of the CacheFlushAttack research. It includes clients, a resolver, and three authoritative name servers. This environment is designed to analyze and examine the behavior of a DNS resolver in detail.

## Authors

- Yehuda Afek, Tel-Aviv University
- Anat Bremler-Barr, Tel-Aviv University
- Shoham Danino, Reichman University
- Yuval Shavitt, Tel-Aviv University

## Abstract

To understand the CacheFlushAttack and analyze its effective flush rate, a mini-lab setup disconnected from the Internet was developed. This setup includes all DNS system components: clients, resolvers, and authoritative name servers. It allows for detailed analysis of resolver behavior and can be useful for further behavioral analysis of different DNS system components.

## Description & Requirements

DNS-CacheFlushSimulator is built using Docker and includes:

- Clients
- A BIND9 recursive resolver (version 9.18.21)
- Three authoritative name servers:
  - A 'root' server
  - Two malicious delegation authoritative name servers

## Docker Usage

If you are unfamiliar with Docker I suggest to first read about Docker here: [https://docs.docker.com/get-started/](https://docs.docker.com/get-started/)

1. Download the docker from Docker Hub `docker pull shohamd/cacheflushsimulator:latest` or [cacheflushsimulator](https://hub.docker.com/r/shohamd/cacheflushsimulator)

2. Run the docker image as a container interactively so you can control the environment `docker container run --dns 127.0.0.1 -it shohamd/cacheflushsimulator:latest /bin/bash` (It is important to use –dns 127.0.0.1 flag so the environment DNS will be local. **Changing resolv.conf inside a Docker won’t work**)

3. Now you will have a terminal inside the environment.

4. In order to open another terminal for the environment first run `docker container ls`, look for “cacheflushsimulator” docker name and copy the Docker ID. Run `docker exec -it <CONTAINER_ID> bash`
5. To open more terminals into the environment, repeat step 4

**Remember, in order to run `resolver` and `authoritative` you must open more than one terminal for you environment**

## Environment Configuration

The environment includes a resolver and at least three authoritative servers. The IP addresses are as follows:

- **Client:** `127.0.0.1`
- **Resolver:** `127.0.0.1`
- **Root authoritative server:** `127.0.0.2`
- **TLD authoritative servers:**
  - `"fun.lan":` `127.0.0.100`
  - `"home.lan":` `127.0.0.200`
- **Default resolver:** `127.0.0.53` (used for software installation only)

## Authoritative Servers
Our authoritative servers are located at `/env/nsd\_root`, `/env/nsd\_attack\_home` and `/env/nsd\_attack\_fun`.
To use them, first configure their zone files which are located inside their folder and called `ZONE\_NAME.forward`. 
After changing the zone file restart the authoritative in order to apply the changes.

## Resolver
Go to the resolver implementation folder `/env/bind9\_18\_21` and run: `make install`.

### Starting the Environment

Open four terminals in the Docker container:

1. **Turn on the Resolver using the following commands:**
   ```bash
   cd /etc
   named -g -c /etc/named.conf
2. Turn on the Authoritative name servers in a different environment terminal:
Navigate to the Authoritative server folders (`/env/nsd\_root`, `/env/nsd\_attack\_home` and `/env/nsd\_attack\_fun`.), then run in each authoritative server folder:
   ```bash
   nsd -c nsd.conf -d -f nsd.db

### Basic Test

To make sure that the setup is ready and well configured, follow these steps:

1. **Run another shell inside the docker container and start `tcpdump`:**
   ```bash
   docker exec -ti <container id> bash
   tcpdump -i lo -s 65535 -w /app/dump.pcap
2. Query the resolver from within the docker container
   ```bash
   dig firewall.fun.lan
  and make sure that the correct IP address is received, you should see Address: `127.0.0.207`.
  
3. Stop `tcpdump` (you can use `^C`), Open Wireshark load the file `<local_folder_path>/dump.pcap` and filter DNS
  requests.

You should observe the whole DNS resolution route for the domain name requested `firewall.fun.lan`:
  1. **Client Query to Resolver**
     - Query: `firewall.fun.lan` from client `127.0.0.1` to resolver `127.0.0.1`
  
  2. **Resolver Queries Root Server**
     - Query: `firewall.fun.lan` from resolver `127.0.0.1` to root server `127.0.0.2`
  
  3. **Root Server Response**
     - Response: SLD address for `fun.lan` from root server `127.0.0.2` to resolver `127.0.0.1`
  
  4. **Resolver Queries SLD**
     - Query: `firewall.fun.lan` from resolver `127.0.0.1` to SLD `127.0.0.100`
  
  5. **SLD Response**
     - Response: IP address `127.0.0.207` for `firewall.fun.lan` from SLD `127.0.0.100`
  
  6. **Resolver Returns Address to Client**
     - Response: IP address `127.0.0.207` for `firewall.fun.lan` from resolver `127.0.0.1` to client `127.0.0.1`

This sequence illustrates the journey of a DNS query starting from the client's request through to the resolver obtaining and returning the IP address associated with `firewall.fun.lan`.

**NOTE**: The address `firewall.fun.lan` is configured in `/env/nsd_attack/fun.lan.forward` and performing the above test ensures that the resolver accesses the authoritative through the root server.

## Contact
CacheFlush Simulator: [CacheFlushSimulator](https://github.com/shohamda/CacheFlushSimulator)

## Contribution
Bug reports and pull requests are welcome on GitHub at https://github.com/shohamda/CacheFlushSimulator. This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the Contributor Covenant code of conduct.

### Building the Docker
`docker build -t cacheflushsimulator .`

> **NOTE:** make sure the submodules have been downloaded (Check that bind9 and nsd folder aren't empty), if they are, run `git submodule update --init`

## Notes on Reusability
The simulator above was built based on a simulator that was created for NRDelegationAttack [https://github.com/ShaniBenAtya/dnssim](https://github.com/ShaniBenAtya/dnssim), and it was modified to meet our needs. Those who conduct research on DNS can use this simulator as it contains all of the necessary components, and it can be easily modified by adding authoritative name servers, updating resolver versions, modifying authoritative zone files, and modifying all component configurations.

**For more information**: [README](README.pdf)
