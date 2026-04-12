---
header-includes:
  - \usepackage{braket}
---

# General Qubit Hamiltonian

*From abstract matrices to rotations on the Bloch sphere*

In previous chapters, we introduced:

* Pauli matrices as the fundamental operators for two‑level systems

* The qubit as a state on the Bloch sphere

* The geometric representation of pure states

In this chapter, we connect these ideas to dynamics.
We show that the most general Hamiltonian of a qubit generates a rotation of the Bloch vector around some axis in space.
This is the core of real quantum control and quantum computing.

## General form of a qubit Hamiltonian

Any Hermitian $2 \times 2$ operator can be written as:

$$H= a_0 I + a_x \sigma_x + a_y \sigma_y + a_z \sigma_z = a_0 I + \vec{a}.\vec{\sigma}$$

Where:

* $a_0 \in \mathbb{R}$

* $\vec{a} = (a_x,a_y,a_z) \in \mathbb{R^3}$

* $\vec{\sigma} =(\sigma_x,\sigma_y,\sigma_z)$

This is the most general Hamiltonian for a single qubit.

The time evolution operator is:

$$U(t)= e^{-iH t /\hbar}$$

The term $a_0 I$ only contributes a **global phase**, and therefore does not affect any observable:

$$e^{-i (a_0 I)t/\hbar}=e^{-i a_0 t/\hbar} I$$

which has no physical effect on measurement probabilities.

Therefore, the physically relevant part of the Hamiltonian is:

$$H'=\vec{a}.\vec{\sigma}$$

From now on, we focus on this term.

## Geometric interpretation: $\vec{a}$ as a rotation axis

The Pauli matrices correspond to the three axes of the Bloch sphere:

* $\sigma_x$ $\to$ $x-axis$

* $\sigma_y$ $\to$ $y-axis$

* $\sigma_z$ $\to$ $z-axis$

The combination:

$$\vec{a}.\vec{\sigma}= a_x\sigma_x + a_y\sigma_y + a_z\sigma_z$$

is therefore associated with a direction in 3D space.

We define:

$$\hat{n}=\frac{\vec{a}}{|\vec{a}|} \quad,\quad \Omega=\frac{|\vec{a}|}{\hbar}.$$

Then:

$$H'=\vec{a}.\vec{\sigma}=\hbar\Omega\hat{n}.\vec{\sigma}$$

The unit vector $\hat{n}$  is the **axis of rotation** on the Bloch sphere.

The scalar $\Omega$ is the **rotation frequency**.

## Exponential of the Hamiltonian: why it is a rotation

The time evolution operator is:

