# Query Engine Module

The `qekgr.query` module provides natural language query processing capabilities for quantum entangled knowledge graphs. The `EntangledQueryEngine` class translates natural language questions into quantum operations and returns ranked results based on quantum confidence measures.

## Classes Overview

### `EntangledQueryEngine`

Main query processing engine that handles natural language queries and quantum search.

### Result Classes

- `QueryResult` - Complete query results with quantum confidence
- `SuperposedQuery` - Queries represented in quantum superposition

---

## EntangledQueryEngine

### Class Definition

```python
class EntangledQueryEngine:
    """
    Quantum-enhanced query processor for entangled knowledge graphs.
    
    This engine projects natural language queries into the Hilbert space
    of the quantum graph and uses entanglement-based reasoning to find
    the most relevant answers.
    """
```

### Constructor

```python
def __init__(self, graph: EntangledGraph) -> None
```

**Parameters:**

- `graph` (EntangledGraph): The entangled graph to query

**Example:**

```python
from qekgr import EntangledGraph, EntangledQueryEngine

graph = EntangledGraph(hilbert_dim=4)
# ... populate graph ...
query_engine = EntangledQueryEngine(graph)
```

### Configuration Properties

#### `context_dimension`

```python
@property
def context_dimension(self) -> int
```

Dimension of query context vector space (default: 64).

#### `max_reasoning_steps`

```python
@property  
def max_reasoning_steps(self) -> int
```

Maximum steps in quantum reasoning chain (default: 15).

#### `interference_threshold`

```python
@property
def interference_threshold(self) -> float
```

Threshold for quantum interference effects (default: 0.4).

### Core Query Methods

#### `query`

```python
def query(
    self,
    query_text: str,
    context: Optional[Dict[str, Any]] = None,
    max_results: int = 10
) -> List[QueryResult]
```

Process a natural language query against the entangled graph.

**Parameters:**

- `query_text` (str): Natural language query
- `context` (Dict[str, Any], optional): Optional context for query interpretation
- `max_results` (int): Maximum number of results to return (default: 10)

**Returns:**

- `List[QueryResult]`: Ranked list of query results

**Example:**

```python
# Simple queries
results = query_engine.query("Who collaborates with Alice?")
results = query_engine.query("What drugs treat inflammation?")

# Query with context
context = {
    "domain": "molecular_biology",
    "focus": "protein_interactions",
    "time_period": "recent"
}
results = query_engine.query(
    "Find proteins that interact with BRCA1",
    context=context,
    max_results=5
)

for result in results:
    print(f"Answer: {', '.join(result.answer_nodes)}")
    print(f"Confidence: {result.confidence_score:.3f}")
    print(f"Reasoning: {' → '.join(result.reasoning_path)}")
```

#### `superposed_query`

```python
def superposed_query(
    self,
    query_components: List[str],
    amplitudes: List[complex],
    max_results: int = 10
) -> List[QueryResult]
```

Process a query in quantum superposition of multiple components.

**Parameters:**

- `query_components` (List[str]): Different query formulations
- `amplitudes` (List[complex]): Quantum amplitudes for each component
- `max_results` (int): Maximum results to return

**Returns:**

- `List[QueryResult]`: Results from superposed query processing

**Example:**

```python
# Superposed query for drug discovery
components = [
    "What drugs target COX proteins?",
    "Which medications reduce inflammation?", 
    "Find anti-inflammatory compounds?"
]
amplitudes = [0.6, 0.5, 0.4]

results = query_engine.superposed_query(
    query_components=components,
    amplitudes=amplitudes,
    max_results=8
)

print(f"Superposed query returned {len(results)} results")
```

#### `semantic_search`

```python
def semantic_search(
    self,
    query_vector: np.ndarray,
    search_type: str = "quantum_similarity",
    threshold: float = 0.5
) -> List[QueryResult]
```

Perform semantic search using query vector.

**Parameters:**

- `query_vector` (np.ndarray): Semantic embedding of query
- `search_type` (str): Type of search ("quantum_similarity", "entanglement_based")
- `threshold` (float): Similarity threshold

**Returns:**

- `List[QueryResult]`: Semantically similar results

**Example:**

```python
# Create query embedding (example with random vector)
query_embedding = np.random.random(64)
query_embedding = query_embedding / np.linalg.norm(query_embedding)

# Semantic search
results = query_engine.semantic_search(
    query_vector=query_embedding,
    search_type="entanglement_based",
    threshold=0.6
)
```

### Advanced Query Methods

#### `quantum_reasoning_chain`

