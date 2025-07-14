# Graphs Module

The `qekgr.graphs` module provides the fundamental data structures for quantum entangled knowledge graphs. This module contains the core classes that represent quantum nodes, entangled edges, and the graph structure itself.

## Classes Overview

### `EntangledGraph`

The main graph class that represents a quantum knowledge graph with entangled relationships.

### `QuantumNode`

Represents individual entities as quantum states in Hilbert space.

### `EntangledEdge`

Represents relationships between nodes as quantum entangled connections.

---

## EntangledGraph

### Class Definition

```python
class EntangledGraph:
    """
    Quantum Entangled Knowledge Graph implementation.
    
    This class represents knowledge as a quantum system where:
    - Nodes are quantum states in Hilbert space
    - Edges are entanglement tensors supporting superposed relations
    - Graph operations respect quantum mechanical principles
    """
```

### Constructor

```python
def __init__(self, hilbert_dim: int = 2) -> None
```

**Parameters:**

- `hilbert_dim` (int): Dimension of the Hilbert space for quantum states. Default is 2.

**Example:**

```python
from qekgr import EntangledGraph

# Create graph with 4-dimensional quantum states
graph = EntangledGraph(hilbert_dim=4)
print(f"Hilbert space dimension: {graph.hilbert_dim}")
```

### Properties

#### `hilbert_dim`

```python
@property
def hilbert_dim(self) -> int
```

Returns the dimension of the Hilbert space used for quantum states.

#### `nodes`

```python
@property  
def nodes(self) -> Dict[str, QuantumNode]
```

Returns dictionary of all quantum nodes in the graph.

#### `edges`

```python
@property
def edges(self) -> Dict[Tuple[str, str], EntangledEdge]
```

Returns dictionary of all entangled edges in the graph.

### Methods

#### `add_quantum_node`

```python
def add_quantum_node(
    self, 
    node_id: str, 
    state: Union[str, np.ndarray] = None, 
    metadata: Dict[str, Any] = None
) -> QuantumNode
```

Add a quantum node to the graph.

**Parameters:**

- `node_id` (str): Unique identifier for the node
- `state` (str or ndarray, optional): Initial quantum state. Can be:
  - String label (converted to quantum state)
  - Complex numpy array representing quantum state vector
  - None (uses default |0⟩ state)
- `metadata` (dict, optional): Additional node information

**Returns:**

- `QuantumNode`: The created quantum node object

**Raises:**

- `ValueError`: If node_id already exists or state is invalid
- `QuantumStateError`: If quantum state is not properly normalized

**Example:**

```python
# Add node with string state
alice = graph.add_quantum_node("Alice", state="physicist", 
                              metadata={"institution": "MIT"})

# Add node with custom quantum state  
custom_state = np.array([0.6, 0.8, 0.0, 0.0])  # Normalized
bob = graph.add_quantum_node("Bob", state=custom_state)

# Add node with default state
charlie = graph.add_quantum_node("Charlie")
```

#### `add_entangled_edge`

```python
def add_entangled_edge(
    self,
    source: Union[str, QuantumNode],
    target: Union[str, QuantumNode], 
    relations: List[str],
    amplitudes: List[Union[float, complex]],
    weight: float = 1.0
) -> EntangledEdge
```

Add an entangled edge between two nodes.

**Parameters:**

- `source` (str or QuantumNode): Source node (ID or object)
- `target` (str or QuantumNode): Target node (ID or object)
- `relations` (List[str]): List of relation types in superposition
- `amplitudes` (List[float/complex]): Quantum amplitudes for each relation
- `weight` (float, optional): Classical edge weight. Default is 1.0.

**Returns:**

- `EntangledEdge`: The created entangled edge object

**Raises:**

- `ValueError`: If nodes don't exist or relations/amplitudes length mismatch
- `EntanglementError`: If amplitudes are invalid

**Example:**

```python
# Simple entangled relationship
edge1 = graph.add_entangled_edge("Alice", "Bob",
                                relations=["collaborates"],
                                amplitudes=[0.8])

# Complex superposed relationship
edge2 = graph.add_entangled_edge(alice, bob,
                                relations=["collaborates", "friends", "co-authors"],
                                amplitudes=[0.8, 0.6, 0.4])

# With complex amplitudes
edge3 = graph.add_entangled_edge("Alice", "Charlie",
                                relations=["mentors", "advises"],
                                amplitudes=[0.7+0.2j, 0.5-0.1j])
```

#### `get_neighbors`

```python
def get_neighbors(self, node_id: str) -> List[str]
```

