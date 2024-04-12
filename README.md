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
The authoritative name servers are implemented with Name Server Daemon \href{https://www.nlnetlabs.nl/projects/nsd/about/}{(NSD)} version 4.3.3.
The clients are deployed on the same machine, which was configured to send DNS queries directly to the local recursive resolver. 
The setup configuration and environment are provided in \href{https://github.com/shohamda/CacheFlushSimulator}{GitHub} (\textit{https://github.com/shohamda/CacheFlushSimulator}).

In order to use \envname, a docker \href{https://docs.docker.com/get-docker/}{docker} is required.
### Security, Privacy, and Ethical Concerns

To ensure safety, the environment runs locally in a closed Docker container environment. It's crucial to use the "--dns 127.0.0.1" flag for configuration.

### How to Access

The source code and Docker image for the environment can be found on GitHub and DockerHub, respectively.

### Hardware Dependencies

No hardware dependencies are required.

### Software Dependencies

- Docker
- WireShark
- Resperf

### Benchmarks

Detailed benchmarks and setup requirements are provided in the [Benchmarks](#benchmarks) section.

## Set-up

Detailed setup instructions and directory structure are provided in the [Setup](#setup) section.

## Evaluation Workflow

The evaluation workflow includes major claims and experiments, outlined in the [Evaluation Workflow](#evaluation-workflow) section.

## Notes on Reusability

The environment can be easily modified and reused for DNS research purposes.

## Version

Based on the LaTeX template for Artifact Evaluation V20231005.
