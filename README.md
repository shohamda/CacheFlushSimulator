# CacheFlushAttack Environment Setup

## Abstract

To fully understand the root cause of the CacheFlushAttack and to analyze its effective flush rate, we developed a mini-lab setup, disconnected from the Internet, that contains all the components of the DNS system, clients, resolvers, and authoritative name servers. 
This setup is built to analyze and examine the behavior of a resolver (or any other component) in details.
On the other hand it is not useful for performance analysis (stress analysis).  
Here we provide the code and details of this setup enabling to reproduce our analysis.  Moreover, researchers may find it useful for
farther behavioral analysis and examination of different components in the DNS system.
## Description & Requirements

The CacheFlushAttack environment, named DNS-CacheFlushSimulator, is an Inner-Emulator environment for DNS protocol research. It includes clients, a resolver, and four authoritative name servers. The resolver is a BIND9 recursive resolver (version 9.18.21), while the authoritative name servers are implemented with Name Server Daemon (NSD) version 4.3.3. Docker is required to use this environment.

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
