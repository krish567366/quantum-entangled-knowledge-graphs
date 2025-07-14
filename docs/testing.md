# Testing Guide for QE-KGR

This comprehensive testing guide covers all aspects of testing the Quantum Entangled Knowledge Graphs (QE-KGR) library, from unit tests to quantum-specific validation and performance benchmarking.

## 🎯 Testing Philosophy

### Core Principles

- **Quantum mechanics validation**: Ensure all quantum properties are preserved
- **Numerical stability**: Test with edge cases and numerical precision
- **Performance verification**: Validate computational efficiency
- **Integration testing**: Test complete workflows and use cases
- **Documentation testing**: Ensure examples work as documented

## 🏗️ Test Structure

### Test Organization

```
tests/
├── unit/                    # Unit tests for individual components
│   ├── test_entangled_graph.py
│   ├── test_quantum_inference.py
│   ├── test_query_engine.py
│   └── test_visualization.py
├── integration/             # Integration tests for workflows
│   ├── test_end_to_end.py
│   ├── test_use_cases.py
│   └── test_examples.py
├── performance/             # Performance and benchmark tests
│   ├── test_performance.py
│   └── benchmark_quantum_ops.py
├── quantum/                 # Quantum-specific validation tests
│   ├── test_quantum_properties.py
│   ├── test_entanglement.py
│   └── test_coherence.py
├── fixtures/                # Test data and fixtures
│   ├── sample_graphs.py
│   └── quantum_states.py
└── conftest.py             # Pytest configuration and shared fixtures
```

## 🔧 Test Setup

### Installation

```bash
# Install test dependencies
pip install pytest pytest-cov pytest-benchmark pytest-mock
pip install hypothesis  # Property-based testing
pip install numpy-testing  # NumPy testing utilities
```

### Configuration

```python
# conftest.py
import pytest
import numpy as np
from qekgr import EntangledGraph, QuantumInference

@pytest.fixture
def small_graph():
    """Create small test graph."""
    graph = EntangledGraph(hilbert_dim=4)
    graph.add_quantum_node("A", "state_a")
    graph.add_quantum_node("B", "state_b")
    graph.add_entangled_edge("A", "B", ["connects"], [0.8])
    return graph

@pytest.fixture
def medium_graph():
    """Create medium-sized test graph."""
    graph = EntangledGraph(hilbert_dim=8)
    nodes = ["node_" + str(i) for i in range(10)]
    for node in nodes:
        graph.add_quantum_node(node, f"state_{node}")
    
    # Add random entangled edges
    for i in range(len(nodes)-1):
        graph.add_entangled_edge(
            nodes[i], nodes[i+1], 
            ["connects"], [np.random.uniform(0.3, 0.9)]
        )
    return graph

@pytest.fixture
def quantum_test_tolerance():
    """Standard tolerance for quantum tests."""
    return 1e-10
```

## 🧪 Unit Testing

### Testing Quantum Nodes

