# Quantum Computing Learning Project — From Theory to Simulation  
### A self‑driven journey toward Master 2 in Quantum Information

---

## Motivation

My goal is to join the **Master 2 Quantum Information**  
To prepare myself seriously — and to demonstrate both motivation and technical maturity — I decided to build a structured project that reconstructs the foundations of quantum computing **from first principles**, both theoretically and numerically.

This repository is the result of several weeks of focused work, curiosity, and genuine passion for quantum technologies.  
It reflects my desire not only to *learn*, but to *understand deeply*, *simulate*, *visualize*, and *explain* quantum phenomena with clarity.

---

## Project Overview

The project is divided into two complementary parts:

---

# **Part I — Theoretical Foundations (10 Chapters)**  
Before writing a single line of code, I spent significant time building a **complete theoretical base** for single‑qubit quantum mechanics and quantum information.

These 10 chapters form a coherent mini‑course that I wrote for myself to ensure I truly understood the physics and mathematics behind qubits.

### **The 10 chapters cover:**

1. **Complex vector spaces & Dirac notation**  
2. **Qubit states, normalization, global vs relative phase**  
3. **Pauli matrices & observables**  
4. **Expectation values & measurement postulates**  
5. **Unitary evolution & Schrödinger equation**  
6. **Hamiltonians of two‑level systems**  
7. **Rotations on the Bloch sphere**  
8. **SU(2) and SO(3) correspondence**  
9. **Single‑qubit gates as rotations**  
10. **Geometric interpretation of quantum operations**

These chapters were essential for me: they allowed me to approach the coding part with confidence and a strong conceptual foundation.

---

# **Part II — Numerical Simulation (Jupyter Notebooks)**
**Note: All notebooks share a centralized utils.py module for core matrix mathematics and visualization functions, ensuring clean and reusable code.*

After building the theoretical base, I translated the concepts into **NumPy simulations** and **visualizations**.

---

### **1. Qubit Dynamics Under Hamiltonians**  
- Time evolution under Pauli Hamiltonians  
- Larmor precession  
- Expectation values of observables  
- Numerical simulation using matrix exponentials  
- Visual interpretation of qubit trajectories  

---

### **2. From State Vectors to the Bloch Sphere**  
- Pure states and normalization  
- Global vs relative phases  
- Bloch sphere parametrization  
- Conversion between state vectors and Bloch vectors  
- 3D visualization of quantum states  

---

### **3. Single‑Qubit Gates and Their Geometric Action**  
- Fundamental gates (X, Y, Z, H, S, T)  
- Rotation gates $R_x, R_y, R_z$  
- Action of gates on state vectors  
- Action of gates as rotations in SO(3)  
- Before/after visualization on the Bloch sphere  

---

### **4. (In Progress) Qiskit 1.x Introduction & Re-implementation**  
To complement the NumPy‑based theoretical work, I am now learning **Qiskit** to:

- prepare states  
- apply gates  
- simulate circuits  
- extract Bloch vectors  
- visualize states using Qiskit tools  
- re‑implement parts of the previous notebooks in a real QC framework  

This notebook will demonstrate my ability to transition from theory to practice — a crucial skill for M2 and beyond.

---

## What I Learned

Throughout this project, I strengthened my understanding of:

- the mathematical structure of qubits  
- the role of Hamiltonians in quantum dynamics  
- the geometry of quantum states  
- the SU(2) → SO(3) correspondence  
- the physical meaning of quantum gates  
- numerical simulation techniques  
- scientific visualization  
- clean code organization (with a shared `utils.py`)  

This project also helped me develop:

- autonomy in learning  
- scientific rigor  
- clarity in explanation  
- and a strong foundation for future work in quantum information

---

## Next Steps

- Complete the Qiskit repository  
- Reproduce Bloch sphere visualizations using Qiskit  
- Explore measurement and the Born rule  
- Study multi‑qubit systems and entanglement  
- Prepare for potential interviews by reviewing all notebooks  

---

##  About Me

I have a **Master 1 in Physics**, and I am deeply motivated to specialize in **quantum information and quantum technologies**.  

This project reflects my commitment to learning, my curiosity, and my desire to contribute to the field.

If you are reviewing this repository as part of my M2 application:  
**thank you for your time and consideration.**

I would be honored to continue this journey within your program.

---


