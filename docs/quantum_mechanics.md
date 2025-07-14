# Quantum Mechanics Foundations

This page provides a comprehensive introduction to the quantum mechanics principles underlying QE-KGR. Understanding these concepts is crucial for effectively using quantum entangled knowledge graphs.

## 🌊 Quantum Mechanics Basics

### Wave-Particle Duality

Quantum mechanics reveals that particles exhibit both wave and particle properties. In QE-KGR, knowledge entities are represented as quantum states that can exist in superposition - simultaneously embodying multiple characteristics.

```python
import numpy as np
from qekgr import EntangledGraph

# A node can be in superposition of multiple states
graph = EntangledGraph(hilbert_dim=4)

# Superposition state: 60% physicist + 40% engineer
superposition_state = np.array([0.6, 0.4, 0.0, 0.0]) 
node = graph.add_quantum_node("Alex", state=superposition_state)

print(f"State amplitudes: {node.state_vector}")
print(f"Probabilities: {np.abs(node.state_vector)**2}")
```

### Quantum Superposition

**Mathematical Foundation:**
A quantum state |ψ⟩ can be written as a linear combination of basis states:

$$|\psi\rangle = \alpha|0\rangle + \beta|1\rangle + \gamma|2\rangle + \delta|3\rangle$$

where $|\alpha|^2 + |\beta|^2 + |\gamma|^2 + |\delta|^2 = 1$ (normalization condition).

**In QE-KGR:**

```python
# Create superposition of entity types
alpha, beta, gamma, delta = 0.5, 0.5, 0.5, 0.5
# Normalize
norm = np.sqrt(alpha**2 + beta**2 + gamma**2 + delta**2)
superposition = np.array([alpha, beta, gamma, delta]) / norm

entity = graph.add_quantum_node("Entity", state=superposition)
print(f"Entity exists in superposition: {entity.state_vector}")
```

### Quantum Entanglement

**Definition:** Quantum entanglement occurs when particles become correlated such that the quantum state of each particle cannot be described independently.

**Mathematical Representation:**
For two entangled qubits:
$$|\psi\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$$

**In Knowledge Graphs:**

```python
# Create entangled relationship
graph.add_entangled_edge("Alice", "Bob",
                        relations=["collaborates", "friends", "co-authors"],
                        amplitudes=[0.8, 0.6, 0.4])

# The relationship exists in quantum superposition
# When measured, it collapses to one specific relation
edge = graph.edges[("Alice", "Bob")]
measured_relation = edge.collapse_relation()
print(f"Measured relation: {measured_relation}")
```

## 🎯 Quantum States in Knowledge Representation

### Pure States vs Mixed States

**Pure State:** Complete quantum information, represented by state vector |ψ⟩

```python
# Pure state - complete information
pure_state = np.array([1.0, 0.0, 0.0, 0.0])  # Definitely in state |0⟩
node_pure = graph.add_quantum_node("PureEntity", state=pure_state)
print(f"Entropy (pure): {node_pure.measure_entropy():.3f}")  # Should be 0
```

**Mixed State:** Incomplete information, represented by density matrix ρ

```python
# Mixed state - statistical mixture
# 70% probability |0⟩, 30% probability |1⟩
p0, p1 = 0.7, 0.3
density_matrix = p0 * np.outer([1,0,0,0], [1,0,0,0]) + p1 * np.outer([0,1,0,0], [0,1,0,0])

node_mixed = graph.add_quantum_node("MixedEntity", state=None)
node_mixed.density_matrix = density_matrix
print(f"Entropy (mixed): {node_mixed.measure_entropy():.3f}")  # > 0
```

### Hilbert Space Representation

**Hilbert Space:** Complex vector space with inner product, where quantum states live.

**Dimensionality in QE-KGR:**

- **2D:** Binary characteristics (yes/no, active/inactive)
- **4D:** Quaternary states (4 distinct entity types)
- **8D:** Octal representation (richer quantum effects)
- **16D+:** High-dimensional semantic embeddings

```python
# Different Hilbert space dimensions
binary_graph = EntangledGraph(hilbert_dim=2)     # Simple binary states
quaternary_graph = EntangledGraph(hilbert_dim=4) # Quaternary states  
complex_graph = EntangledGraph(hilbert_dim=8)    # Rich quantum effects

print(f"State space sizes: {2**1}, {2**2}, {2**3}")
```

### Bloch Sphere Representation (2D Case)

For 2-dimensional Hilbert space, quantum states can be visualized on the Bloch sphere:

