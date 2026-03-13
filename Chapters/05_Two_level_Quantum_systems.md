# Two‑Level Quantum Systems
*(The simplest non‑trivial quantum system)*

A two‑level quantum system is the simplest system that can exhibit all fundamental quantum phenomena:
superposition, interference, relative phases, and non‑trivial time evolution.

It is the minimal Hilbert space in which quantum mechanics becomes genuinely different from classical physics.

## Hilbert Space of a Two‑Level System

A two-level system is described by a Hilbert space of dimension 2: 

$$H \approxeq C^2$$

 We choose an orthonormal basis, often written as:

$$\ket0 \quad \quad, \quad \quad \ket 1$$

These basis states may represent:

* two energy levels of an atom (ground/excited)
*  spin-up & spin-down of a spin $\frac{-1}{2}$ particle
* two stable states of a superconducting qubit
* any physical system with exactly two  distinguishable states

A general pure state is a linear combination:

$$\ket \psi =\alpha\ket0 +\beta\ket1$$
with complex coefficients satisfiying the normalization condition:

$$\vert{\alpha}\vert^2 + \vert{\beta}\vert^2 = 1$$

As established earlier:

* the **global phase** of $\ket \psi$ is physically irrelevant
* the **relative phase** btween $\alpha$ & $\beta$ carries physical information

Thus, the physical content of a two-level state is encoded in:

* the probability amplitudes $|\alpha|$, $|\beta|$
* the relative phase between the two components

## Energy Eigenbasis

Often, the two basis states correspond to two energy eigenstates:

$$H\ket0 =E_0 \ket0, \quad\quad H\ket1 =E_1\ket1$$

In  this basis, the Hamiltonian is diagonal:

$$H=\begin{pmatrix} E_0 & 0 \\ 0 & E_1 \end{pmatrix}$$

If the system is prepared in an energy eigenstate, its time evolution is simple:

$$\ket{0(t)}= e^{-iE_0 t/\hbar}\ket0, \quad\quad \ket{1(t)}= e^{-iE_1 t/\hbar}\ket1$$

Each eigenstate acquires only a phase factor.

No transitions occur between the two levels.

## Superpositions and Relative Phase Evolution

If the initial state is a superposition:

$$\ket \psi =\alpha\ket0 +\beta\ket1$$

Then at time t:

$$\ket{\psi(t)} =\alpha e^{-iE_0 t/\hbar}\ket0 +\beta e^{-iE_1 t/\hbar}\ket1$$

The **relative phase** evolves as:

$$\Delta{\phi(t)}=\frac{(E_1 -E_0)t}{\hbar}$$

This time‑dependent phase difference leads to interference effects when measuring in any basis different from {$\ket0,\ket1$}.

Thus, even without transitions between levels, a two‑level system already exhibits non‑trivial dynamics.

## General Hamiltonian for a Two‑Level System

The most general Hamiltonian acting on a two‑dimensional Hilbert space is a 2×2 **Hermitian matrix:**

$$H=\begin{pmatrix} a & b \\ c^* & b \end{pmatrix};\quad\quad a,b \in R, c \in C.$$

* The diagonal terms $a$ and $b$ correspond to the energies of $\ket0$ and $\ket1$
* The *off-diagonal* term $c$ represents a **coupling** between the two states

If $c=0$, the system has no transitions between levels

If $c \not = 0$, the Hamiltonian mixes the two states, and the system can oscillate between them.

This is the simplest example of quantum transitions.

## Coupled Two-level system: basic dynamics.

Consider a Hamiltonian with real coupling:

$$H=\begin{pmatrix} E_0 & V \\ V & E_1 \end{pmatrix}; \quad V\in R$$

This Hamiltonian is no longer diagonal in the $\ket 0$, $\ket 1$ basis.

The true  energy eigenstates are linear combinations of $\ket 0$ and $\ket 1$.

Diagonalizing $H$ gives two eigenvalues:

$$E_{\pm} =\frac{E_0 +E_1}{2} \pm \sqrt{\left(\frac{E_1 -E_0}{2}\right)^2 + V^2}$$

The corresponding eigenstates are superpositions of $\ket 0$ and $\ket 1$.

If the system starts in $\ket 0$, the time evolution leads to **oscillations** between $\ket 0$ and $\ket 1$.

this phenomenon is the simplest form of coherent population transfer.

The oscillation frequency is determined by the energy splitting:

$$\Omega = \frac{E_+ -E_-}{\hbar}$$

This is the origin of **Rabi oscillations**, which will be studied in more detail later.

## Why Two-Level Systems Matter

Two‑level systems are fundamental because:

* they are mathematically simple

* they capture all essential quantum behavior

* they form the basis of quantum information theory

* any qubit is a two‑level system

* any finite‑dimensional system can be decomposed into two‑level subsystems

In quantum computing, the states $\ket 0$ and $\ket 1$ become the logical states of a **qubit**.

