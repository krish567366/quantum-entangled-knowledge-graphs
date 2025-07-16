# Examples

This section provides practical examples of using QE-KGR for various applications.

## Basic Graph Creation

```python
import qekgr
from qekgr import EntangledGraph, QuantumInference, EntangledQueryEngine

# Create a quantum knowledge graph
graph = EntangledGraph(hilbert_dim=4)

# Add researchers as quantum nodes
alice = graph.add_quantum_node("Alice", 
                              state="researcher",
                              metadata={
                                  "field": "quantum_computing",
                                  "institution": "Commercial",
                                  "expertise": ["quantum_algorithms", "error_correction"]
                              })

bob = graph.add_quantum_node("Bob",
                            state="professor", 
                            metadata={
                                "field": "machine_learning",
                                "institution": "Stanford", 
                                "expertise": ["neural_networks", "deep_learning"]
                            })

charlie = graph.add_quantum_node("Charlie",
                                state="student",
                                metadata={
                                    "field": "quantum_ml",
                                    "institution": "Caltech",
                                    "expertise": ["quantum_neural_nets"]
                                })

# Add entangled relationships
graph.add_entangled_edge(alice, bob,
                        relations=["collaborates", "co_authors", "friends"],
                        amplitudes=[0.8, 0.6, 0.4])

graph.add_entangled_edge(bob, charlie,
                        relations=["mentors", "supervises", "advises"], 
                        amplitudes=[0.9, 0.7, 0.5])

graph.add_entangled_edge(alice, charlie,
                        relations=["knows", "potential_collaboration"],
                        amplitudes=[0.5, 0.3])

print(f"Created graph with {len(graph)} nodes")
print(f"Graph entanglement structure: {graph}")
```

## Quantum Walks and Exploration

```python
# Initialize quantum inference engine
inference = QuantumInference(graph)

# Perform quantum walk starting from Alice
walk_result = inference.quantum_walk(
    start_node="Alice",
    steps=15,
    bias_relations=["collaborates", "mentors"]
)

print("Quantum Walk Results:")
print(f"Path: {' -> '.join(walk_result.path)}")
print(f"Final amplitude: {walk_result.amplitudes[-1]:.3f}")
print(f"Entanglement evolution: {walk_result.entanglement_trace}")

# Analyze interference patterns
interference = walk_result.interference_pattern
print(f"Interference strength: {interference.mean():.3f} ± {interference.std():.3f}")
```

## Natural Language Queries

```python
# Create query engine
query_engine = EntangledQueryEngine(graph)

# Example queries
queries = [
    "Who might Alice collaborate with on quantum machine learning?",
    "Find researchers working on quantum neural networks",
    "What connections exist between Commercial and Stanford researchers?",
    "Who could mentor students in quantum computing?"
]

for query in queries:
    print(f"\nQuery: {query}")
    results = query_engine.query(query, max_results=3)
    
    for i, result in enumerate(results, 1):
        print(f"  Result {i} (confidence: {result.confidence_score:.3f}):")
        print(f"    Nodes: {', '.join(result.answer_nodes)}")
        print(f"    Path: {' -> '.join(result.reasoning_path)}")
        
        # Get explanation for top result
        if i == 1:
            explanation = query_engine.explain_reasoning(result)
            print(f"    Quantum effects: {explanation['quantum_effects']}")
```

## Query Chains with Context Transfer

```python
# Chain related queries with context transfer
query_chain = [
    "Who works on quantum computing at Commercial?",
    "What machine learning researchers might they collaborate with?", 
    "What joint projects could emerge from this collaboration?"
]

chain_results = query_engine.chain_queries(query_chain, context_transfer=True)

print("Query Chain Results:")
for i, (query, result) in enumerate(zip(query_chain, chain_results)):
    print(f"\nStep {i+1}: {query}")
    print(f"  Answer: {', '.join(result.answer_nodes)}")
    print(f"  Confidence: {result.confidence_score:.3f}")
```

## Subgraph Discovery

```python
# Discover entangled communities
discovery = inference.discover_entangled_subgraph(
    seed_nodes=["Alice", "Bob"],
    expansion_steps=3,
    min_entanglement=0.3
)

print("Entangled Subgraph Discovery:")
print(f"  Discovered nodes: {discovery.nodes}")
print(f"  Entanglement density: {discovery.entanglement_density:.3f}")
print(f"  Coherence measure: {discovery.coherence_measure:.3f}")
print(f"  Discovery confidence: {discovery.discovery_confidence:.3f}")
```

