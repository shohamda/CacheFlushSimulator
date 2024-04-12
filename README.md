# CacheFlushAttack Environment Setup

## Abstract

To fully understand the root cause of the CacheFlushAttack and to analyze its effective flush rate, we developed a mini-lab setup, disconnected from the Internet, that contains all the components of the DNS system, clients, resolvers, and authoritative name servers. 
This setup is built to analyze and examine the behavior of a resolver (or any other component) in details.
On the other hand it is not useful for performance analysis (stress analysis).  
Here we provide the code and details of this setup enabling to reproduce our analysis.  Moreover, researchers may find it useful for
farther behavioral analysis and examination of different components in the DNS system.

## Description & Requirements

DNS-CacheFlushSimulator is an Inner-Emulator environment for DNS protocol which was built as part of CacheFlushAttack research.
DNS-CacheFlushSimulator includes clients, resolver and four authoritative name servers. The resolver is a BIND9 recursive resolver with the latest version (9.18.21). The four authoritative name servers are: a ‘root’, an attacker, and two malicious delegation authoritative name servers.
Most of the CacheFlushAttack measurements were carried out on a BIND9 version 9.18.21 resolver compiled to work with the local ‘root’ authoritative name server.
The authoritative name servers are implemented with Name Server Daemon [NSD](https://www.nlnetlabs.nl/projects/nsd/about/) version 4.3.3.
The clients are deployed on the same machine, which was configured to send DNS queries directly to the local recursive resolver. 
The setup configuration and environment are provided in [GitHub](https://github.com/shohamda/CacheFlushSimulator).
In order to use \envname, a [docker](https://docs.docker.com/get-docker/) is required.

### Security, Privacy, and Ethical Concerns

To ensure that no harm may be done outside of the setup, the environment runs locally in closed Docker container environment.
It is thus important to use "–dns 127.0.0.1" flag to configure this.
Changing the "resolv.conf" configuration inside the docker container is not enough (see #setup)

### How to Access
 
The environment docker image can be accessed through [DockerHub](https://hub.docker.com/r/shohamd/cacheflushsimulator) (1.0 Tag).

### Hardware Dependencies

There is no hardware dependencies required for using DNS-CacheFlushSimulator.
During our research, we used an Ubuntu computer or Virtual Machine (we recommend using Ubuntu 20.04 or above) which is capable of running Docker images according to "Install Docker Engine on Ubuntu" [specification](https://docs.docker.com/engine/install/ubuntu/).

### Software Dependencies

- [Docker](https://docs.docker.com/engine/install/ubuntu/)
- [WireShark](https://www.wireshark.org/)
- [Resperf](https://linux.die.net/man/1/resperf)

