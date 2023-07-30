---
title: Hybrid Arguments and PRFs
type: posts
---

### Hybrid Arguments and applications

Hybrid argument, much like induction, is a pr2oof technique to prove that two distributions are computaionally indistinguishable. Why would you need such a proof? Turns out, cryptographic primitives (especially one proof we will talk about later) depend on such proof mechanisms.

To put it down more formally, assume two distributions exist, $D_1$ and $D_2$. Let us assume these two distributions are computationally indistinguable (this is a starting assumption). From here, we can define a hybrid distribution such that $D_1 := H_0, H_1, ..., H_k =: D_2$, where $k$ is an upperbound we don't have to worry about right now.

Assume now, that there exists an interpolation $D_i$ such that as $i$ is (reasonably) small and as it increases, we go from $D_1$ to $D_2$. 

Next assumption we can do is assume there is a probablistic efficieint algorithm $A$ (An algorithm that run in polynomial time and are allowed to use randomness in their computations). The advantage of A in distinguishing $D_1$ from $D_2$ is given by the following expression.

$Adv(A) = \left| \Pr[A(x) = 1, x \text{ sampled from } D_1] - \Pr[A(x) = 1, x \text{ sampled from } D_2] \right|$


In simpler terms, the advantage of $A$ measures how much better $A$ can distinguish between samples drawn from $D_1$ and $D_2$ compared to a random guess. If $Adv(A)$ is close to 0, it means $A$ cannot distinguish between $D_1$ and $D_2$ better than random chance, indicating that the two distributions are computationally indistinguishable. Conversely, if $Adv(A)$ is significantly greater than 0, it implies that $A$ can successfully distinguish between $D_1$ and $D_2$, suggesting that the two distributions are not computationally indistinguishable.
![Hybrid Arguments](/images/hybrid-distribution.png)

### Reference
Corollary 81.7 in [Pass' A course in cryptography](https://www.cs.cornell.edu/courses/cs4830/2010fa/lecnotes.pdf)