Get all neighboring nodes connected to the specified node.

**Parameters:**

- `node_id` (str): ID of the node to find neighbors for

**Returns:**

- `List[str]`: List of neighbor node IDs

**Example:**

```python
neighbors = graph.get_neighbors("Alice")
print(f"Alice's neighbors: {neighbors}")
```

#### `get_quantum_state_overlap`

```python
def get_quantum_state_overlap(self, node1_id: str, node2_id: str) -> complex
```

Calculate quantum state overlap between two nodes.

**Parameters:**

- `node1_id` (str): First node ID
- `node2_id` (str): Second node ID  

**Returns:**

- `complex`: Quantum overlap ⟨ψ₁|ψ₂⟩

**Example:**

```python
overlap = graph.get_quantum_state_overlap("Alice", "Bob")
similarity = abs(overlap)**2  # Probability of measurement agreement
print(f"Quantum similarity: {similarity:.3f}")
```

#### `measure_total_entanglement`

```python
def measure_total_entanglement(self) -> float
```

Calculate total entanglement in the graph.

**Returns:**

- `float`: Total entanglement measure

**Example:**

```python
total_entanglement = graph.measure_total_entanglement()
print(f"Graph entanglement: {total_entanglement:.3f}")
```

#### `get_adjacency_matrix`

```python
def get_adjacency_matrix(self) -> np.ndarray
```

Get quantum adjacency matrix representation.

**Returns:**

- `np.ndarray`: Complex adjacency matrix with quantum amplitudes

**Example:**

```python
adj_matrix = graph.get_adjacency_matrix()
print(f"Adjacency matrix shape: {adj_matrix.shape}")
print(f"Is Hermitian: {np.allclose(adj_matrix, adj_matrix.conj().T)}")
```

---

## QuantumNode

### Class Definition

```python
@dataclass
class QuantumNode:
    """
    Represents a quantum node in the entangled graph.
    
    Attributes:
        node_id: Unique identifier for the node
        state_vector: Complex vector representing quantum state |ψ⟩
        density_matrix: Density matrix ρ for mixed states
        metadata: Additional node information
    """
```

### Attributes

- `node_id` (str): Unique identifier
- `state_vector` (np.ndarray): Quantum state vector |ψ⟩
- `density_matrix` (np.ndarray): Density matrix ρ = |ψ⟩⟨ψ|
- `metadata` (Dict[str, Any]): Additional node information

### Properties

#### `hilbert_dim`

```python
@property
def hilbert_dim(self) -> int
```

Get the dimension of the Hilbert space.

### Methods

#### `measure_entropy`

```python
def measure_entropy(self) -> float
```

Calculate von Neumann entropy S = -Tr(ρ log ρ).

**Returns:**

- `float`: Von Neumann entropy of the quantum state

**Example:**

```python
node = graph.nodes["Alice"]
entropy = node.measure_entropy()
print(f"Alice's quantum entropy: {entropy:.3f}")

# Pure states have zero entropy
# Mixed states have positive entropy
```

#### `evolve_state`

```python
def evolve_state(self, unitary: np.ndarray) -> None
```

Evolve quantum state using unitary transformation.

**Parameters:**

- `unitary` (np.ndarray): Unitary matrix for state evolution

**Example:**

```python
import numpy as np

# Pauli-X rotation (bit flip)
pauli_x = np.array([[0, 1, 0, 0],
                   [1, 0, 0, 0], 
                   [0, 0, 0, 1],
                   [0, 0, 1, 0]])

node = graph.nodes["Alice"]
node.evolve_state(pauli_x)
```

#### `collapse_state`

```python
def collapse_state(self, measurement_basis: np.ndarray) -> Tuple[int, float]
```

Perform quantum measurement and collapse state.

**Parameters:**

- `measurement_basis` (np.ndarray): Measurement basis vectors

**Returns:**

- `Tuple[int, float]`: (outcome_index, measurement_probability)

**Example:**

```python
# Computational basis measurement
computational_basis = np.eye(4)
outcome, probability = node.collapse_state(computational_basis)
print(f"Measurement outcome: {outcome}, probability: {probability:.3f}")
```

---

## EntangledEdge

### Class Definition

```python
@dataclass
class EntangledEdge:
    """
    Represents an entangled edge between quantum nodes.
    
    Attributes:
        source_id: Source node identifier
        target_id: Target node identifier
        relations: List of relation types in superposition
        amplitudes: Complex amplitudes for each relation
        entanglement_tensor: Tensor representing the entanglement
        weight: Classical weight for the edge
    """
```

