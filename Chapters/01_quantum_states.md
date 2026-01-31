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

