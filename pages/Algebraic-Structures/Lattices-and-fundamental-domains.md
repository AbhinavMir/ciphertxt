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

![orbit](/images/orbit.gif)

In the animation above, you can see that the blue object is moving away from red in a certain path, following a certain law. Now from where, work back to the formal definition and see if you understand it.



![Lattice and Fundamental Domain](/images/lattice-and-fd.png)

In the context of lattices, let's consider a topological space $\mathcal{X}$ equipped with a group action of a group $G$. We denote this action as $\Phi: G \times \mathcal{X} \rightarrow \mathcal{X}$, where $\Phi(g, x)$ represents the action of group element $g \in G$ on the point $x \in \mathcal{X}$.

Given a point $x_0 \in \mathcal{X}$, we can form the orbit of $x_0$ under the group action as follows:

$\text{Orbit of } x_0: \mathcal{O}_{x_0} = \{ \Phi(g, x_0) \mid g \in G \}$

Now, we define a fundamental domain (or fundamental region) $\mathcal{F}$ for this group action as a subset of $\mathcal{X}$ that contains exactly one representative point from each distinct orbit. In other words:

$\forall x \in \mathcal{X}, \exists g \in G \text{ such that } \Phi(g, x_0) = x \iff x \in \mathcal{F}$

In mathematical terms, the fundamental domain $\mathcal{F}$ can be expressed as:

$\mathcal{F} = \{ x \in \mathcal{X} \mid \exists g \in G \text{ such that } \Phi(g, x_0) = x \}$

It is essential to note that the fundamental domain $\mathcal{F}$ provides a geometric realization for the set of representatives of the orbits of the group action. It allows us to study the action of $G$ on $\mathcal{X}$ by considering only a representative from each orbit, simplifying the analysis of the group action.

In the context of lattices, the group $G$ would typically be a group of transformations preserving the lattice structure (e.g., translations, rotations, reflections). The space $\mathcal{X}$ would then be the lattice itself, and the action of $G$ on $\mathcal{X}$ would represent the lattice symmetries. The fundamental domain would give us a unique and representative portion of the lattice, capturing its essential structure, while all other points on the lattice can be obtained by applying group elements from $G$ to points in the fundamental domain.