```python
def quantum_reasoning_chain(
    self,
    query_text: str,
    chain_length: int = 5,
    reasoning_type: str = "interference"
) -> List[QueryResult]
```

Perform multi-step quantum reasoning.

**Parameters:**

- `query_text` (str): Initial query
- `chain_length` (int): Length of reasoning chain
- `reasoning_type` (str): Type of reasoning ("interference", "entanglement", "superposition")

**Returns:**

- `List[QueryResult]`: Results from quantum reasoning chain

**Example:**

```python
# Multi-step reasoning for drug discovery
results = query_engine.quantum_reasoning_chain(
    query_text="How does aspirin reduce inflammation?",
    chain_length=7,
    reasoning_type="entanglement"
)

print("Reasoning chain results:")
for i, result in enumerate(results):
    print(f"Step {i+1}: {result.query}")
    print(f"  Answer: {', '.join(result.answer_nodes)}")
    print(f"  Confidence: {result.confidence_score:.3f}")
```

#### `contextual_query`

```python
def contextual_query(
    self,
    query_text: str,
    context_nodes: List[str],
    context_weight: float = 0.3
) -> List[QueryResult]
```

Query with specific contextual focus on certain nodes.

**Parameters:**

- `query_text` (str): Natural language query
- `context_nodes` (List[str]): Nodes to use as context
- `context_weight` (float): Weight of contextual influence

**Returns:**

- `List[QueryResult]`: Context-aware query results

**Example:**

```python
# Query with molecular context
results = query_engine.contextual_query(
    query_text="What are the side effects?",
    context_nodes=["Aspirin", "COX1", "COX2"],
    context_weight=0.4
)
```

#### `temporal_query`

```python
def temporal_query(
    self,
    query_text: str,
    time_evolution_steps: int = 10,
    temporal_bias: str = "forward"
) -> List[QueryResult]
```

Query considering temporal evolution of the graph.

**Parameters:**

- `query_text` (str): Query text
- `time_evolution_steps` (int): Steps of temporal evolution
- `temporal_bias` (str): Temporal direction ("forward", "backward", "bidirectional")

**Returns:**

- `List[QueryResult]`: Temporally-aware results

### Query Analysis Methods

#### `analyze_query_complexity`

```python
def analyze_query_complexity(self, query_text: str) -> Dict[str, Any]
```

Analyze the complexity and structure of a natural language query.

**Parameters:**

- `query_text` (str): Query to analyze

**Returns:**

- `Dict[str, Any]`: Query complexity analysis

**Example:**

```python
complexity = query_engine.analyze_query_complexity(
    "What proteins interact with BRCA1 and are involved in DNA repair?"
)

print("Query analysis:")
print(f"  Complexity score: {complexity['complexity_score']:.3f}")
print(f"  Entity count: {complexity['entity_count']}")
print(f"  Relation types: {complexity['relation_types']}")
print(f"  Quantum requirements: {complexity['quantum_requirements']}")
```

#### `explain_query_reasoning`

```python
def explain_query_reasoning(
    self,
    query_result: QueryResult,
    explanation_depth: int = 3
) -> Dict[str, Any]
```

Provide detailed explanation of query reasoning process.

**Parameters:**

- `query_result` (QueryResult): Result to explain
- `explanation_depth` (int): Depth of explanation

**Returns:**

- `Dict[str, Any]`: Detailed reasoning explanation

**Example:**

```python
results = query_engine.query("How does metformin treat diabetes?")
explanation = query_engine.explain_query_reasoning(results[0])

print("Query reasoning explanation:")
print(f"  Quantum path: {explanation['quantum_path']}")
print(f"  Interference effects: {explanation['interference_analysis']}")
print(f"  Entanglement contributions: {explanation['entanglement_breakdown']}")
```

---

## Result Classes

### QueryResult

```python
@dataclass
class QueryResult:
    """Result of a quantum query operation."""
    query: str                          # Original query text
    answer_nodes: List[str]             # Primary answer nodes
    answer_edges: List[Tuple[str, str]] # Relevant edges in answer
    confidence_score: float             # Overall confidence (0-1)
    quantum_amplitudes: List[complex]   # Quantum amplitudes for answers
    reasoning_path: List[str]           # Step-by-step reasoning path
    metadata: Dict[str, Any]           # Additional result metadata
```

**Properties:**

- `certainty_level` (str): Qualitative certainty ("high", "medium", "low")
- `quantum_coherence` (float): Coherence of quantum reasoning
- `classical_support` (float): Support from classical graph structure

**Methods:**

