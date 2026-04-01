# Qubit Definition

*Structure and physical meaning of a two‑level quantum system*

A **qubit** is the fundamental unit of quantum information.

* Mathematically, it is a quantum system whose state lives in a **two‑dimensional Hilbert space**.

* Physically, it is any system that has **exactly two distinguishable states**.

examples include:

* spin ‑½ particles.
* two energy levels of an atom
* polarization of a photon
* superconducting qubits

In this chapter, we formalize what a qubit is, how its state is represented, and how measurements act on it.

## State Space of a Qubit

A qubit is described by a normalized vector in a 2‑dimensional Hilbert space:

$$\ket \psi= \alpha \ket0 +\beta \ket1, \quad\quad |\alpha|^2 +|\beta|^2=1.$$

The states $\ket 0$ and $\ket 1$ form the **computational basis**, which is the standard basis used in quantum information.

They are typically chosen as the eigenstates of $\sigma_z$:

$$\sigma_z \ket0=+\ket0;\quad \sigma_z \ket1=-\ket1.$$

**This basis plays the same role as the classical bit values 0 and 1.**

## Global Phase and Physical Degrees of Freedom

A qubit state is defined up to a global phase:

$$\ket\psi \thicksim e^{i\gamma}\ket\psi.$$

This phase has no physical effect on any measurement outcome. Combined with normalization, this means that a **qubit has two real degrees of freedom**.

This is why the state of a qubit can be represented as a point on a sphere (the Bloch sphere), which will be introduced in the next chapter.

## Canonical Parametrization of a Qubit

Because a qubit has only two physical degrees of freedom, we can parametrize its state using two angles $\theta$ and $\phi$:

$$\ket\psi=\cos{\frac{\theta}{2}} \ket0 +e^{i\phi} \sin{\frac{\theta}{2}}\ket1 .$$

with:

$$0 \leq \theta \leq \pi \quad,\quad 0\leq \phi \leq 2\pi.$$

### Why this parametrization?

Start from the general state:

$$\ket \psi= \alpha \ket0 +\beta \ket1$$

Write the amplitudes in polar form:

$$\alpha = |\alpha| \quad, \quad \beta=e^{i\phi}|\beta|$$

Normalization gives:

$$|\alpha|^2 +|\beta|^2=1.$$

So we can set:

$$|\alpha| =\cos{\frac{\theta}{2}} \quad,\quad |\beta| =\sin{\frac{\theta}{2}}.$$

This parametrization:

* automatically enforces normalization
* isolates the relative phase $e^{i\phi}$
* uses exactly two real parameters $\to$ the physical degrees of freedom

**This is the natural coordinate system for qubit states.**

## Measurement of a Qubit

Measurement is the process that extracts classical information from a quantum state.
It is inherently probabilistic and **depends on the basis** in which the measurement is performed.

### i. Measurement in the computational basis

Given:

$$\ket \psi= \alpha \ket0 +\beta \ket1$$

A measurement in the $\lbrace \ket0,\ket1 \rbrace$,basis :

* outcome 0 with probability $|\alpha|^2$
* outcome 1 with probability $|\beta|^2$

After the measurement, the state collapses to the corresponding eigenstate.

This is the quantum analogue of reading a classical bit.

### ii. Measurement in a different basis

A qubit can also be measured in other bases, such as:

$\sigma_x$ basis:

$$\ket+= \frac{\ket0 + \ket1}{\sqrt2} \quad, \quad \ket-= \frac{\ket0 - \ket1}{\sqrt2}.$$

$\to$ Probabilities $\to$

$$P(+)=|\braket{+|\psi}|^2 \quad, \quad P(-)=|\braket{-|\psi}|^2$$

$\sigma_y$ basis:

$$\ket{+i}= \frac{\ket0 + i\ket1}{\sqrt2} \quad, \quad \ket{-i}= \frac{\ket0 - i\ket1}{\sqrt2}.$$

$\to$ Probabilities $\to$

$$P(+i)=|\braket{+i|\psi}|^2 \quad, \quad P(-i)=|\braket{-i|\psi}|^2$$

### iii. What does “measuring in a different basis” mean physically?

It does not mean the system changes.

It means we choose a different question to ask the same system.

* Measurement in the $\sigma_z$ basis asks:

*“Is the qubit in* $\ket0$ *or* $\ket1$?"

* Measurement in the $\sigma_x$ basis asks:

*"Is the qubit aligned or anti‑aligned with the x‑axis?"*

* Measurement in the $\sigma_y$ basis asks:

*"Is the qubit aligned or anti‑aligned with the y‑axis?"*

The system is the same.
The measurement apparatus is oriented differently.

This is exactly like measuring the spin of an electron along different axes.

### iv. Why do different bases give different probabilities?

Because the qubit state has a relative phase and a population distribution that depend on the basis.

Example:

$$\ket{\psi_1}=\frac{\ket0 + \ket1}{\sqrt2} \quad ; \quad \ket{\psi_2}=\frac{\ket0 - \ket1}{\sqrt2}$$

In the $\sigma_z$ basis:

$P(0)=P(1)=1/2$ , for both states

But in the $\sigma_x$ basis:

$$\ket{\psi_1}=\ket+ \quad,\quad \ket{\psi_2}=\ket-$$

So

* $\psi_1$ gives outcome $+$ with probability $1$

* $\psi_2$ gives outcome $-$ with probability $1$

The difference comes entirely from the relative phase.

This is the essence of quantum interference.

## Why a Qubit Is Not a Classical Bit

A classical bit has only two states: 0 or 1.

A qubit has:

* infinitely many pure states

* continuous parameters $\theta$ & $\phi$

* basis‑dependent measurement outcomes

* non‑commuting observables

* interference effects

* collapse upon measurement

This richer structure is what gives quantum computing its power.