```python
# tests/unit/test_entangled_graph.py
import pytest
import numpy as np
from qekgr.graphs import EntangledGraph, QuantumNode

class TestQuantumNode:
    """Test quantum node functionality."""
    
    def test_quantum_node_creation(self):
        """Test quantum node initialization."""
        node = QuantumNode(
            node_id="test_node",
            classical_state="person",
            hilbert_dim=4
        )
        
        assert node.node_id == "test_node"
        assert node.classical_state == "person"
        assert node.state_vector.shape == (4,)
        assert np.isclose(np.linalg.norm(node.state_vector), 1.0)
    
    def test_quantum_state_normalization(self):
        """Test quantum state is properly normalized."""
        node = QuantumNode("test", "state", hilbert_dim=8)
        norm = np.linalg.norm(node.state_vector)
        assert np.isclose(norm, 1.0, rtol=1e-10)
    
    def test_quantum_state_evolution(self):
        """Test quantum state evolution preserves normalization."""
        node = QuantumNode("test", "state", hilbert_dim=4)
        
        # Apply unitary evolution
        unitary = np.array([[1, 0, 0, 0],
                           [0, 0, 1, 0], 
                           [0, 1, 0, 0],
                           [0, 0, 0, 1]], dtype=complex)
        
        initial_norm = np.linalg.norm(node.state_vector)
        node.evolve_state(unitary)
        final_norm = np.linalg.norm(node.state_vector)
        
        assert np.isclose(initial_norm, final_norm, rtol=1e-10)

class TestEntangledGraph:
    """Test entangled graph operations."""
    
    def test_graph_initialization(self):
        """Test graph initialization with various Hilbert dimensions."""
        for dim in [2, 4, 8, 16]:
            graph = EntangledGraph(hilbert_dim=dim)
            assert graph.hilbert_dim == dim
            assert len(graph.nodes) == 0
            assert len(graph.edges) == 0
    
    def test_node_addition(self, small_graph):
        """Test adding quantum nodes to graph."""
        assert len(small_graph.nodes) == 2
        assert "A" in small_graph.nodes
        assert "B" in small_graph.nodes
    
    def test_edge_addition(self, small_graph):
        """Test adding entangled edges."""
        assert len(small_graph.edges) == 1
        edge_key = ("A", "B")
        assert edge_key in small_graph.edges
        
        edge = small_graph.edges[edge_key]
        assert "connects" in edge.relation_types
        assert len(edge.amplitudes) == 1
    
    def test_quantum_state_overlap(self, small_graph):
        """Test quantum state overlap calculation."""
        overlap = small_graph.get_quantum_state_overlap("A", "B")
        
        # Overlap should be a complex number
        assert isinstance(overlap, (complex, np.complex128))
        
        # Overlap magnitude should be <= 1 (Cauchy-Schwarz)
        assert abs(overlap) <= 1.0 + 1e-10
    
    @pytest.mark.parametrize("hilbert_dim", [2, 4, 8, 16])
    def test_various_hilbert_dimensions(self, hilbert_dim):
        """Test graph with various Hilbert space dimensions."""
        graph = EntangledGraph(hilbert_dim=hilbert_dim)
        graph.add_quantum_node("test", "state")
        
        node = graph.nodes["test"]
        assert node.state_vector.shape == (hilbert_dim,)
        assert np.isclose(np.linalg.norm(node.state_vector), 1.0)
```

### Testing Quantum Inference

```python
# tests/unit/test_quantum_inference.py
import pytest
import numpy as np
from qekgr.reasoning import QuantumInference

class TestQuantumWalk:
    """Test quantum walk algorithms."""
    
    def test_quantum_walk_basic(self, small_graph):
        """Test basic quantum walk functionality."""
        inference = QuantumInference(small_graph)
        result = inference.quantum_walk("A", steps=5)
        
        # Verify result structure
        assert hasattr(result, 'path')
        assert hasattr(result, 'final_state')
        assert hasattr(result, 'probabilities')
        
        # Verify path properties
        assert result.path[0] == "A"
        assert len(result.path) == 6  # steps + 1
        
        # Verify quantum properties
        assert np.isclose(np.linalg.norm(result.final_state), 1.0)
        assert np.all(result.probabilities >= 0)
        assert np.isclose(np.sum(result.probabilities), 1.0)
    
    def test_quantum_walk_deterministic_single_node(self):
        """Test quantum walk on single-node graph."""
        graph = EntangledGraph(hilbert_dim=4)
        graph.add_quantum_node("isolated", "state")
        
        inference = QuantumInference(graph)
        result = inference.quantum_walk("isolated", steps=10)
        
        # Should stay on same node
        assert all(node == "isolated" for node in result.path)
    
    def test_quantum_walk_symmetry(self):
        """Test quantum walk on symmetric graph."""
        graph = EntangledGraph(hilbert_dim=4)
        graph.add_quantum_node("A", "state")
        graph.add_quantum_node("B", "state")
        graph.add_entangled_edge("A", "B", ["symmetric"], [0.8])
        graph.add_entangled_edge("B", "A", ["symmetric"], [0.8])
        
        inference = QuantumInference(graph)
        
        # Walk from A and from B should have similar properties
        result_a = inference.quantum_walk("A", steps=20)
        result_b = inference.quantum_walk("B", steps=20)
        
        # Final probability distributions should be similar
        prob_a = result_a.probabilities
        prob_b = result_b.probabilities[::-1]  # Reverse for symmetry
        
        assert np.allclose(prob_a, prob_b, rtol=0.1)
    
    @pytest.mark.parametrize("steps", [1, 5, 10, 50, 100])
    def test_quantum_walk_various_steps(self, small_graph, steps):
        """Test quantum walk with various step counts."""
        inference = QuantumInference(small_graph)
        result = inference.quantum_walk("A", steps=steps)
        
        assert len(result.path) == steps + 1
        assert np.isclose(np.linalg.norm(result.final_state), 1.0)

class TestQuantumLinkPrediction:
    """Test quantum link prediction algorithms."""
    
    def test_predict_links_basic(self, medium_graph):
        """Test basic link prediction functionality."""
        inference = QuantumInference(medium_graph)
        predictions = inference.predict_links(num_predictions=5)
        
        assert len(predictions) <= 5
        for pred in predictions:
            assert hasattr(pred, 'node_pair')
            assert hasattr(pred, 'probability')
            assert 0 <= pred.probability <= 1
    
    def test_predict_links_exclude_existing(self, medium_graph):
        """Test link prediction excludes existing edges."""
        inference = QuantumInference(medium_graph)
        predictions = inference.predict_links(num_predictions=10)
        
        existing_edges = set(medium_graph.edges.keys())
        predicted_edges = set(pred.node_pair for pred in predictions)
        
        # No overlap between existing and predicted edges
        assert len(existing_edges.intersection(predicted_edges)) == 0
```

