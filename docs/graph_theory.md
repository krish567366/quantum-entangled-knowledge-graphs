# Graph Theory Foundations

This document explores how classical graph theory extends into the quantum realm within QE-KGR. Understanding these graph-theoretic concepts is essential for effectively working with quantum entangled knowledge graphs.

## 📊 Classical Graph Theory Recap

### Basic Definitions

**Graph:** A mathematical structure G = (V, E) consisting of:

- **V**: Set of vertices (nodes)
- **E**: Set of edges (connections between nodes)

**Types of Graphs:**

- **Undirected**: Edges have no direction
- **Directed**: Edges have direction (source → target)
- **Weighted**: Edges have numerical weights
- **Multigraph**: Multiple edges between same node pair

```python
import networkx as nx
import numpy as np
from qekgr import EntangledGraph

# Classical graph representation
classical_graph = nx.Graph()
classical_graph.add_nodes_from(['Alice', 'Bob', 'Charlie'])
classical_graph.add_edges_from([('Alice', 'Bob'), ('Bob', 'Charlie')])

print(f"Classical graph: {classical_graph.number_of_nodes()} nodes, {classical_graph.number_of_edges()} edges")

# Quantum graph representation  
quantum_graph = EntangledGraph(hilbert_dim=4)
alice = quantum_graph.add_quantum_node("Alice", state="researcher")
bob = quantum_graph.add_quantum_node("Bob", state="professor") 
charlie = quantum_graph.add_quantum_node("Charlie", state="student")

quantum_graph.add_entangled_edge(alice, bob, relations=["collaborates"], amplitudes=[0.8])
quantum_graph.add_entangled_edge(bob, charlie, relations=["mentors"], amplitudes=[0.9])

print(f"Quantum graph: {len(quantum_graph.nodes)} nodes, {len(quantum_graph.edges)} edges")
```

### Graph Metrics

**Fundamental Metrics:**

- **Degree**: Number of edges connected to a node
- **Path Length**: Number of edges in shortest path between nodes
- **Clustering Coefficient**: Measure of local connectivity
- **Centrality**: Importance measures for nodes

```python
def classical_graph_metrics(graph):
    """Calculate classical graph theory metrics."""
    
    # Degree centrality
    degree_centrality = nx.degree_centrality(graph)
    
    # Betweenness centrality
    betweenness = nx.betweenness_centrality(graph)
    
    # Clustering coefficient
    clustering = nx.clustering(graph)
    
    # Average shortest path length
    if nx.is_connected(graph):
        avg_path_length = nx.average_shortest_path_length(graph)
    else:
        avg_path_length = float('inf')
    
    return {
        'degree_centrality': degree_centrality,
        'betweenness': betweenness,
        'clustering': clustering,
        'avg_path_length': avg_path_length
    }

# Example usage
metrics = classical_graph_metrics(classical_graph)
print(f"Degree centrality: {metrics['degree_centrality']}")
```

### Adjacency Matrix Representation

**Classical Adjacency Matrix:**
$$A_{ij} = \begin{cases}
1 & \text{if edge } (i,j) \text{ exists} \\
0 & \text{otherwise}
\end{cases}$$

**Weighted Adjacency Matrix:**
$$W_{ij} = \text{weight of edge } (i,j)$$

```python
def create_adjacency_matrix(graph_nodes, graph_edges):
    """Create adjacency matrix from graph structure."""
    n = len(graph_nodes)
    node_to_idx = {node: i for i, node in enumerate(graph_nodes)}
    # Initialize adjacency matrix
    adj_matrix = np.zeros((n, n))
    # Fill matrix based on edges
    for source, target in graph_edges:
        i, j = node_to_idx[source], node_to_idx[target]
        adj_matrix[i, j] = 1
        adj_matrix[j, i] = 1  # Undirected graph
    return adj_matrix, node_to_idx

# Example adjacency matrix
nodes = ['Alice', 'Bob', 'Charlie']
edges = [('Alice', 'Bob'), ('Bob', 'Charlie')]
adj_matrix, node_map = create_adjacency_matrix(nodes, edges)

print("Classical Adjacency Matrix:")
print(adj_matrix)
```

