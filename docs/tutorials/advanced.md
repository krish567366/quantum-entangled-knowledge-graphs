# Advanced Tutorial

This tutorial covers advanced features and techniques for building sophisticated quantum entangled knowledge graphs. We'll explore complex reasoning patterns, optimization strategies, and advanced quantum operations.

## Prerequisites

Before proceeding with this tutorial, ensure you have completed the [Basic Usage Tutorial](basic_usage.md) and are familiar with:

- Basic quantum graph operations
- Entanglement concepts
- Query engine fundamentals
- Visualization basics

## Advanced Graph Construction

### Multi-Domain Knowledge Integration

Learn to build complex graphs that span multiple knowledge domains:

```python
from qekgr import EntangledGraph, QuantumNode, EntangledEdge
import numpy as np

# Create a large-scale multi-domain graph
multi_domain_graph = EntangledGraph(hilbert_dim=16)

# Define domain-specific node types and properties
domains = {
    "biology": {
        "protein": ["p53", "BRCA1", "insulin"],
        "gene": ["TP53", "BRCA1", "INS"],
        "disease": ["cancer", "diabetes"]
    },
    "chemistry": {
        "compound": ["aspirin", "caffeine", "glucose"],
        "element": ["carbon", "oxygen", "hydrogen"],
        "reaction": ["oxidation", "reduction"]
    },
    "medicine": {
        "drug": ["ibuprofen", "metformin", "warfarin"],
        "symptom": ["pain", "inflammation", "fever"],
        "treatment": ["chemotherapy", "surgery"]
    }
}

# Add nodes with domain-specific quantum properties
for domain, categories in domains.items():
    for category, entities in categories.items():
        for entity in entities:
            # Create domain-specific quantum states
            domain_amplitude = 0.8 if domain == "biology" else 0.6
            
            node = QuantumNode(
                entity,
                node_type=category,
                domain=domain,
                amplitude=domain_amplitude,
                properties={
                    "domain_specificity": domain_amplitude,
                    "category_weight": len(entities) / 10.0
                }
            )
            multi_domain_graph.add_node(node)

print(f"Multi-domain graph: {len(multi_domain_graph.nodes)} nodes")
```

### Complex Entanglement Patterns

Implement sophisticated entanglement patterns for rich knowledge representation:

```python
def create_cross_domain_entanglements(graph, strength_matrix):
    """Create complex entanglement patterns across domains."""
    
    # Define cross-domain relationship patterns
    cross_domain_patterns = [
        # Biology-Medicine connections
        ("p53", "cancer", "biomarker_for", 0.9),
        ("BRCA1", "chemotherapy", "treatment_target", 0.8),
        ("insulin", "diabetes", "regulates", 0.95),
        
        # Chemistry-Medicine connections  
        ("aspirin", "pain", "treats", 0.85),
        ("glucose", "diabetes", "related_to", 0.7),
        ("carbon", "chemotherapy", "component_of", 0.6),
        
        # Biology-Chemistry connections
        ("protein", "compound", "interacts_with", 0.7),
        ("gene", "element", "composed_of", 0.8),
        ("oxidation", "cancer", "contributes_to", 0.6)
    ]
    
    # Add quantum entangled edges
    for source, target, relation, base_strength in cross_domain_patterns:
        if source in graph.nodes and target in graph.nodes:
            # Apply quantum interference for strength modulation
            quantum_mod = np.random.normal(1.0, 0.1)  # Quantum uncertainty
            final_strength = min(0.99, max(0.1, base_strength * quantum_mod))
            
            edge = EntangledEdge(
                source, target,
                relation=relation,
                entanglement_strength=final_strength,
                quantum_phase=np.random.uniform(0, 2*np.pi)  # Quantum phase
            )
            graph.add_edge(edge)

# Apply complex entanglement patterns
create_cross_domain_entanglements(multi_domain_graph, None)
print(f"Added entanglements: {len(multi_domain_graph.edges)} edges")
```

### Hierarchical Quantum Structures

Build hierarchical knowledge structures with quantum superposition:

