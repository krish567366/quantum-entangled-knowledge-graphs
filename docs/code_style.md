# Code Style Guide for QE-KGR

This document outlines the coding standards, conventions, and best practices for the Quantum Entangled Knowledge Graphs (QE-KGR) project. Following these guidelines ensures code consistency, readability, and maintainability across the project.

## 📋 General Principles

### Code Philosophy

- **Clarity over cleverness**: Write code that is easy to understand and maintain
- **Quantum-aware design**: Consider quantum mechanics principles in API design
- **Performance with readability**: Optimize for performance without sacrificing clarity
- **Comprehensive documentation**: Every public interface should be well-documented
- **Test-driven development**: Write tests alongside code implementation

## 🐍 Python Style Standards

### Base Standards

We follow **PEP 8** with specific modifications and additions for quantum computing contexts.

### Line Length

- **Maximum line length**: 88 characters (Black formatter default)
- **Docstring line length**: 72 characters
- **Comment line length**: 72 characters

### Imports

```python
# Standard library imports first
import os
import sys
from typing import Dict, List, Optional, Union, Tuple

# Third-party imports second
import numpy as np
import networkx as nx
from scipy.sparse import csr_matrix

# Local imports last
from qekgr.graphs import QuantumNode, EntangledEdge
from qekgr.utils import normalize_quantum_state
```

### Naming Conventions

#### Variables and Functions
```python
# Use snake_case for variables and functions
quantum_state_vector = np.array([1+0j, 0+1j])
entanglement_strength = 0.75

def calculate_quantum_overlap(state_a: np.ndarray, state_b: np.ndarray) -> complex:
    """Calculate overlap between quantum states."""
    return np.vdot(state_a, state_b)
```

#### Classes
```python
# Use PascalCase for classes
class EntangledGraph:
    """Represents a quantum entangled knowledge graph."""
    
class QuantumInferenceEngine:
    """Provides quantum-enhanced reasoning capabilities."""
```

#### Constants
```python
# Use UPPER_SNAKE_CASE for constants
DEFAULT_HILBERT_DIMENSION = 8
MAX_QUANTUM_WALK_STEPS = 1000
PLANCK_CONSTANT = 6.62607015e-34
```

#### Quantum-Specific Naming
```python
# Quantum states and operators
psi_state = np.array([0.6+0.8j, 0.0+0.0j])  # Use Greek letters for states
hamiltonian_matrix = np.array([[1, 0], [0, -1]])  # Descriptive operator names
density_matrix = np.outer(psi_state, np.conj(psi_state))

# Quantum measurements
measurement_probabilities = np.abs(psi_state)**2
expectation_value = np.real(np.vdot(psi_state, hamiltonian_matrix @ psi_state))

# Entanglement measures
entanglement_entropy = calculate_von_neumann_entropy(density_matrix)
quantum_coherence = calculate_coherence_measure(psi_state)
```

## 🔬 Quantum Computing Conventions

### Complex Numbers

```python
# Always use complex datatypes for quantum amplitudes
amplitude = 0.707 + 0.707j  # Explicit complex notation
# Or
amplitude = complex(0.707, 0.707)

# For arrays representing quantum states
quantum_state = np.array([1+0j, 0+0j], dtype=complex)
```

### State Normalization

```python
def normalize_quantum_state(state: np.ndarray) -> np.ndarray:
    """Normalize quantum state to unit norm.
    
    Args:
        state: Quantum state vector
        
    Returns:
        Normalized quantum state
        
    Raises:
        ValueError: If state has zero norm
    """
    norm = np.linalg.norm(state)
    if np.isclose(norm, 0):
        raise ValueError("Cannot normalize zero state")
    return state / norm
```

### Quantum Operations