## ⚛️ Quantum Graph Theory

### Quantum Adjacency Matrix

In quantum graphs, the adjacency matrix becomes complex-valued with quantum amplitudes:

$$\mathcal{A}_{ij} = \sum_k \alpha_k e^{i\phi_k} |r_k\rangle$$

where $\alpha_k$ are amplitude weights and $|r_k\rangle$ represent relation types.

```python
def create_quantum_adjacency_matrix(quantum_graph):
    """Create quantum adjacency matrix with complex amplitudes."""
    nodes = list(quantum_graph.nodes.keys())
    n = len(nodes)
    node_to_idx = {node: i for i, node in enumerate(nodes)}
    # Complex adjacency matrix
    quantum_adj = np.zeros((n, n), dtype=complex)
    for (source, target), edge in quantum_graph.edges.items():
        i, j = node_to_idx[source], node_to_idx[target]
        # Quantum superposition of relations
        total_amplitude = sum(edge.amplitudes)
        quantum_adj[i, j] = total_amplitude
        quantum_adj[j, i] = np.conj(total_amplitude)  # Hermitian
    return quantum_adj, node_to_idx

# Create quantum adjacency matrix
q_adj, q_node_map = create_quantum_adjacency_matrix(quantum_graph)
print("Quantum Adjacency Matrix:")
print(q_adj)
print(f"Is Hermitian: {np.allclose(q_adj, q_adj.conj().T)}")
```

### Quantum Graph Laplacian

**Classical Laplacian:** $L = D - A$ where D is degree matrix, A is adjacency matrix

**Quantum Laplacian:**
$$\mathcal{L} = \mathcal{D} - \mathcal{A}$$

where $\mathcal{D}$ and $\mathcal{A}$ are quantum degree and adjacency matrices.

```python
def quantum_laplacian(quantum_adj):
    """Compute quantum graph Laplacian."""
    # Quantum degree matrix (diagonal)
    degrees = np.sum(quantum_adj, axis=1)
    quantum_degree = np.diag(degrees)
    # Quantum Laplacian
    laplacian = quantum_degree - quantum_adj
    return laplacian

# Compute quantum Laplacian
q_laplacian = quantum_laplacian(q_adj)
print("Quantum Laplacian:")
print(q_laplacian)

# Eigenvalue analysis
eigenvals, eigenvecs = np.linalg.eigh(q_laplacian)
print(f"Laplacian eigenvalues: {eigenvals}")
```

### Spectral Properties

**Spectral Graph Theory:** Study of graph properties through eigenvalues and eigenvectors

**Key Properties:**
- **Smallest eigenvalue**: Always 0 for connected graphs
- **Second smallest eigenvalue (Fiedler value)**: Algebraic connectivity
- **Largest eigenvalue**: Related to graph expansion

```python
def spectral_analysis(adjacency_matrix):
    """Perform spectral analysis of graph."""
    # Eigendecomposition
    eigenvals, eigenvecs = np.linalg.eigh(adjacency_matrix)
    # Sort by eigenvalue magnitude
    idx = np.argsort(np.abs(eigenvals))[::-1]
    eigenvals = eigenvals[idx]
    eigenvecs = eigenvecs[:, idx]
    # Spectral properties
    spectral_radius = np.max(np.abs(eigenvals))
    spectral_gap = np.abs(eigenvals[0]) - np.abs(eigenvals[1])
    return {
        'eigenvalues': eigenvals,
        'eigenvectors': eigenvecs,
        'spectral_radius': spectral_radius,
        'spectral_gap': spectral_gap
    }

# Analyze quantum graph spectrum
spectrum = spectral_analysis(q_adj)
print(f"Spectral radius: {spectrum['spectral_radius']:.3f}")
print(f"Spectral gap: {spectrum['spectral_gap']:.3f}")
```

## 🚶 Random Walks vs Quantum Walks

### Classical Random Walk

**Transition Matrix:** $P_{ij} = \frac{A_{ij}}{d_i}$ where $d_i$ is degree of node $i$

**Walk Evolution:** $\pi_t = P^t \pi_0$