## Link Prediction

```python
# Predict potential future collaborations
predictions = inference.interference_link_prediction(
    source_node="Alice",
    num_predictions=5
)

print("Link Prediction Results:")
for pred in predictions:
    print(f"  {pred.source_node} -> {pred.target_node}")
    print(f"    Quantum score: {pred.quantum_score:.3f}")
    print(f"    Classical score: {pred.classical_score:.3f}")
    print(f"    Predicted relations: {pred.predicted_relations}")
```

## Visualization

```python
from qekgr.utils import QuantumGraphVisualizer

# Create visualizer
viz = QuantumGraphVisualizer(graph)

# Generate different visualizations
fig_2d = viz.visualize_graph_2d(layout="spring")
fig_3d = viz.visualize_graph_3d(color_by="entanglement") 
fig_heatmap = viz.visualize_entanglement_heatmap()
fig_states = viz.visualize_quantum_states(method="pca")

# Visualize query results
query_result = results[0]  # From previous query
fig_query = viz.visualize_query_result(query_result)

# Visualize quantum walk
fig_walk = viz.visualize_quantum_walk(walk_result, show_amplitudes=True)

# Create comprehensive dashboard
dashboard = viz.create_interactive_dashboard()

# Save visualizations
fig_2d.write_html("graph_2d.html")
fig_3d.write_html("graph_3d.html") 
dashboard.write_html("dashboard.html")

print("Visualizations saved to HTML files")
```

## Quantum State Analysis

```python
# Analyze quantum properties of nodes
print("Node Quantum Properties:")
for node_id in graph.get_all_nodes():
    node = graph.nodes[node_id]
    entropy = graph.get_entanglement_entropy(node_id)
    neighbors = graph.get_neighbors(node_id)
    
    print(f"\n{node_id}:")
    print(f"  Entropy: {entropy:.3f}")
    print(f"  Degree: {len(neighbors)}")
    print(f"  State vector: {node.state_vector}")
    
    # Calculate overlaps with other nodes
    for other_id in neighbors:
        overlap = graph.get_quantum_state_overlap(node_id, other_id)
        print(f"  Overlap with {other_id}: {abs(overlap):.3f}")

# Edge entanglement analysis
print("\nEdge Entanglement Strengths:")
for (source, target), edge in graph.edges.items():
    print(f"{source} -> {target}: {edge.entanglement_strength:.3f}")
    print(f"  Relations: {edge.relations}")
    print(f"  Amplitudes: {[f'{amp:.3f}' for amp in edge.amplitudes]}")
```

## Quantum State Evolution

```python
import numpy as np

# Define a Hamiltonian for quantum evolution
def create_research_hamiltonian(graph, coupling_strength=0.1):
    """Create Hamiltonian based on research field similarities."""
    dim = graph.hilbert_dim
    H = np.zeros((dim, dim), dtype=complex)
    
    # Add field-dependent energy levels
    field_energies = {
        "quantum_computing": 1.0,
        "machine_learning": 0.8, 
        "quantum_ml": 1.2
    }
    
    # Diagonal terms (field energies)
    for i in range(dim):
        H[i, i] = field_energies.get(f"field_{i}", 1.0)
    
    # Off-diagonal coupling terms
    for i in range(dim-1):
        H[i, i+1] = H[i+1, i] = coupling_strength
    
    return H

# Evolve Alice's quantum state
hamiltonian = create_research_hamiltonian(graph)
initial_state = graph.nodes["Alice"].state_vector.copy()

print("Quantum State Evolution:")
print(f"Initial state: {initial_state}")

# Evolve for different time steps
for time in [0.1, 0.5, 1.0, 2.0]:
    graph.evolve_quantum_state("Alice", hamiltonian, time)
    evolved_state = graph.nodes["Alice"].state_vector
    fidelity = abs(np.vdot(initial_state, evolved_state))**2
    
    print(f"Time {time}: fidelity = {fidelity:.3f}")
    print(f"  State: {evolved_state}")

# Reset to initial state
graph.nodes["Alice"].state_vector = initial_state
```

## Real-World Application: Scientific Collaboration Network

