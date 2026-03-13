# Quantum States

A quantum system is described by a **quantum state**, whose time evolution (for closed systems) is governed by the Schrödinger equation.

The Schrödinger equation involves a linear operator called the **Hamiltonian**.  
The eigenfunctions of the Hamiltonian are the **eigenstates** of the system, associated with definite energy values.

The state of a quantum system can be expressed as a **linear combination of eigenstates** of a chosen operator (for example, the Hamiltonian), provided that these eigenstates form a complete basis.

**RK:** The main difference between classical and quantum systems is **indeterminacy**.  
In quantum mechanics, even if the quantum state is perfectly known, the outcomes of measurements are generally probabilistic. A quantum system is therefore described by a **superposition of possible states**, and a measurement projects the state onto one of the possible outcomes (eigenstates of the measured observable).

Quantum states can be **pure** or **mixed**, and admit several representations.  
Pure quantum states are commonly represented as vectors in a **Hilbert space**.  
Mixed states are statistical mixtures of pure states and cannot be represented by a single vector; they are instead described using **density matrices**.

**Hilbert space:** A Hilbert space is a vector space equipped with a scalar product, which allows one to define norms and angles between vectors. It is a *complete* space, meaning that all convergent sequences of vectors have a limit inside the space.

Vectors are written using bra–ket notation:

- $\ket{\psi}$ : ket (column vector)  
- $\bra{\psi}$ : bra (row vector)

The scalar product between two states $\ket{\psi}$ and $\ket{\phi}$ is written as:

$\braket{\psi|\phi}$

This scalar product allows one to define:
- the **norm** of a state
- **probability amplitudes** associated with measurements

**Density matrix:** A density matrix is a mathematical representation of a quantum system that combines classical probabilities with quantum state vectors.

A quantum state is an abstract object, independent of any particular representation.  
In practice, a representation is obtained by choosing a basis, usually defined by the eigenstates of a given observable.

So, the same quantum states ( physics information) might be represented by different wave functions depending on the basis

For example, in standard quantum mechanics, the position representation leads to the wave function $\psi(x) = \langle x | \psi \rangle$.  
In other contexts, such as finite-dimensional systems ( which is the case in quantum computing), the quantum state is represented by a finite set of complex coefficients in a chosen basis: $\ket \psi = \sum_n C_n\ket n$, The $C_n$ coefficients are the representations of state in this particular basis.

At this stage, the quantum state is defined up to an overall normalization factor.  
The physical interpretation of the scalar product, together with the normalization condition and the measurement postulate, will be introduced in the next section.

