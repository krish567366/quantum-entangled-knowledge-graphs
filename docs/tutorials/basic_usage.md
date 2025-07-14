# Basic Usage Tutorial

This tutorial will guide you through the fundamental concepts and basic operations of the Quantum Entangled Knowledge Graphs (QE-KGR) library. We'll start with simple examples and gradually introduce more advanced features.

## Prerequisites

Before starting this tutorial, ensure you have:

- Python 3.8 or higher installed
- QE-KGR library installed (`pip install quantum-entangled-knowledge-graphs`)
- Basic understanding of graphs and quantum concepts (see [Theory](../theory.md))

## Getting Started

### 1. Creating Your First Quantum Graph

Let's start by creating a simple quantum entangled knowledge graph:

```python
from qekgr import EntangledGraph, QuantumNode, EntangledEdge

# Create a quantum graph with 4-dimensional Hilbert space
graph = EntangledGraph(hilbert_dim=4)

# Add quantum nodes
alice = QuantumNode("Alice", node_type="person")
bob = QuantumNode("Bob", node_type="person")
charlie = QuantumNode("Charlie", node_type="person")

# Add nodes to the graph
graph.add_node(alice)
graph.add_node(bob)
graph.add_node(charlie)

print(f"Graph has {len(graph.nodes)} nodes")
print(f"Hilbert space dimension: {graph.hilbert_dim}")
```

### 2. Creating Entangled Connections

Quantum graphs use entangled edges to represent relationships:

```python
# Create entangled relationships
friendship_edge = EntangledEdge(
    "Alice", "Bob",
    relation="friend",
    entanglement_strength=0.8,
    edge_type="social"
)

collaboration_edge = EntangledEdge(
    "Bob", "Charlie", 
    relation="collaborator",
    entanglement_strength=0.6,
    edge_type="professional"
)

# Add edges to the graph
graph.add_edge(friendship_edge)
graph.add_edge(collaboration_edge)

print(f"Graph has {len(graph.edges)} edges")
```

### 3. Exploring Quantum Properties

Let's examine the quantum properties of our graph:

```python
# Get quantum state of a node
alice_state = graph.get_node_state("Alice")
print(f"Alice's quantum state: {alice_state}")

# Check entanglement between nodes
entanglement = graph.measure_entanglement("Alice", "Bob")
print(f"Alice-Bob entanglement: {entanglement:.3f}")

# Get the adjacency matrix representation
adj_matrix = graph.get_adjacency_matrix()
print(f"Adjacency matrix shape: {adj_matrix.shape}")
```

### 4. Basic Quantum Operations

Perform fundamental quantum operations on the graph:

```python
# Apply quantum superposition to a node
graph.apply_superposition("Alice", amplitudes=[0.6, 0.8])

# Measure quantum state (collapses superposition)
measurement = graph.measure_node("Alice")
print(f"Alice's measured state: {measurement}")

# Create quantum entanglement between nodes
graph.entangle_nodes("Alice", "Charlie", strength=0.7)

# Check if nodes are entangled
is_entangled = graph.are_entangled("Alice", "Charlie")
print(f"Alice and Charlie entangled: {is_entangled}")
```

## Working with Real Data

### Building a Simple Knowledge Base

Let's create a more realistic example with a small knowledge base about movies:

```python
from qekgr import EntangledGraph

# Create movie knowledge graph
movie_graph = EntangledGraph(hilbert_dim=8)

# Add movie entities
entities = {
    "Inception": {"type": "movie", "genre": "sci-fi"},
    "Leonardo DiCaprio": {"type": "actor"},
    "Christopher Nolan": {"type": "director"},
    "Mind Bending": {"type": "concept"},
    "Dreams": {"type": "concept"},
    "Reality": {"type": "concept"}
}

# Add all entities as quantum nodes
for entity_id, properties in entities.items():
    node = QuantumNode(entity_id, **properties)
    movie_graph.add_node(node)

# Create relationships with entanglement
relationships = [
    ("Leonardo DiCaprio", "Inception", "acts_in", 0.9),
    ("Christopher Nolan", "Inception", "directs", 0.9),
    ("Inception", "Mind Bending", "explores", 0.8),
    ("Inception", "Dreams", "features", 0.7),
    ("Dreams", "Reality", "contrasts_with", 0.6),
    ("Mind Bending", "Christopher Nolan", "signature_of", 0.8)
]

for source, target, relation, strength in relationships:
    edge = EntangledEdge(source, target, relation=relation, 
                        entanglement_strength=strength)
    movie_graph.add_edge(edge)

print(f"Movie graph: {len(movie_graph.nodes)} nodes, {len(movie_graph.edges)} edges")
```