```python
def create_collaboration_network():
    """Create a realistic scientific collaboration network."""
    
    # Larger research collaboration graph
    collab_graph = EntangledGraph(hilbert_dim=8)
    
    # Add researchers from different institutions
    researchers = [
        ("Dr_Smith", "quantum_cryptography", "Commercial"),
        ("Prof_Johnson", "quantum_algorithms", "Stanford"), 
        ("Dr_Chen", "quantum_error_correction", "IBM"),
        ("Prof_Williams", "quantum_machine_learning", "Google"),
        ("Dr_Brown", "quantum_simulation", "Caltech"),
        ("Prof_Davis", "quantum_networks", "Oxford"),
        ("Dr_Wilson", "quantum_sensing", "NIST"),
        ("Prof_Garcia", "topological_quantum", "Microsoft")
    ]
    
    for name, field, institution in researchers:
        collab_graph.add_quantum_node(
            name,
            state=field,
            metadata={
                "field": field,
                "institution": institution,
                "publications": np.random.randint(10, 100),
                "h_index": np.random.randint(10, 50)
            }
        )
    
    # Add collaboration edges based on field similarity
    collaborations = [
        ("Dr_Smith", "Dr_Chen", ["co_authors", "joint_grants"], [0.8, 0.6]),
        ("Prof_Johnson", "Prof_Williams", ["collaborates", "shares_students"], [0.9, 0.5]),
        ("Dr_Brown", "Prof_Garcia", ["theoretical_discussions", "conferences"], [0.6, 0.4]),
        ("Prof_Davis", "Dr_Wilson", ["experimental_collaboration"], [0.7]),
        ("Dr_Smith", "Prof_Johnson", ["quantum_foundations", "reviews"], [0.5, 0.3]),
        ("Prof_Williams", "Dr_Brown", ["quantum_advantage", "applications"], [0.6, 0.7]),
        ("Dr_Chen", "Dr_Wilson", ["error_correction", "sensing"], [0.4, 0.5]),
        ("Prof_Davis", "Prof_Garcia", ["theoretical_networks"], [0.3])
    ]
    
    for source, target, relations, amplitudes in collaborations:
        collab_graph.add_entangled_edge(source, target, relations, amplitudes)
    
    return collab_graph

# Create and analyze collaboration network
collab_graph = create_collaboration_network()
collab_inference = QuantumInference(collab_graph)
collab_query = EntangledQueryEngine(collab_graph)

print(f"Collaboration network: {len(collab_graph)} researchers")

# Find research communities
communities = collab_inference.discover_entangled_subgraph(
    seed_nodes=["Dr_Smith", "Prof_Johnson"],
    expansion_steps=2,
    min_entanglement=0.4
)

print(f"Research community: {communities.nodes}")
print(f"Community coherence: {communities.coherence_measure:.3f}")

# Query for interdisciplinary collaborations
interdisciplinary_query = "Find researchers who could bridge quantum cryptography and machine learning"
results = collab_query.query(interdisciplinary_query)

print(f"\nInterdisciplinary collaboration suggestions:")
for result in results:
    print(f"  {', '.join(result.answer_nodes)} (confidence: {result.confidence_score:.3f})")
```

## Advanced: Custom Quantum Operations

```python
def custom_entanglement_measure(graph, node1, node2):
    """Calculate custom entanglement measure between two nodes."""
    
    # Get quantum states
    state1 = graph.nodes[node1].state_vector
    state2 = graph.nodes[node2].state_vector
    
    # Create joint state (tensor product)
    joint_state = np.kron(state1, state2)
    
    # Reshape for partial trace calculation
    dim = len(state1)
    joint_density = np.outer(joint_state, np.conj(joint_state))
    joint_density = joint_density.reshape(dim, dim, dim, dim)
    
    # Partial trace over second subsystem
    reduced_density = np.trace(joint_density, axis1=1, axis2=3)
    
    # Calculate entanglement entropy
    eigenvals = np.linalg.eigvals(reduced_density)
    eigenvals = eigenvals[eigenvals > 1e-12]
    
    if len(eigenvals) == 0:
        return 0.0
    
    entanglement = -np.sum(eigenvals * np.log2(eigenvals))
    return entanglement

# Test custom entanglement measure
entanglement_ab = custom_entanglement_measure(graph, "Alice", "Bob")
entanglement_ac = custom_entanglement_measure(graph, "Alice", "Charlie")

print(f"Custom entanglement Alice-Bob: {entanglement_ab:.3f}")
print(f"Custom entanglement Alice-Charlie: {entanglement_ac:.3f}")
```

These examples demonstrate the full capabilities of QE-KGR for quantum-enhanced knowledge graph reasoning. The library enables novel approaches to knowledge discovery through quantum mechanical principles while maintaining practical usability for real-world applications.
