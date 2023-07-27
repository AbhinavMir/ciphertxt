
---
title: DNAs in Cryptography.
type: posts
---

Found a pretty cool paper this week - [A New Hybrid Cryptosystem Involving DNA,
Rabin, One Time Pad and Fiestel](https://arxiv.org/pdf/2307.09322.pdf). Thought I'd discuss it.

This paper proposes a novel approach to cryptography by combining DNA sequences, the Rabin cryptosystem, one-time pad (OTP), and a Feistel structure. DNA cryptography provides several advantages that enhance the security of traditional methods.
<u>**Why DNA?**</u>
- Extremely large keyspace - DNA sequences of length $n$ have $4^n$ possible combinations, enabling an astronomically large number of keys. Even relatively short DNA strands can have keyspaces infeasible for brute force attacks.
- True randomness - Biologically generated DNA sequences exhibit more randomness than computationally generated keys, improving cryptographic security.
- Availability - Many websites provide randomly generated DNA sequences that can be readily used as cryptographic keys. 
- Compact storage - DNA can store vast amounts of data at a molecular scale, allowing the use of large keys in a small footprint.

<u>**Feistel Network**</u>
The Feistel structure splits the input data into two halves and works through multiple rounds of substitution and permutation (confusion and diffusion) on the halves to scramble the data thoroughly.

<u><b>Rabin key-gen, encryption, decryption</b></u>
The Rabin cryptosystem is a public-key cryptosystem based on the difficulty of factorizing large composite numbers into their prime factors. It was invented by Michael O. Rabin in 1979. The scheme consists of four algorithms: Key Generation, Encryption, Decryption, and Primality Testing.

The Rabin cryptosystem can be defined as follows:

1. Key Generation:
   - Choose two distinct prime numbers, $p$ and $q$, of equal length such that $p \neq q$.
   - Compute the modulus $N = p \cdot q$.
   - The public key is the modulus $N$.
   - The private key consists of the prime factors $p$ and $q$.

2. Encryption:
   - Convert the plaintext message $M$ into an integer representation.
   - Compute the ciphertext $C$ as $C = M^2 \mod N$.

3. Decryption:
   - Compute the four possible square roots of the ciphertext $C$ modulo $N$.
   - The four possible plaintexts $M_1, M_2, M_3, M_4$ are given by $M_i = \sqrt{C} \mod N$, for $i = 1,2,3,4$.

4. Primality Testing:
   - To verify the primality of an integer $x$, check if $x^{\frac{N-1}{2}} \equiv 1 \mod N$ or $x^{\frac{N-1}{2}} \equiv -1 \mod N$. If neither condition holds, $N$ is composite.

The security of the Rabin cryptosystem relies on the difficulty of factoring the modulus $N$ into its prime factors. To ensure secure communication, the prime factors $p$ and $q$ must be kept secret.

The Rabin cryptosystem has certain vulnerabilities related to its deterministic nature, such as the existence of non-trivial square roots of ciphertexts. To address these issues, additional steps and techniques, such as padding and digital signatures, can be incorporated into the scheme.

<u>**The algorithm discussed**</u>

Key Generation:

1. Sender generates a random DNA sequence to be used as a one-time pad (OTP) key. 
2. Receiver generates a public/private key pair for the Rabin cryptosystem. Sends the public key to sender.

Encryption:

1. Sender preprocesses plaintext by inserting a "spy" character at the start of each character.
2. Convert plaintext characters to ASCII values, concatenate pairs of ASCII values. 
3. Encrypt the ASCII values with Rabin encryption using receiver's public key.
4. Convert the Rabin ciphertext to binary. 
5. XOR the binary ciphertext with the random DNA OTP key.
6. Rearrange the XOR output using a Feistel network structure.
7. Send the rearranged ciphertext to the receiver.

Decryption: 
1. Receiver reverses the Feistel network scrambling. 
2. XORs the result with the DNA OTP key to undo that step.
3. Decrypts the Rabin ciphertext using private key. Gets 4 possibilities for each.
4. Checks "spy" character to select the correct plaintext from the 4 options.
5. Removes "spy" characters and converts ASCII values back to characters.

This achieves a high level of security by combining the strengths of all the components - DNA key randomness, Rabin asymmetric encryption, OTP unbreakability, and Feistel structure scrambling.

### TL;DR (Thanks GPT!)
- Proposes new encryption method combining DNA sequences, Rabin cryptosystem, one-time pad (OTP), and Feistel structure. 
- DNA sequences used as cryptographic keys provide massive keyspace, true randomness, availability, and compact storage. Harder to crack.
- Rabin public-key encryption used for asymmetric crypto. Computational security based on factoring large semi-primes. 

- OTP with DNA key gives unbreakable security through XORing.

- Feistel structure adds confusion through multiple rounds of substituting and shuffling halves.

- Hybrid system leverages strengths of each: DNA randomness/keyspace, Rabin math security, OTP unbreakability, Feistel confusion.

- Goal is very secure cipher resistant to various crypto attacks by synergizing different techniques.
