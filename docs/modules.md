# API Reference Overview

Welcome to the comprehensive API reference for Quantum Entangled Knowledge Graphs (QE-KGR). This documentation provides detailed information about all classes, methods, and functions available in the library.

## 📚 Module Structure

QE-KGR is organized into four main modules:

- **[qekgr.graphs](api/graphs.md)** - Core graph structures and quantum node/edge implementations
- **[qekgr.reasoning](api/reasoning.md)** - Quantum inference algorithms and reasoning engines  
- **[qekgr.query](api/query.md)** - Natural language query processing and entangled search
- **[qekgr.utils](api/visualization.md)** - Visualization tools and utility functions

## 🚀 Quick Import Guide

### Main Classes

```python
# Core imports
from qekgr import EntangledGraph, QuantumInference, EntangledQueryEngine

# Graph components
from qekgr.graphs import QuantumNode, EntangledEdge

# Visualization
from qekgr.utils import QuantumGraphVisualizer

# CLI tools
from qekgr.cli import main as cli_main
```

### Common Usage Patterns

```python
# Create and populate graph
graph = EntangledGraph(hilbert_dim=4)
node = graph.add_quantum_node("entity", state="type")
edge = graph.add_entangled_edge("source", "target", 
                               relations=["relates"], 
                               amplitudes=[0.8])

# Reasoning and queries
inference = QuantumInference(graph)
query_engine = EntangledQueryEngine(graph)

# Visualization
visualizer = QuantumGraphVisualizer(graph)
```

## 🔧 Configuration Options

### Global Settings

```python
import qekgr

# Set global configuration
qekgr.config.set_default_hilbert_dim(8)
qekgr.config.set_decoherence_rate(0.1)
qekgr.config.set_visualization_theme('quantum')
```

### Environment Variables

```bash
export QEKGR_DEFAULT_HILBERT_DIM=4
export QEKGR_DECOHERENCE_RATE=0.05
export QEKGR_ENABLE_GPU=true
export QEKGR_CACHE_DIR=/tmp/qekgr_cache
```

## 📊 Data Types and Structures

### Core Data Types

| Type | Description | Example |
|------|-------------|---------|
| `complex128` | Complex quantum amplitudes | `0.8 + 0.6j` |
| `ndarray` | Quantum state vectors | `np.array([1, 0, 0, 0])` |
| `Dict[str, Any]` | Node/edge metadata | `{"type": "person", "age": 30}` |
| `List[str]` | Relation types | `["collaborates", "knows"]` |
| `Tuple[str, str]` | Edge keys | `("Alice", "Bob")` |

### Return Objects

```python
# Quantum walk result
@dataclass
class QuantumWalkResult:
    path: List[str]
    amplitudes: List[complex]
    final_state: np.ndarray
    entanglement_trace: List[float]
    interference_pattern: np.ndarray

# Query result  
@dataclass
class QueryResult:
    query: str
    answer_nodes: List[str]
    answer_edges: List[Tuple[str, str]]
    confidence_score: float
    quantum_amplitudes: List[complex]
    reasoning_path: List[str]
    metadata: Dict[str, Any]
```

## ⚡ Performance Considerations

### Memory Usage

```python
# Estimate memory usage
nodes = len(graph.nodes)
hilbert_dim = graph.hilbert_dim
estimated_memory = nodes * hilbert_dim**2 * 16  # bytes for complex128

print(f"Estimated memory: {estimated_memory / 1024**2:.1f} MB")
```

### Optimization Tips

1. **Hilbert Dimension**: Start with dim=2-4 for exploration, use 8+ for production
2. **Batch Operations**: Group node/edge additions for efficiency
3. **Caching**: Enable query caching for repeated searches
4. **GPU Acceleration**: Use CUDA-compatible operations when available

## 🔍 Error Handling

### Common Exceptions

```python
from qekgr.exceptions import (
    QuantumStateError,
    EntanglementError, 
    GraphStructureError,
    QueryParsingError
)

try:
    # Quantum operations
    graph.add_quantum_node("test", state="invalid_state")
except QuantumStateError as e:
    print(f"Invalid quantum state: {e}")

try:
    # Entanglement operations
    graph.add_entangled_edge("node1", "node2", relations=[], amplitudes=[0.5])
except EntanglementError as e:
    print(f"Entanglement error: {e}")
```

### Error Recovery

```python
def safe_quantum_operation(func, *args, **kwargs):
    """Safely execute quantum operation with fallback."""
    try:
        return func(*args, **kwargs)
    except QuantumStateError:
        # Fallback to default state
        return func(*args, state=None, **kwargs)
    except EntanglementError:
        # Use classical connection
        return func(*args, amplitudes=[1.0], **kwargs)
```

## 🧪 Testing and Validation

### Unit Testing

```python
import unittest
from qekgr import EntangledGraph

class TestQuantumGraph(unittest.TestCase):
    
    def setUp(self):
        self.graph = EntangledGraph(hilbert_dim=4)
    
    def test_node_creation(self):
        node = self.graph.add_quantum_node("test", state="physicist")
        self.assertIn("test", self.graph.nodes)
        self.assertEqual(len(node.state_vector), 4)
    
    def test_entanglement(self):
        self.graph.add_quantum_node("A", state="type1")
        self.graph.add_quantum_node("B", state="type2")
        edge = self.graph.add_entangled_edge("A", "B", 
                                           relations=["connects"], 
                                           amplitudes=[0.8])
        self.assertGreater(edge.entanglement_strength, 0)

if __name__ == '__main__':
    unittest.main()
```

## 📚 Module Documentation

For detailed API documentation of each module, see:

- **[Graphs Module](api/graphs.md)** - `EntangledGraph`, `QuantumNode`, `EntangledEdge`
- **[Reasoning Module](api/reasoning.md)** - `QuantumInference`, quantum walks, link prediction
- **[Query Module](api/query.md)** - `EntangledQueryEngine`, natural language processing
- **[Visualization Module](api/visualization.md)** - `QuantumGraphVisualizer`, plotting tools
