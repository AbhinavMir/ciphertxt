1. **Symmetric Key Encryption**

**Problem 1 [Perfect Secrecy] (10 Points)**



---

2. **Message Authentication Codes**

**Problem 4 [Message Authentication Codes] (10 Points)**

**(a)** To authenticate $$m = m_1 || m_2$$, $$m_1, m_2 \in \{0, 1\}^n$$, use the tag $$F_k(m_1) || F_k(m_2)$$.

**(b)** To authenticate $$m = m_1 || m_2$$, $$m_1, m_2 \in \{0, 1\}^{n-1}$$, use the tag $$F_k(0 || m_1) || F_k(1 || m_2)$$.

---

3. **Signatures**

**Problem 5 [Signatures] (10 Points)**

Let (Gen, Sign, Vrfy) be a multi-message UF-CMA secure digital signature scheme that can be used to sign messages of length $$n$$. Consider the following new scheme for signing messages of length $$2n$$.

**Gen':** Compute $$(sk_1, pk_1) \leftarrow Gen(1^n)$$ and $$(sk_2, pk_2) \leftarrow Gen(1^n)$$. Set $$sk = (sk_1, sk_2)$$ and $$pk = (pk_1, pk_2)$$. Output $$(sk, pk)$$.

**Sign'(m = m_1 || m_2, sk = sk_1 || sk_2):** Compute $$\sigma_1 \leftarrow Sign(m_1, sk_1)$$ and $$\sigma_2 \leftarrow Sign(m_2, sk_2)$$. Output $$\sigma = \sigma_1 || \sigma_2$$.

**Vrfy'(m = m_1 || m_2, \sigma, pk = pk_1 || pk_2):** Compute $$b_1 = Vrfy(\sigma_1, pk_1)$$ and $$b_2 = Vrfy(\sigma_2, pk_2)$$. Output $$b_1 \land b_2$$.

---

4. **Key Exchange**

**Problem 6 [Key Exchange] (10 Points)**

Alice chooses random exponents $$a_1, a_2$$ from $$\{0, 1\}^n$$ and sends $$a = a_1 \oplus a_2$$ to Bob. Bob chooses random exponents $$b_1, b_2$$ from $$\{0, 1\}^n$$ and sends $$b = b_1 \oplus b_2$$ to Alice. Both Alice and Bob compute the key $$k = g^{ab}$$, where $$g$$ is the generator of the group $$G$$. Alice sends $$Enc_k(m)$$ to Bob for some message $$m$$.

**Problem 7 [Man in the Middle] (15 Points)**

Consider the following protocol used by a Client and Server.

They have a shared group and generator pair $$(G, g)$$ where $$G$$ is the group and $$g \in G$$ is an element that generates the group. The computational Diffie-Hellman problem is hard in this group.

The client chooses a random exponent $$a$$ and sends $$g^a$$ to the server. The server chooses a random exponent $$b$$ and sends $$g^b$$ to the client. Both client and server compute the key $$k = g^{ab}$$. The client sends $$Enc_k(m)$$ to the server who can decrypt it since it has the key $$k$$.

**(a)** An eavesdropper, who may not tamper with messages, cannot learn anything beyond the public information exchanged in the protocol.

**(b)** An attacker with complete control over the channel can perform a man-in-the-middle attack by intercepting the communication without alerting either party. The attacker can relay messages between the client and server while establishing separate connections with each of them. This allows the attacker to read and modify messages as they pass through, potentially gaining access to sensitive information or injecting malicious content.