$$|\psi\rangle = \cos(\theta/2)|0\rangle + e^{i\phi}\sin(\theta/2)|1\rangle$$

```python
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def bloch_sphere_coordinates(state_vector):
    """Convert 2D quantum state to Bloch sphere coordinates."""
    if len(state_vector) != 2:
        raise ValueError("Bloch sphere only for 2D states")
    
    alpha, beta = state_vector[0], state_vector[1]
    
    # Bloch sphere coordinates
    x = 2 * np.real(alpha * np.conj(beta))
    y = 2 * np.imag(alpha * np.conj(beta))
    z = np.abs(alpha)**2 - np.abs(beta)**2
    
    return x, y, z

# Example: Entity in superposition
theta = np.pi/3  # 60 degrees
entity_state = np.array([np.cos(theta/2), np.sin(theta/2)])
x, y, z = bloch_sphere_coordinates(entity_state)

print(f"Bloch coordinates: ({x:.3f}, {y:.3f}, {z:.3f})")
```

## ⚛️ Quantum Operations in Graphs

### Quantum Gates and Unitary Operations

**Unitary Evolution:** Quantum states evolve through unitary transformations U:
$$|\psi'⟩ = U|\psi⟩$$

**Common Quantum Gates:**

```python
# Pauli-X gate (bit flip)
pauli_x = np.array([[0, 1], [1, 0]])

# Pauli-Y gate
pauli_y = np.array([[0, -1j], [1j, 0]])

# Pauli-Z gate (phase flip)
pauli_z = np.array([[1, 0], [0, -1]])

# Hadamard gate (creates superposition)
hadamard = np.array([[1, 1], [1, -1]]) / np.sqrt(2)

# Apply Hadamard to create superposition
initial_state = np.array([1, 0])  # |0⟩
superposition = hadamard @ initial_state
print(f"After Hadamard: {superposition}")  # (|0⟩ + |1⟩)/√2
```

### Quantum Measurements

**Born Rule:** Probability of measuring state |φ⟩ in state |ψ⟩ is |⟨φ|ψ⟩|²

```python
def measure_state(state_vector, measurement_basis):
    """Measure quantum state in given basis."""
    probabilities = np.abs(np.dot(measurement_basis.conj(), state_vector))**2
    # Collapse state (measurement)
    outcome = np.random.choice(len(probabilities), p=probabilities)
    collapsed_state = measurement_basis[:, outcome]
    return outcome, collapsed_state, probabilities

# Example measurement
state = np.array([0.6, 0.8])  # Normalized superposition
computational_basis = np.eye(2)  # |0⟩, |1⟩ basis

outcome, collapsed, probs = measure_state(state, computational_basis)
print(f"Measurement outcome: {outcome}")
print(f"Collapsed state: {collapsed}")
print(f"Probabilities: {probs}")
```

## 🔗 Quantum Entanglement Theory

### Bell States

**Maximally Entangled States:**
$$|\Phi^+\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$$
$$|\Phi^-\rangle = \frac{1}{\sqrt{2}}(|00\rangle - |11\rangle)$$
$$|\Psi^+\rangle = \frac{1}{\sqrt{2}}(|01\rangle + |10\rangle)$$
$$|\Psi^-\rangle = \frac{1}{\sqrt{2}}(|01\rangle - |10\rangle)$$

```python
# Create Bell state between two entities
def create_bell_state(graph, node1_id, node2_id, bell_type="phi_plus"):
    """Create maximally entangled Bell state between two nodes."""
    
    bell_states = {
        "phi_plus": np.array([1, 0, 0, 1]) / np.sqrt(2),
        "phi_minus": np.array([1, 0, 0, -1]) / np.sqrt(2),
        "psi_plus": np.array([0, 1, 1, 0]) / np.sqrt(2),
        "psi_minus": np.array([0, 1, -1, 0]) / np.sqrt(2)
    }
    
    entangled_state = bell_states[bell_type]
    
    # Add maximally entangled edge
    graph.add_entangled_edge(node1_id, node2_id,
                           relations=["quantum_correlated"],
                           amplitudes=[1.0])
    
    return entangled_state

# Create Bell pair
bell_state = create_bell_state(graph, "Alice", "Bob", "phi_plus")
print(f"Bell state: {bell_state}")
```

### Entanglement Entropy

**Von Neumann Entropy:** Measure of entanglement in quantum states
$$S(\rho) = -\text{Tr}(\rho \log_2 \rho)$$