```python
# Always verify unitarity for quantum operators
def verify_unitary(operator: np.ndarray, tolerance: float = 1e-10) -> bool:
    """Verify if operator is unitary."""
    product = operator @ operator.T.conj()
    identity = np.eye(operator.shape[0])
    return np.allclose(product, identity, atol=tolerance)

# Include quantum mechanics validation
def apply_quantum_operation(state: np.ndarray, operator: np.ndarray) -> np.ndarray:
    """Apply quantum operator to state."""
    if not verify_unitary(operator):
        raise ValueError("Operator must be unitary")
    return operator @ state
```

## 📝 Documentation Standards

### Docstring Format

We use **Google style** docstrings with quantum-specific extensions:

```python
def quantum_walk(
    self,
    start_node: str,
    steps: int,
    bias_relations: Optional[List[str]] = None,
    measurement_basis: str = "computational"
) -> QuantumWalkResult:
    """Perform quantum walk on entangled graph.
    
    This function implements a discrete-time quantum walk using the 
    coin-position formalism on the entangled graph structure.
    
    Args:
        start_node: Starting node identifier for the walk
        steps: Number of quantum walk steps to perform
        bias_relations: Optional list of edge relations to bias walk
        measurement_basis: Measurement basis for final state ("computational" or "position")
    
    Returns:
        QuantumWalkResult containing:
            - path: Most probable path taken
            - final_state: Final quantum state vector  
            - probabilities: Position probability distribution
            - coherence: Quantum coherence measure
    
    Raises:
        ValueError: If start_node not in graph or steps < 0
        QuantumError: If quantum state evolution fails
    
    Quantum Details:
        The walk uses a Hadamard coin operator and standard shift operator.
        Entanglement between nodes modifies the transition amplitudes.
        
    Mathematical Formulation:
        U = S(C ⊗ I) where S is shift, C is coin, I is identity
        
    Example:
        >>> graph = EntangledGraph()
        >>> graph.add_quantum_node("A", "state_a")
        >>> result = graph.quantum_walk("A", steps=10)
        >>> print(f"Final position: {result.path[-1]}")
    """
```

### Class Documentation

```python
class EntangledGraph:
    """Quantum entangled knowledge graph representation.
    
    This class implements a knowledge graph where nodes represent entities
    in quantum superposition states and edges represent entangled relationships
    between entities. The graph operates in a Hilbert space of specified
    dimension.
    
    Attributes:
        hilbert_dim: Dimension of the Hilbert space
        nodes: Dictionary mapping node IDs to QuantumNode objects
        edges: Dictionary mapping edge tuples to EntangledEdge objects
        quantum_register: Global quantum state register
        
    Quantum Properties:
        - Nodes exist in superposition of multiple classical states
        - Edges create quantum entanglement between node states
        - Graph evolution preserves quantum coherence
        - Measurements collapse superposition states
        
    Example:
        >>> graph = EntangledGraph(hilbert_dim=8)
        >>> graph.add_quantum_node("alice", "person")
        >>> graph.add_quantum_node("quantum_physics", "concept")
        >>> graph.add_entangled_edge("alice", "quantum_physics", 
        ...                         ["studies", "researches"], [0.8, 0.6])
    """
```

### Module Documentation

```python
"""Quantum inference algorithms for entangled knowledge graphs.

This module provides quantum-enhanced reasoning algorithms that leverage
quantum mechanics principles for graph analysis and inference. The algorithms
include quantum walks, entangled subgraph discovery, and quantum machine
learning approaches.

Quantum Algorithms:
    - Quantum Random Walks: Enhanced graph traversal using quantum superposition
    - Quantum Link Prediction: Entanglement-based relationship prediction  
    - Quantum Community Detection: Coherence-based clustering
    - Quantum Centrality: Quantum PageRank and eigenvector centrality

Mathematical Foundation:
    The algorithms operate on quantum states |ψ⟩ ∈ ℂⁿ where n is the
    Hilbert space dimension. Evolution follows the Schrödinger equation:
    iℏ d|ψ⟩/dt = Ĥ|ψ⟩

Usage:
    >>> from qekgr.reasoning import QuantumInference
    >>> inference = QuantumInference(graph)
    >>> result = inference.quantum_walk("start_node", steps=20)
"""
```