## ⚛️ Quantum-Specific Testing

### Testing Quantum Properties

```python
# tests/quantum/test_quantum_properties.py
import pytest
import numpy as np
from qekgr import EntangledGraph

class TestQuantumProperties:
    """Test quantum mechanics properties are preserved."""
    
    def test_state_normalization_preservation(self, quantum_test_tolerance):
        """Test quantum states remain normalized after operations."""
        graph = EntangledGraph(hilbert_dim=8)
        graph.add_quantum_node("test", "state")
        
        # Apply various operations
        for _ in range(10):
            # Random unitary operation
            random_unitary = self._generate_random_unitary(8)
            graph.nodes["test"].evolve_state(random_unitary)
            
            # Check normalization
            norm = np.linalg.norm(graph.nodes["test"].state_vector)
            assert np.isclose(norm, 1.0, atol=quantum_test_tolerance)
    
    def test_unitarity_of_evolution_operators(self, small_graph):
        """Test evolution operators are unitary."""
        from qekgr.reasoning import QuantumInference
        
        inference = QuantumInference(small_graph)
        evolution_operator = inference._get_evolution_operator()
        
        # Test unitarity: U† U = I
        conjugate_transpose = evolution_operator.T.conj()
        product = conjugate_transpose @ evolution_operator
        identity = np.eye(evolution_operator.shape[0])
        
        assert np.allclose(product, identity, rtol=1e-10)
    
    def test_entanglement_measures(self, small_graph):
        """Test entanglement measures are physically valid."""
        # Entanglement entropy should be non-negative
        entropy = small_graph.calculate_entanglement_entropy("A", "B")
        assert entropy >= 0
        
        # Concurrence should be between 0 and 1
        concurrence = small_graph.calculate_concurrence("A", "B")
        assert 0 <= concurrence <= 1
    
    def test_quantum_no_cloning_theorem(self, small_graph):
        """Test quantum no-cloning theorem is respected."""
        original_state = small_graph.nodes["A"].state_vector.copy()
        
        # Attempting to clone should not produce identical states
        with pytest.raises(Exception):
            cloned_state = small_graph._clone_quantum_state("A")
    
    def _generate_random_unitary(self, dim: int) -> np.ndarray:
        """Generate random unitary matrix using QR decomposition."""
        # Generate random complex matrix
        real_part = np.random.randn(dim, dim)
        imag_part = np.random.randn(dim, dim)
        random_matrix = real_part + 1j * imag_part
        
        # QR decomposition to get unitary matrix
        q, r = np.linalg.qr(random_matrix)
        
        # Ensure determinant is 1 (special unitary)
        q = q * (np.linalg.det(q) ** (-1/dim))
        
        return q

class TestEntanglementProperties:
    """Test quantum entanglement properties."""
    
    def test_entanglement_symmetry(self, small_graph):
        """Test entanglement is symmetric between nodes."""
        ent_ab = small_graph.calculate_entanglement_entropy("A", "B")
        ent_ba = small_graph.calculate_entanglement_entropy("B", "A")
        
        assert np.isclose(ent_ab, ent_ba, rtol=1e-10)
    
    def test_entanglement_monotonicity(self):
        """Test entanglement increases with interaction strength."""
        graph = EntangledGraph(hilbert_dim=4)
        graph.add_quantum_node("X", "state_x")
        graph.add_quantum_node("Y", "state_y")
        
        entanglements = []
        strengths = [0.1, 0.3, 0.5, 0.7, 0.9]
        
        for strength in strengths:
            graph.add_entangled_edge("X", "Y", ["test"], [strength])
            ent = graph.calculate_entanglement_entropy("X", "Y")
            entanglements.append(ent)
            graph.remove_edge("X", "Y")  # Reset for next test
        
        # Entanglement should generally increase with strength
        # (allowing for some quantum mechanical subtleties)
        assert entanglements[-1] >= entanglements[0]
    
    def test_maximal_entanglement_bounds(self):
        """Test maximal entanglement bounds."""
        graph = EntangledGraph(hilbert_dim=4)
        graph.add_quantum_node("A", "state")
        graph.add_quantum_node("B", "state")
        
        # Create maximally entangled state
        graph.add_entangled_edge("A", "B", ["maximal"], [1.0])
        
        entropy = graph.calculate_entanglement_entropy("A", "B")
        max_entropy = np.log(min(2, 2))  # log(min(dim_A, dim_B))
        
        assert entropy <= max_entropy + 1e-10
```