```python
def von_neumann_entropy(density_matrix):
    """Calculate von Neumann entropy of quantum state."""
    eigenvalues = np.linalg.eigvals(density_matrix)
    # Remove zero eigenvalues to avoid log(0)
    nonzero_eigenvals = eigenvalues[eigenvalues > 1e-12]
    entropy = -np.sum(nonzero_eigenvals * np.log2(nonzero_eigenvals))
    return entropy

# Compare entropies
pure_state_rho = np.outer([1,0], [1,0])  # |0⟩⟨0|
mixed_state_rho = 0.5 * np.outer([1,0], [1,0]) + 0.5 * np.outer([0,1], [0,1])

print(f"Pure state entropy: {von_neumann_entropy(pure_state_rho):.3f}")
print(f"Mixed state entropy: {von_neumann_entropy(mixed_state_rho):.3f}")
```

### Schmidt Decomposition

For bipartite systems, any pure state can be written as:
$$|\psi\rangle = \sum_i \sqrt{\lambda_i} |i_A\rangle \otimes |i_B\rangle$$

```python
def schmidt_decomposition(bipartite_state, dim_A, dim_B):
    """Perform Schmidt decomposition of bipartite quantum state."""
    # Reshape state vector into matrix
    state_matrix = bipartite_state.reshape(dim_A, dim_B)
    
    # Singular Value Decomposition
    U, s, Vh = np.linalg.svd(state_matrix)
    
    # Schmidt coefficients are singular values
    schmidt_coeffs = s
    
    # Schmidt rank (number of non-zero coefficients)
    schmidt_rank = np.sum(s > 1e-12)
    
    return schmidt_coeffs, schmidt_rank, U, Vh

# Example: Entangled state
entangled_state = np.array([1, 0, 0, 1]) / np.sqrt(2)  # Bell state
coeffs, rank, U, Vh = schmidt_decomposition(entangled_state, 2, 2)

print(f"Schmidt coefficients: {coeffs}")
print(f"Schmidt rank: {rank}")
print(f"Entanglement: {'Yes' if rank > 1 else 'No'}")
```

## 🌊 Quantum Interference

### Constructive and Destructive Interference

**Amplitude Addition:** When quantum paths combine, amplitudes add:
$$A_{total} = A_1 + A_2$$

**Probability:** $P = |A_{total}|^2 = |A_1 + A_2|^2$

```python
def quantum_interference_demo():
    """Demonstrate quantum interference effects."""
    
    # Two quantum paths with different phases
    amplitude_1 = 0.7 * np.exp(1j * 0)        # Path 1: real amplitude
    amplitude_2 = 0.7 * np.exp(1j * np.pi)    # Path 2: opposite phase
    
    # Constructive interference (same phase)
    constructive = amplitude_1 + amplitude_1
    prob_constructive = np.abs(constructive)**2
    
    # Destructive interference (opposite phases)
    destructive = amplitude_1 + amplitude_2
    prob_destructive = np.abs(destructive)**2
    
    print(f"Constructive interference probability: {prob_constructive:.3f}")
    print(f"Destructive interference probability: {prob_destructive:.3f}")
    
    return constructive, destructive

constructive, destructive = quantum_interference_demo()
```

### Interference in Quantum Walks

```python
from qekgr import QuantumInference

def analyze_quantum_walk_interference(graph):
    """Analyze interference patterns in quantum walks."""
    
    inference = QuantumInference(graph)
    
    # Perform quantum walk
    walk_result = inference.quantum_walk("Alice", steps=10)
    
    # Analyze interference pattern
    interference = walk_result.interference_pattern
    
    # Find constructive interference peaks
    mean_amplitude = np.mean(np.abs(interference))
    constructive_nodes = np.where(np.abs(interference) > 1.5 * mean_amplitude)[0]
    
    print(f"Constructive interference at nodes: {constructive_nodes}")
    print(f"Mean amplitude: {mean_amplitude:.3f}")
    print(f"Max interference: {np.max(np.abs(interference)):.3f}")
    
    return interference

# Analyze interference in your graph
interference_pattern = analyze_quantum_walk_interference(graph)
```

## 📊 Quantum Information Theory

### Quantum Mutual Information

**Classical Mutual Information:** $I(A:B) = H(A) + H(B) - H(A,B)$

**Quantum Mutual Information:** $I(\rho_{AB}) = S(\rho_A) + S(\rho_B) - S(\rho_{AB})$

