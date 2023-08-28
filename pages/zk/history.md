**The history of ZKs**

Zero-knowledge proofs (ZKPs), a class of cryptographic protocols, have revolutionized the world of digital communication and privacy. They have a unique ability to prove the validity of a statement without revealing any information about the statement itself, a radical departure from the traditional concept of proof. This ground-breaking approach was first introduced in the 1980s by Shafi Goldwasser, Silvio Micali, and Charles Rackoff, three computer scientists who would later be awarded the Turing Award for their contributions to cryptography and complexity theory.

The development of zero-knowledge proofs was motivated by the need for privacy and security in digital communication. The advent of the digital age brought about a paradigm shift in communication and data storage, creating an urgent need for secure communication channels and reliable ways to protect sensitive information. Traditional cryptographic protocols, while effective at ensuring data integrity and confidentiality, often required the disclosure of some information during the verification process. This was not ideal in many scenarios where privacy was a critical concern. The notion of a proof that conveys conviction but not knowledge was a significant advancement in cryptography, making it possible to verify data without exposing any information about it.

The "Ali Baba" or "cave and door" scenario offers a simple, intuitive way to understand the concept of ZKPs. In this thought experiment, Peggy (the Prover) wants to convince Victor (the Verifier) that she knows a secret password to a magic door inside a circular cave. Peggy proves her knowledge by consistently emerging from the path Victor specifies, without ever revealing the password itself. Through this process, Peggy demonstrates knowledge of the password in "zero knowledge", i.e., without revealing any information about the password.

While the "cave and door" scenario offers an illustrative understanding of ZKPs, the actual implementation of these proofs in real-world situations involves complex mathematical procedures and computational techniques. The original formulations of ZKPs were largely theoretical and impractical due to their computational complexity. However, the need for practical applications of ZKPs in the burgeoning field of digital currencies and blockchain technology led to significant advancements.

In the 2010s, new cryptographic techniques, such as zk-SNARKs (Zero-Knowledge Succinct Non-interactive ARguments of Knowledge), were developed. These allowed for the practical implementation of ZKPs, providing a robust method for privacy-preserving transactions on blockchain networks. The development of zk-SNARKs marked a new era in the application of ZKPs, making them a critical component in cryptocurrencies like Zcash.

Further research and development have led to more efficient and scalable ZKP systems, such as zk-STARKs (Zero-Knowledge Scalable Transparent ARguments of Knowledge), which do not require a trusted setup, unlike zk-SNARKs.

We will talk more about STARKs, SNARKs and practical applications, as well as use of Circom and such, but first we must understand the basics of ZKPs and everything related to it.

Homework reading: https://mathoverflow.net/questions/22624/example-of-a-good-zero-knowledge-proof

Putting it here for the sake of consistency, but you can read it on the link above.

"The classic example, given in all complexity classes I've ever taken, is the following: Imagine your friend is color-blind. You have two billiard balls; one is red, one is green, but they are otherwise identical. To your friend they seem completely identical, and he is skeptical that they are actually distinguishable. You want to prove to him (I say "him" as most color-blind people are male) that they are in fact differently-colored. On the other hand, you do not want him to learn which is red and which is green.

Here is the proof system. You give the two balls to your friend so that he is holding one in each hand. You can see the balls at this point, but you don't tell him which is which. Your friend then puts both hands behind his back. Next, he either switches the balls between his hands, or leaves them be, with probability 1/2 each. Finally, he brings them out from behind his back. You now have to "guess" whether or not he switched the balls.

By looking at their colors, you can of course say with certainty whether or not he switched them. On the other hand, if they were the same color and hence indistinguishable, there is no way you could guess correctly with probability higher than 1/2.

If you and your friend repeat this "proof" 𝑡
times (for large 𝑡
), your friend should become convinced that the balls are indeed differently colored; otherwise, the probability that you would have succeeded at identifying all the switch/non-switches is at most 2−𝑡
. Furthermore, the proof is "zero-knowledge" because your friend never learns which ball is green and which is red; indeed, he gains no knowledge about how to distinguish the balls."
~ Ryan O'Donnell
