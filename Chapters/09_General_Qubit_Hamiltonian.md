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

The term $a_0 I$ only contributes a **global phase**:

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

The key algebraic fact is:.

$$(\hat{n}.\vec{\sigma})^2=I.$$

for any unit vector $\hat n$.

This follows from the Pauli algebra and the fact that $|\hat{n}|=1$.

Using this, the exponential can be written exactly as:

$$U(t)=\cos(\Omega t)I - i \sin(\Omega t) \hat n .\vec \sigma.$$

This is the standard form of a **rotation operator** in the spin‑½ representation.

On the Bloch sphere, it corresponds to a rotation of the Bloch vector around the axis $\hat n$ with angular frequency $\Omega$.

