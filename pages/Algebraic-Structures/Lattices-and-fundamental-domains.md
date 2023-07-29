### Analogy

Before we start, please note that fundamental domains aren't strictly defined. We will go with a general definition.

Imagine a garden with flowers planted in a regular, repeating pattern. The lattice represents the way these flowers are arranged, forming a grid-like structure throughout the garden. However, the lattice does not have to follow the direction of the garden's slope; it can have its own orientation and spacing.

Now, consider a smaller section of the garden that contains a representative sample of the flower pattern. This smaller section can be a unique and self-contained shape, like a flowerbed or a specific arrangement of flowers. This smaller section represents the fundamental domain.

The fundamental domain is not restricted to align with the lattice's basis vectors. It can have its own orientation and shape within the larger garden, as long as it captures the essence of the lattice's repeating pattern. When you replicate and translate this fundamental domain through the lattice (like shifting and copying the flowerbed across the garden), it will cover the entire garden without leaving any gaps or overlaps.

### Formal Definition

**Understanding Orbits**: An orbit is a fundamental concept in the study of group actions. Given a group $G$ acting on a set $\mathcal{X}$, the orbit of an element $x \in \mathcal{X}$ under this group action is the set of all elements obtained by applying the group elements to $x$. In other words, it is the collection of all possible images of $x$ under the action of the group. (An orbit in math is similar to an orbit in astronomy, which is the path of a celestial body around another celestial body under the influence of gravity.)

Formally, the orbit of $x \in \mathcal{X}$, denoted as $\mathcal{O}_x$ or simply $\mathcal{O}(x)$, is defined as:

$\mathcal{O}_x = \{ \Phi(g, x) \mid g \in G \}$

where $\Phi: G \times \mathcal{X} \rightarrow \mathcal{X}$ represents the group action, and $\Phi(g, x)$ is the result of applying the group element $g$ to the element $x$.

It is important to note that an orbit is a subset of the set $\mathcal{X}$, and it depends on both the element $x$ and the group $G$ and its action. The size of the orbit can vary; it can be finite, countably infinite, or uncountably infinite, depending on the nature of the group action and the set $\mathcal{X}$.

In the context of lattices and the geometric realization of orbits, the orbit of a lattice point $x_0$ will be the set of all lattice points that can be obtained by applying the group of symmetries to $x_0$. The fundamental domain, as previously defined, contains exactly one representative from each distinct orbit, thereby partitioning the lattice into a collection of non-overlapping fundamental domains, each corresponding to a unique orbit under the lattice symmetry group action.

![Lattice and Fundamental Domain](/images/lattice-and-fd.png)
