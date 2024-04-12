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

### Benchmarks

In order to conduct the experiments described in \systemname{} paper (Section~\ref{Experimental_Results}), the setup should contain a BIND resolver with a new version bind9.18.21 and at four authoritative servers (local root authoritative and three authoritative to simulate the "attack.com" and "delegation.attack" authoritative in Figure~\ref{fig:CacheFlushNS}). 
For CacheFlushNS Attack, a malicious zone file is required for the attacker authoritative (i.e., ``home.lan.forward'' for ``home.lan'' server).
The malicious zone file contain malicious referral list with 1900 NS for each domain, which all delegate the resolver to a server IP address that is non-responsive to DNS queries through another authoritative server (the local root server can also be used to delegate the resolver to this
IP address).
For CacheFlushCNAME Attack, a malicious zone file is required for the attacker authoritative as well (i.e., ``home.lan.forward\_CNAME'' for ``home.lan'' server).
The malicious zone file contains a malicious CNAME chain of 1 million records, each pointing to the next domain.

For instance, if the malicious request from the client is ``attacker0.home.lan'', the malicious referral response include a 1,900 list of name servers return. In order to create such referral list the ``/env/nsd\_attack\_home/home.lan.forward'' zone file needs to have 1900 records per one malicious request.
That is, the malicious zone file includes 1900 records for the malicious request which leads to a none existent domain name (e.g., attacker0 IN NS auth0.fun.lan. ... auth1900.fun.lan.) and the ``fun.lan'' authoritative server, which does not have any record to the non-responsive domain name, includes a wildcard record delegating the resolver to a non responsive IP address (e.g., * IN A 127.0.0.212).
## Set-up

Detailed setup instructions and directory structure are provided in the [Setup](#setup) section.

## Evaluation Workflow

The evaluation workflow includes major claims and experiments, outlined in the [Evaluation Workflow](#evaluation-workflow) section.

## Notes on Reusability

The environment can be easily modified and reused for DNS research purposes.

## Version

Based on the LaTeX template for Artifact Evaluation V20231005.