## 🚀 Performance Testing

### Benchmark Tests

```python
# tests/performance/test_performance.py
import pytest
import numpy as np
import time
from qekgr import EntangledGraph, QuantumInference

class TestPerformance:
    """Performance and scalability tests."""
    
    @pytest.mark.benchmark
    def test_graph_creation_performance(self, benchmark):
        """Benchmark graph creation with many nodes."""
        def create_large_graph():
            graph = EntangledGraph(hilbert_dim=8)
            for i in range(1000):
                graph.add_quantum_node(f"node_{i}", f"state_{i % 10}")
            return graph
        
        graph = benchmark(create_large_graph)
        assert len(graph.nodes) == 1000
    
    @pytest.mark.benchmark
    def test_quantum_walk_performance(self, benchmark, medium_graph):
        """Benchmark quantum walk performance."""
        inference = QuantumInference(medium_graph)
        
        def run_quantum_walk():
            return inference.quantum_walk("node_0", steps=100)
        
        result = benchmark(run_quantum_walk)
        assert len(result.path) == 101
    
    @pytest.mark.slow
    def test_large_graph_scalability(self):
        """Test performance with large graphs."""
        sizes = [100, 500, 1000]
        times = []
        
        for size in sizes:
            graph = EntangledGraph(hilbert_dim=8)
            
            start_time = time.time()
            
            # Create nodes
            for i in range(size):
                graph.add_quantum_node(f"n_{i}", f"state_{i % 10}")
            
            # Create edges (sparse connectivity)
            for i in range(0, size-1, 5):
                graph.add_entangled_edge(
                    f"n_{i}", f"n_{i+1}", 
                    ["connects"], [0.7]
                )
            
            # Perform quantum walk
            inference = QuantumInference(graph)
            inference.quantum_walk("n_0", steps=20)
            
            end_time = time.time()
            times.append(end_time - start_time)
        
        # Performance should scale reasonably
        # (not more than quadratic for this sparse graph)
        assert times[1] / times[0] < 10  # 5x nodes, <10x time
        assert times[2] / times[0] < 50  # 10x nodes, <50x time
    
    def test_memory_usage(self):
        """Test memory usage doesn't grow excessively."""
        import tracemalloc
        
        tracemalloc.start()
        
        # Create graph and perform operations
        graph = EntangledGraph(hilbert_dim=16)
        for i in range(100):
            graph.add_quantum_node(f"node_{i}", "state")
        
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        # Memory usage should be reasonable (<100MB for this test)
        assert peak < 100 * 1024 * 1024  # 100 MB
```

## 🔗 Integration Testing

### End-to-End Tests