### Attributes

- `source_id` (str): Source node identifier
- `target_id` (str): Target node identifier  
- `relations` (List[str]): Relation types in superposition
- `amplitudes` (List[complex]): Quantum amplitudes for relations
- `entanglement_tensor` (np.ndarray): Entanglement tensor representation
- `weight` (float): Classical edge weight

### Properties

#### `entanglement_strength`

```python
@property
def entanglement_strength(self) -> float
```

Calculate entanglement strength from amplitude superposition.

### Methods

#### `collapse_relation`

```python
def collapse_relation(self) -> str
```

Collapse superposed relations to a single relation via measurement.

**Returns:**

- `str`: Measured relation type

**Example:**

```python
edge = graph.edges[("Alice", "Bob")]
print(f"Relations in superposition: {edge.relations}")
print(f"Amplitudes: {edge.amplitudes}")

# Quantum measurement collapses to single relation
measured_relation = edge.collapse_relation()
print(f"Measured relation: {measured_relation}")
```

#### `measure_entanglement_entropy`

```python
def measure_entanglement_entropy(self) -> float
```

Calculate entanglement entropy for the edge.

**Returns:**

- `float`: Entanglement entropy

#### `evolve_amplitudes`

```python
def evolve_amplitudes(self, evolution_operator: np.ndarray) -> None
```

Evolve quantum amplitudes using given operator.

**Parameters:**

- `evolution_operator` (np.ndarray): Evolution operator for amplitudes

## Usage Examples

### Basic Graph Construction

```python
from qekgr import EntangledGraph
import numpy as np

# Create quantum knowledge graph
graph = EntangledGraph(hilbert_dim=4)

# Add entities as quantum nodes
alice = graph.add_quantum_node("Alice", state="researcher",
                              metadata={"field": "quantum_physics", "h_index": 25})

bob = graph.add_quantum_node("Bob", state="professor", 
                            metadata={"field": "computer_science", "h_index": 40})

# Create superposed relationship
graph.add_entangled_edge(alice, bob,
                        relations=["collaborates", "co-authors", "friends"],
                        amplitudes=[0.8, 0.6, 0.4])

print(f"Graph: {len(graph.nodes)} nodes, {len(graph.edges)} edges")
print(f"Total entanglement: {graph.measure_total_entanglement():.3f}")
```

### Quantum State Manipulation

```python
# Access and modify quantum states
alice_node = graph.nodes["Alice"]
print(f"Alice's quantum state: {alice_node.state_vector}")
print(f"Alice's entropy: {alice_node.measure_entropy():.3f}")

# Create custom superposition state
theta = np.pi / 3
custom_state = np.array([
    np.cos(theta/2),
    np.sin(theta/2),
    0,
    0
])

charlie = graph.add_quantum_node("Charlie", state=custom_state)
print(f"Charlie's state: {charlie.state_vector}")
```

### Edge Analysis

```python
# Analyze entangled relationships
edge = graph.edges[("Alice", "Bob")]
print(f"Edge relations: {edge.relations}")
print(f"Edge amplitudes: {edge.amplitudes}")
print(f"Entanglement strength: {edge.entanglement_strength:.3f}")

# Measure quantum overlap between nodes
overlap = graph.get_quantum_state_overlap("Alice", "Bob")
print(f"Quantum overlap: {overlap}")
print(f"State similarity: {abs(overlap)**2:.3f}")
```

## Performance Notes

- **Memory Usage**: Each node requires O(d²) memory where d is Hilbert dimension
- **Computation**: Quantum operations scale as O(d²) to O(d³)
- **Recommended Dimensions**: 
  - d=2-4 for exploration and prototyping
  - d=8-16 for production applications
  - d=32+ for high-dimensional semantic embeddings

## Error Handling

The graphs module provides several custom exceptions:

```python
try:
    # Invalid quantum state
    bad_state = np.array([1, 1, 1, 1])  # Not normalized
    graph.add_quantum_node("bad", state=bad_state)
except QuantumStateError as e:
    print(f"Quantum state error: {e}")

try:
    # Mismatched relations and amplitudes
    graph.add_entangled_edge("A", "B", 
                           relations=["rel1", "rel2"],
                           amplitudes=[0.5])  # Wrong length
except EntanglementError as e:
    print(f"Entanglement error: {e}")
```

This module forms the foundation of QE-KGR, providing the quantum-enhanced data structures needed for advanced knowledge graph reasoning! ⚛️📊
