# Quick Start Guide

Get up and running with Quantum Entangled Knowledge Graphs (QE-KGR) in just a few minutes! This guide walks you through the basics of creating and querying quantum knowledge graphs.

## 🚀 Your First Quantum Graph

### Step 1: Import QE-KGR

```python
import qekgr
from qekgr import EntangledGraph, QuantumInference, EntangledQueryEngine
```

### Step 2: Create a Quantum Graph

```python
# Create a graph with 4-dimensional Hilbert space
graph = EntangledGraph(hilbert_dim=4)
print(f"Created quantum graph with {graph.hilbert_dim}D Hilbert space")
```

### Step 3: Add Quantum Nodes

```python
# Add people as quantum nodes
alice = graph.add_quantum_node("Alice", state="physicist", 
                              metadata={"institution": "Commercial", "field": "quantum_mechanics"})

bob = graph.add_quantum_node("Bob", state="engineer",
                            metadata={"institution": "Stanford", "field": "quantum_computing"})

charlie = graph.add_quantum_node("Charlie", state="student",
                                metadata={"institution": "Caltech", "field": "physics"})

print(f"Added {len(graph.nodes)} quantum nodes")
```

### Step 4: Create Entangled Relationships

```python
# Add entangled edges with superposed relations
graph.add_entangled_edge(alice, bob,
                        relations=["collaborates", "co-authors", "friends"],
                        amplitudes=[0.8, 0.6, 0.4])

graph.add_entangled_edge(bob, charlie,
                        relations=["mentors", "teaches"],
                        amplitudes=[0.9, 0.7])

graph.add_entangled_edge(alice, charlie,
                        relations=["advises", "inspires"],
                        amplitudes=[0.7, 0.5])

print(f"Created {len(graph.edges)} entangled relationships")
```

### Step 5: Quantum Reasoning

```python
# Initialize quantum inference engine
inference = QuantumInference(graph)

# Perform quantum walk
walk_result = inference.quantum_walk("Alice", steps=10)
print(f"Quantum walk path: {' → '.join(walk_result.path)}")
print(f"Final quantum amplitudes: {walk_result.amplitudes[-1]}")
```

### Step 6: Query the Graph

```python
# Initialize query engine
query_engine = EntangledQueryEngine(graph)

# Ask natural language questions
results = query_engine.query("Who does Alice collaborate with?")

for result in results:
    print(f"Answer: {', '.join(result.answer_nodes)}")
    print(f"Confidence: {result.confidence_score:.3f}")
    print(f"Reasoning: {' → '.join(result.reasoning_path)}")
```

## 🧬 Complete Example: Molecular Discovery

Let's build a more sophisticated example for drug discovery:

```python
import numpy as np
from qekgr import EntangledGraph, QuantumInference, EntangledQueryEngine

def create_drug_discovery_graph():
    """Create a quantum knowledge graph for drug discovery."""
    
    # Higher dimensional space for complex molecular interactions
    graph = EntangledGraph(hilbert_dim=8)
    
    # Add drug molecules
    aspirin = graph.add_quantum_node("Aspirin", state="anti_inflammatory",
                                   metadata={"target": "COX", "side_effects": ["stomach_irritation"]})
    
    ibuprofen = graph.add_quantum_node("Ibuprofen", state="anti_inflammatory", 
                                     metadata={"target": "COX", "side_effects": ["kidney_risk"]})
    
    metformin = graph.add_quantum_node("Metformin", state="antidiabetic",
                                     metadata={"target": "AMPK", "side_effects": ["nausea"]})
    
    # Add protein targets
    cox1 = graph.add_quantum_node("COX1", state="enzyme",
                                metadata={"function": "prostaglandin_synthesis", "location": "stomach"})
    
    cox2 = graph.add_quantum_node("COX2", state="enzyme", 
                                metadata={"function": "inflammation", "location": "inflammatory_sites"})
    
    ampk = graph.add_quantum_node("AMPK", state="kinase",
                                metadata={"function": "energy_metabolism", "location": "liver"})
    
    # Add diseases/conditions
    pain = graph.add_quantum_node("Pain", state="symptom",
                                metadata={"category": "sensory", "severity": "variable"})
    
    inflammation = graph.add_quantum_node("Inflammation", state="process",
                                        metadata={"category": "immune_response", "type": "pathological"})
    
    diabetes = graph.add_quantum_node("Diabetes", state="disease",
                                    metadata={"category": "metabolic", "type": "chronic"})
    
    # Create quantum entangled drug-target interactions
    graph.add_entangled_edge(aspirin, cox1,
                           relations=["inhibits", "binds", "acetylates"],
                           amplitudes=[0.9, 0.8, 0.7])
    
    graph.add_entangled_edge(aspirin, cox2,
                           relations=["inhibits", "selective_binding"],
                           amplitudes=[0.8, 0.6])
    
    graph.add_entangled_edge(ibuprofen, cox1,
                           relations=["inhibits", "competes"],
                           amplitudes=[0.7, 0.8])
    
    graph.add_entangled_edge(ibuprofen, cox2,
                           relations=["inhibits", "preferential_binding"],
                           amplitudes=[0.9, 0.8])
    
    graph.add_entangled_edge(metformin, ampk,
                           relations=["activates", "phosphorylates"],
                           amplitudes=[0.9, 0.7])
    
    # Drug-condition relationships
    graph.add_entangled_edge(aspirin, pain,
                           relations=["treats", "reduces", "alleviates"],
                           amplitudes=[0.8, 0.7, 0.6])
    
    graph.add_entangled_edge(aspirin, inflammation,
                           relations=["reduces", "suppresses"],
                           amplitudes=[0.7, 0.6])
    
    graph.add_entangled_edge(ibuprofen, pain,
                           relations=["treats", "stronger_than_aspirin"],
                           amplitudes=[0.9, 0.8])
    
    graph.add_entangled_edge(ibuprofen, inflammation,
                           relations=["reduces", "anti_inflammatory"],
                           amplitudes=[0.8, 0.9])
    
    graph.add_entangled_edge(metformin, diabetes,
                           relations=["treats", "controls_glucose", "first_line_therapy"],
                           amplitudes=[0.9, 0.8, 0.9])
    
    # Target-condition relationships
    graph.add_entangled_edge(cox1, pain,
                           relations=["mediates", "peripheral_signaling"],
                           amplitudes=[0.6, 0.7])
    
    graph.add_entangled_edge(cox2, inflammation,
                           relations=["drives", "central_mediator"],
                           amplitudes=[0.8, 0.9])
    
    graph.add_entangled_edge(ampk, diabetes,
                           relations=["regulates", "metabolic_control"],
                           amplitudes=[0.7, 0.8])
    
    return graph

# Create the graph
drug_graph = create_drug_discovery_graph()
print(f"Created drug discovery graph: {len(drug_graph.nodes)} nodes, {len(drug_graph.edges)} edges")

# Initialize reasoning engines
inference = QuantumInference(drug_graph)
query_engine = EntangledQueryEngine(drug_graph)

# Discover new connections
print("\n🔍 Quantum Discovery Session")
print("=" * 40)

# Query 1: Drug repurposing opportunities
results = query_engine.query("What anti-inflammatory drugs might help with diabetes?")
print(f"\nQuery: Anti-inflammatory drugs for diabetes")
for result in results[:2]:  # Top 2 results
    print(f"  Answer: {', '.join(result.answer_nodes)}")
    print(f"  Confidence: {result.confidence_score:.3f}")

# Query 2: Novel drug combinations
results = query_engine.query("Which drugs target similar pathways and could be combined?")
print(f"\nQuery: Drug combination opportunities")
for result in results[:2]:
    print(f"  Answer: {', '.join(result.answer_nodes)}")
    print(f"  Confidence: {result.confidence_score:.3f}")

# Quantum walk exploration
print(f"\n🚶 Quantum Walk from Aspirin")
walk_result = inference.quantum_walk("Aspirin", steps=8)
print(f"Path: {' → '.join(walk_result.path)}")
print(f"Entanglement evolution: {[f'{e:.3f}' for e in walk_result.entanglement_trace[:5]]}")

# Subgraph discovery
print(f"\n🕸️ Discovering Molecular Networks")
subgraph = inference.discover_entangled_subgraph(
    seed_nodes=["COX1", "COX2"], 
    expansion_steps=3, 
    min_entanglement=0.5
)
print(f"Network nodes: {', '.join(list(subgraph.nodes)[:8])}")  # Show first 8
print(f"Network density: {subgraph.entanglement_density:.3f}")
print(f"Discovery confidence: {subgraph.discovery_confidence:.3f}")
```

## 🎯 Key Concepts Explained

### Quantum Nodes

Quantum nodes represent entities as quantum states in Hilbert space:

```python
# Pure state |ψ⟩ 
node = graph.add_quantum_node("Entity", state="physicist")

# Mixed state (density matrix)
custom_state = np.array([0.8, 0.6, 0.0, 0.0])  # Custom quantum state
node = graph.add_quantum_node("Entity", state=custom_state)

# Check quantum properties
print(f"Hilbert dimension: {node.hilbert_dim}")
print(f"Entropy: {node.measure_entropy()}")
```

### Entangled Edges

Edges exist in quantum superposition of multiple relations:

```python
# Superposed relations with quantum amplitudes
edge = graph.add_entangled_edge("Alice", "Bob",
                               relations=["collaborates", "friends", "co-authors"],
                               amplitudes=[0.8, 0.6, 0.4])

print(f"Entanglement strength: {edge.entanglement_strength}")
print(f"Collapsed relation: {edge.collapse_relation()}")  # Quantum measurement
```

### Quantum Walks

Navigate the graph using quantum superposition:

```python
# Biased quantum walk
walk_result = inference.quantum_walk(
    start_node="Alice",
    steps=15,
    bias_relations=["collaborates", "mentors"]  # Prefer these relations
)

# Analyze quantum interference
print(f"Interference pattern shape: {walk_result.interference_pattern.shape}")
print(f"Path coherence: {np.abs(walk_result.final_state).sum()}")
```

### Link Prediction

Predict missing connections using quantum interference:

```python
# Predict links with quantum confidence
predictions = inference.predict_links("Alice", max_predictions=5)

for pred in predictions:
    print(f"{pred.source_node} → {pred.target_node}")
    print(f"  Relations: {pred.predicted_relations}")
    print(f"  Quantum score: {pred.quantum_score:.3f}")
    print(f"  Classical score: {pred.classical_score:.3f}")
```

## 🎨 Visualization

Create beautiful visualizations of your quantum graphs:

```python
from qekgr.utils import QuantumGraphVisualizer

# Initialize visualizer
visualizer = QuantumGraphVisualizer(graph)

# 3D interactive visualization
fig_3d = visualizer.visualize_graph_3d(color_by="entanglement")
fig_3d.show()

# Entanglement heatmap
fig_heatmap = visualizer.visualize_entanglement_heatmap()
fig_heatmap.show()

# Quantum state projection
fig_projection = visualizer.visualize_quantum_states_2d(method="tsne")
fig_projection.show()

# Save visualizations
fig_3d.write_html("my_quantum_graph.html")
```

## 📊 Performance Tips

### Optimize Graph Size

```python
# Use appropriate Hilbert dimensions
small_graph = EntangledGraph(hilbert_dim=2)    # Fast, simple
medium_graph = EntangledGraph(hilbert_dim=4)   # Good balance
large_graph = EntangledGraph(hilbert_dim=8)    # Rich quantum effects
```

### Batch Operations

```python
# Add multiple nodes efficiently
nodes_data = [
    ("Alice", "physicist", {"field": "quantum"}),
    ("Bob", "engineer", {"field": "computing"}),
    ("Charlie", "student", {"field": "physics"})
]

for name, state, metadata in nodes_data:
    graph.add_quantum_node(name, state=state, metadata=metadata)
```

### Memory Management

```python
# Monitor graph statistics
print(f"Nodes: {len(graph.nodes)}")
print(f"Edges: {len(graph.edges)}")
print(f"Memory usage estimate: {len(graph.nodes) * graph.hilbert_dim**2 * 16} bytes")
```

## 🔧 Advanced Features

### Custom Quantum States

```python
# Create custom quantum superposition
theta = np.pi / 4  # Rotation angle
custom_state = np.array([
    np.cos(theta),     # |0⟩ amplitude  
    np.sin(theta),     # |1⟩ amplitude
    0,                 # |2⟩ amplitude
    0                  # |3⟩ amplitude
])

node = graph.add_quantum_node("CustomNode", state=custom_state)
print(f"Custom state norm: {np.linalg.norm(custom_state)}")
```

### Decoherence Effects

```python
# Simulate quantum decoherence
inference.decoherence_rate = 0.2  # Higher rate = faster decoherence

walk_result = inference.quantum_walk("Alice", steps=20)
print(f"Coherence over time: {walk_result.entanglement_trace}")
```

### Query Context

```python
# Provide context for better query understanding
context = {
    "domain": "drug_discovery",
    "focus": "molecular_interactions",
    "exclude": ["side_effects"]
}

results = query_engine.query(
    "Find drugs that target inflammation pathways",
    context=context,
    max_results=10
)
```

## 🏃‍♂️ What's Next?

Now that you've mastered the basics, explore:

1. **[Theory](theory.md)** - Deep dive into quantum mechanics principles
2. **[API Reference](modules.md)** - Complete documentation of all classes and methods
3. **[Tutorials](tutorials/basic_usage.md)** - Step-by-step advanced tutorials
4. **[Use Cases](use_cases/drug_discovery.md)** - Real-world applications

## 💡 Tips for Success

1. **Start Small**: Begin with simple graphs (2-4 dimensional Hilbert space)
2. **Experiment**: Try different quantum states and entanglement patterns
3. **Visualize**: Use visualization tools to understand quantum effects
4. **Monitor Performance**: Track graph size and computation time
5. **Join Community**: Connect with other quantum graph researchers

Ready to explore the quantum realm of knowledge? Let's build something amazing! 🚀
