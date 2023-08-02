---
title: MACs, and Chosen Ciphertext Secure Encryption
---

MAC stands for Message Authentication Code. In cryptography, it is a technique used to verify the integrity and authenticity of a message or data transmitted between two parties over an insecure channel. The primary purpose of a MAC is to ensure that the data has not been altered or tampered with during transmission and that it originates from the expected sender.

The process of generating and verifying a MAC involves the use of a secret key known only to the sender and the receiver. Here's a general overview of how MAC works:

1. Key Generation: The sender and receiver agree on a secret key beforehand. This key is kept confidential and is used to generate and verify the MAC.

2. MAC Generation (Sender's Perspective):
   a. The sender takes the original message (plaintext) that needs to be transmitted.
   b. The sender applies a MAC algorithm, which typically involves a cryptographic hash function, along with the secret key, to create a fixed-size hash value or tag based on the message and the key. The process of hashing produces a unique output, called the MAC value.

3. MAC Verification (Receiver's Perspective):
   a. The receiver receives the transmitted message and the associated MAC value.
   b. The receiver applies the same MAC algorithm, using the secret key, to the received message to generate a new MAC value.
   c. The receiver then compares the calculated MAC value with the received MAC value.
   d. If the calculated MAC value matches the received MAC value, it indicates that the message has not been altered during transmission and that it likely originated from the expected sender. In this case, the receiver can trust the integrity and authenticity of the message.

It's important to note that MACs only provide integrity and authenticity for the message itself, not confidentiality. If confidentiality is also required, the data should be encrypted using a separate encryption algorithm, such as AES (Advanced Encryption Standard), in addition to using MAC.

Popular MAC algorithms include HMAC (Hash-based MAC) that uses cryptographic hash functions like SHA-256 or SHA-3 and CMAC (Cipher-based MAC) that employs block ciphers like AES in CBC mode. The choice of MAC algorithm depends on security requirements and performance considerations.

> Good to know: AES is a widely used symmetric encryption algorithm known for its security and efficiency, and in CBC mode, it encrypts a message by splitting it into blocks and processing each block separately, mixing it with the previously encrypted block to prevent revealing patterns from the original message, thus enhancing security.

Let's do a non-trivial example now. I'll do these type of examples to get you used to the vernacular and concepts and then deal with the actual definitions later. Understand the words at a very surface level for now.
To secure a plaintext message $M$, follow these steps:

1. Generate a Message Authentication Code (MAC) using HMAC-SHA256 with a secret key $K_{\text{MAC}}$: $T = \text{HMAC-SHA256}(K_{\text{MAC}}, M)$. (HMAC stands for Hash-based Message Authentication Code. It is a type of MAC that uses a cryptographic hash function like SHA-256. HMACs are like encryption, but you cannot decrypt them. An important example of such a system is in passwords: you store the hash of the password, not the password itself. This way, if the database is compromised, the attacker cannot get the passwords. However, when the user logs in, you can hash the password they entered and compare it to the stored hash. If they match, the user entered the correct password. This is why you cannot decrypt HMACs. You can only compare them to other HMACs.)

2. Encrypt the MACed message using AES-256 in CBC mode with a separate encryption key $K_{\text{Enc}}$ and an Initialization Vector (IV) to produce ciphertext $C$. (For now, think of IV as a seed, I'll talk more about it in a minute. So this function is basically encrypting the hash to produce a ciphertext - which is where the name of the website comes from!)

3. Send both the ciphertext $C$ and IV over the insecure channel. (An insecure channel is usually something like a public WiFi)

4. On the receiver's side, decrypt the ciphertext to obtain the MACed message: $M_{\text{MACed}} = \text{AES-256-CBC-Decrypt}(K_{\text{Enc}}, IV, C)$.

5. Verify the integrity of the message by recomputing the MAC value $T_{\text{received}} = \text{HMAC-SHA256}(K_{\text{MAC}}, M_{\text{MACed}})$. If $T_{\text{received}}$ matches the transmitted MAC $T$, the message is both authentic and unaltered.

There are two methods of hashing and encrypting. The first method is called Hash-then-Encrypt, and the second method is called Encrypt-then-Hash. The difference between the two methods is the order of operations. In the Hash-then-Encrypt method, the message is first hashed and then encrypted. In the Encrypt-then-Hash method, the message is first encrypted and then hashed. The following table summarizes the pros and the cons –

| Approach          | Pros                                                          | Cons                                                 |
|-------------------|---------------------------------------------------------------|------------------------------------------------------|
| Encrypt and MAC   | - Provides both confidentiality and data integrity.         | - Slightly more computational overhead.               |
|                   | - Encrypts the message first, making it unreadable.          | - Slightly more complex implementation.              |
|                   | - Verifies integrity after decryption, ensuring authenticity.| - Requires two separate keys for encryption and MAC. |
| MAC and Encrypt   | - Simpler implementation, requiring a single key.            | - Data integrity verified before decryption.         |
|                   | - Verifies integrity before decryption, ensuring authenticity.| - Only the MAC is authenticated, not the ciphertext.|
|                   | - Lower computational overhead compared to Encrypt and MAC.  | - No confidentiality guarantee for the MAC.         |

Choose the approach based on the specific security requirements and performance considerations of your application. Both approaches can provide adequate security when implemented correctly, but "Encrypt and MAC" is generally considered more secure and widely used in practice.

Secure communication protocols like TLS/SSL (Transport Layer Security/Secure Sockets Layer) use "Encrypt and MAC" to ensure data confidentiality and integrity during data transmission over the internet.

## Some possible attacks

I have dedicated a whole section to cryptoanalysis, but I wanted to discuss two attacks (and how IVs help against these attacks).

**Birthday Attack**
The birthday attack exploits the probability of finding two different inputs that produce the same hash output (collision). In encryption, it is used to highlight the importance of using an Initialization Vector (IV) to ensure different ciphertexts are produced for the same plaintext and key combination. Without an IV, an attacker could potentially identify patterns or repetitions in the ciphertext, making certain cryptographic attacks more feasible.

**Known-Plaintext Attack**
In a known-plaintext attack, the attacker has access to both the plaintext and the corresponding ciphertext. The objective is to deduce the encryption key. An IV helps mitigate the impact of known-plaintext attacks by adding an extra layer of randomness to each encryption operation, making it more challenging for the attacker to identify relationships between plaintext and ciphertext.

## Indistinguishability under Chosen Ciphertext Attack

Unlike the other two attacks I discussed, this one's important for us in the now as we begin solving some problem sets.

Chosen Ciphertext Attack is a type of cryptographic attack that aims to break an encryption scheme by gaining access to the decryption oracle. Unlike other attacks, such as chosen plaintext attacks or known plaintext attacks, where the attacker can only choose or observe plaintexts, in a CCA, the attacker can submit ciphertexts of their choice to the decryption oracle and receive the corresponding decrypted plaintexts. This access to the decryption oracle enables the attacker to gain deeper insight into the encryption process and find potential weaknesses.

IND-CCA stands for "INDistinguishability under Chosen-Ciphertext Attack." It is a security property that cryptographic encryption schemes should possess to ensure the confidentiality of data in the presence of attackers.

In an encryption scheme, an adversary may try to obtain information about the plaintext by submitting chosen ciphertexts to be decrypted by the encryption oracle. The adversary's goal is to distinguish the decryption of two different ciphertexts that encrypt the same plaintext or gain any other useful information about the plaintext.

An encryption scheme is said to be IND-CCA secure if an attacker, even with access to an encryption oracle and a decryption oracle, cannot distinguish between two ciphertexts that encrypt the same plaintext or learn any information about the plaintext through chosen-ciphertext attacks.

Formally, IND-CCA security can be defined as follows:

$$
\text{Adv(A) = Pr}[A(C) = m \,|\, C = E(k, m) \text{ for some random key k and random message m}] - \frac{1}{2},
$$

where C is a ciphertext obtained from A's queries, m is a message, and k is a randomly chosen encryption key.

In simple terms, an IND-CCA secure encryption scheme ensures that an attacker cannot leverage chosen-ciphertext queries to reveal any information about the encrypted data or the encryption key. This property is crucial for secure communication and data protection in various cryptographic protocols and systems.

## IND-CCA vs IND-CPA by analogy

IND-CPA is like a safe that can withstand burglars who can try to open it by only observing its response to a series of chosen-plaintext attacks (i.e., they can choose plaintexts and see the encrypted results). The safe should remain secure even if an attacker can observe the encryption of several chosen plaintexts.

IND-CCA is like a safe that not only resists burglars but also has a mechanism to resist attackers who can interact with the safe by presenting ciphertexts and receiving decrypted results (chosen-ciphertext attacks). The safe should remain secure even when facing adversaries that can adapt their attacks based on previously obtained decryption information.