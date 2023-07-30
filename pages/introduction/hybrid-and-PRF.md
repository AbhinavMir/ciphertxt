---
title: Hybrid Arguments and PRFs
type: posts
---

- One-Way Function (OWF): A function that is easy to compute but difficult to reverse.

- One-Way Permutation (OWP): A one-to-one function that is easy to compute but difficult to reverse.

- Pseudo-Random Function (PRF): A function that is indistinguishable from a random function.

- A hardcore bit for a one-way function is a bit in the function's output that is computationally hard to predict given its input but can be efficiently verified.

### Hybrid Arguments and applications

Hybrid argument, much like induction, is a pr2oof technique to prove that two distributions are computaionally indistinguishable. Why would you need such a proof? Turns out, cryptographic primitives (especially one proof we will talk about later) depend on such proof mechanisms.

To put it down more formally, assume two distributions exist, $D_1$ and $D_2$. Let us assume these two distributions are computationally indistinguable (this is a starting assumption). From here, we can define a hybrid distribution such that $D_1 := H_0, H_1, ..., H_k =: D_2$, where $k$ is an upperbound we don't have to worry about right now.

Assume now, that there exists an interpolation $D_i$ such that as $i$ is (reasonably) small and as it increases, we go from $D_1$ to $D_2$. 

Next assumption we can do is assume there is a probablistic efficieint algorithm $A$ (An algorithm that run in polynomial time and are allowed to use randomness in their computations). The advantage of A in distinguishing $D_1$ from $D_2$ is given by the following expression.

$Adv(A) = \left| \Pr[A(x) = 1, x \text{ sampled from } D_1] - \Pr[A(x) = 1, x \text{ sampled from } D_2] \right|$


In simpler terms, the advantage of $A$ measures how much better $A$ can distinguish between samples drawn from $D_1$ and $D_2$ compared to a random guess. If $Adv(A)$ is close to 0, it means $A$ cannot distinguish between $D_1$ and $D_2$ better than random chance, indicating that the two distributions are computationally indistinguishable. Conversely, if $Adv(A)$ is significantly greater than 0, it implies that $A$ can successfully distinguish between $D_1$ and $D_2$, suggesting that the two distributions are not computationally indistinguishable.

In the following image you can see two distributions (here visualised as true and pseudo randomness), and they start to become indistinguishable as we move "forward" in the values.

![Hybrid Arguments](/images/hybrid-distribution.png)

### Let's prove a corollary using hybrid arguments

**Corollary 81.7:** Let $f$ be a one-way permutation (OWP) and $h$ a hard core bit for $f$. Then the function $G(x) = h(x) \| h(f(x)) \| h(f^{(2)}(x)) \| \ldots \| h(f^{(n)}(x))$ is a pseudorandom generator (PRG).

**Proof by intuition**

1. Hybrid 0: Start with a truly random string R_0.
2. Hybrid 1: Replace the last bit of R_0 with h(f(x)). Since h is a hard core bit, Hybrid 1 is computationally indistinguishable from Hybrid 0.
3. Hybrid 2: Replace the last two bits of R_0 with h(f(x)) \| h(f^{(2)}(x)). Since h is a hard core bit and f is a one-way permutation, Hybrid 2 is computationally indistinguishable from Hybrid 1.
4. Continue this process up to Hybrid n, where $G(x) = h(x) \| h(f(x)) \| h(f^{(2)}(x)) \| ... \| h(f^{(n)}(x))$.
5. Since each step only introduces a small change to the distribution, G(x) is computationally indistinguishable from a truly random string.
6. Therefore, G(x) is a pseudorandom generator (PRG) based on the assumption that f is a one-way permutation and h is a hard core bit for f.

The formal proof is found in the reference.

[Problem](/Problem-Sets/hybrid-and-prf)

### Reference
Corollary 81.7 in [Pass' A course in cryptography](https://www.cs.cornell.edu/courses/cs4830/2010fa/lecnotes.pdf)
[Lecture Notes](https://web.archive.org/web/20210506221743/https://kodu.ut.ee/~peeter_l/teaching/krprot08s/hybridarg.pdf)