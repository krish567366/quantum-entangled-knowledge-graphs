# Reasoning Module

The `qekgr.reasoning` module implements quantum-enhanced reasoning algorithms for entangled knowledge graphs. This module provides the `QuantumInference` class and associated algorithms for quantum walks, link prediction, and subgraph discovery.

## Classes Overview

### `QuantumInference`

Main quantum reasoning engine that performs quantum walks, link prediction, and subgraph discovery.

### Result Classes

- `QuantumWalkResult` - Results from quantum walk operations
- `LinkPrediction` - Link prediction results with quantum confidence  
- `SubgraphDiscovery` - Subgraph discovery results

---

## QuantumInference

### Class Definition

```python
class QuantumInference:
    """
    Quantum-enhanced reasoning engine for entangled knowledge graphs.
    
    This class implements quantum algorithms for reasoning over knowledge
    graphs using quantum mechanical principles like superposition, 
    entanglement, and interference.
    """
```

### Constructor

```python
def __init__(self, graph: EntangledGraph) -> None
```

**Parameters:**

- `graph` (EntangledGraph): The entangled graph to reason over

**Example:**

```python
from qekgr import EntangledGraph, QuantumInference

graph = EntangledGraph(hilbert_dim=4)
# ... add nodes and edges ...
inference = QuantumInference(graph)
```

### Properties

#### `decoherence_rate`

```python
@property
def decoherence_rate(self) -> float
```

Rate of quantum decoherence (default: 0.1).

#### `interference_threshold`

```python  
@property
def interference_threshold(self) -> float
```

Threshold for constructive interference (default: 0.5).

### Core Methods

#### `quantum_walk`

```python
def quantum_walk(
    self,
    start_node: str,
    steps: int = 10,
    bias_relations: Optional[List[str]] = None
) -> QuantumWalkResult
```

Perform quantum walk on the entangled graph.

**Parameters:**

- `start_node` (str): Starting node for the walk
- `steps` (int): Number of quantum walk steps (default: 10)
- `bias_relations` (List[str], optional): Relations to bias the walk towards

**Returns:**

- `QuantumWalkResult`: Complete walk results with quantum information

**Example:**

```python
# Basic quantum walk
walk_result = inference.quantum_walk("Alice", steps=15)
print(f"Walk path: {' → '.join(walk_result.path)}")
print(f"Final amplitudes: {walk_result.amplitudes[-1]}")

# Biased quantum walk
biased_walk = inference.quantum_walk(
    start_node="Alice",
    steps=20,
    bias_relations=["collaborates", "mentors"]
)
print(f"Biased path: {' → '.join(biased_walk.path)}")
```

#### `predict_links`

```python
def predict_links(
    self,
    source_node: str,
    max_predictions: int = 5,
    min_confidence: float = 0.3
) -> List[LinkPrediction]
```

Predict missing links using quantum interference.

**Parameters:**

- `source_node` (str): Source node for link prediction
- `max_predictions` (int): Maximum number of predictions (default: 5)
- `min_confidence` (float): Minimum confidence threshold (default: 0.3)

**Returns:**

- `List[LinkPrediction]`: Ranked list of link predictions

**Example:**

```python
# Predict links from Alice
predictions = inference.predict_links("Alice", max_predictions=3)

for pred in predictions:
    print(f"{pred.source_node} → {pred.target_node}")
    print(f"  Relations: {pred.predicted_relations}")
    print(f"  Quantum score: {pred.quantum_score:.3f}")
    print(f"  Classical score: {pred.classical_score:.3f}")
```

#### `discover_entangled_subgraph`

```python
def discover_entangled_subgraph(
    self,
    seed_nodes: List[str],
    expansion_steps: int = 3,
    min_entanglement: float = 0.4
) -> SubgraphDiscovery
```

Discover highly entangled subgraphs using quantum expansion.

**Parameters:**

- `seed_nodes` (List[str]): Starting nodes for expansion
- `expansion_steps` (int): Number of expansion steps (default: 3)
- `min_entanglement` (float): Minimum entanglement threshold (default: 0.4)