```python
def classical_random_walk(adj_matrix, start_node, steps):
    """Simulate classical random walk on graph."""
    n = adj_matrix.shape[0]
    # Create transition matrix
    degrees = np.sum(adj_matrix, axis=1)
    degrees[degrees == 0] = 1  # Avoid division by zero
    P = adj_matrix / degrees[:, np.newaxis]
    # Initialize state vector
    state = np.zeros(n)
    state[start_node] = 1.0
    # Evolve walk
    states = [state.copy()]
    for step in range(steps):
        state = P.T @ state  # Matrix-vector multiplication
        states.append(state.copy())
    return states

# Classical random walk example
classical_states = classical_random_walk(adj_matrix, 0, 10)  # Start from Alice (index 0)
print(f"Classical walk final distribution: {classical_states[-1]}")
```

### Quantum Walk

**Quantum Evolution:** $|\psi_t\rangle = U^t |\psi_0\rangle$

**Unitary Operator:** $U = e^{-iH\tau}$ where H is Hamiltonian, τ is time step

```python
def quantum_walk_evolution(quantum_adj, start_node, steps, tau=0.1):
    """Simulate quantum walk evolution."""
    n = quantum_adj.shape[0]
    # Hamiltonian (use adjacency matrix)
    H = quantum_adj
    # Time evolution operator
    U = expm(-1j * H * tau)
    # Initialize quantum state
    psi = np.zeros(n, dtype=complex)
    psi[start_node] = 1.0
    # Evolve quantum walk
    quantum_states = [psi.copy()]
    for step in range(steps):
        psi = U @ psi
        quantum_states.append(psi.copy())
    return quantum_states, U

# Quantum walk example
from scipy.linalg import expm

quantum_states, U = quantum_walk_evolution(q_adj, 0, 10)
final_probabilities = np.abs(quantum_states[-1])**2
print(f"Quantum walk final probabilities: {final_probabilities}")
```

### Comparing Classical vs Quantum Walks

```python
def compare_walks(adj_matrix, quantum_adj, start_node, steps):
    """Compare classical and quantum walk spreading."""
    # Classical random walk
    classical_states = classical_random_walk(adj_matrix, start_node, steps)
    classical_final = classical_states[-1]
    # Quantum walk
    quantum_states, _ = quantum_walk_evolution(quantum_adj, start_node, steps)
    quantum_probs = [np.abs(state)**2 for state in quantum_states]
    quantum_final = quantum_probs[-1]
    # Spreading metrics
    classical_entropy = -np.sum(classical_final * np.log2(classical_final + 1e-12))
    quantum_entropy = -np.sum(quantum_final * np.log2(quantum_final + 1e-12))
    return {
        'classical_final': classical_final,
        'quantum_final': quantum_final,
        'classical_entropy': classical_entropy,
        'quantum_entropy': quantum_entropy
    }

# Compare walk behaviors
comparison = compare_walks(adj_matrix, q_adj, 0, 20)
print(f"Classical spreading entropy: {comparison['classical_entropy']:.3f}")
print(f"Quantum spreading entropy: {comparison['quantum_entropy']:.3f}")
```

## 🔍 Graph Algorithms in Quantum Regime

### Quantum Search on Graphs

**Grover's Algorithm on Graphs:** Quantum amplitude amplification for marked vertices

```python
def quantum_graph_search(quantum_adj, marked_nodes, iterations):
    """Quantum search algorithm on graph structure."""
    n = quantum_adj.shape[0]
    # Initialize uniform superposition
    psi = np.ones(n, dtype=complex) / np.sqrt(n)
    # Oracle operator (marks target nodes)
    oracle = np.eye(n, dtype=complex)
    for node in marked_nodes:
        oracle[node, node] = -1
    # Diffusion operator
    diffuser = 2 * np.outer(psi, psi.conj()) - np.eye(n)
    # Quantum search iterations
    for _ in range(iterations):
        psi = oracle @ psi      # Apply oracle
        psi = diffuser @ psi    # Apply diffusion
    # Measurement probabilities
    probabilities = np.abs(psi)**2
    return probabilities, psi

# Search for specific nodes
marked = [1]  # Search for Bob (index 1)
search_probs, search_state = quantum_graph_search(q_adj, marked, 3)
print(f"Search probabilities: {search_probs}")
print(f"Success probability: {search_probs[1]:.3f}")
```

