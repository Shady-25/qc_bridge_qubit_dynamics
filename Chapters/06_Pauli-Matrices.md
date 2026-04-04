---
header-includes:
  - \usepackage{braket}
---

# Pauli Matrices

*Fundamental operators for two‑level quantum systems*

Two‑level quantum systems require operators acting on a two‑dimensional Hilbert space. The most general Hermitian operator on $\mathbb{C^2}$ contains four real parameters.

The identity matrix and the three Pauli matrices form a complete, orthogonal basis for this space. Because of this, Pauli matrices appear naturally in the description of qubits, spin‑½ particles, and any two‑state quantum system.

## Why Pauli matrices appear in two-level systems

A general Hermitian $2 \times 2$ operator has the form:

$$H=
\left(
\begin{array}{cc}
a & c \\
c^* & b
\end{array}
\right)
, \quad\quad a,b \in \mathbb{R}, \quad c\in \mathbb{C}
$$

This operator contains four real degrees of freedom. The following four matrices form a complete basis:

$$ I, \quad \sigma_x, \quad \sigma_y, \quad \sigma_z.$$

This decomposition will become essential when describing **qubit Hamiltonians**, **Bloch sphere geometry**, and **single‑qubit gates**.

## Definition of the Pauli matrices

$$\sigma_x=
\left(
\begin{array}{cc}
0 & 1 \\
1 & 0
\end{array}
\right), \quad 
\sigma_y=
\left(
\begin{array}{cc}
0 & -i \\
i & 0
\end{array}
\right), \quad
\sigma_z=
\left(
\begin{array}{cc}
1 & 0 \\
0 & -1
\end{array}
\right).$$

These matrices are:
* Hermitian
* Unitary
* Traceless
* Determinant=-1
* Involutive:${\sigma_i}^2$= $I$

They represent the three fundemental directions in the state space of a qubit.

## Measurement bases associated with Pauli matrices

Each Pauli matrix corresponds to a measurement in a specific orthonormal basis:
* $\sigma_z$:computational basis 

$$\ket 0, \quad \ket 1.$$
* $\sigma_x$: symmetric/anti-symmetric superpositions 

$$\ket += \frac{\ket 0 + \ket 1}{\sqrt{2}}.$$
* $\sigma_y$: superpositions with a relative phase 

$$\ket \pm= \frac{\ket 0 \pm i \ket 1}{\sqrt{2}}.$$

These three axes will become the $x$, $y$ and $z$ directions of the Bloch sphere.

## Commutation and anti‑commutation: a brief conceptual window

### Commutator

$$[A,B]=AB - BA$$

The commutator measures whether two operations influence each other.
If $[A,B] \neq 0$, **the order of operations matters**. For Pauli matrices: 

$$[\sigma_i , \sigma_j]= 2i \epsilon_{ijk} \sigma_k .$$

This structure is identical to the algebra of angular momentum in quantum mechanics.

### Anti-commutator

$$\lbrace A,B \rbrace= AB + BA$$

Pauli matrices satisfy:

$$\lbrace \sigma_i , \sigma_j \rbrace= 2 \delta_{ij} I.$$

Consequences:
* If i $\neq j$, the matrices anti-commute $\to$ algebraic orthogonality.

* If $i=j$, we obtain $\sigma_i ^2=I$.
This orthogonality ensures that Pauli matrices form a complete basis for Hermitian operators on $\mathbb{C}^2$.

## Connection to quantum angular momentum

The angular momentum operators satisfy:

$$[L_x,L_y]=i\hbar L_z$$

and cyclic permutations. For a spin ‑½ particle:

$$S_x=\frac{\hbar}{2} \sigma_x, \quad S_y=\frac{\hbar}{2} \sigma_y, \quad S_z=\frac{\hbar}{2} \sigma_z.$$

Using the Pauli commutation relation: $[\sigma_x, \sigma_y]= 2i \sigma_z$, we obtain:

$$[S_x,S_y]=i \hbar S_z.$$

This shows that Pauli matrices realize the angular momentum algebra in the smallest possible representation. This is why they describe spin ‑½ systems and why qubit dynamics resemble rotations in three‑dimensional space.

A concrete example:
Rotating a spin‑½ state around the x‑axis and then the y‑axis gives a different result than rotating around y first and then x. This non‑commutativity is encoded directly in the Pauli commutators.

## Eigenvalues and eigenstates

Each Pauli matrix has eigenvalues:

$$ \lambda= +1,-1.$$

The corresponding eigenstates define the fundamental measurement directions:

* $\sigma_z: \ket 0 , \ket 1$
* $\sigma_x: \ket + , \ket -$
* $\sigma_y: \ket {+i} , \ket {-i}$

These will become the poles and equatorial axes of the Bloch sphere.

## Role of Pauli matrices in qubit dynamics

Any qubit Hamiltonian can be written as:

$$H= a_0 I + \vec{a}. \vec{\sigma}.$$

The term $a_0 I$ contributes only a global phase. The vector $\vec{a}$ determines the actual dynamics. The time evolution operator is:

$$U(t)= e^{-iHt/\hbar}=e^{-i(\vec{a}.\vec{\sigma})t/\hbar}.$$

This exponential describes a rotation of the qubit state around the axis $\vec{a}$ on the Bloch sphere.

This geometric interpretation will be developed in the next chapters.