```python
def create_hierarchical_structure(graph, hierarchy_data):
    """Create hierarchical knowledge with quantum superposition."""
    
    # Example: Medical hierarchy
    medical_hierarchy = {
        "Disease": {
            "children": ["Cancer", "Metabolic Disease"],
            "quantum_weight": 1.0
        },
        "Cancer": {
            "children": ["Breast Cancer", "Lung Cancer"],
            "quantum_weight": 0.8,
            "parent": "Disease"
        },
        "Metabolic Disease": {
            "children": ["Diabetes", "Obesity"],
            "quantum_weight": 0.8,
            "parent": "Disease"
        },
        "Breast Cancer": {
            "children": ["BRCA1 Cancer", "Sporadic Cancer"],
            "quantum_weight": 0.6,
            "parent": "Cancer"
        }
    }
    
    # Create hierarchical nodes with quantum superposition
    for concept, data in medical_hierarchy.items():
        # Create superposed state representing concept hierarchy
        children = data.get("children", [])
        parent = data.get("parent", None)
        
        # Quantum amplitudes for hierarchical relationships
        if children:
            child_amplitudes = [data["quantum_weight"] / len(children)] * len(children)
        else:
            child_amplitudes = [data["quantum_weight"]]
        
        # Add hierarchical node
        hierarchical_node = QuantumNode(
            concept,
            node_type="concept",
            hierarchy_level=len(concept.split()) - 1,
            quantum_amplitudes=child_amplitudes
        )
        graph.add_node(hierarchical_node)
        
        # Create hierarchical entanglements
        if parent:
            parent_edge = EntangledEdge(
                parent, concept,
                relation="parent_of",
                entanglement_strength=0.9,
                edge_type="hierarchical"
            )
            graph.add_edge(parent_edge)
        
        for child in children:
            child_edge = EntangledEdge(
                concept, child,
                relation="child_of", 
                entanglement_strength=0.8,
                edge_type="hierarchical"
            )
            graph.add_edge(child_edge)

# Create hierarchical structure
create_hierarchical_structure(multi_domain_graph, None)
```

## Advanced Quantum Operations

### Quantum State Manipulation

Perform sophisticated quantum state operations:

```python
from qekgr import QuantumInference
import scipy.linalg as la

def advanced_quantum_operations(graph):
    """Demonstrate advanced quantum state manipulation."""
    
    # 1. Quantum State Superposition
    def create_knowledge_superposition(node_ids, weights=None):
        """Create superposed state across multiple knowledge nodes."""
        if weights is None:
            weights = [1.0/len(node_ids)] * len(node_ids)
        
        # Normalize weights for quantum superposition
        norm = np.sqrt(sum(w**2 for w in weights))
        normalized_weights = [w/norm for w in weights]
        
        superposed_state = np.zeros(graph.hilbert_dim, dtype=complex)
        for i, (node_id, weight) in enumerate(zip(node_ids, normalized_weights)):
            if node_id in graph.nodes:
                node_state = graph.get_node_state(node_id)
                superposed_state += weight * node_state
        
        return superposed_state
    
    # Create superposition of related medical concepts
    medical_concepts = ["cancer", "chemotherapy", "p53"]
    medical_superposition = create_knowledge_superposition(
        medical_concepts, 
        weights=[0.6, 0.8, 0.4]
    )
    print(f"Medical superposition norm: {np.linalg.norm(medical_superposition):.3f}")
    
    # 2. Quantum Entanglement Manipulation
    def enhance_entanglement(node1, node2, enhancement_factor=1.2):
        """Enhance entanglement between two nodes using quantum operations."""
        if (node1, node2) in graph.edges:
            current_edge = graph.edges[(node1, node2)]
            new_strength = min(0.99, current_edge.entanglement_strength * enhancement_factor)
            
            # Apply quantum gate operation
            enhanced_edge = EntangledEdge(
                node1, node2,
                relation=current_edge.relation,
                entanglement_strength=new_strength,
                quantum_phase=current_edge.quantum_phase + np.pi/4  # Phase shift
            )
            graph.edges[(node1, node2)] = enhanced_edge
            
            return new_strength
        return 0.0
    
    # Enhance medical-related entanglements
    enhanced_strength = enhance_entanglement("p53", "cancer", 1.3)
    print(f"Enhanced p53-cancer entanglement: {enhanced_strength:.3f}")
    
    # 3. Quantum Coherence Optimization
    def optimize_graph_coherence(graph, target_coherence=0.8):
        """Optimize graph coherence through quantum operations."""
        current_coherence = graph.measure_coherence()
        print(f"Initial coherence: {current_coherence:.3f}")
        
        optimization_steps = 0
        max_steps = 50
        
        while current_coherence < target_coherence and optimization_steps < max_steps:
            # Apply coherence-preserving transformations
            for node_id in graph.nodes:
                node_state = graph.get_node_state(node_id)
                
                # Apply decoherence correction
                corrected_state = node_state / np.linalg.norm(node_state)
                graph.set_node_state(node_id, corrected_state)
            
            # Recompute coherence
            current_coherence = graph.measure_coherence()
            optimization_steps += 1
        
        print(f"Optimized coherence: {current_coherence:.3f} in {optimization_steps} steps")
        return current_coherence
    
    # Optimize graph coherence
    final_coherence = optimize_graph_coherence(multi_domain_graph, 0.75)

# Apply advanced quantum operations
advanced_quantum_operations(multi_domain_graph)
```

### Quantum Algorithm Implementation

Implement advanced quantum algorithms for knowledge reasoning:

```python
def implement_quantum_algorithms(graph):
    """Implement advanced quantum algorithms for knowledge reasoning."""
    
    inference = QuantumInference(graph)
    
    # 1. Quantum Page Rank Algorithm
    def quantum_pagerank(damping_factor=0.85, max_iterations=100, tolerance=1e-6):
        """Quantum version of PageRank algorithm."""
        
        n_nodes = len(graph.nodes)
        node_list = list(graph.nodes.keys())
        
        # Initialize quantum PageRank vector
        qpr_vector = np.ones(n_nodes, dtype=complex) / np.sqrt(n_nodes)
        
        # Create quantum transition matrix
        transition_matrix = np.zeros((n_nodes, n_nodes), dtype=complex)
        
        for i, source in enumerate(node_list):
            out_edges = [edge for (src, _), edge in graph.edges.items() if src == source]
            if out_edges:
                for (src, target), edge in graph.edges.items():
                    if src == source:
                        j = node_list.index(target)
                        # Quantum transition probability with entanglement
                        transition_matrix[j, i] = edge.entanglement_strength / len(out_edges)
            else:
                # Handle dangling nodes with uniform distribution
                transition_matrix[:, i] = 1.0 / n_nodes
        
        # Apply quantum PageRank iterations
        for iteration in range(max_iterations):
            new_qpr = (damping_factor * transition_matrix @ qpr_vector + 
                      (1 - damping_factor) / n_nodes * np.ones(n_nodes, dtype=complex))
            
            # Normalize quantum state
            new_qpr = new_qpr / np.linalg.norm(new_qpr)
            
            # Check convergence
            if np.linalg.norm(new_qpr - qpr_vector) < tolerance:
                break
            
            qpr_vector = new_qpr
        
        # Return quantum PageRank scores
        qpr_scores = {node_list[i]: abs(qpr_vector[i])**2 for i in range(n_nodes)}
        return sorted(qpr_scores.items(), key=lambda x: x[1], reverse=True)
    
    # Compute quantum PageRank
    qpr_results = quantum_pagerank()
    print("Top 5 nodes by Quantum PageRank:")
    for node, score in qpr_results[:5]:
        print(f"  {node}: {score:.4f}")
    
    # 2. Quantum Community Detection
    def quantum_community_detection(n_communities=3):
        """Detect communities using quantum spectral clustering."""
        
        # Create quantum Laplacian matrix
        n_nodes = len(graph.nodes)
        node_list = list(graph.nodes.keys())
        
        # Adjacency matrix with quantum weights
        adj_matrix = np.zeros((n_nodes, n_nodes))
        for i, source in enumerate(node_list):
            for j, target in enumerate(node_list):
                if (source, target) in graph.edges:
                    edge = graph.edges[(source, target)]
                    adj_matrix[i, j] = edge.entanglement_strength
        
        # Quantum Laplacian
        degree_matrix = np.diag(np.sum(adj_matrix, axis=1))
        laplacian = degree_matrix - adj_matrix
        
        # Compute eigenvectors for clustering
        eigenvals, eigenvecs = la.eigh(laplacian)
        
        # Use smallest eigenvectors for clustering
        clustering_features = eigenvecs[:, :n_communities]
        
        # Apply k-means clustering
        from sklearn.cluster import KMeans
        kmeans = KMeans(n_clusters=n_communities, random_state=42)
        communities = kmeans.fit_predict(clustering_features)
        
        # Create community mapping
        community_mapping = {node_list[i]: int(communities[i]) for i in range(n_nodes)}
        return community_mapping
    
    # Detect quantum communities
    communities = quantum_community_detection(4)
    
    print("\nQuantum Community Structure:")
    for community_id in range(4):
        members = [node for node, comm in communities.items() if comm == community_id]
        print(f"  Community {community_id}: {', '.join(members[:5])}")  # Show first 5 members
    
    # 3. Quantum Link Prediction with Interference
    def quantum_link_prediction_with_interference(threshold=0.4):
        """Advanced link prediction using quantum interference patterns."""
        
        predictions = []
        node_list = list(graph.nodes.keys())
        
        for i, source in enumerate(node_list):
            for j, target in enumerate(node_list[i+1:], i+1):
                if (source, target) not in graph.edges and (target, source) not in graph.edges:
                    
                    # Compute quantum interference score
                    source_state = graph.get_node_state(source)
                    target_state = graph.get_node_state(target)
                    
                    # Quantum interference amplitude
                    interference_amplitude = np.vdot(source_state, target_state)
                    interference_score = abs(interference_amplitude)**2
                    
                    # Factor in neighborhood overlap
                    source_neighbors = set(target for (src, target) in graph.edges if src == source)
                    target_neighbors = set(target for (src, target) in graph.edges if src == target)
                    
                    common_neighbors = len(source_neighbors & target_neighbors)
                    total_neighbors = len(source_neighbors | target_neighbors)
                    
                    if total_neighbors > 0:
                        neighborhood_score = common_neighbors / total_neighbors
                    else:
                        neighborhood_score = 0.0
                    
                    # Combined quantum prediction score
                    prediction_score = 0.7 * interference_score + 0.3 * neighborhood_score
                    
                    if prediction_score > threshold:
                        predictions.append((source, target, prediction_score, interference_score))
        
        return sorted(predictions, key=lambda x: x[2], reverse=True)
    
    # Predict quantum links
    link_predictions = quantum_link_prediction_with_interference(0.3)
    
    print(f"\nTop Quantum Link Predictions:")
    for source, target, score, interference in link_predictions[:5]:
        print(f"  {source} -> {target}: {score:.3f} (interference: {interference:.3f})")

# Run advanced quantum algorithms
implement_quantum_algorithms(multi_domain_graph)
```