### Quantum Page Rank

**Quantum Version of PageRank:** Uses quantum walks for ranking

```python
def quantum_pagerank(quantum_adj, damping=0.85, iterations=100):
    """Quantum PageRank algorithm using quantum walks."""

    n = quantum_adj.shape[0]

    # Quantum transition matrix
    degrees = np.sum(np.abs(quantum_adj), axis=1)
    degrees[degrees == 0] = 1
    Q = quantum_adj / degrees[:, np.newaxis]
    # Quantum PageRank operator
    uniform = np.ones((n, n)) / n
    M = damping * Q + (1 - damping) * uniform
    # Power iteration with quantum states
    rank_vector = np.ones(n, dtype=complex) / np.sqrt(n)
    for _ in range(iterations):
        rank_vector = M @ rank_vector
        # Normalize
        rank_vector = rank_vector / np.linalg.norm(rank_vector)
    # Convert to probabilities
    quantum_ranks = np.abs(rank_vector)**2
    return quantum_ranks

# Quantum PageRank
q_ranks = quantum_pagerank(q_adj)
print(f"Quantum PageRank scores: {q_ranks}")

# Compare with classical PageRank
classical_ranks = nx.pagerank(classical_graph)
print(f"Classical PageRank: {classical_ranks}")
```

## 🌐 Network Analysis in Quantum Graphs

### Quantum Centrality Measures

**Quantum Betweenness Centrality:** Based on quantum path amplitudes

```python
def quantum_betweenness_centrality(quantum_graph):
    """Calculate quantum betweenness centrality."""
    nodes = list(quantum_graph.nodes.keys())
    n = len(nodes)
    betweenness = {node: 0 for node in nodes}
    # For each pair of nodes
    for i, source in enumerate(nodes):
        for j, target in enumerate(nodes):
            if i >= j:  # Avoid double counting
                continue
            # Find quantum paths
            paths = find_all_quantum_paths(quantum_graph, source, target, max_length=4)
            if not paths:
                continue
            # Calculate total quantum amplitude
            total_amplitude = 0
            path_contributions = {}
            for path in paths:
                amplitude = calculate_quantum_path_amplitude(quantum_graph, path)
                total_amplitude += amplitude
                # Track intermediate nodes
                for intermediate in path[1:-1]:  # Exclude source and target
                    if intermediate not in path_contributions:
                        path_contributions[intermediate] = 0
                    path_contributions[intermediate] += amplitude
            # Quantum betweenness contribution
            if abs(total_amplitude) > 0:
                for intermediate, contribution in path_contributions.items():
                    quantum_weight = abs(contribution / total_amplitude)**2
                    betweenness[intermediate] += quantum_weight
return betweenness

def find_all_quantum_paths(graph, source, target, max_length):
    """Find all quantum paths between source and target."""
    # Use NetworkX for path finding (simplified)
    classical_graph = graph._graph
    try:
        paths = list(nx.all_simple_paths(classical_graph, source, target, max_length))
        return paths
    except:
        return []

def calculate_quantum_path_amplitude(graph, path):
    """Calculate quantum amplitude along a path."""
    amplitude = 1.0 + 0j
    for i in range(len(path) - 1):
        edge_key = (path[i], path[i+1])
        if edge_key in graph.edges:
            edge = graph.edges[edge_key]
            # Use first amplitude for simplicity
            amplitude *= edge.amplitudes[0]
        else:
            amplitude *= 0.1  # Small amplitude for missing edges
    return amplitude

# Calculate quantum betweenness
q_betweenness = quantum_betweenness_centrality(quantum_graph)
print(f"Quantum betweenness centrality: {q_betweenness}")
```

### Quantum Clustering

**Quantum Community Detection:** Using quantum modularity

