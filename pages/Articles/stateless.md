> This document discusses KZG scheme, but Ethereum is tending towards IPA, which is a different scheme. I'll update this document once I have a better understanding of IPA.


# The State of Stateless in Ethereum ecosystem

Statelessness is important in Ethereum as it allows for nodes that sync fast to be used, increasing trust assumptions for users due to an increased decentralised verification system. It is also great for state resurrection should we ever decide to prune out the stale state or even delete less relevant states. We will likely keep a state stored elsewhere instead of on full nodes, and should we ever need it, clients can use stateless blocks for execution and verification.

Verkle trees are similar to Merkle trees in that they store large amounts of data and provide a proof for any single piece. If you're new to Merkle trees, we probably should go over it really quickly.

We don't want absolute statelessness, we want weak statelessness. In the words of Darkrad, that means: "Validating block requires no state, but proposing blocks requires the full state". ETH2 Validators won't need full state - so staking from mobile devices (raspberry pi etc) becomes much easier. Light clients, however, should also be able to validate single blocks as fraud proofs.

A quick note on states: "For the state tree, however, the situation is more complex. The state in Ethereum essentially consists of a key-value map, where the keys are addresses and the values are account declarations, listing the balance, nonce, code and storage for each account (where the storage is itself a tree)." [1](https://blog.ethereum.org/2015/11/15/merkling-in-ethereum)

<hr>

### Merkle Trees

Imagine you have a lot of data that you want to verify hasn't been tampered with. Instead of checking each piece of data individually, which can be time-consuming, you can use a Merkle tree.

A Merkle tree starts with the original data, which could be a collection of files or any other kind of data. The data is then divided into smaller chunks, let's call them "blocks." Each block is represented by a unique cryptographic hash.

Next, pairs of these blocks are combined and hashed together. This process continues until there's only one hash left, called the "root hash" or "Merkle root." The root hash is the final result of the Merkle tree construction.

Here's the cool part: By looking at just the root hash, you can verify the integrity of the entire data set. If any part of the data changes, even a single bit, the root hash will be completely different. So if someone tries to tamper with any block in the data, it will be immediately detected when you compare the new root hash with the original one.

To verify a specific block, you don't need to check the entire data set. Instead, you only need to follow a path from the root hash down to the specific block you want to verify. This path consists of the hashes of the blocks that were combined at each level of the tree.

```go
// Struct definition for a typical Binary Merkle tree node
type MerkleNode struct {
  Data  []byte         // Data stored in the node
  Left  *MerkleNode    // Reference to the left child node
  Right *MerkleNode    // Reference to the right child node
  Hash  []byte         // Hash of the node's data
}

// Interface for a Merkle tree
type MerkleTree interface {
  GetRootHash() []byte                 // Get the root hash of the Merkle tree
  AddData(data []byte)                  // Add data to the Merkle tree
  VerifyData(data []byte) bool           // Verify the integrity of a specific data in the Merkle tree
}
```

Some technical depth: To construct a Merkle tree, the process of combining and hashing pairs of blocks is repeated until there is only one hash remaining, known as the root hash or Merkle root. Here's a step-by-step explanation of the process:

1. Start with the original data, which can be divided into individual blocks. Each block is assigned a unique identifier.
2. Compute the cryptographic hash for each block using a hash function (e.g., SHA-256). The hash function takes the block's data as input and produces a fixed-length hash value as output.
3. Pair up adjacent blocks and concatenate their hashes together.
4. Hash the concatenated hashes from step 3. This hash becomes the new data for the next level of the tree.
5. Repeat steps 3 and 4 until only one hash remains. This final hash is the root hash or Merkle root of the tree.
![[Pasted image 20230618191833.png]]
### Where does Verkle Tries come into picture

Verkle Trees = **V**ector Commitment + M**erkle Trees**. A Trie just means that each node represents a prefix of keys in the Key-Value pairs. Verkle Trees are used in place of Merkle trees to statelessly store states (accounts and balances).

In a Merkle tree, as we go "up" the tree, we hash the two nodes to construct the nodes above. A d-ary Merkle tree needs $(d-1)(log_d n)$ hashes for a single proof at position $n$. Thus for a typical Ethereum Merkle tree, which is a hexnary merkle tree, we need $5(log_5 n)$ hashes at position $n$, and thus the complexity of verifying a proof is $(log_5 n)$. 

So for proving that, say L2, is part of the Merkle tree, we need the full tree upto the leaf you're validating. So if you're syncing a fresh node, you need the full node to test that the latest node you have is in face part of the Ethereum state - you can see how bloated this becomes no?

Verkle trees are used to prove membership in state more effectively.

### Commitment Scheme 

***(This part is directly pasted from [RISC Zero's video](https://www.youtube.com/watch?v=pTAj9QFGrog))***

A commitment scheme is a way to ensure that someone doesn’t change their answer after the fact.

All commitments scheme are binding.
A commitment scheme may also be hiding.

A “commitment scheme” consists of:
- A method of “committing” to something
- A method of “revealing” pieces of the commitment
- A method of “checking” whether the revealed pieces matched the original commitment

### Vector Commitments

Vectors are one dimensional arrays, you might've come across them in LinAl or Rustlang, same concept. Commitments is a concept from cryptography, which means that you can choose a value from your option set, without revealing to anyone else what the option is. You can of course, reveal it later, but the idea is that you choose a commitment $C$ from space $S$. 

If you've never done cryptography, don't be scared: I'm going to use some notations, but they're mild, weird looking English. You can read them.

Let's say a vector space, $\overrightarrow[v] = v_1, v_2 ... v_n$ exists. 
For this vector space, there will be four algorithms in a vector commitment scheme.

1. $Setup \rightarrow cr\space s$ // Sets up public parameters and such
2. $Commit (cs\space s \overrightarrow[v])\rightarrow C$ // Chooses a commitment 
3. $Open (cs\space s, v_i, \overrightarrow[v])\rightarrow \pi_i$ // Creates a proof $\pi_i$ for $v_i$
4. $Verify(cs\space s, C, i, v_i, \pi_i)\rightarrow 0 \space or \space 1$

It is important for these to be succinct, which means the proof must be constant size. Also, an aggregate of two proofs should still be valid and constant size. Creating such a proof is non-trivial, it has a complexity of $O(n^2)$ - which is not good.

Usually, a hash-based commitment, as shown in Merkle tree, would formally be defined as such:
Hash function: $H: MxR\rightarrow C$ with only one mandatory requirement, that $H$ is collision resistant, and a preference which is $|R|>>|C|$ (Random space is much greater than commitment space).

You'd commit as such: $commit(m\epsilon M, r\leftarrow R)$, and verify as such: $verify(m, com \space r)$ {where "com" is commitment scheme = $H(m,r)$}. But there can be a collision even with collision resistance and it also has a randomness assumption from $H$.

### KZG polynomial commitments as our vector commitment scheme

"Better vector commitments change this equation; by using the KZG polynomial commitment scheme as a vector commitment, each level only requires a constant size proof, so the annoying factor of d−1 that kills d-ary Merkle trees disappears. ~ Darkrad

The KZG commitment scheme is a cryptographic technique used to commit to a value while keeping it hidden, similar to a cryptographic hash function.

The KZG commitment scheme is based on polynomial interpolation and evaluation. Here's a high-level overview of how it works (remember the four algorithms needed from vector commitments from before):

1. Setup: The commitment scheme involves a setup phase where a trusted party generates parameters and publishes them. These parameters typically include a prime number, a generator, and other values needed for the commitment scheme.

2. Commitment: To commit to a value, the committer chooses a random polynomial of a certain degree and sets the constant term of the polynomial to the value they want to commit. Then, they compute the evaluations of this polynomial at specific points, called "evaluation points." These evaluation points are usually derived from the parameters generated in the setup phase. The committer sends the evaluations as the commitment to the receiver.

3. Verification: To verify the commitment, the receiver randomly selects a subset of the evaluation points and requests the committer to provide the polynomial coefficients corresponding to those points. The receiver can use these coefficients and the evaluation points to reconstruct the polynomial.

4. Opening: If the receiver is satisfied with the commitment and wants to reveal the committed value, they can request the committer to provide the polynomial coefficients for all the evaluation points. By knowing the coefficients, the receiver can interpolate the polynomial and retrieve the committed value.

The security of the KZG commitment scheme relies on the hardness of certain mathematical problems, such as polynomial interpolation, polynomial evaluation, and the hiding property of the committed value.

The KZG commitment scheme involves polynomials and their evaluations. Let's denote a polynomial of degree $d$ as $f(x)$, and the committed value as $v$. The KZG commitment scheme proceeds as follows:

1. Setup: The trusted party generates parameters. Let's denote the prime number as $p$ and the generator as $g$.

2. Commitment: The committer chooses a random polynomial $f(x)$ of degree $d$ such that $f(0) = v$. The polynomial can be represented as: $[f(x) = c_0 + c_1x + c_2x^2 + \ldots + c_dx^d]$ (where $c_0 = v$ is the constant term - this represents the constant term of the polynomial).
   
   The committer computes the evaluations of the polynomial at specific points, denoted as $x_1, x_2, \ldots, x_n$, which are derived from the setup parameters. The commitment is then computed as: $[commit = g^{f(x_1)} \cdot g^{f(x_2)} \cdot \ldots \cdot g^{f(x_n)} = g^{c_0} \cdot g^{c_1x_1} \cdot g^{c_2x_2^2} \cdot \ldots \cdot g^{c_dx_d^d}]$. The committer then sends the commitment to the receiver.

3. Verification: The receiver randomly selects a subset of the evaluation points, say $x_{i_1}, x_{i_2}, \ldots, x_{i_k}$, and requests the committer to provide the corresponding polynomial coefficients $c_{i_1}, c_{i_2}, \ldots, c_{i_k}$. The receiver can use these coefficients and the evaluation points to reconstruct the polynomial $f(x)$ using interpolation techniques (I discuss this in another blog, but I can't find it right now!).

4. Opening: If the receiver is satisfied with the commitment and wants to reveal the committed value, they can request the committer to provide all the polynomial coefficients $c_0, c_1, c_2, \ldots, c_d$. By knowing these coefficients, the receiver can interpolate the polynomial and retrieve the committed value $v$.

Now, let's compare the KZG commitment scheme to vector commitments and highlight its advantages:

1. Compactness: KZG commitments are more compact compared to vector commitments. Instead of committing to a whole vector of values, KZG commitments only require the commitment to a single value. This can save on storage and communication costs.

2. Scalability: KZG commitments can be efficiently computed and verified for large polynomials, making them suitable for scenarios involving a large number of commitments.

3. Hiding property: KZG commitments hide the committed value within the polynomial coefficients. Without knowledge of the polynomial coefficients, it is computationally difficult to determine the committed value. This property is crucial for maintaining the integrity of the commitment.

4. Flexibility: KZG commitments can be easily integrated into various cryptographic protocols, allowing for the construction of more complex systems such as zero-knowledge proofs, range proofs, and verifiable computation.

### References and further reading
1. Merkling in Ethereum: https://blog.ethereum.org/2015/11/15/merkling-in-ethereum
2. Merkle Tree diagram: https://en.wikipedia.org/wiki/Merkle_tree#/media/File:Hash_Tree.svg
3. Condrieu : A verkle tree testnet demo: https://www.youtube.com/watch?v=cPLHFBeC0Vg
4. Why it's so important to go stateless: https://dankradfeist.de/ethereum/2021/02/14/why-stateless.html
5. Vector Commitment Techniques and Applications to Verifiable Decentralized Storage: https://www.youtube.com/watch?v=MFJMWA0Pk1s
6. Verkle Trees by John Kuszmaul https://math.mit.edu/research/highschool/primes/materials/2018/Kuszmaul.pdf
7. Darkrad's blog: https://dankradfeist.de/ethereum/2021/06/18/verkle-trie-for-eth1.html
8. Lecture 10.2: Cryptographic Commitments: https://www.youtube.com/watch?v=IkNZWJFcfcU
9. BLS12-381 algorithm: https://hackmd.io/@benjaminion/bls12-381