## Advanced Query Processing

### Multi-Modal Query Fusion

Implement sophisticated query processing with quantum superposition:

```python
from qekgr import EntangledQueryEngine

def advanced_query_processing(graph):
    """Demonstrate advanced query processing techniques."""
    
    query_engine = EntangledQueryEngine(graph)
    
    # 1. Multi-Modal Query Fusion
    def process_multimodal_query(text_query, concept_filters, semantic_weights):
        """Process queries that combine text, concepts, and semantic constraints."""
        
        # Primary text query
        text_results = query_engine.query(text_query, max_results=10)
        
        # Concept-based filtering
        concept_results = []
        for concept in concept_filters:
            concept_matches = query_engine.semantic_search(concept, max_results=5)
            concept_results.extend(concept_matches)
        
        # Fusion using quantum superposition
        fused_results = []
        all_nodes = set()
        
        # Collect all candidate nodes
        for result in text_results:
            all_nodes.update(result.answer_nodes)
        
        for result in concept_results:
            all_nodes.add(result.node_id)
        
        # Score fusion with quantum interference
        for node in all_nodes:
            text_score = 0.0
            concept_score = 0.0
            
            # Text relevance score
            for result in text_results:
                if node in result.answer_nodes:
                    text_score = max(text_score, result.confidence_score)
            
            # Concept relevance score
            for result in concept_results:
                if result.node_id == node:
                    concept_score = max(concept_score, result.relevance_score)
            
            # Quantum interference fusion
            interference_factor = np.sqrt(text_score * concept_score)
            fused_score = (semantic_weights['text'] * text_score + 
                          semantic_weights['concept'] * concept_score + 
                          semantic_weights['interference'] * interference_factor)
            
            if fused_score > 0.2:
                fused_results.append((node, fused_score, text_score, concept_score))
        
        return sorted(fused_results, key=lambda x: x[1], reverse=True)
    
    # Example multi-modal query
    multimodal_results = process_multimodal_query(
        text_query="What treats cancer?",
        concept_filters=["drug", "therapy", "treatment"],
        semantic_weights={'text': 0.4, 'concept': 0.4, 'interference': 0.2}
    )
    
    print("Multi-modal Query Results:")
    for node, fused_score, text_score, concept_score in multimodal_results[:5]:
        print(f"  {node}: fused={fused_score:.3f}, text={text_score:.3f}, concept={concept_score:.3f}")
    
    # 2. Temporal Query Processing
    def temporal_quantum_query(query, time_weights, temporal_decay=0.1):
        """Process queries with temporal quantum evolution."""
        
        # Get base query results
        base_results = query_engine.query(query, max_results=15)
        
        # Apply temporal quantum evolution
        temporal_results = []
        
        for result in base_results:
            for node in result.answer_nodes:
                node_state = graph.get_node_state(node)
                
                # Simulate temporal evolution using quantum dynamics
                time_evolution_operator = np.exp(-1j * temporal_decay * np.random.rand())
                evolved_state = time_evolution_operator * node_state
                
                # Compute temporal relevance
                temporal_amplitude = np.vdot(node_state, evolved_state)
                temporal_score = abs(temporal_amplitude)**2
                
                # Weight by time preferences
                weighted_score = result.confidence_score * temporal_score
                
                temporal_results.append((node, weighted_score, temporal_score))
        
        return sorted(temporal_results, key=lambda x: x[1], reverse=True)
    
    # Example temporal query
    temporal_results = temporal_quantum_query(
        "Recent cancer treatments",
        time_weights={'recent': 0.8, 'established': 0.2}
    )
    
    print("\nTemporal Query Results:")
    for node, weighted_score, temporal_score in temporal_results[:5]:
        print(f"  {node}: score={weighted_score:.3f}, temporal={temporal_score:.3f}")
    
    # 3. Uncertainty-Aware Query Processing
    def uncertainty_aware_query(query, confidence_threshold=0.6):
        """Process queries with quantum uncertainty quantification."""
        
        # Get query results with uncertainty estimation
        results = query_engine.query(query, max_results=20)
        
        uncertainty_results = []
        
        for result in results:
            # Estimate uncertainty from quantum state variance
            answer_states = []
            for node in result.answer_nodes:
                node_state = graph.get_node_state(node)
                answer_states.append(node_state)
            
            if answer_states:
                # Compute state variance as uncertainty measure
                mean_state = np.mean(answer_states, axis=0)
                variance = np.mean([np.linalg.norm(state - mean_state)**2 
                                  for state in answer_states])
                
                uncertainty = np.sqrt(variance)
                confidence = result.confidence_score * (1 - uncertainty)
                
                if confidence > confidence_threshold:
                    uncertainty_results.append((
                        result.answer_nodes, 
                        confidence, 
                        uncertainty,
                        result.reasoning_path
                    ))
        
        return sorted(uncertainty_results, key=lambda x: x[1], reverse=True)
    
    # Example uncertainty-aware query
    uncertainty_results = uncertainty_aware_query(
        "What proteins are involved in cancer?",
        confidence_threshold=0.5
    )
    
    print("\nUncertainty-Aware Query Results:")
    for answers, confidence, uncertainty, reasoning in uncertainty_results[:3]:
        print(f"  Answers: {', '.join(answers)}")
        print(f"    Confidence: {confidence:.3f}, Uncertainty: {uncertainty:.3f}")
        print(f"    Reasoning: {reasoning}")

# Run advanced query processing
advanced_query_processing(multi_domain_graph)
```