## 🧪 Testing Standards

### Test Structure

```python
import pytest
import numpy as np
from unittest.mock import Mock, patch

from qekgr import EntangledGraph
from qekgr.reasoning import QuantumInference

class TestQuantumInference:
    """Test suite for quantum inference algorithms."""
    
    @pytest.fixture
    def sample_graph(self):
        """Create sample graph for testing."""
        graph = EntangledGraph(hilbert_dim=4)
        graph.add_quantum_node("A", "type_a")
        graph.add_quantum_node("B", "type_b") 
        graph.add_entangled_edge("A", "B", ["connects"], [0.8])
        return graph
    
    @pytest.fixture
    def inference_engine(self, sample_graph):
        """Create inference engine with sample graph."""
        return QuantumInference(sample_graph)
    
    def test_quantum_walk_basic_functionality(self, inference_engine):
        """Test basic quantum walk execution."""
        # Arrange
        start_node = "A"
        steps = 5
        
        # Act
        result = inference_engine.quantum_walk(start_node, steps)
        
        # Assert
        assert result.path[0] == start_node
        assert len(result.path) == steps + 1
        assert 0 <= result.final_probability <= 1
        assert np.isclose(np.linalg.norm(result.final_state), 1.0)
    
    @pytest.mark.parametrize("steps", [1, 5, 10, 50])
    def test_quantum_walk_various_steps(self, inference_engine, steps):
        """Test quantum walk with various step counts."""
        result = inference_engine.quantum_walk("A", steps)
        assert len(result.path) == steps + 1
    
    def test_quantum_state_normalization(self, inference_engine):
        """Test quantum state remains normalized during walk."""
        result = inference_engine.quantum_walk("A", steps=10)
        norm = np.linalg.norm(result.final_state)
        assert np.isclose(norm, 1.0, rtol=1e-10)
    
    def test_invalid_start_node_raises_error(self, inference_engine):
        """Test error handling for invalid start node."""
        with pytest.raises(ValueError, match="Node 'invalid' not found"):
            inference_engine.quantum_walk("invalid", steps=5)
    
    @pytest.mark.slow
    def test_quantum_walk_performance(self, inference_engine):
        """Test performance with large step count."""
        import time
        start_time = time.time()
        result = inference_engine.quantum_walk("A", steps=1000)
        end_time = time.time()
        
        # Should complete within reasonable time
        assert end_time - start_time < 5.0
        assert result is not None
```

### Quantum Testing Considerations

```python
def test_quantum_properties():
    """Test quantum mechanics properties are preserved."""
    graph = EntangledGraph(hilbert_dim=4)
    
    # Test state normalization
    state = graph.get_quantum_state("node_id")
    assert np.isclose(np.linalg.norm(state), 1.0)
    
    # Test unitarity of operations
    operator = graph.get_evolution_operator()
    assert verify_unitary(operator)
    
    # Test entanglement measures
    entanglement = graph.calculate_entanglement("A", "B")
    assert 0 <= entanglement <= 1

def test_numerical_stability():
    """Test numerical stability with quantum operations."""
    # Test with very small amplitudes
    small_state = np.array([1e-15 + 1e-15j, 1.0 + 0j])
    normalized = normalize_quantum_state(small_state)
    assert np.isfinite(normalized).all()
    
    # Test with large phase factors
    large_phase = np.exp(1j * 1000)
    state_with_phase = np.array([large_phase, 0])
    assert np.isclose(np.linalg.norm(state_with_phase), 1.0)
```

## 🚀 Performance Guidelines

### Efficient Quantum Operations

```python
# Use vectorized operations for quantum states
def efficient_state_evolution(states: np.ndarray, operator: np.ndarray) -> np.ndarray:
    """Evolve multiple quantum states efficiently."""
    # Good: Vectorized matrix multiplication
    return operator @ states
    
    # Avoid: Loop over individual states
    # return np.array([operator @ state for state in states.T]).T

# Cache expensive quantum calculations
from functools import lru_cache

@lru_cache(maxsize=128)
def cached_quantum_operation(state_tuple: tuple, operator_tuple: tuple) -> tuple:
    """Cache quantum operations for repeated calculations."""
    state = np.array(state_tuple)
    operator = np.array(operator_tuple)
    result = operator @ state
    return tuple(result)
```