```python
# tests/integration/test_end_to_end.py
import pytest
from qekgr import EntangledGraph, QuantumInference, EntangledQueryEngine

class TestEndToEndWorkflows:
    """Test complete workflows from start to finish."""
    
    def test_drug_discovery_workflow(self):
        """Test complete drug discovery workflow."""
        # Create pharmaceutical knowledge graph
        graph = EntangledGraph(hilbert_dim=16)
        
        # Add entities
        graph.add_quantum_node("Aspirin", "drug")
        graph.add_quantum_node("Pain_Relief", "indication") 
        graph.add_quantum_node("COX_Inhibition", "mechanism")
        graph.add_quantum_node("Heart_Disease", "condition")
        
        # Add relationships
        graph.add_entangled_edge("Aspirin", "Pain_Relief", 
                                ["treats", "indicated_for"], [0.9, 0.8])
        graph.add_entangled_edge("Aspirin", "COX_Inhibition",
                                ["mechanism", "acts_via"], [0.95, 0.9])
        graph.add_entangled_edge("COX_Inhibition", "Heart_Disease",
                                ["prevents", "cardioprotective"], [0.7, 0.6])
        
        # Test quantum inference
        inference = QuantumInference(graph)
        
        # Test drug repurposing discovery
        walk_result = inference.quantum_walk("Aspirin", steps=10)
        assert "Heart_Disease" in walk_result.path
        
        # Test link prediction
        predictions = inference.predict_links(num_predictions=3)
        assert len(predictions) > 0
        
        # Test query engine
        query_engine = EntangledQueryEngine(graph)
        results = query_engine.query("What conditions can Aspirin treat?")
        
        assert len(results) > 0
        assert any("Heart_Disease" in str(result) for result in results)
    
    def test_recommendation_system_workflow(self):
        """Test recommendation system workflow."""
        # Create e-commerce graph
        graph = EntangledGraph(hilbert_dim=12)
        
        # Add users and products
        graph.add_quantum_node("User_Alice", "tech_user")
        graph.add_quantum_node("Smartphone", "electronics")
        graph.add_quantum_node("Laptop", "electronics")
        graph.add_quantum_node("Cookbook", "books")
        
        # Add preferences
        graph.add_entangled_edge("User_Alice", "Smartphone",
                                ["interested", "purchased_similar"], [0.8, 0.6])
        graph.add_entangled_edge("Smartphone", "Laptop",
                                ["complementary", "same_category"], [0.7, 0.9])
        
        # Test recommendation generation
        inference = QuantumInference(graph)
        
        # Quantum walk from user should discover products
        walk_result = inference.quantum_walk("User_Alice", steps=8)
        product_visits = [node for node in walk_result.path 
                         if node in ["Smartphone", "Laptop", "Cookbook"]]
        
        assert len(product_visits) > 0
        
        # Should prefer tech products for tech user
        tech_visits = [p for p in product_visits if p in ["Smartphone", "Laptop"]]
        assert len(tech_visits) > 0
    
    def test_scientific_research_workflow(self):
        """Test scientific research discovery workflow."""
        # Create research graph
        graph = EntangledGraph(hilbert_dim=12)
        
        # Add research entities
        graph.add_quantum_node("Quantum_Computing", "field")
        graph.add_quantum_node("Machine_Learning", "field")
        graph.add_quantum_node("Drug_Discovery", "application")
        graph.add_quantum_node("Dr_Smith", "researcher")
        
        # Add relationships
        graph.add_entangled_edge("Quantum_Computing", "Machine_Learning",
                                ["intersects", "enables"], [0.7, 0.8])
        graph.add_entangled_edge("Machine_Learning", "Drug_Discovery",
                                ["applied_to", "accelerates"], [0.8, 0.9])
        graph.add_entangled_edge("Dr_Smith", "Quantum_Computing",
                                ["expert_in", "researches"], [0.9, 0.85])
        
        # Test interdisciplinary discovery
        inference = QuantumInference(graph)
        
        # Walk from researcher should discover applications
        walk_result = inference.quantum_walk("Dr_Smith", steps=10)
        assert "Drug_Discovery" in walk_result.path
        
        # Test subgraph discovery
        subgraph = inference.discover_entangled_subgraph(
            seed_nodes=["Quantum_Computing", "Machine_Learning"],
            expansion_steps=2
        )
        
        assert len(subgraph.nodes) >= 2
        assert subgraph.coherence_measure > 0
```

## 📊 Property-Based Testing

### Using Hypothesis

