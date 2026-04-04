# Bloch Sphere
*Geometric representation of a qubit state*

A qubit is a two‑level quantum system.

Although its state is described by complex amplitudes, the physical degrees of freedom reduce to two real parameters.
This remarkable simplification allows us to represent any pure qubit state as a point on a sphere: the Bloch sphere.

This chapter introduces the Bloch sphere, explains how a qubit state maps to a point on it, and shows how measurement directions correspond to axes on the sphere.

## Why a Geometric Representation

A general qubit state is:

$$\ket \psi= \alpha \ket0 +\beta \ket1, \quad\quad |\alpha|^2 +|\beta|^2=1.$$

At first sight, this seems to require four real parameters (two complex numbers).

But:

* normalization removes one parameter

* global phase removes another

A qubit therefore has two real degrees of freedom.

Two real parameters $\to$ a point on a sphere.

This is the origin of the **Bloch sphere**

***The Bloch sphere is the exact geometric space of pure qubit states.*** 

## Canonical Parametrization $\to$ Coordinates on a sphere

From chapter 07, any qubit state can be written as:

$$\ket\psi=\cos{\frac{\theta}{2}} \ket0 +e^{i\phi} \sin{\frac{\theta}{2}}\ket1 .$$

with:

$$0 \leq \theta \leq \pi \quad,\quad 0\leq \phi \leq 2\pi.$$

These two angles are precisely the spherical coordinates of a point on the unit sphere.

We define the **Bloch vector**:

$$\vec{r}=(\sin\theta \cos\phi, \sin\theta \sin\phi, \cos\theta).$$

This vector lies on the unit sphere:

$$|\vec r| =1.$$

Thus, every pure qubit state corresponds to a unique point on the Bloch sphere.

![Bloch_sphere](image.png "Bloch Sphere" )

## Pauli Matrices Define the Axes

The three Pauli matrices introduced in Chapter 06 correspond to the three coordinate axes of the Bloch sphere:

* $\sigma_z$ $\to$ $z$-axis
* $\sigma_x$ $\to$ $x$-axis
* $\sigma_y$ $\to$ $y$-axis

Their eigenstates are the six cardinal points:

**Z-axis**

$$\ket0 \leftrightarrow (0,0,1) \quad,\quad \ket1 \leftrightarrow (0,0,-1).$$

**X-axis**

$$\ket+ =\frac{\ket0 + \ket1}{\sqrt2} \leftrightarrow (1,0,0) \quad, \quad \ket- =\frac{\ket0 - \ket1}{\sqrt2} \leftrightarrow (-1,0,0).$$

**Y-axis**

$$\ket{+i} =\frac{\ket0 + i\ket1}{\sqrt2} \leftrightarrow (0,1,0) \quad, \quad \ket{-i} =\frac{\ket0 - i\ket1}{\sqrt2} \leftrightarrow (0,-1,0).$$

This is the geometric meaning of the Pauli matrices:
they define the fundamental measurement directions of the qubit.

## Measurement on the Bloch Sphere

Measurement does not depend on the representation.
It depends on the basis, which corresponds to choosing an axis on the sphere.

### i. Measurement in the $\sigma_z$ basis

This is the computational basis:

* outcome 0 $\longrightarrow$ projection onto the noth pole

* outcome 1 $\longrightarrow$ projection onto the south pole

Probabilties:

$$P(0)=\frac{1+\cos\theta}{2} \quad,\quad P(1)=\frac{1-\cos\theta}{2}.$$

### ii. Measurement in the $\sigma_x$ basis

This corresponds to projecting onto the x‑axis:

$$P(+)=\frac{1+\sin\theta \cos\phi}{2} \quad,\quad P(-)=\frac{1-\sin\theta \cos\phi}{2}.$$

### iii. Measurement in the $\sigma_y$ basis

Projectio onto the y-axis

$$P(+i)=\frac{1+\sin\theta \sin\phi}{2} \quad,\quad P(-i)=\frac{1-\sin\theta \sin\phi}{2}.$$

## What Does "Measuring in a Different Basis" Mean

This is a crucial conceptual point.

* The system is the same.

* The state is the same.

* What changes is the question you ask.

Measuring in different bases corresponds to:

* rotating the measurement apparatus

* choosing a different axis on the Bloch sphere

* projecting the same Bloch vector onto a different direction

This is exactly like measuring the spin of an electron along different axes.

**The qubit does not change. Only the orientation of the measurement changes.**

## Why the Bloch Sphere is powerful

The Bloch sphere provides:

* a geometric representation of qubit states

* a visual interpretation of relative phase

* a clear picture of measurement directions

* a natural way to understand qubit rotations

* a foundation for quantum gates and control

In the next chapter, we will see that the general qubit Hamiltonian:

$$H= a_0 I + \vec{a}.\vec{\sigma}$$

generates a rotation of the Bloch vector around the axis $\vec{a}$.

This geometric interpretation is the heart of qubit dynamics.

