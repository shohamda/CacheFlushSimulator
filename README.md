# CacheFlushSimulator

## Abstract
To fully understand the root cause of the CacheFlushAttack and to analyze its effective flush rate, we developed a mini-lab setup, disconnected from the Internet, that contains all the components of the DNS system: clients, resolvers, and authoritative name servers. This setup is built to analyze and examine the behavior of a resolver (or any other component) in detail. However, it is not useful for performance analysis (stress analysis). Here we provide the code and details of this setup enabling to reproduce our analysis. Moreover, researchers may find it useful for further behavioral analysis and examination of different components in the DNS system.

## Description & Requirements
envname is an Inner-Emulator environment for DNS protocol, which was built as part of CacheFlushAttack research. envname includes clients, resolver, and four authoritative name servers. The resolver is a BIND9 recursive resolver with the latest version (9.18.21). The four authoritative name servers are: a ‘root’, an attacker, and two malicious delegation authoritative name servers.

Most of the CacheFlushAttack measurements were carried out on a BIND9 version 9.18.21 resolver compiled to work with the local ‘root’ authoritative name server. The authoritative name servers are implemented with Name Server Daemon (NSD) version 4.3.3. The clients are deployed on the same machine, which was configured to send DNS queries directly to the local recursive resolver. The setup configuration and environment are provided on GitHub (envname GitHub).

In order to use envname, a Docker is required.

## Security, privacy, and ethical concerns
To ensure that no harm may be done outside of the setup, the environment runs locally in a closed Docker container environment. It is thus important to use the --dns 127.0.0.1 flag to configure this. Changing the resolv.conf configuration inside the docker container is not enough (see the setup section).

### How to access
envname source code can be found at envname GitHub (1.0 Tag). The environment Docker image can be accessed through DockerHub (1.0 Tag).

### Hardware dependencies
There are no hardware dependencies required for using envname. During our research, we used an Ubuntu computer or Virtual Machine (we recommend using Ubuntu 20.04 or above) which is capable of running Docker images according to "Install Docker Engine on Ubuntu" specification.

#### Software dependencies
Docker
WireShark (To install WireShark on Ubuntu use: apt install wireshark).
Resperf (To install Resperf on Ubuntu use: apt install resperf).

## Benchmarks
In order to conduct the experiments described in CacheFlushAttack paper (see Benchmarks section), the setup should contain a BIND resolver with a new version bind9.18.21 and at four authoritative servers (local root authoritative and three authoritative to simulate the attack.com and delegation.attack authoritative). For CacheFlushNS Attack, a malicious zone file is required for the attacker authoritative (i.e., home.lan.forward for home.lan server). The malicious zone file contains malicious referral list with 1900 NS for each domain, which all delegate the resolver to a server IP address that is non-responsive to DNS queries through another authoritative server (the local root server can also be used to delegate the resolver to this IP address). For CacheFlushCNAME Attack, a malicious zone file is required for the attacker authoritative as well (i.e., home.lan.forward_CNAME for home.lan server). The malicious zone file contains a malicious CNAME chain of 1 million records, each pointing to the next domain.

## Set-up
### Installation
Pull the Docker image from Docker Hub (docker pull shohamd/cacheflushsimulator:1.0).
Run the Docker image as a container interactively so you can control the environment (docker container run --dns 127.0.0.1 --mount type=bind,source=<local_folder_path>,target=/app -it shohamd/cacheflushsimulator:1.0 /bin/bash). It is important to use the --dns 127.0.0.1 flag so the environment DNS will be local, changing the resolv.conf file inside a Docker container is not enough.
Inside the container, the systemname is installed in /root/cacheFlushAttack and the envname is installed in /app.
Reproducing Experiments
To reproduce the experiments presented in the CacheFlushAttack paper, please follow the instructions detailed in the experiments directory in the systemname. Specifically, the experiments for CacheFlushNS are in the experiments/CacheFlushNS directory, and the experiments for CacheFlushCNAME are in the experiments/CacheFlushCNAME directory. For more details, please refer to the CacheFlushAttack paper.

### Citation
If you find envname or this artifact useful in your work, please consider citing:

bibtex
Copy code
@inproceedings{DBLP:conf/uss/DaganDK20,
  author    = {Shoham Dagan and
               Yuval Elovici and
               Asaf Shabtai and
               Lior Rokach and
               Rami Puzis},
  title     = {CacheFlushAttack: A CPU Cache Attack on Recursive {DNS} Resolvers},
  booktitle = {29th {USENIX} Security Symposium, {USENIX} Security 2020, August
               12-14, 2020, Boston, MA, {USA}},
  pages     = {2017--2034},
  publisher = {{USENIX} Association},
  year      = {2020},
  url       = {https://www.usenix.org/conference/usenixsecurity20/presentation/dagan},
  timestamp = {Thu, 15 Oct 2020 11:01:00 +0200},
  biburl    = {https://dblp.org/rec/conf/uss/DaganDK20.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
This README provides detailed instructions on how to set up and use the artifact appendix for the CacheFlushAttack research, including all necessary dependencies, installation steps, and how to reproduce experiments.