```python
def quantum_mutual_information(joint_density_matrix, dim_A, dim_B):
    """Calculate quantum mutual information between subsystems."""
    
    # Partial traces to get reduced density matrices
    rho_A = partial_trace(joint_density_matrix, dim_B, 'B')
    rho_B = partial_trace(joint_density_matrix, dim_A, 'A') 
    
    # Von Neumann entropies
    S_A = von_neumann_entropy(rho_A)
    S_B = von_neumann_entropy(rho_B)
    S_AB = von_neumann_entropy(joint_density_matrix)
    
    # Quantum mutual information
    I_AB = S_A + S_B - S_AB
    
    return I_AB

def partial_trace(rho, dim_trace_out, subsystem):
    """Compute partial trace of density matrix."""
    if subsystem == 'A':
        # Trace out subsystem A
        dim_keep = rho.shape[0] // dim_trace_out
        rho_B = np.zeros((dim_keep, dim_keep), dtype=complex)
        for i in range(dim_trace_out):
            rho_B += rho[i*dim_keep:(i+1)*dim_keep, i*dim_keep:(i+1)*dim_keep]
        return rho_B
    else:
        # Trace out subsystem B  
        dim_keep = rho.shape[0] // dim_trace_out
        rho_A = np.zeros((dim_keep, dim_keep), dtype=complex)
        for i in range(dim_keep):
            for j in range(dim_keep):
                for k in range(dim_trace_out):
                    rho_A[i,j] += rho[i*dim_trace_out + k, j*dim_trace_out + k]
        return rho_A
```

### Quantum Discord

**Quantum Discord:** Measures quantum correlations beyond entanglement
$$\mathcal{D}(\rho_{AB}) = I(\rho_{AB}) - \max_{\{M_k\}} I(\rho_{AB}|\{M_k\})$$

```python
def quantum_discord_approximation(joint_state, dim_A, dim_B):
    """Approximate quantum discord calculation."""
    
    # This is a simplified approximation
    # Full calculation requires optimization over all possible measurements
    
    joint_rho = np.outer(joint_state, joint_state.conj())
    
    # Quantum mutual information
    I_quantum = quantum_mutual_information(joint_rho, dim_A, dim_B)
    
    # Classical mutual information (approximation using computational basis)
    I_classical = classical_mutual_information_approx(joint_rho, dim_A, dim_B)
    
    # Discord approximation
    discord = I_quantum - I_classical
    
    return max(0, discord)  # Discord is non-negative

def classical_mutual_information_approx(joint_rho, dim_A, dim_B):
    """Approximate classical mutual information."""
    # This is simplified - full calculation requires optimization
    # Here we use computational basis measurement
    
    # Extract probabilities from diagonal elements
    probs_joint = np.diag(joint_rho).real
    
    # Marginal probabilities
    probs_A = np.zeros(dim_A)
    probs_B = np.zeros(dim_B) 
    
    for i in range(dim_A):
        for j in range(dim_B):
            idx = i * dim_B + j
            probs_A[i] += probs_joint[idx]
            probs_B[j] += probs_joint[idx]
    
    # Classical mutual information calculation
    I_classical = 0
    for i in range(dim_A):
        for j in range(dim_B):
            idx = i * dim_B + j
            if probs_joint[idx] > 0 and probs_A[i] > 0 and probs_B[j] > 0:
                I_classical += probs_joint[idx] * np.log2(probs_joint[idx] / (probs_A[i] * probs_B[j]))
    
    return I_classical
```

## 🔄 Quantum Decoherence

### Environmental Interaction

**Decoherence:** Loss of quantum coherence due to environmental interaction

**Master Equation:**
$$\frac{d\rho}{dt} = -\frac{i}{\hbar}[H, \rho] + \mathcal{L}[\rho]$$

where $\mathcal{L}[\rho]$ is the Lindblad superoperator describing decoherence.

```python
def simulate_decoherence(initial_state, decoherence_rate, time_steps):
    """Simulate quantum decoherence over time."""
    
    state = initial_state.copy()
    density_matrix = np.outer(state, state.conj())
    
    # Time evolution with decoherence
    dt = 0.1
    coherence_trace = []
    
    for t in range(time_steps):
        # Decoherence: exponential decay of off-diagonal elements
        for i in range(len(state)):
            for j in range(len(state)):
                if i != j:  # Off-diagonal elements
                    density_matrix[i,j] *= np.exp(-decoherence_rate * dt)
        
        # Measure coherence (sum of off-diagonal elements)
        coherence = np.sum(np.abs(density_matrix - np.diag(np.diag(density_matrix))))
        coherence_trace.append(coherence)
    
    return density_matrix, coherence_trace

# Simulate decoherence of superposition state
superposition = np.array([1, 1]) / np.sqrt(2)
final_state, coherence = simulate_decoherence(superposition, decoherence_rate=0.1, time_steps=50)

print(f"Initial coherence: {coherence[0]:.3f}")
print(f"Final coherence: {coherence[-1]:.3f}")
```