## Performance Optimization

### Quantum State Caching

Implement efficient caching for quantum computations:

```python
import functools
from typing import Dict, Any
import hashlib

class QuantumStateCache:
    """Efficient caching system for quantum state computations."""
    
    def __init__(self, max_cache_size=1000):
        self.cache: Dict[str, Any] = {}
        self.max_cache_size = max_cache_size
        self.access_order = []
    
    def _generate_key(self, graph_state, operation, *args):
        """Generate cache key from graph state and operation."""
        # Create hash from graph state
        state_hash = hashlib.md5(str(graph_state).encode()).hexdigest()[:16]
        operation_hash = hashlib.md5(f"{operation}_{args}".encode()).hexdigest()[:16]
        return f"{state_hash}_{operation_hash}"
    
    def get(self, key):
        """Get cached result."""
        if key in self.cache:
            # Update access order for LRU
            self.access_order.remove(key)
            self.access_order.append(key)
            return self.cache[key]
        return None
    
    def set(self, key, value):
        """Cache computation result."""
        if len(self.cache) >= self.max_cache_size:
            # Remove least recently used item
            lru_key = self.access_order.pop(0)
            del self.cache[lru_key]
        
        self.cache[key] = value
        self.access_order.append(key)
    
    def cached_quantum_operation(self, operation_name):
        """Decorator for caching quantum operations."""
        def decorator(func):
            @functools.wraps(func)
            def wrapper(graph, *args, **kwargs):
                # Generate cache key
                graph_signature = f"{len(graph.nodes)}_{len(graph.edges)}"
                cache_key = self._generate_key(graph_signature, operation_name, args, tuple(kwargs.items()))
                
                # Check cache
                cached_result = self.get(cache_key)
                if cached_result is not None:
                    return cached_result
                
                # Compute and cache result
                result = func(graph, *args, **kwargs)
                self.set(cache_key, result)
                return result
            return wrapper
        return decorator

# Initialize quantum cache
quantum_cache = QuantumStateCache(max_cache_size=500)

# Apply caching to expensive operations
@quantum_cache.cached_quantum_operation("coherence_measurement")
def cached_coherence_measurement(graph):
    """Cached version of coherence measurement."""
    return graph.measure_coherence()

@quantum_cache.cached_quantum_operation("entanglement_matrix")
def cached_entanglement_matrix(graph):
    """Cached computation of full entanglement matrix."""
    nodes = list(graph.nodes.keys())
    n = len(nodes)
    matrix = np.zeros((n, n))
    
    for i, node1 in enumerate(nodes):
        for j, node2 in enumerate(nodes):
            if i != j:
                matrix[i, j] = graph.measure_entanglement(node1, node2)
    
    return matrix

# Demonstrate caching benefits
print("Testing quantum caching performance:")

import time

# Without caching
start_time = time.time()
for _ in range(10):
    coherence = multi_domain_graph.measure_coherence()
uncached_time = time.time() - start_time

# With caching
start_time = time.time()
for _ in range(10):
    coherence = cached_coherence_measurement(multi_domain_graph)
cached_time = time.time() - start_time

print(f"Uncached time: {uncached_time:.4f}s")
print(f"Cached time: {cached_time:.4f}s")
print(f"Speedup: {uncached_time/cached_time:.2f}x")
```

### Parallel Quantum Processing

Implement parallel processing for quantum operations:

```python
import concurrent.futures
import multiprocessing as mp
from typing import List, Callable

def parallel_quantum_processing(graph, operations: List[Callable], max_workers=None):
    """Execute quantum operations in parallel."""
    
    if max_workers is None:
        max_workers = min(mp.cpu_count(), len(operations))
    
    # Divide graph into sub-components for parallel processing
    def partition_graph(graph, n_partitions):
        """Partition graph for parallel processing."""
        nodes = list(graph.nodes.keys())
        partition_size = len(nodes) // n_partitions
        
        partitions = []
        for i in range(n_partitions):
            start_idx = i * partition_size
            end_idx = start_idx + partition_size if i < n_partitions - 1 else len(nodes)
            partition_nodes = nodes[start_idx:end_idx]
            partitions.append(partition_nodes)
        
        return partitions
    
    # Parallel quantum walk computation
    def parallel_quantum_walks(start_nodes, steps=10):
        """Compute quantum walks in parallel."""
        
        def single_quantum_walk(start_node):
            inference = QuantumInference(graph)
            return inference.quantum_walk(start_node, steps)
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = [executor.submit(single_quantum_walk, node) for node in start_nodes]
            results = [future.result() for future in concurrent.futures.as_completed(futures)]
        
        return results
    
    # Parallel entanglement computation
    def parallel_entanglement_computation(node_pairs):
        """Compute entanglements for node pairs in parallel."""
        
        def compute_entanglement_pair(node_pair):
            node1, node2 = node_pair
            return (node1, node2, graph.measure_entanglement(node1, node2))
        
        with concurrent.futures.ProcessPoolExecutor(max_workers=max_workers) as executor:
            futures = [executor.submit(compute_entanglement_pair, pair) for pair in node_pairs]
            results = [future.result() for future in concurrent.futures.as_completed(futures)]
        
        return results
    
    # Example parallel operations
    nodes = list(graph.nodes.keys())
    
    # Parallel quantum walks
    print("Running parallel quantum walks...")
    start_time = time.time()
    walk_results = parallel_quantum_walks(nodes[:5])  # First 5 nodes
    parallel_walk_time = time.time() - start_time
    print(f"Parallel quantum walks completed in {parallel_walk_time:.3f}s")
    
    # Parallel entanglement computation
    print("Running parallel entanglement computation...")
    node_pairs = [(nodes[i], nodes[j]) for i in range(len(nodes)) 
                  for j in range(i+1, min(i+10, len(nodes)))]  # Limit pairs for demo
    
    start_time = time.time()
    entanglement_results = parallel_entanglement_computation(node_pairs[:20])
    parallel_entanglement_time = time.time() - start_time
    print(f"Parallel entanglement computation completed in {parallel_entanglement_time:.3f}s")
    
    return {
        'quantum_walks': walk_results,
        'entanglements': entanglement_results,
        'timing': {
            'walk_time': parallel_walk_time,
            'entanglement_time': parallel_entanglement_time
        }
    }

# Run parallel processing
parallel_results = parallel_quantum_processing(multi_domain_graph)
print(f"Computed {len(parallel_results['quantum_walks'])} quantum walks")
print(f"Computed {len(parallel_results['entanglements'])} entanglement pairs")
```

## Advanced Visualization Techniques

### Dynamic Quantum State Visualization

Create advanced visualizations for quantum state evolution:

```python
from qekgr.utils import QuantumGraphVisualizer
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def create_advanced_visualizations(graph):
    """Create sophisticated quantum visualizations."""
    
    visualizer = QuantumGraphVisualizer(graph)
    
    # 1. Quantum State Evolution Heatmap
    def create_evolution_heatmap(evolution_steps=20):
        """Create heatmap showing quantum state evolution over time."""
        
        nodes = list(graph.nodes.keys())[:10]  # Limit for visualization
        evolution_data = np.zeros((len(nodes), evolution_steps))
        
        # Simulate quantum evolution
        for step in range(evolution_steps):
            for i, node in enumerate(nodes):
                # Apply small quantum evolution
                current_state = graph.get_node_state(node)
                evolved_state = current_state * np.exp(-1j * 0.1 * step)
                
                # Measure probability amplitude
                probability = np.sum(np.abs(evolved_state)**2)
                evolution_data[i, step] = probability
        
        # Create heatmap
        fig = go.Figure(data=go.Heatmap(
            z=evolution_data,
            x=list(range(evolution_steps)),
            y=nodes,
            colorscale='Viridis',
            colorbar=dict(title="Quantum Probability")
        ))
        
        fig.update_layout(
            title="Quantum State Evolution Over Time",
            xaxis_title="Evolution Step",
            yaxis_title="Graph Nodes",
            height=600
        )
        
        return fig
    
    # 2. Multi-Dimensional Entanglement Visualization
    def create_entanglement_3d_surface():
        """Create 3D surface plot of entanglement landscape."""
        
        nodes = list(graph.nodes.keys())[:15]  # Limit for performance
        
        # Create entanglement surface
        x_nodes = []
        y_nodes = []
        z_entanglement = []
        
        for i, node1 in enumerate(nodes):
            for j, node2 in enumerate(nodes):
                if i != j:
                    entanglement = graph.measure_entanglement(node1, node2)
                    x_nodes.append(i)
                    y_nodes.append(j)
                    z_entanglement.append(entanglement)
        
        # Create 3D surface
        fig = go.Figure(data=[go.Scatter3d(
            x=x_nodes,
            y=y_nodes,
            z=z_entanglement,
            mode='markers',
            marker=dict(
                size=8,
                color=z_entanglement,
                colorscale='Rainbow',
                showscale=True,
                colorbar=dict(title="Entanglement Strength")
            ),
            text=[f"{nodes[x]} -> {nodes[y]}" for x, y in zip(x_nodes, y_nodes)],
            hovertemplate="<b>%{text}</b><br>Entanglement: %{z:.3f}<extra></extra>"
        )])
        
        fig.update_layout(
            title="3D Entanglement Landscape",
            scene=dict(
                xaxis_title="Source Node Index",
                yaxis_title="Target Node Index", 
                zaxis_title="Entanglement Strength"
            ),
            height=700
        )
        
        return fig
    
    # 3. Interactive Quantum Dashboard
    def create_quantum_dashboard():
        """Create comprehensive interactive dashboard."""
        
        # Create subplots
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=("Graph Network", "Quantum States", 
                           "Entanglement Heatmap", "Community Structure"),
            specs=[[{"type": "scatter"}, {"type": "scatter"}],
                   [{"type": "heatmap"}, {"type": "scatter"}]]
        )
        
        # Add 2D graph network
        graph_2d = visualizer.visualize_graph_2d(layout="spring")
        for trace in graph_2d.data:
            trace.showlegend = False
            fig.add_trace(trace, row=1, col=1)
        
        # Add quantum state projection
        try:
            states_2d = visualizer.visualize_quantum_states_2d(method="pca")
            for trace in states_2d.data:
                trace.showlegend = False
                fig.add_trace(trace, row=1, col=2)
        except:
            # Fallback if PCA fails
            pass
        
        # Add entanglement heatmap
        try:
            heatmap = visualizer.visualize_entanglement_heatmap()
            for trace in heatmap.data:
                trace.showlegend = False
                fig.add_trace(trace, row=2, col=1)
        except:
            pass
        
        # Update layout
        fig.update_layout(
            height=800,
            title_text="Quantum Knowledge Graph Dashboard",
            showlegend=False
        )
        
        return fig
    
    # Generate visualizations
    evolution_fig = create_evolution_heatmap()
    entanglement_3d_fig = create_entanglement_3d_surface()
    dashboard_fig = create_quantum_dashboard()
    
    return {
        'evolution': evolution_fig,
        'entanglement_3d': entanglement_3d_fig,
        'dashboard': dashboard_fig
    }

# Create advanced visualizations
advanced_viz = create_advanced_visualizations(multi_domain_graph)

# Display visualizations
print("Advanced visualizations created:")
print("- Quantum state evolution heatmap")
print("- 3D entanglement landscape")
print("- Interactive quantum dashboard")

# Save visualizations
advanced_viz['evolution'].write_html("quantum_evolution.html")
advanced_viz['entanglement_3d'].write_html("entanglement_3d.html")
advanced_viz['dashboard'].write_html("quantum_dashboard.html")
```

## Best Practices for Advanced Applications

### Design Patterns for Quantum Knowledge Graphs

```python
# 1. Builder Pattern for Complex Graphs
class QuantumGraphBuilder:
    """Builder pattern for constructing complex quantum graphs."""
    
    def __init__(self, hilbert_dim=8):
        self.graph = EntangledGraph(hilbert_dim)
        self.node_registry = {}
        self.edge_patterns = []
    
    def add_domain(self, domain_name, entities):
        """Add entire domain with entities."""
        for entity_id, properties in entities.items():
            node = QuantumNode(entity_id, domain=domain_name, **properties)
            self.graph.add_node(node)
            self.node_registry[entity_id] = node
        return self
    
    def add_relationship_pattern(self, pattern_func):
        """Add relationship pattern function."""
        self.edge_patterns.append(pattern_func)
        return self
    
    def apply_patterns(self):
        """Apply all relationship patterns."""
        for pattern_func in self.edge_patterns:
            pattern_func(self.graph, self.node_registry)
        return self
    
    def build(self):
        """Build final graph."""
        return self.graph

# 2. Strategy Pattern for Quantum Algorithms
class QuantumAlgorithmStrategy:
    """Strategy pattern for different quantum algorithms."""
    
    def execute(self, graph, **params):
        raise NotImplementedError

class QuantumWalkStrategy(QuantumAlgorithmStrategy):
    def execute(self, graph, start_node, steps=10):
        inference = QuantumInference(graph)
        return inference.quantum_walk(start_node, steps)

class QuantumPageRankStrategy(QuantumAlgorithmStrategy):
    def execute(self, graph, damping_factor=0.85):
        # Implementation from earlier example
        pass

# 3. Observer Pattern for Quantum State Changes
class QuantumStateObserver:
    """Observer for quantum state changes."""
    
    def __init__(self):
        self.observers = []
    
    def add_observer(self, observer):
        self.observers.append(observer)
    
    def notify_state_change(self, node_id, old_state, new_state):
        for observer in self.observers:
            observer.on_quantum_state_change(node_id, old_state, new_state)

class CoherenceMonitor:
    """Monitor and log coherence changes."""
    
    def on_quantum_state_change(self, node_id, old_state, new_state):
        coherence_change = np.linalg.norm(new_state - old_state)
        if coherence_change > 0.1:
            print(f"Significant coherence change in {node_id}: {coherence_change:.3f}")
```