```python
def quantum_modularity(quantum_adj, communities):
    """Calculate quantum modularity for community structure."""
    n = quantum_adj.shape[0]
    total_weight = np.sum(np.abs(quantum_adj))
    if total_weight == 0:
        return 0
    modularity = 0
    # For each community
    for community in communities:
        for i in community:
            for j in community:
                # Actual edge weight
                actual = np.abs(quantum_adj[i, j])
                # Expected weight (null model)
                ki = np.sum(np.abs(quantum_adj[i, :]))
                kj = np.sum(np.abs(quantum_adj[:, j]))
                expected = ki * kj / total_weight
                modularity += actual - expected
    return modularity / total_weight

def quantum_community_detection(quantum_adj, method='spectral'):
    """Detect communities in quantum graph."""
    if method == 'spectral':
        # Spectral clustering on quantum Laplacian
        laplacian = quantum_laplacian(quantum_adj)
        eigenvals, eigenvecs = np.linalg.eigh(laplacian)
        # Use Fiedler vector for bisection
        fiedler_vector = eigenvecs[:, 1].real  # Second smallest eigenvalue
        # Split based on sign of Fiedler vector
        community1 = np.where(fiedler_vector >= 0)[0]
        community2 = np.where(fiedler_vector < 0)[0]
        communities = [community1.tolist(), community2.tolist()]
    return communities

# Detect quantum communities
communities = quantum_community_detection(q_adj)
modularity = quantum_modularity(q_adj, communities)

print(f"Detected communities: {communities}")
print(f"Quantum modularity: {modularity:.3f}")
```

## 📐 Geometric Properties

### Quantum Graph Embeddings

**Embedding in Euclidean Space:** Map quantum nodes to geometric coordinates

```python
def quantum_graph_embedding(quantum_adj, dimensions=2):
    """Embed quantum graph in Euclidean space."""
    # Use quantum Laplacian eigenvectors for embedding
    laplacian = quantum_laplacian(quantum_adj)
    eigenvals, eigenvecs = np.linalg.eigh(laplacian)
    # Use smallest non-zero eigenvalues for embedding
    # Skip first eigenvector (constant)
    embedding = eigenvecs[:, 1:dimensions+1].real
    return embedding

# Create quantum embedding
embedding = quantum_graph_embedding(q_adj, dimensions=2)
print(f"Quantum embedding shape: {embedding.shape}")
print("Embedding coordinates:")
for i, node in enumerate(quantum_graph.nodes.keys()):
    print(f"  {node}: ({embedding[i, 0]:.3f}, {embedding[i, 1]:.3f})")
```

### Quantum Graph Distances

**Quantum Distance Measures:**

```python
def quantum_graph_distances(quantum_graph):
    """Calculate various quantum distance measures."""
    nodes = list(quantum_graph.nodes.keys())
    n = len(nodes)
    # Quantum state overlap distances
    overlap_distances = np.zeros((n, n))
    for i, node1 in enumerate(nodes):
        for j, node2 in enumerate(nodes):
            if i != j:
                state1 = quantum_graph.nodes[node1].state_vector
                state2 = quantum_graph.nodes[node2].state_vector
                # Quantum fidelity distance
                fidelity = abs(np.vdot(state1, state2))**2
                distance = 1 - fidelity
                overlap_distances[i, j] = distance
    return overlap_distances

# Calculate quantum distances
distances = quantum_graph_distances(quantum_graph)
print("Quantum state distances:")
print(distances)
```

## 🔄 Dynamic Quantum Graphs

### Temporal Evolution

**Time-Dependent Quantum Graphs:** Graphs that evolve over time