## 🎯 Applications in Knowledge Graphs

### Quantum-Enhanced Entity Resolution

```python
def quantum_entity_resolution(graph, entity1, entity2):
    """Use quantum overlap to determine if entities are the same."""
    
    node1 = graph.nodes[entity1]
    node2 = graph.nodes[entity2] 
    
    # Quantum state overlap
    overlap = np.abs(np.vdot(node1.state_vector, node2.state_vector))**2
    
    # Metadata similarity (classical)
    metadata_sim = jaccard_similarity(node1.metadata, node2.metadata)
    
    # Combined quantum-classical similarity
    similarity = 0.7 * overlap + 0.3 * metadata_sim
    
    return similarity, overlap, metadata_sim

def jaccard_similarity(dict1, dict2):
    """Calculate Jaccard similarity between two dictionaries."""
    set1 = set(str(v) for v in dict1.values())
    set2 = set(str(v) for v in dict2.values())
    
    intersection = len(set1 & set2)
    union = len(set1 | set2)
    
    return intersection / union if union > 0 else 0

# Example usage
similarity, q_overlap, c_similarity = quantum_entity_resolution(graph, "Alice", "Bob")
print(f"Total similarity: {similarity:.3f}")
print(f"Quantum overlap: {q_overlap:.3f}")
print(f"Classical similarity: {c_similarity:.3f}")
```

### Quantum Link Prediction

```python
def quantum_link_prediction(graph, source, target):
    """Predict link probability using quantum interference."""
    
    # Find all paths between source and target
    paths = find_quantum_paths(graph, source, target, max_length=4)
    
    # Calculate quantum amplitudes for each path
    total_amplitude = 0
    for path in paths:
        path_amplitude = calculate_path_amplitude(graph, path)
        total_amplitude += path_amplitude
    
    # Link probability from quantum amplitude
    link_probability = np.abs(total_amplitude)**2
    
    return link_probability, paths

def find_quantum_paths(graph, source, target, max_length):
    """Find all quantum paths between two nodes."""
    # Simplified implementation - use networkx for path finding
    import networkx as nx
    
    classical_graph = graph._graph  # NetworkX representation
    try:
        paths = list(nx.all_simple_paths(classical_graph, source, target, max_length))
        return paths[:10]  # Limit to first 10 paths
    except nx.NetworkXNoPath:
        return []

def calculate_path_amplitude(graph, path):
    """Calculate quantum amplitude along a path."""
    amplitude = 1.0 + 0j
    
    for i in range(len(path) - 1):
        edge_key = (path[i], path[i+1])
        if edge_key in graph.edges:
            edge = graph.edges[edge_key]
            # Use mean amplitude of superposed relations
            edge_amplitude = np.mean(edge.amplitudes)
            amplitude *= edge_amplitude
        else:
            amplitude *= 0.1  # Small amplitude for missing edges
    
    return amplitude

# Predict missing link
prob, paths = quantum_link_prediction(graph, "Alice", "Charlie")
print(f"Link prediction probability: {prob:.3f}")
print(f"Found {len(paths)} quantum paths")
```

## 📚 Further Reading

### Textbooks

- **Nielsen & Chuang**: "Quantum Computation and Quantum Information"
- **Preskill**: "Lecture Notes on Quantum Computation"
- **Wilde**: "Quantum Information Theory"

### Research Papers

- **Quantum Walks**: "Quantum walks and search algorithms" (Shenvi et al.)
- **Quantum Machine Learning**: "Quantum advantage in learning" (Liu et al.)
- **Graph Theory**: "Spectral Graph Theory" (Chung)

### Online Resources

- [Qiskit Textbook](https://qiskit.org/textbook/)
- [Quantum Computing for Computer Scientists](https://www.cambridge.org/core/books/quantum-computing/8AEA723BEE5CC9F5C03FDD4BA850C711)
- [Quantum Algorithm Zoo](https://quantumalgorithmzoo.org/)

---

Understanding these quantum mechanics foundations will greatly enhance your ability to design and interpret quantum entangled knowledge graphs. The interplay between quantum superposition, entanglement, and interference creates powerful new possibilities for knowledge representation and reasoning! 🌊⚛️