## Performance Monitoring and Debugging

### Quantum State Debugging Tools

```python
def quantum_debugging_tools(graph):
    """Advanced debugging tools for quantum graphs."""
    
    # 1. Quantum State Validator
    def validate_quantum_states():
        """Validate all quantum states in the graph."""
        issues = []
        
        for node_id, node in graph.nodes.items():
            state = graph.get_node_state(node_id)
            
            # Check normalization
            norm = np.linalg.norm(state)
            if abs(norm - 1.0) > 1e-6:
                issues.append(f"Node {node_id} state not normalized: {norm:.6f}")
            
            # Check for NaN values
            if np.any(np.isnan(state)):
                issues.append(f"Node {node_id} contains NaN values")
            
            # Check state dimension
            if len(state) != graph.hilbert_dim:
                issues.append(f"Node {node_id} state dimension mismatch: {len(state)} vs {graph.hilbert_dim}")
        
        return issues
    
    # 2. Entanglement Consistency Checker
    def check_entanglement_consistency():
        """Check consistency of entanglement relationships."""
        issues = []
        
        for (source, target), edge in graph.edges.items():
            # Check bidirectional consistency
            if (target, source) in graph.edges:
                reverse_edge = graph.edges[(target, source)]
                if abs(edge.entanglement_strength - reverse_edge.entanglement_strength) > 0.1:
                    issues.append(f"Asymmetric entanglement: {source}-{target}")
            
            # Check strength bounds
            if edge.entanglement_strength < 0 or edge.entanglement_strength > 1:
                issues.append(f"Invalid entanglement strength: {source}-{target}: {edge.entanglement_strength}")
        
        return issues
    
    # 3. Performance Profiler
    def profile_quantum_operations():
        """Profile performance of quantum operations."""
        import time
        
        operations = [
            ("measure_coherence", lambda: graph.measure_coherence()),
            ("quantum_walk", lambda: QuantumInference(graph).quantum_walk(list(graph.nodes.keys())[0], 5)),
            ("entanglement_measure", lambda: graph.measure_entanglement(*list(graph.nodes.keys())[:2]))
        ]
        
        performance_report = {}
        
        for op_name, op_func in operations:
            times = []
            for _ in range(5):  # Run 5 times for average
                start_time = time.time()
                try:
                    result = op_func()
                    end_time = time.time()
                    times.append(end_time - start_time)
                except Exception as e:
                    times.append(float('inf'))
                    print(f"Error in {op_name}: {e}")
            
            performance_report[op_name] = {
                'avg_time': np.mean(times),
                'std_time': np.std(times),
                'min_time': np.min(times),
                'max_time': np.max(times)
            }
        
        return performance_report
    
    # Run debugging checks
    print("=== Quantum Graph Debugging Report ===")
    
    state_issues = validate_quantum_states()
    if state_issues:
        print("Quantum State Issues:")
        for issue in state_issues:
            print(f"  - {issue}")
    else:
        print("✓ All quantum states valid")
    
    entanglement_issues = check_entanglement_consistency()
    if entanglement_issues:
        print("Entanglement Issues:")
        for issue in entanglement_issues:
            print(f"  - {issue}")
    else:
        print("✓ All entanglements consistent")
    
    performance_report = profile_quantum_operations()
    print("Performance Report:")
    for op_name, metrics in performance_report.items():
        print(f"  {op_name}: {metrics['avg_time']:.4f}s ± {metrics['std_time']:.4f}s")

# Run debugging tools
quantum_debugging_tools(multi_domain_graph)
```

Congratulations! You've mastered the advanced features of Quantum Entangled Knowledge Graphs. You can now build sophisticated quantum knowledge systems that leverage the full power of quantum mechanics for knowledge representation and reasoning! 🎓⚛️

Next, explore the [Custom Tutorial](custom.md) to learn how to build domain-specific applications, or check out the practical [Use Cases](../use_cases/) for real-world implementations.