**Returns:**

- `SubgraphDiscovery`: Discovered subgraph with quantum measures

**Example:**

```python
# Discover molecular pathway
subgraph = inference.discover_entangled_subgraph(
    seed_nodes=["COX1", "COX2"],
    expansion_steps=4,
    min_entanglement=0.5
)

print(f"Discovered nodes: {', '.join(list(subgraph.nodes))}")
print(f"Network density: {subgraph.entanglement_density:.3f}")
print(f"Coherence measure: {subgraph.coherence_measure:.3f}")
```

#### `grover_search`

```python
def grover_search(
    self,
    target_criteria: Dict[str, Any],
    max_iterations: int = None
) -> List[Tuple[str, float]]
```

Quantum search using Grover's algorithm for marked nodes.

**Parameters:**

- `target_criteria` (Dict[str, Any]): Search criteria for target nodes
- `max_iterations` (int, optional): Maximum search iterations

**Returns:**

- `List[Tuple[str, float]]`: List of (node_id, probability) pairs

**Example:**

```python
# Search for specific node types
results = inference.grover_search(
    target_criteria={"metadata.field": "quantum_physics"},
    max_iterations=5
)

for node_id, probability in results:
    print(f"Found: {node_id} (probability: {probability:.3f})")
```

### Advanced Methods

#### `measure_quantum_centrality`

```python
def measure_quantum_centrality(
    self,
    centrality_type: str = "quantum_pagerank"
) -> Dict[str, float]
```

Calculate quantum centrality measures for all nodes.

**Parameters:**

- `centrality_type` (str): Type of centrality ("quantum_pagerank", "quantum_betweenness")

**Returns:**

- `Dict[str, float]`: Centrality scores for each node

**Example:**

```python
# Quantum PageRank
pagerank_scores = inference.measure_quantum_centrality("quantum_pagerank")
for node, score in sorted(pagerank_scores.items(), key=lambda x: x[1], reverse=True):
    print(f"{node}: {score:.3f}")

# Quantum betweenness centrality
betweenness = inference.measure_quantum_centrality("quantum_betweenness")
```

#### `quantum_community_detection`

```python
def quantum_community_detection(
    self,
    resolution: float = 1.0,
    method: str = "spectral"
) -> Dict[str, int]
```

Detect communities using quantum modularity optimization.

**Parameters:**

- `resolution` (float): Community detection resolution (default: 1.0)
- `method` (str): Detection method ("spectral", "quantum_modularity")

**Returns:**

- `Dict[str, int]`: Community assignment for each node

**Example:**

```python
# Detect quantum communities
communities = inference.quantum_community_detection(resolution=1.2)

# Group nodes by community
from collections import defaultdict
community_groups = defaultdict(list)
for node, community_id in communities.items():
    community_groups[community_id].append(node)

for community_id, nodes in community_groups.items():
    print(f"Community {community_id}: {', '.join(nodes)}")
```

#### `simulate_quantum_dynamics`

```python
def simulate_quantum_dynamics(
    self,
    time_steps: int = 100,
    dt: float = 0.01,
    hamiltonian_type: str = "adjacency"
) -> List[Dict[str, complex]]
```

Simulate quantum dynamics evolution of the graph.

**Parameters:**

- `time_steps` (int): Number of time evolution steps
- `dt` (float): Time step size
- `hamiltonian_type` (str): Type of Hamiltonian ("adjacency", "laplacian")

**Returns:**

- `List[Dict[str, complex]]`: Time evolution of quantum amplitudes

**Example:**

```python
# Simulate quantum evolution
evolution = inference.simulate_quantum_dynamics(
    time_steps=50,
    dt=0.05,
    hamiltonian_type="laplacian"
)

# Analyze evolution at different times
initial_state = evolution[0]
final_state = evolution[-1]

print("Initial quantum amplitudes:")
for node, amplitude in initial_state.items():
    print(f"  {node}: {amplitude}")
```

---

## Result Classes

### QuantumWalkResult