### Exploring Quantum Relationships

Now let's explore the quantum properties of our movie knowledge base:

```python
# Find strongly entangled concepts
strong_entanglements = []
for (source, target), edge in movie_graph.edges.items():
    if edge.entanglement_strength > 0.7:
        strong_entanglements.append((source, target, edge.entanglement_strength))

print("Strong entanglements:")
for source, target, strength in strong_entanglements:
    print(f"  {source} <-> {target}: {strength:.3f}")

# Measure quantum coherence of the entire graph
coherence = movie_graph.measure_coherence()
print(f"Graph coherence: {coherence:.3f}")
```

## Basic Querying

### Using the Query Engine

The EntangledQueryEngine allows natural language querying:

```python
from qekgr import EntangledQueryEngine

# Create query engine for our movie graph
query_engine = EntangledQueryEngine(movie_graph)

# Simple entity queries
results = query_engine.query("Who acts in Inception?")
print("Query: Who acts in Inception?")
for result in results:
    print(f"Answer: {', '.join(result.answer_nodes)} (confidence: {result.confidence_score:.3f})")

# Concept exploration queries  
results = query_engine.query("What concepts are explored in movies?")
print("\nQuery: What concepts are explored in movies?")
for result in results:
    print(f"Answer: {', '.join(result.answer_nodes)} (confidence: {result.confidence_score:.3f})")
```

### Advanced Query Features

Let's explore more sophisticated query capabilities:

```python
# Semantic search across the graph
semantic_results = query_engine.semantic_search(
    "mind-bending sci-fi concepts", 
    max_results=3
)

print("Semantic search for 'mind-bending sci-fi concepts':")
for result in semantic_results:
    print(f"  {result.node_id}: {result.relevance_score:.3f}")

# Superposed queries (quantum parallel search)
superposed_query = query_engine.superposed_query([
    "Who directs movies?",
    "What are sci-fi concepts?",
    "Who acts in movies?"
])

print("\nSuperposed query results:")
for i, query_result in enumerate(superposed_query.query_results):
    print(f"Query {i+1}: {len(query_result)} results")
```

## Basic Quantum Reasoning

### Quantum Walks

Quantum walks are fundamental for reasoning in quantum graphs:

```python
from qekgr import QuantumInference

# Create inference engine
inference = QuantumInference(movie_graph)

# Perform quantum walk starting from "Leonardo DiCaprio"
walk_result = inference.quantum_walk("Leonardo DiCaprio", steps=10)

print(f"Quantum walk from Leonardo DiCaprio:")
print(f"Final state distribution:")
for node_id, probability in walk_result.final_distribution.items():
    if probability > 0.1:  # Show only significant probabilities
        print(f"  {node_id}: {probability:.3f}")
```

### Link Prediction

Predict missing relationships using quantum inference:

```python
# Predict potential links
predictions = inference.predict_links(threshold=0.3)

print("Predicted missing relationships:")
for prediction in predictions[:5]:  # Show top 5 predictions
    print(f"  {prediction.source} -> {prediction.target}")
    print(f"    Confidence: {prediction.confidence_score:.3f}")
    print(f"    Reasoning: {prediction.reasoning_path}")
```

## Visualization Basics

### Creating Basic Visualizations

Visualize your quantum graph to better understand its structure:

```python
from qekgr.utils import QuantumGraphVisualizer

# Create visualizer
visualizer = QuantumGraphVisualizer(movie_graph)

# 2D visualization
fig_2d = visualizer.visualize_graph_2d(
    layout="spring",
    color_by="node_type"
)
fig_2d.show()

# Entanglement heatmap
heatmap = visualizer.visualize_entanglement_heatmap()
heatmap.show()
```

### Interactive Exploration

```python
# 3D interactive visualization
fig_3d = visualizer.visualize_graph_3d(
    layout="spring_3d",
    color_by="entanglement",
    size_by="degree"
)
fig_3d.show()

# Save visualization
fig_3d.write_html("movie_graph_3d.html")
```

## Common Patterns and Best Practices

### 1. Node Initialization

Always initialize nodes with meaningful attributes:

```python
# Good: Descriptive node with type information
good_node = QuantumNode(
    "entity_id",
    node_type="concept",
    domain="science",
    confidence=0.9
)

# Avoid: Minimal node without context
minimal_node = QuantumNode("entity_id")
```