### Memory Management

```python
class QuantumGraph:
    """Memory-efficient quantum graph implementation."""
    
    def __init__(self, hilbert_dim: int):
        # Use appropriate data types
        self._states = {}  # Store only when needed
        self._sparse_operators = {}  # Use sparse matrices for large operators
    
    def get_state(self, node_id: str) -> np.ndarray:
        """Get quantum state with lazy loading."""
        if node_id not in self._states:
            self._states[node_id] = self._compute_state(node_id)
        return self._states[node_id]
    
    def clear_cache(self) -> None:
        """Clear cached states to free memory."""
        self._states.clear()
```

## 🔧 Error Handling

### Quantum-Specific Errors

```python
class QuantumError(Exception):
    """Base exception for quantum-related errors."""
    pass

class StateNormalizationError(QuantumError):
    """Raised when quantum state normalization fails."""
    pass

class EntanglementError(QuantumError):
    """Raised when entanglement operations fail."""
    pass

def safe_quantum_operation(state: np.ndarray) -> np.ndarray:
    """Perform quantum operation with proper error handling."""
    try:
        if np.isclose(np.linalg.norm(state), 0):
            raise StateNormalizationError("Cannot operate on zero state")
        
        # Perform operation
        result = some_quantum_operation(state)
        
        # Validate result
        if not np.isfinite(result).all():
            raise QuantumError("Operation produced non-finite values")
        
        return result
        
    except np.linalg.LinAlgError as e:
        raise QuantumError(f"Linear algebra error in quantum operation: {e}")
```

## 📊 Code Quality Tools

### Formatting

```bash
# Use Black for code formatting
black qekgr/ tests/

# Configuration in pyproject.toml
[tool.black]
line-length = 88
target-version = ['py38']
```

### Linting

```bash
# Use flake8 for linting
flake8 qekgr/ tests/

# Configuration in setup.cfg
[flake8]
max-line-length = 88
ignore = E203, W503
per-file-ignores = __init__.py:F401
```

### Type Checking

```bash
# Use mypy for type checking
mypy qekgr/

# Configuration in mypy.ini
[mypy]
python_version = 3.8
warn_return_any = True
warn_unused_configs = True
```

## 🔄 Pre-commit Hooks

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/psf/black
    rev: 23.3.0
    hooks:
      - id: black
        language_version: python3.8

  - repo: https://github.com/pycqa/flake8
    rev: 6.0.0
    hooks:
      - id: flake8

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.3.0
    hooks:
      - id: mypy
        additional_dependencies: [types-all]

  - repo: https://github.com/pycqa/isort
    rev: 5.12.0
    hooks:
      - id: isort
        args: ["--profile", "black"]
```

## 📈 Performance Profiling

```python
# Use cProfile for performance analysis
import cProfile
import pstats

def profile_quantum_operation():
    """Profile quantum operation performance."""
    profiler = cProfile.Profile()
    profiler.enable()
    
    # Perform quantum operations
    result = expensive_quantum_calculation()
    
    profiler.disable()
    stats = pstats.Stats(profiler)
    stats.sort_stats('cumulative').print_stats(10)
    
    return result

# Use decorators for method profiling  
def profile_method(func):
    """Decorator to profile method execution."""
    def wrapper(*args, **kwargs):
        profiler = cProfile.Profile()
        profiler.enable()
        result = func(*args, **kwargs)
        profiler.disable()
        
        # Log or save profiling results
        stats = pstats.Stats(profiler)
        print(f"Profiling {func.__name__}:")
        stats.print_stats(5)
        
        return result
    return wrapper
```

Following these code style guidelines ensures that QE-KGR maintains high code quality, readability, and scientific rigor across all quantum computing implementations! 🚀⚛️
