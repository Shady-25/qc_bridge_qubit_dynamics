# Normalization & Measurement

To understand why we introduce the concept of **normalization** of a wave function, we first recall the **Born statistical interpretation**.

The Born rule provides the link between the mathematical formalism of quantum mechanics and experimental outcomes.  
Max Born proposed that the wave function does not represent a physical wave, but a **probability amplitude**. Specifically, the modulus squared of the wave function gives a probability density.

In the position representation, the probability density of finding a particle at position $ x $ and time $ t $ is given by:
$$
|\psi(x,t)|^2 = \psi^*(x,t)\psi(x,t).
$$

Since this quantity represents a probability density, it must satisfy:
$$
\int_{-\infty}^{\infty} |\psi(x,t)|^2 \, dx = 1.
$$

This condition is called the **normalization condition**.

A wave function may be a mathematical solution of the Schrödinger equation without representing a physical quantum state.  
To represent a physical state, it must also satisfy the Born probabilistic interpretation, and therefore be normalizable.

In other words, the physical content of quantum mechanics is not contained in the Schrödinger equation alone, but in its probabilistic interpretation.
