---
header-includes:
  - \usepackage{braket}
---

# Hamiltonian and time evolution in quantum system

*(Evolution in quantum systems)*

Classically, a system evolves because forces act upon it, positions and velocity changes under the effect of these forces. **But in quantum mechanics, what exactly evolves?**

A quantum state is a vector in Hilbert space
The fundamental object that describes a quantum system is the state vector $\ket{\psi(t)} \in H$. This vector contains all the information about the system.

So when we talk about “time evolution” in quantum mechanics, we mean:

**Time evolution = the state vector changes with time.**

However, normalization must be preserved all along system evolution, so the total probability remain equal to 1 at all times. 
$$\braket{\psi(t)|\psi(t)}=1 \quad\quad \forall t$$
If the evolution takes an initial state $\ket{\psi(0)}$ to a later state $\ket{\psi(t)}$ then for any two states $\ket\phi$ & $\ket\psi$:
$$\braket{\phi(0)|\psi(0)}= \braket{\phi(t)|\psi(t)}$$
Measurement probabilities depend on inner products, means that inner product is preserved.

The only transformations on a Hilbert space that preserve all inner products are unitary operators.

Thus, the most general form of time evolution is:
$$\ket{\psi(t)}=U(t)\ket{\psi(0)} \quad,\quad U(t)^\dagger U(t)=I$$

*This is the most fundemental and general statement about time evolution in quantum mechanics.*

Physics does not allow the state to “jump” discontinuously when time changes by an infinitesimal amount. So we require:

$$\lim\limits_{\Delta t \rightarrow 0} U(\Delta t)=I$$

 *"Small changes in time produce small changes in the state."*

Time evolution must satisfy:

$U(t_1)U(t_2)=U(t_1+t_2)$
because evolving for $t_1$ and then for $t_2$ is the same as evolving for $t_1 +t_2$. This is called a **one‑parameter unitary group.**

For finite-dimensional systems (which includes qubits), any continuous unitary one-parameter group has a Hermitian generator: "Any strongly continuous one‑parameter unitary group can be written as: $U(t)=e^{-iGt}$"

where $G$ is a unique self‑adjoint operator.

$$U^\dagger U=I$$

Differentiate this condition at $t=0$:

$$G^\dagger =G$$

That shows:

Hermiticity is required by probability conservation

With other words this theorem tells us that **unitarity + continuity + group structure** force the time evolution operator to be an exponential of some **Hermitian** operator.

Let’s call that operator $\frac{H}{\hbar} \rightarrow  \boxed{U(t)=e^{-iHt/\hbar}}$.

---

**The operator $H$ as generator of time evolution:**

By definition: ${U(t)=e^{-iHt/\hbar}}$

Differentiate at t=0:

$$\frac{d}{dt} U(t) |_{t=0} = \frac{-i}{\hbar} H$$

So:

$$H= i\hbar \frac{d}{dt} U(t) |_{t=0}$$

This shows:

### The Hamiltonian is the generator of infinitesimal time evolution.
*The Hamiltonian is not introduced as “energy” here.
It is first introduced as the generator required by unitarity and continuity.*

Deriving the Schrödinger equation

Start from:

$$\ket{\psi(t)}= U(t) \ket{\psi(0)}=e^{-iHt/\hbar} \ket{\psi(0)}$$

Differentiate with respect to time:

$$\frac{d}{dt} \ket{\psi(t)}=-\frac{i}{\hbar} H \ket{\psi(t)}$$

Multiply both sides by $i\hbar$:

$$\boxed{i\hbar \frac{d}{dt} \ket{\psi(t)}=H \ket{\psi(t)}}$$

This is the **time‑dependent Schrödinger equation.**

So, we've established that time evolutio in quantum mechanics is unitary: $U(t)=e^{-iHt/\hbar}$.

But why does the generator of time translations correspond to the physical quantity we call energy?

**For one:** Noether’s theorem states:

*"Every continuous symmetry corresponds to a conserved quantity."*

**For two :** The laws of nature do not depend on when you perform an experiment; This is called time translation invariance, and this symmetry must be represented in quantum mechanics by a unitary operator.

For time translation symmetry, the conserved quantity is **energy**.

In quantum mechanics, this means:

- the generator of time translations must be the operator whose expectation value is conserved,

- that operator is what we call the Hamiltonian 𝐻.

This is not a definition — it is a consequence of symmetry.

If $\ket{E_n}$ is an eigenstate of 𝐻,
$$H\ket{E_n}=E_n \ket{E_n}$$

then its time evolution is:
$$\ket{E_n(t)}=e^{-iE_n t/\hbar} \ket{E_n}$$

Each energy eigenstate rotates in the complex plane with **angular frequency:** $\omega_n=\frac{E_n}{\hbar}$

### Relation with relative phase:

If the state is a superposition:
$$\ket{\psi(0)}=c_1 \ket{E_1} + c_2 \ket{E_2}$$

at time t:

$$\ket{\psi(t)}=c_1 e^{-iE_1 t/\hbar}\ket{E_1} + c_2 e^{-iE_2 t/\hbar} \ket{E_2}$$

the relative phase is: $$\Delta \phi(t)=\frac{(E_2-E_1)t}{\hbar}$$

This relative phase changes in time because the two energies rotate at different frequencies.