```python
# tests/unit/test_property_based.py
import pytest
import numpy as np
from hypothesis import given, strategies as st
from qekgr import EntangledGraph

class TestPropertyBased:
    """Property-based tests using Hypothesis."""
    
    @given(st.integers(min_value=2, max_value=32))
    def test_hilbert_dimension_properties(self, hilbert_dim):
        """Test properties hold for any valid Hilbert dimension."""
        graph = EntangledGraph(hilbert_dim=hilbert_dim)
        graph.add_quantum_node("test", "state")
        
        node = graph.nodes["test"]
        
        # State vector should have correct dimension
        assert node.state_vector.shape == (hilbert_dim,)
        
        # State should be normalized
        assert np.isclose(np.linalg.norm(node.state_vector), 1.0)
        
        # State should be complex
        assert node.state_vector.dtype == complex
    
    @given(st.floats(min_value=0.0, max_value=1.0))
    def test_entanglement_strength_properties(self, strength):
        """Test properties for any valid entanglement strength."""
        graph = EntangledGraph(hilbert_dim=4)
        graph.add_quantum_node("A", "state_a")
        graph.add_quantum_node("B", "state_b")
        graph.add_entangled_edge("A", "B", ["test"], [strength])
        
        edge = graph.edges[("A", "B")]
        
        # Amplitude should match input strength
        assert np.isclose(abs(edge.amplitudes[0]), strength)
        
        # Entanglement should be non-negative
        entanglement = graph.calculate_entanglement_entropy("A", "B")
        assert entanglement >= 0
    
    @given(st.integers(min_value=1, max_value=100))
    def test_quantum_walk_properties(self, steps):
        """Test quantum walk properties for any number of steps."""
        graph = EntangledGraph(hilbert_dim=4)
        graph.add_quantum_node("start", "state")
        graph.add_quantum_node("end", "state")
        graph.add_entangled_edge("start", "end", ["connects"], [0.8])
        
        from qekgr.reasoning import QuantumInference
        inference = QuantumInference(graph)
        result = inference.quantum_walk("start", steps=steps)
        
        # Path length should be steps + 1
        assert len(result.path) == steps + 1
        
        # Final state should be normalized
        assert np.isclose(np.linalg.norm(result.final_state), 1.0)
        
        # Probabilities should sum to 1
        assert np.isclose(np.sum(result.probabilities), 1.0)
        
        # All probabilities should be non-negative
        assert np.all(result.probabilities >= 0)
```

## 🔍 Test Utilities

### Testing Helpers

```python
# tests/fixtures/quantum_states.py
import numpy as np

def create_bell_state(hilbert_dim: int = 4) -> np.ndarray:
    """Create Bell state for testing entanglement."""
    state = np.zeros(hilbert_dim, dtype=complex)
    state[0] = 1/np.sqrt(2)
    state[-1] = 1/np.sqrt(2)
    return state

def create_ghz_state(num_qubits: int = 3) -> np.ndarray:
    """Create GHZ state for testing multipartite entanglement."""
    dim = 2 ** num_qubits
    state = np.zeros(dim, dtype=complex)
    state[0] = 1/np.sqrt(2)
    state[-1] = 1/np.sqrt(2)
    return state

def verify_quantum_state(state: np.ndarray, tolerance: float = 1e-10) -> bool:
    """Verify state is valid quantum state."""
    # Check normalization
    if not np.isclose(np.linalg.norm(state), 1.0, atol=tolerance):
        return False
    
    # Check complex dtype
    if state.dtype != complex:
        return False
    
    return True

def assert_states_equal(state1: np.ndarray, state2: np.ndarray, 
                       tolerance: float = 1e-10):
    """Assert two quantum states are equal up to global phase."""
    # Normalize both states
    state1_norm = state1 / np.linalg.norm(state1)
    state2_norm = state2 / np.linalg.norm(state2)
    
    # Check if states are equal up to global phase
    overlap = np.vdot(state1_norm, state2_norm)
    
    # If overlap has magnitude 1, states are equal up to phase
    assert np.isclose(abs(overlap), 1.0, atol=tolerance)
```

## 🚀 Running Tests

### Basic Test Execution

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest tests/unit/test_entangled_graph.py

# Run specific test class
pytest tests/unit/test_entangled_graph.py::TestQuantumNode

# Run specific test method
pytest tests/unit/test_entangled_graph.py::TestQuantumNode::test_quantum_node_creation
```

### Coverage Reports

```bash
# Generate coverage report
pytest --cov=qekgr --cov-report=html tests/

# View coverage in browser
open htmlcov/index.html
```

### Performance Testing

```bash
# Run performance tests only
pytest -m benchmark

# Run slow tests
pytest -m slow

# Skip slow tests
pytest -m "not slow"
```

### Parallel Testing

```bash
# Install pytest-xdist
pip install pytest-xdist

# Run tests in parallel
pytest -n 4  # Use 4 CPU cores
```

This comprehensive testing guide ensures QE-KGR maintains the highest quality standards while preserving quantum mechanical correctness! 🧪⚛️