```python
def get_explanation(self) -> str
    """Get human-readable explanation of result."""

def get_supporting_evidence(self) -> List[Dict[str, Any]]
    """Get supporting evidence for the result."""

def measure_result_stability(self) -> float
    """Measure stability of the result under perturbations."""
```

**Example:**

```python
results = query_engine.query("What causes inflammation?")
result = results[0]

print(f"Query: {result.query}")
print(f"Answer: {', '.join(result.answer_nodes)}")
print(f"Confidence: {result.confidence_score:.3f}")
print(f"Certainty: {result.certainty_level}")
print(f"Coherence: {result.quantum_coherence:.3f}")

# Get detailed explanation
explanation = result.get_explanation()
print(f"Explanation: {explanation}")

# Get supporting evidence
evidence = result.get_supporting_evidence()
for i, ev in enumerate(evidence):
    print(f"Evidence {i+1}: {ev}")
```

### SuperposedQuery

```python
@dataclass
class SuperposedQuery:
    """Represents a query in quantum superposition."""
    query_components: List[str]        # Different query formulations
    amplitudes: List[complex]          # Quantum amplitudes for components
    context_vector: np.ndarray         # Context embedding vector
    entanglement_bias: Optional[List[str]] = None  # Bias towards relations
```

**Methods:**

```python
def collapse_query(self) -> str
    """Collapse superposed query to single formulation."""

def evolve_superposition(self, evolution_operator: np.ndarray) -> None
    """Evolve query superposition using quantum operator."""

def measure_query_entropy(self) -> float
    """Measure entropy of query superposition."""
```

**Example:**

```python
# Create superposed query
superposed = SuperposedQuery(
    query_components=[
        "What treats pain?",
        "Which drugs reduce inflammation?",
        "How to manage chronic pain?"
    ],
    amplitudes=[0.6, 0.5, 0.4],
    context_vector=np.random.random(64),
    entanglement_bias=["treats", "reduces", "manages"]
)

# Measure query properties
entropy = superposed.measure_query_entropy()
print(f"Query entropy: {entropy:.3f}")

# Collapse to specific query
collapsed = superposed.collapse_query()
print(f"Collapsed query: {collapsed}")
```

## Query Processing Pipeline

### Natural Language Processing

```python
def preprocess_query(query_text: str) -> Dict[str, Any]
    """Preprocess natural language query."""
    
    # Extract entities, relations, and intent
    processed = {
        'entities': extract_entities(query_text),
        'relations': extract_relations(query_text), 
        'intent': classify_intent(query_text),
        'modifiers': extract_modifiers(query_text),
        'question_type': classify_question_type(query_text)
    }
    
    return processed

def extract_entities(query_text: str) -> List[Dict[str, Any]]
    """Extract named entities from query."""
    # Implementation details...

def classify_intent(query_text: str) -> str
    """Classify query intent (search, relationship, causation, etc.)."""
    # Implementation details...
```

### Quantum Query Translation

```python
def translate_to_quantum_operations(
    processed_query: Dict[str, Any],
    graph: EntangledGraph
) -> List[Dict[str, Any]]
    """Translate processed query to quantum operations."""
    
    operations = []
    
    # Map entities to quantum nodes
    entity_mapping = map_entities_to_nodes(processed_query['entities'], graph)
    
    # Create quantum search operators
    for entity in entity_mapping:
        if entity['confidence'] > 0.7:
            operations.append({
                'type': 'quantum_walk',
                'start_node': entity['node_id'],
                'bias': processed_query['relations']
            })
    
    # Add interference operations for complex queries
    if len(entity_mapping) > 1:
        operations.append({
            'type': 'quantum_interference',
            'nodes': [e['node_id'] for e in entity_mapping],
            'pattern': 'constructive'
        })
    
    return operations
```

## Advanced Usage Examples

### Complex Query Processing

```python
def process_complex_biomedical_query():
    """Example of complex biomedical query processing."""
    
    # Multi-part biomedical query
    query = """
    What are the molecular mechanisms by which aspirin reduces inflammation,
    and what are the potential side effects related to COX-1 inhibition?
    """
    
    # Break down into subqueries
    subqueries = [
        "How does aspirin reduce inflammation?",
        "What is the mechanism of aspirin action?", 
        "What are COX-1 inhibition side effects?",
        "How does aspirin affect COX-1?"
    ]
    
    # Process each subquery
    all_results = []
    for subquery in subqueries:
        results = query_engine.query(subquery, max_results=3)
        all_results.extend(results)
    
    # Combine results using quantum interference
    combined_results = query_engine.superposed_query(
        query_components=subqueries,
        amplitudes=[0.8, 0.7, 0.6, 0.5]
    )
    
    return combined_results

results = process_complex_biomedical_query()
```