```python
@dataclass
class QuantumWalkResult:
    """Result of a quantum walk operation."""
    path: List[str]                    # Sequence of visited nodes
    amplitudes: List[complex]          # Quantum amplitudes at each step
    final_state: np.ndarray           # Final quantum state vector
    entanglement_trace: List[float]   # Entanglement evolution over time
    interference_pattern: np.ndarray  # Quantum interference pattern
```

**Properties:**

- `path_length` (int): Length of the walk path
- `total_entanglement` (float): Total entanglement accumulated
- `coherence_measure` (float): Quantum coherence of final state

**Methods:**

```python
def get_visit_probabilities(self) -> Dict[str, float]
    """Get probability of visiting each node."""

def measure_interference_strength(self) -> float
    """Measure strength of quantum interference effects."""
```

**Example:**

```python
walk_result = inference.quantum_walk("Alice", steps=20)

# Analyze walk results
print(f"Path length: {walk_result.path_length}")
print(f"Total entanglement: {walk_result.total_entanglement:.3f}")

visit_probs = walk_result.get_visit_probabilities()
print("Visit probabilities:")
for node, prob in visit_probs.items():
    print(f"  {node}: {prob:.3f}")

interference = walk_result.measure_interference_strength()
print(f"Interference strength: {interference:.3f}")
```

### LinkPrediction

```python
@dataclass
class LinkPrediction:
    """Link prediction result with quantum confidence."""
    source_node: str                      # Source node ID
    target_node: str                      # Target node ID  
    predicted_relations: List[str]        # Predicted relation types
    confidence_amplitudes: List[complex]  # Quantum confidence amplitudes
    quantum_score: float                  # Quantum prediction score
    classical_score: float               # Classical prediction score
```

**Properties:**

- `combined_score` (float): Weighted combination of quantum and classical scores
- `prediction_uncertainty` (float): Quantum uncertainty in prediction

**Example:**

```python
predictions = inference.predict_links("Alice")

for pred in predictions:
    print(f"Prediction: {pred.source_node} → {pred.target_node}")
    print(f"  Relations: {pred.predicted_relations}")
    print(f"  Combined score: {pred.combined_score:.3f}")
    print(f"  Uncertainty: {pred.prediction_uncertainty:.3f}")
```

### SubgraphDiscovery  

```python
@dataclass
class SubgraphDiscovery:
    """Subgraph discovery result."""
    nodes: Set[str]                    # Discovered nodes
    edges: List[Tuple[str, str]]       # Discovered edges
    entanglement_density: float       # Density of entanglement
    coherence_measure: float          # Quantum coherence of subgraph
    discovery_confidence: float       # Confidence in discovery
```

**Methods:**

```python
def get_subgraph(self, original_graph: EntangledGraph) -> EntangledGraph
    """Extract discovered subgraph from original graph."""

def measure_modularity(self) -> float
    """Calculate quantum modularity of discovered subgraph."""
```

**Example:**

```python
subgraph = inference.discover_entangled_subgraph(["Alice", "Bob"])

# Extract as new graph
discovered_graph = subgraph.get_subgraph(original_graph)
modularity = subgraph.measure_modularity()

print(f"Subgraph modularity: {modularity:.3f}")
print(f"Subgraph size: {len(subgraph.nodes)} nodes, {len(subgraph.edges)} edges")
```

## Advanced Usage Examples

### Multi-step Quantum Reasoning

```python
def quantum_reasoning_pipeline(graph, start_node, target_criteria):
    """Complete quantum reasoning pipeline."""
    
    inference = QuantumInference(graph)
    
    # Step 1: Quantum walk exploration
    walk_result = inference.quantum_walk(start_node, steps=15)
    exploration_nodes = list(set(walk_result.path))
    
    # Step 2: Community detection around exploration
    communities = inference.quantum_community_detection()
    relevant_community = communities[start_node]
    community_nodes = [node for node, comm in communities.items() 
                      if comm == relevant_community]
    
    # Step 3: Subgraph discovery
    subgraph = inference.discover_entangled_subgraph(
        seed_nodes=community_nodes[:3],
        expansion_steps=3
    )
    
    # Step 4: Link prediction within subgraph
    predictions = []
    for node in subgraph.nodes:
        node_predictions = inference.predict_links(node, max_predictions=2)
        predictions.extend(node_predictions)
    
    # Step 5: Grover search for targets
    search_results = inference.grover_search(target_criteria)
    
    return {
        'exploration': walk_result,
        'communities': communities,
        'subgraph': subgraph,
        'predictions': predictions,
        'search_results': search_results
    }

# Execute pipeline
results = quantum_reasoning_pipeline(
    graph=my_graph,
    start_node="Alice",
    target_criteria={"metadata.field": "quantum_computing"}
)
```