```python
def evolve_quantum_graph(quantum_graph, time_steps, evolution_rate=0.1):
    """Simulate temporal evolution of quantum graph."""
    # Store evolution history
    evolution_history = []
    for t in range(time_steps):
        # Evolve quantum states
        for node_id, node in quantum_graph.nodes.items():
            # Simple random evolution (more sophisticated models possible)
            noise = np.random.normal(0, evolution_rate, len(node.state_vector))
            new_state = node.state_vector + noise * (1j if t % 2 else 1)
            # Renormalize
            new_state = new_state / np.linalg.norm(new_state)
            node.state_vector = new_state
            # Update density matrix
            node.density_matrix = np.outer(new_state, new_state.conj())
        # Evolve edge amplitudes
        for edge_key, edge in quantum_graph.edges.items():
            # Add phase evolution
            phase_evolution = np.exp(1j * evolution_rate * np.random.uniform(-1, 1))
            edge.amplitudes = [amp * phase_evolution for amp in edge.amplitudes]
        # Record state
        state_snapshot = {
            'time': t,
            'node_entropies': {node_id: node.measure_entropy()
                             for node_id, node in quantum_graph.nodes.items()},
            'edge_strengths': {edge_key: edge.entanglement_strength
                             for edge_key, edge in quantum_graph.edges.items()}
        }
        evolution_history.append(state_snapshot)

    return evolution_history

# Simulate evolution
evolution = evolve_quantum_graph(quantum_graph, time_steps=10)

print("Evolution of node entropies:")
for i, snapshot in enumerate(evolution[::2]):  # Every other step
    print(f"  Time {snapshot['time']}: {snapshot['node_entropies']}")
```

### Graph Growth Models

**Quantum Preferential Attachment:** Quantum version of Barabási-Albert model

```python
def quantum_preferential_attachment(initial_nodes, total_nodes, hilbert_dim=4):
    """Generate quantum graph using preferential attachment."""

    graph = EntangledGraph(hilbert_dim=hilbert_dim)

    # Initialize with small complete graph
    for i in range(initial_nodes):
        node_id = f"Node_{i}"
        state = np.random.uniform(0, 1, hilbert_dim)
        state = state / np.linalg.norm(state)  # Normalize
        graph.add_quantum_node(node_id, state=state)

    # Connect initial nodes
    for i in range(initial_nodes):
        for j in range(i+1, initial_nodes):
            amplitude = np.random.uniform(0.5, 1.0)
            graph.add_entangled_edge(f"Node_{i}", f"Node_{j}",
                                   relations=["connected"],
                                   amplitudes=[amplitude])

    # Add remaining nodes with quantum preferential attachment
    for i in range(initial_nodes, total_nodes):
        new_node_id = f"Node_{i}"
        new_state = np.random.uniform(0, 1, hilbert_dim)
        new_state = new_state / np.linalg.norm(new_state)
        graph.add_quantum_node(new_node_id, state=new_state)

        # Calculate quantum attachment probabilities
        existing_nodes = [f"Node_{j}" for j in range(i)]
        attachment_probs = []

        for existing_node in existing_nodes:
            # Quantum preference based on state overlap
            existing_state = graph.nodes[existing_node].state_vector
            overlap = abs(np.vdot(new_state, existing_state))**2

            # Classical degree
            degree = len([edge for edge in graph.edges if existing_node in edge])

            # Combined quantum-classical preference
            preference = 0.7 * overlap + 0.3 * (degree / len(graph.edges) if graph.edges else 0)
            attachment_probs.append(preference)

        # Normalize probabilities
        if sum(attachment_probs) > 0:
            attachment_probs = np.array(attachment_probs) / sum(attachment_probs)

            # Select nodes to connect to
            num_connections = min(2, len(existing_nodes))  # Connect to 2 nodes
            selected_indices = np.random.choice(len(existing_nodes),
                                              size=num_connections,
                                              replace=False,
                                              p=attachment_probs)

            for idx in selected_indices:
                target_node = existing_nodes[idx]
                amplitude = np.random.uniform(0.5, 1.0)
                graph.add_entangled_edge(new_node_id, target_node,
                                       relations=["attached"],
                                       amplitudes=[amplitude])

    return graph

# Generate quantum scale-free network
quantum_network = quantum_preferential_attachment(initial_nodes=3, total_nodes=10)
print(f"Generated quantum network: {len(quantum_network.nodes)} nodes, {len(quantum_network.edges)} edges")
```

## 📊 Graph Visualization and Analysis

### Quantum Graph Layout Algorithms

**Force-directed layout with quantum forces:**

