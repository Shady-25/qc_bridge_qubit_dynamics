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

! [Bloch_sphere](Images\Bloch_sphere.png)

