# Pauli Matrices

*Fundamental operators for two‑level quantum systems*

Two‑level quantum systems require operators acting on a two‑dimensional Hilbert space. The most general Hermitian operator on $C^2$ contains four real parameters.

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

This decomposition will become essential when describing *qubit Hamiltonians**, **Bloch sphere geometry**, and **single‑qubit gates**.

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
* Involutive:$\sigma_{i}^2=I$

They represent the three fundemental directions in the state space of a qubit.

## Measurement bases associated with Pauli matrices

Each Pauli matrix corresponds to a measurement in a specific orthonormal basis:
* $\sigma_z$:computational basis 
$$\ket 0, \quad \ket 1.$$
* $\sigma_y$: symmetric/anti-symmetric superpositions 
$$\ket += \frac{\ket 0 + \ket 1}{\sqrt{2}}.$$
* $\sigma_y$: superpositions with a relative phase 
$$\ket \pm= \frac{\ket 0 \pm i \ket 1}{\sqrt{2}}.$$

These three axes will become the $x$, $y$ and $z$ directions of the Bloch sphere.