$$U(t)= e^{-iH't /\hbar}=e^{-i \Omega t \hat{n}.\sigma}$$

The key algebraic fact is:

$$(\hat{n}.\vec{\sigma})^2=I.$$

for any unit vector $\hat n$.

This follows from the Pauli algebra and the fact that $|\hat{n}|=1$.

Using this, the exponential can be written exactly as:

$$U(t)=\cos(\Omega t)I - i \sin(\Omega t) \hat n .\vec \sigma.$$

This is the standard form of a **rotation operator** in the spin‑½ representation.

On the Bloch sphere, it corresponds to a rotation of the Bloch vector around the axis $\hat n$ with angular frequency $\Omega$.

## Examples: Hamiltonian proportional to $\sigma$ axis

### i. Hamiltonian proportional to $\sigma_z$

Consider:

$$H=\frac{\hbar w}{2}\sigma_z$$

Then:

$$U(t)=e^{-i H t/\hbar}=e^{-i(w t/2)\sigma_z}=\cos(wt/2)I - i\sin(wt/2)\sigma_z$$

We know:

$$\sigma_z \ket 0 = + \ket 0 \quad,\quad \sigma_z \ket 1 = - \ket 1$$

So:

$$U(t) \ket 0 =e^{-iwt/2} \ket 0 \quad,\quad U(t) \ket 1 =e^{+iwt/2} \ket 1$$

For a general state:

$$\ket{\psi(0)}= \alpha \ket 0 + \beta \ket 1$$

We obtain:

$$\ket{\psi(t)}= \alpha e^{-i w t/2} \ket 0 + \beta e^{+i w t  /2} \ket 1.$$

* The populations $|\alpha|^2$ and $|\beta|^2$ remain constant.

* Only the **relative phase** between $\ket 0$ and $\ket 1$ changes.

* On the Bloch sphere, this is a **rotation around the z‑axis**.

This type of Hamiltonian appears, for example, for a spin‑½ in a static magnetic field along z.

### ii. Hamiltonian proportional to $\sigma_x$

Consider:

$$H=\frac{\hbar \Omega}{2} \sigma_x$$

Then:

$$U(t)= e^{-i H t/\hbar}= e^{-i (\Omega t/2) \sigma_x} =\cos{(\frac{\Omega t}{2})} I -i \sin(\frac{\Omega t}{2}) \sigma_x$$

Using:

$$\sigma_x \ket 0 = \ket 1 \quad,\quad \sigma_x \ket 1 = \ket 0$$

We find:

$$U(t) \ket 0= \cos(\frac{\Omega t}{2})\ket 0 -i\sin({\frac{\Omega t}{2}}) \ket 1$$

$$U(t) \ket 1= \cos(\frac{\Omega t}{2})\ket 1 -i\sin({\frac{\Omega t}{2}}) \ket 0$$

If the system starts in $\ket 0$, then:

$$\ket{\psi(t)}= \cos(\frac{\Omega t}{2}) \ket 0 - i\sin(\frac{\Omega t}{2}) \ket 1$$

The probability to find the system in $\ket 1$ at time $t$ is:

$$P_{0 \to t}(t)=|\braket{1|\psi(t)}|^2 =\sin^2 (\frac{\Omega t}{2}).$$

This describes **Rabi oscillations** (to be more explained later) between $\ket 0$ and $\ket 1$

On the Bloch sphere:

* the Bloch vector rotates around the x‑axis

* the populations oscillate between the north and south poles

This type of Hamiltonian appears when a qubit is driven by a resonant field that couples $\ket 0$ and $\ket 1$.

### iii. Hamiltonian proportional to $\sigma_y$

Consider:

$$H=\frac{\hbar \Omega}{2} \sigma_y$$

Then:

$$U(t)= e^{-i H t/\hbar}= e^{-i (\Omega t/2) \sigma_y} =\cos{(\frac{\Omega t}{2})} I -i \sin(\frac{\Omega t}{2}) \sigma_y$$

Using:

$$\sigma_y \ket 0 = i \ket 1 \quad,\quad \sigma_y \ket 1 = -i \ket 0$$

We find:

$$U(t) \ket 0= \cos(\frac{\Omega t}{2})\ket 0 + \sin({\frac{\Omega t}{2}}) \ket 1$$

$$U(t) \ket 1= \cos(\frac{\Omega t}{2})\ket 1 + \sin({\frac{\Omega t}{2}}) \ket 0$$

If the system starts in $\ket 0$, then:

$$\ket{\psi(t)}= \cos(\frac{\Omega t}{2}) \ket 0 + \sin(\frac{\Omega t}{2}) \ket 1$$

The probabilities are:

$$P(0,t)= \cos^2(\frac{\Omega t}{2}) \quad,\quad P(1,t)= \sin^2(\frac{\Omega t}{2})$$

Again, we see oscillations between $\ket 0$ and $\ket 1$, but with a different phase structure compared to the $\sigma_x$ case.

On the Bloch sphere:

* The Bloch vector rotates around the y‑axis

* Both amplitude and phase evolve in a specific way

In the next chapter, we will interpret these rotations explicitly as quantum gates and connect them to the standard gate set used in quantum computing.