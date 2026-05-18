import numpy as np

# =========================================================
# Computational basis states
# =========================================================
ket_0 = np.array([[1], [0]], dtype=complex)
ket_1 = np.array([[0], [1]], dtype=complex)

# =========================================================
# Pauli matrices
# =========================================================
sigma_x = np.array([[0, 1],
                    [1, 0]], dtype=complex)

sigma_y = np.array([[0, -1j],
                    [1j,  0]], dtype=complex)

sigma_z = np.array([[1,  0],
                    [0, -1]], dtype=complex)

# =========================================================
# Bloch vector function
# =========================================================
def bloch_vector(psi):
    """Return the Bloch vector r = <psi|σ|psi>."""
    rx = np.real(psi.conj().T @ sigma_x @ psi)[0,0]
    ry = np.real(psi.conj().T @ sigma_y @ psi)[0,0]
    rz = np.real(psi.conj().T @ sigma_z @ psi)[0,0]
    return np.array([rx, ry, rz])

# =========================================================
# Optional: state from angles (useful for Bloch sphere)
# =========================================================
def state_from_angles(theta, phi):
    """Return |psi> = cos(theta/2)|0> + e^{i phi} sin(theta/2)|1>."""
    return np.array([
        [np.cos(theta/2)],
        [np.exp(1j * phi) * np.sin(theta/2)]
    ], dtype=complex)