### Quantum Knowledge Discovery

```python
def discover_hidden_patterns(graph, seed_concepts):
    """Discover hidden patterns using quantum interference."""
    
    inference = QuantumInference(graph)
    discovered_patterns = []
    
    for concept in seed_concepts:
        # Quantum walk from each concept
        walk = inference.quantum_walk(concept, steps=12)
        
        # Find nodes with high interference
        interference = walk.interference_pattern
        high_interference_nodes = []
        
        for i, amplitude in enumerate(interference):
            if abs(amplitude) > 0.7:  # High interference threshold
                node_id = list(graph.nodes.keys())[i]
                high_interference_nodes.append(node_id)
        
        # Discover subgraph around high-interference nodes
        if high_interference_nodes:
            pattern_subgraph = inference.discover_entangled_subgraph(
                seed_nodes=high_interference_nodes[:2],
                min_entanglement=0.6
            )
            
            discovered_patterns.append({
                'seed_concept': concept,
                'pattern_nodes': pattern_subgraph.nodes,
                'coherence': pattern_subgraph.coherence_measure,
                'confidence': pattern_subgraph.discovery_confidence
            })
    
    return discovered_patterns

# Discover patterns
patterns = discover_hidden_patterns(graph, ["quantum_mechanics", "machine_learning"])
for pattern in patterns:
    print(f"Pattern from {pattern['seed_concept']}:")
    print(f"  Nodes: {', '.join(list(pattern['pattern_nodes']))}")
    print(f"  Coherence: {pattern['coherence']:.3f}")
```

## Performance Optimization

### Caching and Memoization

```python
from functools import lru_cache

class CachedQuantumInference(QuantumInference):
    """Performance-optimized quantum inference with caching."""
    
    def __init__(self, graph, cache_size=128):
        super().__init__(graph)
        self.cache_size = cache_size
    
    @lru_cache(maxsize=128)
    def cached_quantum_walk(self, start_node, steps, bias_tuple=None):
        """Cached version of quantum walk."""
        bias_relations = list(bias_tuple) if bias_tuple else None
        return self.quantum_walk(start_node, steps, bias_relations)
    
    def batch_link_predictions(self, nodes, max_predictions=5):
        """Batch process multiple link predictions."""
        all_predictions = []
        
        # Process in batches to optimize memory usage
        batch_size = 10
        for i in range(0, len(nodes), batch_size):
            batch = nodes[i:i+batch_size]
            batch_results = []
            
            for node in batch:
                predictions = self.predict_links(node, max_predictions)
                batch_results.extend(predictions)
            
            all_predictions.extend(batch_results)
        
        return all_predictions

# Use cached inference
cached_inference = CachedQuantumInference(graph, cache_size=256)
```

## Error Handling

```python
from qekgr.exceptions import QuantumInferenceError, ConvergenceError

try:
    # Quantum walk might fail for disconnected graphs
    walk_result = inference.quantum_walk("isolated_node", steps=10)
except QuantumInferenceError as e:
    print(f"Quantum inference error: {e}")
    # Fallback to classical random walk
    
try:
    # Community detection might not converge
    communities = inference.quantum_community_detection()
except ConvergenceError as e:
    print(f"Algorithm did not converge: {e}")
    # Use alternative method
```

The reasoning module provides the core quantum algorithms that enable QE-KGR to discover patterns and relationships that would be impossible to find with classical graph algorithms! 🧠⚛️