### Interactive Query Session

```python
class InteractiveQuantumQuery:
    """Interactive quantum query session with memory."""
    
    def __init__(self, query_engine):
        self.query_engine = query_engine
        self.query_history = []
        self.context_memory = {}
    
    def ask(self, query_text, use_context=True):
        """Ask question with contextual memory."""
        
        # Build context from previous queries
        context = self.build_context() if use_context else None
        
        # Process query
        results = self.query_engine.query(query_text, context=context)
        
        # Update memory
        self.query_history.append({
            'query': query_text,
            'results': results,
            'timestamp': time.time()
        })
        
        # Extract context for future queries
        self.update_context_memory(results)
        
        return results
    
    def build_context(self):
        """Build context from query history."""
        context = {
            'recent_entities': [],
            'frequent_relations': [],
            'domain_focus': None
        }
        
        # Analyze recent queries
        for query_record in self.query_history[-3:]:  # Last 3 queries
            for result in query_record['results'][:2]:  # Top 2 results
                context['recent_entities'].extend(result.answer_nodes)
        
        return context
    
    def update_context_memory(self, results):
        """Update contextual memory with new results."""
        for result in results:
            for node in result.answer_nodes:
                if node not in self.context_memory:
                    self.context_memory[node] = 0
                self.context_memory[node] += result.confidence_score

# Interactive session example
session = InteractiveQuantumQuery(query_engine)

# Progressive query refinement
results1 = session.ask("What drugs treat pain?")
results2 = session.ask("Which of these are anti-inflammatory?")  # Uses context
results3 = session.ask("What are the mechanisms?")  # Uses accumulated context
```

### Custom Query Extensions

```python
class DomainSpecificQueryEngine(EntangledQueryEngine):
    """Domain-specific query engine for drug discovery."""
    
    def __init__(self, graph, domain_ontology):
        super().__init__(graph)
        self.domain_ontology = domain_ontology
        self.domain_weights = self.load_domain_weights()
    
    def drug_mechanism_query(self, drug_name, condition):
        """Specialized query for drug mechanisms."""
        
        query_text = f"How does {drug_name} treat {condition}?"
        
        # Use domain-specific context
        context = {
            'domain': 'pharmacology',
            'focus': 'mechanism_of_action',
            'drug': drug_name,
            'condition': condition
        }
        
        # Weight results by domain relevance
        results = self.query(query_text, context=context)
        
        # Apply domain-specific scoring
        for result in results:
            domain_score = self.calculate_domain_relevance(result)
            result.confidence_score = 0.7 * result.confidence_score + 0.3 * domain_score
        
        return sorted(results, key=lambda r: r.confidence_score, reverse=True)
    
    def calculate_domain_relevance(self, result):
        """Calculate domain-specific relevance score."""
        relevance = 0
        
        for node in result.answer_nodes:
            if node in self.domain_ontology:
                relevance += self.domain_weights.get(node, 0)
        
        return min(relevance, 1.0)  # Cap at 1.0

# Usage
drug_engine = DomainSpecificQueryEngine(graph, drug_ontology)
mechanism_results = drug_engine.drug_mechanism_query("aspirin", "inflammation")
```

## Performance and Optimization

### Query Caching

```python
from functools import lru_cache
import hashlib

class CachedQueryEngine(EntangledQueryEngine):
    """Query engine with intelligent caching."""
    
    def __init__(self, graph, cache_size=256):
        super().__init__(graph)
        self.cache_size = cache_size
        self.query_cache = {}
    
    def cached_query(self, query_text, context=None, max_results=10):
        """Query with caching support."""
        
        # Create cache key
        cache_key = self.create_cache_key(query_text, context, max_results)
        
        # Check cache
        if cache_key in self.query_cache:
            return self.query_cache[cache_key]
        
        # Process query
        results = self.query(query_text, context, max_results)
        
        # Cache results
        if len(self.query_cache) >= self.cache_size:
            # Remove oldest entry
            oldest_key = min(self.query_cache.keys())
            del self.query_cache[oldest_key]
        
        self.query_cache[cache_key] = results
        return results
    
    def create_cache_key(self, query_text, context, max_results):
        """Create unique cache key for query."""
        key_data = f"{query_text}_{context}_{max_results}"
        return hashlib.md5(key_data.encode()).hexdigest()
```

The query engine module transforms natural language questions into quantum operations, enabling intuitive interaction with quantum knowledge graphs while leveraging the full power of quantum entanglement and interference! 🔍⚛️
