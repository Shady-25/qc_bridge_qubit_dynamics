---
header-includes:
  - \usepackage{braket}
---

# Normalization & Measurement

To understand why we introduce the concept of **normalization** of a wave function, we first recall the **Born statistical interpretation**.

The Born rule provides the link between the mathematical formalism of quantum mechanics and experimental outcomes.  
Max Born proposed that the wave function does not represent a physical wave, but a **probability amplitude**. Specifically, the modulus squared of the wave function gives a probability density.

In the position representation, the probability density of finding a particle at position $x$ and time $t$ is given by:
$$|\psi(x,t)|^2 = \psi^*(x,t)\psi(x,t).$$

Since this quantity represents a probability density, it must satisfy:
$$\int_{-\infty}^{\infty} |\psi(x,t)|^2 \, dx = 1$$

This condition is called the **normalization condition**.

A wave function may be a mathematical solution of the Schrödinger equation without representing a physical quantum state.  
To represent a physical state, it must also satisfy the Born probabilistic interpretation, and therefore be normalizable.

In other words, the physical content of quantum mechanics is not contained in the Schrödinger equation alone, but in its probabilistic interpretation.

## Born rule:

* In position space: $$P(x \in [a,b])= \int_{a}^{b} | \psi(x,t)|^2 dx$$
* In Hilbert space (If $\ket\phi$ corresponds to a possible measurement outcome) : $$P(\phi)=| \langle \phi | \psi \rangle |^2$$
* Probabilities must satisfy a normalization condition: $\sum{P}=1$ or $\int P=1$.

$\quad\quad\quad\quad$ for quantum state: $\langle \psi|\psi \rangle=1$.

## Born formalism in Hilbert space:

* A quantum state is a vector in Hilbert space: $\ket{\psi} \in H$.
* Probability of getting a pure state $\ket{a_n}$ of an **Observable** A is: $P(a_n)=|\langle a_n| \psi \rangle|^2$.

$\quad\quad\quad\quad$ An **observable** is represented by a Hermitian operator.

* Sum of all possible results gives: $\sum_n{|\langle a_n| \psi \rangle|^2}=\langle \psi|\psi \rangle=1$.

## Relation with measurement:

when we do a measurement:

* The possible results are the eingvalues of the operator.

* Probabilities are given by the Born rule.

* post-measurement state will be : $\ket{\psi}\longmapsto \frac{P_n \ket{\psi}}{\sqrt{\braket{\psi|P_n|\psi}}}$.

Where $P_n = |a_n\rangle\langle a_n|$ is the projector onto the eigenstate $|a_n\rangle$.


**RK: The post-measurement state is normalized by construction.**