### 2. Edge Weight Selection

Choose entanglement strengths thoughtfully:

```python
# Strong entanglement for direct relationships
direct_edge = EntangledEdge("A", "B", relation="synonym", 
                           entanglement_strength=0.9)

# Moderate entanglement for related concepts
related_edge = EntangledEdge("A", "C", relation="related_to", 
                            entanglement_strength=0.6)

# Weak entanglement for distant connections
distant_edge = EntangledEdge("A", "D", relation="distant_from", 
                            entanglement_strength=0.3)
```

### 3. Graph Coherence Management

Monitor and maintain quantum coherence:

```python
def check_graph_health(graph):
    """Check the quantum health of the graph."""
    coherence = graph.measure_coherence()
    entanglement_dist = [edge.entanglement_strength 
                        for edge in graph.edges.values()]
    
    avg_entanglement = sum(entanglement_dist) / len(entanglement_dist)
    
    print(f"Graph Health Report:")
    print(f"  Coherence: {coherence:.3f}")
    print(f"  Average entanglement: {avg_entanglement:.3f}")
    print(f"  Nodes: {len(graph.nodes)}")
    print(f"  Edges: {len(graph.edges)}")
    
    if coherence < 0.5:
        print("  Warning: Low coherence detected!")
    
    return coherence > 0.5

# Check our movie graph
is_healthy = check_graph_health(movie_graph)
```

### 4. Incremental Graph Building

Build graphs incrementally for better performance:

```python
def build_graph_incrementally(entities, relationships):
    """Build graph step by step with validation."""
    graph = EntangledGraph(hilbert_dim=len(entities))
    
    # Add nodes first
    for entity_data in entities:
        node = QuantumNode(**entity_data)
        graph.add_node(node)
        
        # Validate after each addition
        if len(graph.nodes) % 100 == 0:  # Check every 100 nodes
            coherence = graph.measure_coherence()
            print(f"Added {len(graph.nodes)} nodes, coherence: {coherence:.3f}")
    
    # Add edges with entanglement optimization
    for rel_data in relationships:
        edge = EntangledEdge(**rel_data)
        graph.add_edge(edge)
        
        # Maintain coherence
        if graph.measure_coherence() < 0.3:
            print("Warning: Coherence dropping, consider reducing edge weights")
    
    return graph
```

## Error Handling and Debugging

### Common Issues and Solutions

```python
def safe_graph_operations(graph):
    """Demonstrate safe graph operations with error handling."""
    
    try:
        # Safe node access
        if "Alice" in graph.nodes:
            alice_state = graph.get_node_state("Alice")
        else:
            print("Node 'Alice' not found in graph")
    
    except QuantumStateError as e:
        print(f"Quantum state error: {e}")
    
    try:
        # Safe entanglement measurement
        entanglement = graph.measure_entanglement("Alice", "Bob")
        if entanglement > 0.8:
            print("High entanglement detected")
    
    except NodeNotFoundError as e:
        print(f"Node error: {e}")
    
    except DecoherenceError as e:
        print(f"Decoherence detected: {e}")
        # Attempt to restore coherence
        graph.restore_coherence()

# Apply safe operations
safe_graph_operations(movie_graph)
```

## Next Steps

Congratulations! You've learned the basics of working with quantum entangled knowledge graphs. Here's what to explore next:

1. **Advanced Features**: Check out the [Advanced Tutorial](advanced.md) for complex reasoning patterns
2. **Custom Applications**: Learn to build domain-specific applications in [Custom Tutorial](custom.md)
3. **Real-world Examples**: Explore practical use cases in the [Examples](../examples.md) section
4. **API Reference**: Dive deeper into specific functions in the [API Documentation](../api/)

### Quick Reference

```python
# Essential imports
from qekgr import EntangledGraph, QuantumNode, EntangledEdge
from qekgr import EntangledQueryEngine, QuantumInference
from qekgr.utils import QuantumGraphVisualizer

# Basic workflow
graph = EntangledGraph(hilbert_dim=8)
graph.add_node(QuantumNode("id", node_type="type"))
graph.add_edge(EntangledEdge("id1", "id2", relation="rel", entanglement_strength=0.7))

query_engine = EntangledQueryEngine(graph)
results = query_engine.query("your question")

visualizer = QuantumGraphVisualizer(graph)
fig = visualizer.visualize_graph_2d()
```

You're now ready to build powerful quantum knowledge applications! 🚀⚛️
