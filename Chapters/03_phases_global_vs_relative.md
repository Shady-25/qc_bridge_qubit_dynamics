# Complex Coefficients, and Phases  
*(Conceptual Foundations before Time Evolution)*

This section aims to clarify **why quantum states are described using complex coefficients**, what **phases** mean physically, and how this naturally leads to **unitary transformations** and the **Hamiltonian**, *before* introducing time evolution explicitly.

In quantum mechanics, a **quantum state** is a mathematical object that allows us to **predict probabilities of measurement outcomes**.

Consider a system with two possible outcomes for a given measurement:

$\ket{u_1} \quad,\quad \ket{u_2}$

A general state is written as:
$\ket{\psi} = c_1 \ket{u_1} + c_2 \ket{u_2}$

At this stage:
- $c_1$ and $c_2$ are numbers called **probability amplitudes**
- The state is a **superposition** of possible outcomes

According to **Born’s rule**:
$P(u_1) = |c_1|^2 \quad, \quad P(u_2) = |c_2|^2$

This correctly gives measurement probabilities.

However, **probabilities alone do not fully characterize the quantum state**.  
Different states may yield the same probabilities for one measurement, but produce different results when measuring another observable.

Therefore, the state must contain **more information than probabilities alone**.

The most general form of the coefficients is:$\quad$
$c_1 = |c_1| e^{i\theta_1}, \quad c_2 = |c_2| e^{i\theta_2}$

The probabilities depend only on the magnitudes:
$|c_1|^2,\quad |c_2|^2$

But the **phases** $\theta_1, \theta_2$ carry additional information about the state.

We can factor out a common phase:
$\ket{\psi} = e^{i\theta_1}
\left(
|c_1| \ket{u_1} + |c_2| e^{i(\theta_2 - \theta_1)} \ket{u_2}\right)$

Any measurable probability is of the form:
$|\braket{\phi | \psi}|^2$

The global phase factor $e^{i\theta_1}$ always cancels out.

**Conclusion:**  
Two states that differ only by a global phase represent the **same physical state**.

The remaining phase difference:
$\Delta\theta = \theta_2 - \theta_1$

is called the **relative phase**.

Example:

$\ket{\psi_1} = \frac{1}{\sqrt{2}} (\ket{u_1} + \ket{u_2})$

$\ket{\psi_2} = \frac{1}{\sqrt{2}} (\ket{u_1} - \ket{u_2})$

These states:
- have identical probabilities in the $\ket{u_1}, \ket{u_2}$ basis
- are physically **distinct**

In another measurement basis, they yield different outcomes due to **interference terms**.

**Relative phases affect measurable quantities.**

But why are these coefficients complex numbers?
Because:
- phases must vary **continuously**
- interference effects depend on smooth phase changes
- probabilities are computed using modulus squared

Complex numbers are the **minimal mathematical structure** that allows:
- amplitudes and phases
- continuous transformations
- consistent probabilistic interpretation

This is not a convention, but a **physical necessity**.

From the above, we conclude:
- A quantum state is a **normalized vector** in a complex vector space
- States differing by a global phase are physically identical

This leads naturally to the concept of **projective Hilbert space**.

Suppose the state undergoes some transformation:
$\ket{\psi} \rightarrow \ket{\psi'}$

This transformation must:
- preserve normalization
- preserve probabilities
- preserve relative phases

The only linear transformations with these properties are **unitary operators**:

$\ket{\psi'} = U \ket{\psi} \quad, \quad U^\dagger U = I$

Thus, **unitarity is not postulated arbitrarily** — it is imposed by the structure of quantum states and measurements.

Any continuous unitary transformation can be written as:
$U(t) = e^{-iHt/\hbar}$

where:
- $H$ is a Hermitian operator
- $H$ generates changes in relative phases

This operator is called the **Hamiltonian**.

**Key idea:**  

The Hamiltonian emerges as the generator of physically meaningful phase evolution, not merely as an energy operator.

---

## Conceptual Summary

- Quantum states require more than probabilities → phases are essential
- Global phase is unobservable
- Relative phases encode physical information
- Complex numbers are unavoidable
- Valid state transformations must be unitary
- The Hamiltonian generates unitary evolution by controlling phase relations

---

This framework prepares the ground for understanding **time-independent Schrödinger equations, stationary states, and quantum dynamics**, which will be introduced in the next section.


---
 For a two-level system, this structure is exactly what defines a qubit, whose physical information is entirely encoded in probability amplitudes and relative phases.
 ---