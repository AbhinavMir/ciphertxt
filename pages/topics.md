## A corpus of my notes and articles on Cryptography, Networking and Formal methods

If something is incomplete, I'll try to finish it up ASAP. I'm tranferring 3-4 notebooks worth of notes first to digital text, formatting it with Markdown + LaTex and then finally posting them here, while dealing with build issues. It's a lot of fun (and this is not sarcastic). Sometimes I'll discover "Wait, this is all off" and other times I go "This could use a practical code example!", thus adding to the delay.

## Broad points of discussion

[Primer to Cryptography](#primer-to-cryptography)

[Graduate Cryptography](#graduate-cryptography)

[ZK Knowledge](#zk-knowledge)

[Elliptic Curves](#elliptic-curves) 

[Number Theory](#number-theory)

[Complex Analysis and Algebraic Structures](#algebraic-structures)

[Application of formal methods](#application-of-formal-methods)

[Complexity Theory and Cryptography](#complexity-theory-and-cryptography)

[Cryptoanalysis](#cryptoanalysis)

[Networking fundamentals](#networking-fundamentals)

[Network Security](#network-security)

<hr>

## Primer to Cryptography

Cryptography is essential for securing information in the digital world. This section covers the core concepts and constructions in cryptography.

1. [Introduction to Cryptography and Perfect Secrecy](/introduction/Introduction-to-cryptography-and-perfect-secrecy) - Overview of cryptography, its goals, and perfect secrecy as defined by Shannon. Understanding the foundations.

2. [Computational Security and Pseudorandom Generators](/introduction/pseudrandom-generators.md) - Moving beyond perfect secrecy to computational security against bounded adversaries. Introducing pseudorandom generators.

3. Hybrid Argument and Pseudorandom Functions - Hybrid argument for proving computational indistinguishability. PRFs from PRGs.

4. Goldreich-Goldwasser-Micali PRF Construction and IND-CPA Encryption - Constructing PRFs from PRGs. Using PRFs for IND-CPA symmetric encryption.

5. Identification Protocols, MACs, and Chosen Ciphertext Secure Encryption - Authentication via identification protocols. Message authentication codes. IND-CCA secure encryption. 

6. One-way Functions and Goldreich-Levin Theorem - Defining one-way functions. The Goldreich-Levin theorem for finding hardcore bits.

7. TCS Perspective on Goldreich-Levin Theorem and Local List Decoding - Theoretical computer science view of Goldreich-Levin theorem. Connections to list decoding.

8. Merkle's Key Exchange and Public-Key Encryption - Key exchange from OWFs. Public-key encryption from key exchange. 

9. Discrete Log Assumption and Diffie-Hellman Key Exchange - Discrete log assumption. Diffie-Hellman key exchange.

10. Trapdoor Functions, RSA, and Homomorphism - Trapdoor functions and RSA construction. Homomorphic encryption.

11. Digital Signatures and Lamport's One-time Signature Scheme - Digital signatures. Lamport's one-time signature scheme.

12. Collision-resistant Hash Functions and Naor-Yung Construction - Collision resistance. Naor-Yung construction of CCA encryption from CRHFs. 

13. Zero Knowledge Proofs I: Definitions and Examples - Zero knowledge proofs. Basic definitions and examples.

14. Zero Knowledge Proofs II: Zero Knowledge Proofs for all of NP - ZKPs for all of NP. ZK proof systems. 

15. Succinct (Zero Knowledge) Argument Systems and Kilian's Protocol - Efficient zero knowledge arguments. Kilian's protocol.

16. Lattices, Learning with Errors (LWE), and LWE-based Cryptography - Introduction to lattices. Learning with errors problem. LWE-based crypto.

17. Fully Homomorphic Encryption and Bootstrapping Theorem - Fully homomorphic encryption. Bootstrapping theorem.

18. Oblivious Transfer and Private Information Retrieval - 1-out-of-2 OT. Private information retrieval. 

19. Secure Two-Party Computation and Goldreich-Micali-Wigderson Protocol - Secure computation. GMW protocol.

20. Secret-Sharing and Secure Multiparty Computation - Secret sharing. Extending two-party computation to multiparty.

21. Program Obfuscation and Applications - Program obfuscation. Applications.

22. Yao's Garbled Circuits - Yao's garbled circuits construction.

23. Quantum Cryptography - Introduction to quantum cryptography.


## Graduate Cryptography

Advanced cryptography topics typically covered in graduate courses.  

1. Introduction to Cryptography - Overview of goals, security definitions, adversarial models.

2. Shannon, Perfect Security, and One-Time Pad - Shannon's perfect secrecy. The one-time pad.

3. Computational Adversary and Symmetric Encryption - Computational security. Definitions for symmetric encryption. 

4. One-way Functions and Goldreich-Levin Theorem - One-way functions. Hardcore bits and the Goldreich-Levin theorem.

5. Pseudorandom Generators and Pseudo-random Functions - PRGs and PRFs. Constructions of PRFs from PRGs. 

6. Pseudo-random Permutations and Symmetric Key Encryption - PRPs. Symmetric encryption from PRPs. 

7. Number Theory 1: Discrete Log, MSB, and QR - Discrete log. Modular square roots. Quadratic residuosity.

8. Number Theory 2: Factoring and RSA - Factoring. The RSA trapdoor permutation.

9. Public Key Encryption I: Construction from RSA and Quadratic Residuosity - Public-key encryption from RSA and QR.

10. Public Key Encryption II: Construction from Diffie-Hellman and Learning with Errors - Public-key encryption from DH and LWE.

11. Digital Signatures and MACs I - Definition and constructions of digital signatures. Message authentication codes.

12. Digital Signatures and MACs II - More on digital signatures and MACs.

13. Merkle Trees and Certificate Transparency - Merkle trees. Certificate transparency. 

14. Proof of Work, Consensus, Cryptographic Transactions, and Bitcoin - Proof of work. Distributed consensus. Bitcoin.

15. Zero Knowledge I: Definitions and Examples - Zero knowledge proofs. Basic definitions and examples. 

16. Zero Knowledge II: NP in ZK - Zero knowledge for all of NP. ZK proof systems.

17. Non-Interactive Zero Knowledge Proofs (NIZK) - Efficient non-interactive zero knowledge proofs. 

18. Zcash: Privacy-preserving Cryptocurrency with Zero-knowledge Proofs - Zcash and its use of NIZKs.

19. Specialized Homomorphic Encryption and Applications - Somewhat homomorphic encryption. Applications. 

20. Lattices and Learning with Errors (LWE) - Introduction to lattices. The learning with errors problem.

21. Fully Homomorphic Encryption - Fully homomorphic encryption. 

22. Private Information Retrieval (PIR) from FHE - Constructing PIR schemes from FHE.

23. Secret Sharing - Secret sharing schemes. 

24. Garbled Circuits and Yao's Two-party Computation Protocol - Yao's garbled circuits. Secure two-party computation.

25. GMW Two-party Computation - The GMW protocol for secure two-party computation.

26. Practical Machine Learning with MPC (optional for Berkeley) - Secure multiparty computation for machine learning.

## ZK Knowledge

Zero knowledge proofs are revolutionizing blockchain technology. This section provides an in-depth overview of modern ZKP constructions and applications.
˜
1. Introduction and History of Zero-Knowledge Proofs, modular arith. - Background and history of ZK proofs.

2. Overview of Modern SNARK Constructions - High-level overview of modern succinct non-interactive arguments of knowledge (SNARKs).

3. Libraries and Compilers to Build ZKP - Tools and libraries for building ZK proofs.

4. Interactive Proofs (IP) and Merkle Trees - Interactive proofs. Using Merkle trees in ZK systems.

5. Plonk Interactive Oracle Proofs (IOP) - The Plonk IOP construction and protocol. 

6. Discrete-log-based Polynomial Commitments - Polynomial commitments based on the discrete log. 

7. ZKP Based on Error-Correcting Codes - Leveraging error correcting codes.

8. Transparent ZKP - Transparency in ZK proofs. 

9. Linear Probabilistically Checkable Proofs (PCP) - Linear PCPs.

10. Recursive SNARKs, Aggregation, and Accumulation - Recursive proof composition. Proof aggregation and accumulation. 

11. Theoretical Foundations & Recent Theoretical Advancements - Theoretical foundations and latest advancements. 

12. Overview of ZKP Applications & zkRollup and zkEVM - ZK proof applications. zkRollup and zkEVM.

13. Building Opcode Compatible zk EVMs - Constructing EVM-compatible zk virtual machines.

14. Privacy-preserving Architectures - Architectures leveraging ZK proofs for privacy.

15. More ZKP Applications - Additional applications of ZK proofs.

16. Formal Verification of ZKP - Formal verification of ZK systems.

17. Hardware Acceleration of ZKP - Hardware optimizations for ZK proofs.

## Elliptic Curves

Elliptic curves are fundamental to modern cryptography. This section provides a deep dive into elliptic curve theory, construction, and applications.

1. Introduction to Elliptic Curves - Basic introduction to elliptic curves.

2. The Group Law, Weierstrass and Edwards Equations - Group law. Weierstrass and Edwards models.

3. Finite Field Arithmetic - Arithmetic in finite fields.

4. Isogenies and Division Polynomials - Isogenies. Division polynomials. 

5. Endomorphism Rings - Endomorphism rings of elliptic curves.

6. Hasse's Theorem and Point Counting - Hasse's theorem. Point counting algorithms.

7. Schoof's Algorithm - Schoof's point counting algorithm.

8. Generic Algorithms for the Discrete Logarithm Problem - Algorithms for the ECDLP. 

9. Index Calculus, Smooth Numbers, and Factoring Integers - Index calculus. Smooth numbers. Factorization algorithms.

10. Elliptic Curve Primality Proving (ECPP) - Using elliptic curves for probabilistic primality proving.

11. Endomorphism Algebras - Endomorphism algebras of elliptic curves.

12. Ordinary and Supersingular Curves - Ordinary vs supersingular curves.

13. Elliptic Curves over Complex Numbers (C) - Elliptic curves over the complex numbers.

14. Complex Multiplication (CM) and CM Torsor - Complex multiplication. CM torsors.

15. Riemann Surfaces and Modular Curves - Riemann surfaces. Modular curves.

16. The Modular Equation - The modular equation. 

17. The Hilbert Class Polynomial - Hilbert class polynomials.

18. Ring Class Fields and the CM Method - Ring class fields. The CM method for constructing curves.

19. Isogeny Volcanoes - Isogeny volcanoes.

20. The Weil Pairing - The Weil pairing and its properties. 

21. Modular Forms and L-functions - Modular forms. L-functions.

22. Fermat's Last Theorem - Using elliptic curves to prove Fermat's last theorem.

### Number Theory

1. Modular Arithmetic - Modular arithmetic, groups, inverses. Important foundation.

2. Prime Numbers and Factorization - Primes, unique factorization. Important cryptographic assumptions.

3. Discrete Logarithm Problem - Discrete log problem, Diffie-Hellman. Core cryptographic hardness assumption. 

4. Primality Testing - Testing primes and generating primes. Used in key generation.

5. Cryptographic Hash Functions - Hash functions, collision resistance. Essential cryptographic primitive.

6. Public-Key Cryptography - Public key encryption, signatures. enabled modern crypto.

7. Lattices - Lattices, LWE. A promising post-quantum alternative.

8. Error-Correcting Codes - ECCs, decoding. Used in code-based crypto. 

### Algebraic Structures

1. [Lattices and fundamental domains](/Algebraic-Structures/Lattices-and-fundamental-domains.md) - Lattices, fundamental domains, and Voronoi cells.
2. Holomorphic functions and modular forms - Holomorphic functions, modular forms, and the modular group.
3. Meromorphic functions and elliptic curves - Mero functions, elliptic curves, and the j-invariant.
3. Primer to Elliptic Functions - Elliptic functions, Weierstrass P function, and the Weierstrass zeta function.

Understanding algebraic structures crucial for cryptography.
Groups, Rings, Fields, Finite Fields, Vector Spaces, Boolean Algebra

### Application of formal methods

`Applcations via Coq`

1. Formal foundations - This covers the core mathematical and logical foundations used in formal methods, including inductively defined data types, functions and relations specified recursively, mathematical induction and rewriting for proofs, operational semantics to formally define program meaning, and data abstraction techniques for organizing proofs about data representations.

2. Type systems - This explores how type systems can enable static verification of programs. Topics include lambda calculus as a model of computation, type soundness proofs showing type safety, and advanced type system features like subtyping and mutable references that increase expressiveness while preserving soundness.

3. Program logics - These logics support reasoning about imperative programs. Hoare logic offers formal verification based on pre- and post-conditions. Different embeddings of source programs enable different proof methods. Separation logic supports modular reasoning about pointer-manipulating programs.

4. Concurrency models - Concurrency introduces new challenges for verification. Operational semantics can model concurrent behavior. Separation logic and rely-guarantee reasoning enable modular proofs about shared state. Process calculi like pi-calculus provide high-level languages for modeling and reasoning about message-passing programs. 

5. Key concepts - There are important high-level concepts that apply across models and methods. Encoding choices have big impacts on proof complexity. Invariants are central to most proofs about stateful programs. Abstraction and modularity enable tackling large systems by breaking them into smaller pieces.

6. Applications to Cryptography - Covers writing some proofs for cryptographic constructions in Coq. Also discusses EasyCrypt.

### Complexity Theory and Cryptography

Complexity theory is a branch of theoretical computer science that studies the resources required to solve computational problems. It provides a theoretical framework for understanding the efficiency of algorithms and the inherent difficulty of solving specific computational tasks. For cryptography, several elements of complexity theory are relevant and essential:

1. Computational Complexity Classes: Complexity theory defines classes of computational problems based on the amount of computational resources required to solve them. The most well-known complexity classes are P (problems solvable in polynomial time) and NP (problems verifiable in polynomial time). Cryptographers often work with problems that are believed to be hard in the worst-case scenario (NP-hard) or difficult to solve efficiently (NP-complete). Understanding these complexity classes helps cryptographers analyze the security of cryptographic protocols and algorithms.

2. One-Way Functions: One-way functions are central to many cryptographic constructions. These are functions that are easy to compute in one direction but computationally infeasible to invert in the other direction without specific additional information. Complexity theory provides the foundation for defining and studying the properties of one-way functions and their applications in cryptography, such as in public key cryptography.

3. Computational Intractability: Complexity theory investigates problems that are computationally intractable, meaning they cannot be solved efficiently by any known algorithm. This is closely related to the concept of hardness in cryptography. Cryptographers often rely on the assumption that certain problems are hard to solve, forming the basis for cryptographic protocols like factoring for RSA and discrete logarithms for Diffie-Hellman.

4. Reductions: Reductions are fundamental tools in complexity theory used to establish relationships between different problems. In cryptography, reductions are used to demonstrate that breaking one problem is equivalent to breaking another problem, thus providing evidence of the security of cryptographic constructions.

5. Randomized Complexity: Randomized algorithms and complexity classes like BPP (bounded-error probabilistic polynomial time) are relevant in cryptography. They allow for probabilistic analysis and the construction of algorithms that may not be guaranteed to be correct every time, but they are correct with high probability. Randomized algorithms are employed in certain cryptographic protocols and algorithms to improve efficiency and security.

6. Interactive Proof Systems: Complexity theory explores interactive proof systems, where a prover tries to convince a verifier about the validity of a claim. These concepts underpin the study of zero-knowledge proofs, which are widely used in modern cryptographic protocols to prove knowledge of information without revealing that information.

7. Hardness Assumptions: Cryptographic security often relies on the assumption that certain computational problems are hard to solve. Complexity theory helps in understanding the strength of these hardness assumptions and their implications for the security of cryptographic schemes.
    
## Cryptoanalysis
[Source](https://hadipourh.github.io/course-cryptanalysis/)

- **Kerckhoffs' Principle**: Security of a cryptographic system relies on the secrecy of the key, not the algorithm.
- **Notions of Security**: Assessing security in terms of confidentiality, integrity, authenticity, and more.
- **Models of Attack**: Different attack models, such as chosen plaintext, chosen ciphertext, etc.
- **Targets of Attack**: Analyzing weaknesses in block ciphers, stream ciphers, hash functions, key exchange protocols, etc.
- **Theoretical Attacks vs. Practical Attacks**: Distinguishing attacks based on mathematical principles from those considering real-world limitations.
- **Lessons Learned from Classic Ciphers**: Insights gained from historical ciphers like the Caesar cipher and Vigenère cipher.
- **Cryptanalysis of Block Ciphers**:
  - Meet-in-the-Middle Attack & TMTO.
  - Basic Differential Analysis.
  - Basic Linear Analysis.
  - Wide-Trail Strategy and AES.
  - Integral Cryptanalysis.
  - Truncated Differential Attack.
  - Higher Order Differential Attack.
  - Boomerang and Rectangle Attacks.
  - Impossible Differential Attack.
  - Multi-Dimensional Linear Attack.
  - Zero-Correlation Linear Attack.
  - Division Property.
  - Demirci-Selcuk MitM Attack.
  - Subspace Trail Cryptanalysis.
- **More (Optional)**: Advanced cryptanalysis techniques and attacks.
- **Cryptanalysis of Stream Ciphers**:
  - Guess-and-Determine Attack on Stream Ciphers.
  - Time-Memory-Data Tradeoff Attack.
  - Linear Distinguisher and Correlation Attacks.
- **Cryptanalysis of Hash Functions**:
  - Birthday Attacks.
  - MD and Sponge.
  - Differential Cryptanalysis and Collision Attacks.
- **Meet-in-the-Middle Pre-image Attack**
- **Computer-Aided Cryptanalysis**:
  - MILP-based Cryptanalysis.
  - SAT-based Cryptanalysis.
  - Algebraic Cryptanalysis.
  - Interpolation Attack.
  - Cube Attacks and Higher Order Differential Attack.
  - Linearization.
- **Merkle-Hellman Knapsack**
- **Diffie-Hellman Key Exchange and MitM**
- **Discrete Log Algorithms**:
  - Baby-Step Giant-Step.
  - Factoring Algorithms.
  - Dixon's Algorithm.
  - Quadratic Sieve.
- **Quantum Algorithms**

## Networking fundamentals
Follows the CCNA guide.

1.1 Explain the role and function of network components
- 1.1.a Routers
- 1.1.b Layer 2 and Layer 3 switches
- 1.1.c Next-generation firewalls and IPS
- 1.1.d Access points
- 1.1.e Controllers (Cisco DNA Center and WLC)
- 1.1.f Endpoints
- 1.1.g Servers
- 1.1.h PoE

1.2 Describe characteristics of network topology architectures
- 1.2.a Two-tier
- 1.2.b Three-tier
- 1.2.c Spine-leaf
- 1.2.d WAN
- 1.2.e Small office/home office (SOHO)
- 1.2.f On-premise and cloud

1.3 Compare physical interface and cabling types
- 1.3.a Single-mode fiber, multimode fiber, copper
- 1.3.b Connections (Ethernet shared media and point-to-point)

1.4 Identify interface and cable issues (collisions, errors, mismatch duplex, and/or speed)

1.5 Compare TCP to UDP

1.6 Configure and verify IPv4 addressing and subnetting

1.7 Describe the need for private IPv4 addressing

1.8 Configure and verify IPv6 addressing and prefix

1.9 Describe IPv6 address types
- 1.9.a Unicast (global, unique local, and link local)
- 1.9.b Anycast
- 1.9.c Multicast
- 1.9.d Modified EUI 64

1.10 Verify IP parameters for Client OS (Windows, Mac OS, Linux)

1.11 Describe wireless principles
- 1.11.a Nonoverlapping Wi-Fi channels
- 1.11.b SSID
- 1.11.c RF
- 1.11.d Encryption

1.12 Explain virtualization fundamentals (server virtualization, containers, and VRFs)

1.13 Describe switching concepts
- 1.13.a MAC learning and aging
- 1.13.b Frame switching
- 1.13.c Frame flooding
- 1.13.d MAC address table

2.1 Configure and verify VLANs (normal range) spanning multiple switches
- 2.1.a Access ports (data and voice)
- 2.1.b Default VLAN
- 2.1.c InterVLAN connectivity

2.2 Configure and verify interswitch connectivity
- 2.2.a Trunk ports
- 2.2.b 802.1Q
- 2.2.c Native VLAN

2.3 Configure and verify Layer 2 discovery protocols (Cisco Discovery Protocol and LLDP)

2.4 Configure and verify (Layer 2/Layer 3) EtherChannel (LACP)

2.5 Interpret basic operations of Rapid PVST+ Spanning Tree Protocol
- 2.5.a Root port, root bridge (primary/secondary), and other port names
- 2.5.b Port states (forwarding/blocking)
- 2.5.c PortFast

2.6 Describe Cisco Wireless Architectures and AP modes

2.7 Describe physical infrastructure connections of WLAN components (AP, WLC, access/trunk ports, and LAG)

2.8 Describe AP and WLC management access connections (Telnet, SSH, HTTP, HTTPS, console, and TACACS+/RADIUS)

2.9 Interpret the wireless LAN GUI configuration for client connectivity, such as WLAN creation, security settings, QoS profiles, and advanced settings

3.1 Interpret the components of the routing table
- 3.1.a Routing protocol code
- 3.1.b Prefix
- 3.1.c Network mask
- 3.1.d Next hop
- 3.1.e Administrative distance
- 3.1.f Metric
- 3.1.g Gateway of last resort

3.2 Determine how a router makes a forwarding decision by default
- 3.2.a Longest prefix match
- 3.2.b Administrative distance
- 3.2.c Routing protocol metric

3.3 Configure and verify IPv4 and IPv6 static routing
- 3.3.a Default route
- 3.3.b Network route
- 3.3.c Host route
- 3.3.d Floating static

3.4 Configure and verify single area OSPFv2
- 3.4.a Neighbor adjacencies
- 3.4.b Point-to-point
- 3.4.c Broadcast (DR/BDR selection)
- 3.4.d Router ID

3.5 Describe the purpose, functions, and concepts of first hop redundancy protocols

4.1 Configure and verify inside source NAT using static and pools

4.2 Configure and verify NTP operating in a client and server mode

4.3 Explain the role of DHCP and DNS within the network

4.4 Explain the function of SNMP in network operations

4.5 Describe the use of syslog features including facilities and levels

4.6 Configure and verify DHCP client and relay

4.7 Explain the forwarding per-hop behavior (PHB) for QoS, such as classification, marking, queuing, congestion, policing, and shaping

4.8 Configure network devices for remote access using SSH

4.9 Describe the capabilities and functions of TFTP/FTP in the network

5.1 Define key security concepts (threats, vulnerabilities, exploits, and mitigation techniques)

5.2 Describe security program elements (user awareness, training, and physical access control)

5.3 Configure and verify device access control using local passwords

5.4 Describe security password policies elements, such as management, complexity, and password alternatives (multifactor authentication, certificates, and biometrics)

5.5 Describe IPsec remote access and site-to-site VPNs

5.6 Configure and verify access control lists

5.7 Configure and verify Layer 2 security features (DHCP snooping, dynamic ARP inspection, and port security)

5.8 Compare authentication, authorization, and accounting concepts

5.9 Describe wireless security protocols (WPA, WPA2, and WPA3)

5.10 Configure and verify WLAN within the GUI using WPA2 PSK

6.1 Explain how automation impacts network management

6.2 Compare traditional networks with controller-based networking

6.3 Describe controller-based, software-defined architecture (overlay, underlay, and fabric)
- 6.3.a Separation of control plane and data plane
- 6.3.b Northbound and Southbound APIs

6.4 Compare traditional campus device management with Cisco DNA Center enabled device management

6.5 Describe characteristics of REST-based APIs (CRUD, HTTP verbs, and data encoding)

6.6 Recognize the capabilities of configuration management mechanisms Puppet, Chef, and Ansible

6.7 Recognize components of JSON-encoded data

## Network Security
(Follows CS558 by Prof. Kaptchuk ~ I was enrolled for his course in Spring '22 and was deeply inspired)


1. Internet Infrastructure Protocols (eg. BGP, ARP, DNS)
2. DDoS and Reflection Attacks
3. TLS (eg. FREAK, Logjam, Drown, Heartbleed, Goto Fail, PKI infrastructure)
4. Crypto Wars
5. Tor (eg. Protocol obfuscation, Protocol tunneling)
6. Proxying (eg. Domain Fronting and Encrypted SNI, Telex and Tapdance)
7. Attacking Secure Messaging (eg. Padding oracles, iMessage attack)
8. Signal Protocol (eg. Forward/Backward Secrecy, OTR, Sealed Sender Messaging, Private Information Retrieval)
9. Private Computation - Trusted Execution Environments and MPC (Security Model, Attacks, Real Applications)
10. Two Party Computation/Multiparty Computation (BU and BWWC, STORMY Tor measurement, End to End 2PC/MPC compilers)
