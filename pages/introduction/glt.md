---
title: The Goldreich-Levin Theorem
type: posts
---

**Objective of the theorem**: Find a hardcore predicate for a one-way function.

A hardcore predicate is a concept in cryptography that is related to the security of one-way functions. One-way functions are functions that are easy to compute in one direction but computationally difficult to invert. A hardcore predicate is a function that is hard to predict even when the value of the one-way function is known.

*Note*: In computational complexity theory, problems are classified into various complexity classes based on how efficiently they can be solved by algorithms. The polynomial hierarchy is a structure that extends the classes P and NP to higher levels of complexity.

The polynomial hierarchy is organized into levels: $\Sigma_0^P$, $\Pi_0^P$, $\Sigma_1^P$, $\Pi_1^P$, $\Sigma_2^P$, $\Pi_2^P$, and so on. Each level contains problems that are "harder" to solve than the levels below it. The third level of the polynomial hierarchy is represented as $\Sigma_3^P$ and $\Pi_3^P$.

**The Goldreich-Levin Theorem:** Let $f$ be a function from $\{0, 1\}^n$ to $\{0, 1\}$ such that there exists a nondeterministic finite automaton (NFA) $A$ with $n$ input bits and $s(n)$ states that accepts $x$ with probability $f(x)$, where $s(n)$ is a polynomial in $n$. Then, unless the polynomial hierarchy collapses to its third level, there is no efficient (i.e., polynomial-time) algorithm that approximates $f(x)$ significantly better than the trivial algorithm.

[under construction]


**Note**: I've been away for a while, very happy to announce [thoughtForest](https://www.thoughtforest.xyz/) is now live! 

### References
[Lecture 6: The Goldreich Levin Theorum by Pandey](https://www3.cs.stonybrook.edu/~omkant/S06.pdf)