```python
def quantum_force_directed_layout(quantum_graph, iterations=100, k=1.0):
    """Force-directed layout considering quantum interactions."""

    nodes = list(quantum_graph.nodes.keys())
    n = len(nodes)

    # Initialize random positions
    positions = np.random.random((n, 2))

    for iteration in range(iterations):
        forces = np.zeros((n, 2))

        # Calculate forces between all pairs
        for i, node1 in enumerate(nodes):
            for j, node2 in enumerate(nodes):
                if i == j:
                    continue

                # Position difference
                diff = positions[i] - positions[j]
                distance = np.linalg.norm(diff)

                if distance < 1e-6:
                    diff = np.random.random(2) * 0.01
                    distance = np.linalg.norm(diff)

                # Classical repulsive force
                repulsive = k**2 / distance
                force_direction = diff / distance

                # Quantum attractive force (if connected)
                attractive = 0
                edge_key = (node1, node2)
                if edge_key in quantum_graph.edges:
                    edge = quantum_graph.edges[edge_key]
                    quantum_strength = edge.entanglement_strength
                    attractive = quantum_strength * distance / k
                elif (node2, node1) in quantum_graph.edges:
                    edge = quantum_graph.edges[(node2, node1)]
                    quantum_strength = edge.entanglement_strength
                    attractive = quantum_strength * distance / k

                # Quantum state similarity force
                state1 = quantum_graph.nodes[node1].state_vector
                state2 = quantum_graph.nodes[node2].state_vector
                similarity = abs(np.vdot(state1, state2))**2
                similarity_force = similarity * 0.1

                # Total force
                total_force = (repulsive - attractive - similarity_force) * force_direction
                forces[i] += total_force

        # Update positions
        positions += forces * 0.01

    # Return as dictionary
    return {node: positions[i] for i, node in enumerate(nodes)}

# Generate quantum layout
layout = quantum_force_directed_layout(quantum_graph)
print("Quantum force-directed layout:")
for node, pos in layout.items():
    print(f"  {node}: ({pos[0]:.3f}, {pos[1]:.3f})")
```

## 🎯 Applications and Extensions

### Quantum Knowledge Graph Completion

**Link Prediction using Quantum Interference:**

```python
def quantum_knowledge_completion(quantum_graph, target_relations):
    """Complete knowledge graph using quantum predictions."""

    nodes= list(quantum_graph.nodes.keys())
    predictions = []

    # For each pair of unconnected nodes
    for i, source in enumerate(nodes):
        for j, target in enumerate(nodes[i+1:], i+1):
            edge_key = (source, target)
            reverse_key = (target, source)

            # Skip if edge already exists
            if edge_key in quantum_graph.edges or reverse_key in quantum_graph.edges:
                continue

            # Calculate quantum prediction score
            score = calculate_quantum_link_probability(quantum_graph, source, target, target_relations)

            if score > 0.3:  # Threshold for prediction
                predictions.append({
                    'source': source,
                    'target': target,
                    'predicted_relations': target_relations,
                    'quantum_score': score
                })
    return predictions

def calculate_quantum_link_probability(graph, source, target, relations):
    """Calculate quantum probability of link between nodes."""

    # Quantum state similarity
    state1 = graph.nodes[source].state_vector
    state2 = graph.nodes[target].state_vector
    state_similarity = abs(np.vdot(state1, state2))**2

    # Path-based quantum interference
    paths = find_all_quantum_paths(graph, source, target, max_length=3)
    path_amplitude = 0

    for path in paths:
        amplitude = calculate_quantum_path_amplitude(graph, path)
        path_amplitude += amplitude

    path_score = abs(path_amplitude)**2 if paths else 0

    # Combined score
    combined_score = 0.6 * state_similarity + 0.4 * path_score

    return combined_score

# Predict missing links
predictions = quantum_knowledge_completion(quantum_graph, ["related_to"])
print(f"Quantum predictions: {len(predictions)} potential links")
for pred in predictions[:3]:  # Show top 3
    print(f"  {pred['source']} -> {pred['target']}: {pred['quantum_score']:.3f}")
```

This comprehensive foundation in graph theory provides the mathematical underpinnings for understanding how quantum mechanics enhances traditional graph-based knowledge representation. The quantum extensions enable richer modeling of uncertainty, correlation, and interference effects that are impossible to capture in classical graphs! 📊⚛️
