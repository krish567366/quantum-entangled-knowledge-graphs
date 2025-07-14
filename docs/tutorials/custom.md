# Custom Applications Tutorial

This tutorial demonstrates how to build domain-specific applications using the Quantum Entangled Knowledge Graphs (QE-KGR) library. We'll create custom quantum knowledge systems for specific domains and use cases.

## Prerequisites

Before starting this tutorial, ensure you have completed:

- [Basic Usage Tutorial](basic_usage.md)
- [Advanced Tutorial](advanced.md)
- Understanding of quantum reasoning concepts

## Building Domain-Specific Applications

### 1. Biomedical Knowledge Graph

Let's build a comprehensive biomedical knowledge graph with quantum entanglement:

```python
from qekgr import EntangledGraph, QuantumNode, EntangledEdge
from qekgr import EntangledQueryEngine, QuantumInference
from qekgr.utils import QuantumGraphVisualizer
import numpy as np
from typing import Dict, List, Any

class BiomedicalQuantumGraph:
    """Custom biomedical knowledge graph with quantum enhancements."""
    
    def __init__(self, hilbert_dim=16):
        self.graph = EntangledGraph(hilbert_dim)
        self.entity_types = {
            'protein': {'color': '#ff6b6b', 'quantum_weight': 0.9},
            'gene': {'color': '#4ecdc4', 'quantum_weight': 0.8},
            'disease': {'color': '#45b7d1', 'quantum_weight': 0.7},
            'drug': {'color': '#96ceb4', 'quantum_weight': 0.8},
            'pathway': {'color': '#ffeaa7', 'quantum_weight': 0.6},
            'tissue': {'color': '#dda0dd', 'quantum_weight': 0.5}
        }
        self.query_engine = None
        self.inference = None
    
    def add_biomedical_entity(self, entity_id: str, entity_type: str, 
                             properties: Dict[str, Any] = None):
        """Add biomedical entity with quantum properties."""
        
        if properties is None:
            properties = {}
        
        # Enhance properties with quantum characteristics
        quantum_props = self.entity_types.get(entity_type, {})
        
        node = QuantumNode(
            entity_id,
            node_type=entity_type,
            quantum_weight=quantum_props.get('quantum_weight', 0.5),
            biomedical_domain=True,
            **properties
        )
        
        self.graph.add_node(node)
        
        # Initialize quantum state based on entity type
        self._initialize_quantum_state(entity_id, entity_type)
    
    def _initialize_quantum_state(self, entity_id: str, entity_type: str):
        """Initialize quantum state based on biomedical context."""
        
        # Create domain-specific quantum states
        if entity_type == 'protein':
            # Proteins have complex folding states
            amplitudes = np.random.normal(0.5, 0.1, self.graph.hilbert_dim)
            amplitudes = amplitudes / np.linalg.norm(amplitudes)
        
        elif entity_type == 'gene':
            # Genes have binary expression states with superposition
            amplitudes = np.zeros(self.graph.hilbert_dim, dtype=complex)
            amplitudes[0] = 0.6  # Expressed state
            amplitudes[1] = 0.8  # Unexpressed state
            amplitudes = amplitudes / np.linalg.norm(amplitudes)
        
        elif entity_type == 'disease':
            # Diseases have progressive states
            amplitudes = np.exp(-np.linspace(0, 2, self.graph.hilbert_dim))
            amplitudes = amplitudes / np.linalg.norm(amplitudes)
        
        else:
            # Default quantum state
            amplitudes = np.ones(self.graph.hilbert_dim) / np.sqrt(self.graph.hilbert_dim)
        
        self.graph.set_node_state(entity_id, amplitudes)
    
    def add_biomedical_relationship(self, source: str, target: str, 
                                   relation_type: str, confidence: float = 0.8,
                                   evidence_strength: float = 1.0):
        """Add biomedical relationship with quantum entanglement."""
        
        # Calculate quantum entanglement strength based on biological relevance
        entanglement_strength = self._calculate_biomedical_entanglement(
            source, target, relation_type, confidence, evidence_strength
        )
        
        edge = EntangledEdge(
            source, target,
            relation=relation_type,
            entanglement_strength=entanglement_strength,
            confidence=confidence,
            evidence_strength=evidence_strength,
            biomedical_relation=True
        )
        
        self.graph.add_edge(edge)
    
    def _calculate_biomedical_entanglement(self, source: str, target: str,
                                         relation_type: str, confidence: float,
                                         evidence_strength: float) -> float:
        """Calculate entanglement strength for biomedical relationships."""
        
        # Base strength from confidence and evidence
        base_strength = confidence * evidence_strength
        
        # Enhance based on relation type
        relation_modifiers = {
            'interacts_with': 0.9,
            'regulates': 0.8,
            'causes': 0.95,
            'treats': 0.85,
            'associated_with': 0.6,
            'inhibits': 0.8,
            'activates': 0.85,
            'expresses': 0.9,
            'metabolizes': 0.7
        }
        
        modifier = relation_modifiers.get(relation_type, 0.5)
        final_strength = min(0.99, base_strength * modifier)
        
        return final_strength
    
    def load_biomedical_data(self, data_sources: Dict[str, Any]):
        """Load biomedical data from multiple sources."""
        
        # Example: Load protein-protein interactions
        if 'proteins' in data_sources:
            for protein_data in data_sources['proteins']:
                self.add_biomedical_entity(
                    protein_data['id'],
                    'protein',
                    {
                        'name': protein_data.get('name', ''),
                        'function': protein_data.get('function', ''),
                        'molecular_weight': protein_data.get('molecular_weight', 0),
                        'organism': protein_data.get('organism', 'human')
                    }
                )
        
        # Load gene data
        if 'genes' in data_sources:
            for gene_data in data_sources['genes']:
                self.add_biomedical_entity(
                    gene_data['id'],
                    'gene',
                    {
                        'symbol': gene_data.get('symbol', ''),
                        'chromosome': gene_data.get('chromosome', ''),
                        'expression_level': gene_data.get('expression_level', 0.5)
                    }
                )
        
        # Load relationships
        if 'interactions' in data_sources:
            for interaction in data_sources['interactions']:
                self.add_biomedical_relationship(
                    interaction['source'],
                    interaction['target'],
                    interaction['type'],
                    interaction.get('confidence', 0.8),
                    interaction.get('evidence_strength', 1.0)
                )
    
    def setup_reasoning_engines(self):
        """Initialize query and inference engines."""
        self.query_engine = EntangledQueryEngine(self.graph)
        self.inference = QuantumInference(self.graph)
    
    def find_drug_targets(self, disease: str, max_results: int = 5):
        """Find potential drug targets for a disease using quantum reasoning."""
        
        if not self.query_engine:
            self.setup_reasoning_engines()
        
        # Use quantum walk to find connected proteins
        walk_result = self.inference.quantum_walk(disease, steps=15)
        
        # Extract high-probability proteins as targets
        targets = []
        for node_id, probability in walk_result.final_distribution.items():
            if (node_id in self.graph.nodes and 
                self.graph.nodes[node_id].node_type == 'protein' and
                probability > 0.1):
                targets.append((node_id, probability))
        
        # Sort by quantum probability
        targets.sort(key=lambda x: x[1], reverse=True)
        
        return targets[:max_results]
    
    def predict_drug_interactions(self, drug1: str, drug2: str):
        """Predict drug-drug interactions using quantum entanglement."""
        
        if not self.inference:
            self.setup_reasoning_engines()
        
        # Measure quantum entanglement between drugs
        direct_entanglement = self.graph.measure_entanglement(drug1, drug2)
        
        # Find common targets/pathways
        drug1_walk = self.inference.quantum_walk(drug1, steps=10)
        drug2_walk = self.inference.quantum_walk(drug2, steps=10)
        
        # Calculate interaction probability
        common_targets = set(drug1_walk.final_distribution.keys()) & \
                        set(drug2_walk.final_distribution.keys())
        
        interaction_score = direct_entanglement
        for target in common_targets:
            prob1 = drug1_walk.final_distribution.get(target, 0)
            prob2 = drug2_walk.final_distribution.get(target, 0)
            interaction_score += prob1 * prob2 * 0.5  # Weight common targets
        
        return {
            'interaction_probability': min(1.0, interaction_score),
            'direct_entanglement': direct_entanglement,
            'common_targets': list(common_targets)
        }
    
    def analyze_pathway_dysregulation(self, pathway: str, disease: str):
        """Analyze pathway dysregulation in disease context."""
        
        if not self.inference:
            self.setup_reasoning_engines()
        
        # Quantum walk from disease to pathway components
        disease_walk = self.inference.quantum_walk(disease, steps=12)
        
        # Find pathway components affected by disease
        affected_components = []
        for node_id, probability in disease_walk.final_distribution.items():
            if node_id in self.graph.nodes:
                node = self.graph.nodes[node_id]
                if (hasattr(node, 'pathway') and node.pathway == pathway) or \
                   (node.node_type in ['protein', 'gene'] and probability > 0.05):
                    affected_components.append((node_id, probability))
        
        # Calculate dysregulation score
        dysregulation_score = sum(prob for _, prob in affected_components)
        
        return {
            'dysregulation_score': dysregulation_score,
            'affected_components': affected_components,
            'pathway_coherence': self._calculate_pathway_coherence(pathway)
        }
    
    def _calculate_pathway_coherence(self, pathway: str):
        """Calculate quantum coherence within a pathway."""
        
        # Find all pathway components
        pathway_nodes = [node_id for node_id, node in self.graph.nodes.items()
                        if hasattr(node, 'pathway') and node.pathway == pathway]
        
        if len(pathway_nodes) < 2:
            return 0.0
        
        # Calculate average entanglement within pathway
        total_entanglement = 0.0
        pairs = 0
        
        for i, node1 in enumerate(pathway_nodes):
            for node2 in pathway_nodes[i+1:]:
                entanglement = self.graph.measure_entanglement(node1, node2)
                total_entanglement += entanglement
                pairs += 1
        
        return total_entanglement / pairs if pairs > 0 else 0.0

# Example usage of BiomedicalQuantumGraph
bio_graph = BiomedicalQuantumGraph(hilbert_dim=20)

# Sample biomedical data
biomedical_data = {
    'proteins': [
        {'id': 'p53', 'name': 'Tumor protein p53', 'function': 'tumor_suppressor'},
        {'id': 'BRCA1', 'name': 'BRCA1 protein', 'function': 'dna_repair'},
        {'id': 'EGFR', 'name': 'Epidermal growth factor receptor', 'function': 'signal_transduction'},
        {'id': 'MYC', 'name': 'MYC proto-oncogene', 'function': 'transcription_regulation'}
    ],
    'genes': [
        {'id': 'TP53', 'symbol': 'TP53', 'chromosome': '17p13.1'},
        {'id': 'BRCA1_gene', 'symbol': 'BRCA1', 'chromosome': '17q21.31'},
        {'id': 'EGFR_gene', 'symbol': 'EGFR', 'chromosome': '7p11.2'}
    ],
    'diseases': [
        {'id': 'breast_cancer', 'name': 'Breast Cancer'},
        {'id': 'lung_cancer', 'name': 'Lung Cancer'}
    ],
    'drugs': [
        {'id': 'tamoxifen', 'name': 'Tamoxifen', 'type': 'hormone_therapy'},
        {'id': 'gefitinib', 'name': 'Gefitinib', 'type': 'tyrosine_kinase_inhibitor'}
    ],
    'interactions': [
        {'source': 'TP53', 'target': 'p53', 'type': 'expresses', 'confidence': 0.95},
        {'source': 'p53', 'target': 'breast_cancer', 'type': 'associated_with', 'confidence': 0.9},
        {'source': 'BRCA1', 'target': 'breast_cancer', 'type': 'associated_with', 'confidence': 0.95},
        {'source': 'tamoxifen', 'target': 'breast_cancer', 'type': 'treats', 'confidence': 0.8},
        {'source': 'EGFR', 'target': 'lung_cancer', 'type': 'associated_with', 'confidence': 0.85},
        {'source': 'gefitinib', 'target': 'EGFR', 'type': 'inhibits', 'confidence': 0.9}
    ]
}

# Load data and setup
bio_graph.load_biomedical_data(biomedical_data)
bio_graph.setup_reasoning_engines()

print(f"Biomedical graph loaded: {len(bio_graph.graph.nodes)} nodes, {len(bio_graph.graph.edges)} edges")

# Find drug targets for breast cancer
targets = bio_graph.find_drug_targets('breast_cancer')
print("\nPotential drug targets for breast cancer:")
for target, probability in targets:
    print(f"  {target}: {probability:.3f}")

# Predict drug interactions
interaction = bio_graph.predict_drug_interactions('tamoxifen', 'gefitinib')
print(f"\nTamoxifen-Gefitinib interaction prediction:")
print(f"  Interaction probability: {interaction['interaction_probability']:.3f}")
print(f"  Direct entanglement: {interaction['direct_entanglement']:.3f}")
```

### 2. Financial Knowledge Graph

Build a quantum-enhanced financial knowledge system:

```python
class FinancialQuantumGraph:
    """Quantum knowledge graph for financial analysis."""
    
    def __init__(self, hilbert_dim=12):
        self.graph = EntangledGraph(hilbert_dim)
        self.time_series_data = {}
        self.market_state = "normal"  # normal, volatile, crisis
        
    def add_financial_entity(self, entity_id: str, entity_type: str, 
                           market_data: Dict[str, Any] = None):
        """Add financial entity with market-aware quantum properties."""
        
        if market_data is None:
            market_data = {}
        
        node = QuantumNode(
            entity_id,
            node_type=entity_type,
            market_cap=market_data.get('market_cap', 0),
            volatility=market_data.get('volatility', 0.1),
            sector=market_data.get('sector', 'unknown'),
            financial_entity=True
        )
        
        self.graph.add_node(node)
        self._initialize_financial_quantum_state(entity_id, entity_type, market_data)
    
    def _initialize_financial_quantum_state(self, entity_id: str, entity_type: str,
                                          market_data: Dict[str, Any]):
        """Initialize quantum state based on financial characteristics."""
        
        volatility = market_data.get('volatility', 0.1)
        
        if entity_type == 'stock':
            # Stock states represent price movements and market sentiment
            base_amplitudes = np.random.normal(0, volatility, self.graph.hilbert_dim)
            
        elif entity_type == 'bond':
            # Bond states are more stable, less quantum uncertainty
            base_amplitudes = np.random.normal(0, volatility * 0.3, self.graph.hilbert_dim)
            
        elif entity_type == 'commodity':
            # Commodity states show supply/demand fluctuations
            base_amplitudes = np.random.normal(0, volatility * 1.2, self.graph.hilbert_dim)
            
        elif entity_type == 'currency':
            # Currency states represent exchange rate dynamics
            base_amplitudes = np.random.normal(0, volatility * 0.8, self.graph.hilbert_dim)
            
        else:
            base_amplitudes = np.random.normal(0, 0.1, self.graph.hilbert_dim)
        
        # Normalize to valid quantum state
        amplitudes = base_amplitudes / np.linalg.norm(base_amplitudes)
        self.graph.set_node_state(entity_id, amplitudes)
    
    def add_market_relationship(self, source: str, target: str, 
                              correlation: float, relationship_type: str):
        """Add market relationship with correlation-based entanglement."""
        
        # Convert correlation to entanglement strength
        entanglement_strength = abs(correlation) * 0.8 + 0.1
        
        edge = EntangledEdge(
            source, target,
            relation=relationship_type,
            entanglement_strength=entanglement_strength,
            correlation=correlation,
            market_relationship=True
        )
        
        self.graph.add_edge(edge)
    
    def update_market_state(self, new_market_state: str):
        """Update market state and adjust quantum properties."""
        
        self.market_state = new_market_state
        
        # Adjust quantum states based on market conditions
        volatility_multipliers = {
            'normal': 1.0,
            'volatile': 1.5,
            'crisis': 2.0,
            'bull': 0.8,
            'bear': 1.3
        }
        
        multiplier = volatility_multipliers.get(new_market_state, 1.0)
        
        for node_id in self.graph.nodes:
            current_state = self.graph.get_node_state(node_id)
            
            # Apply market volatility to quantum state
            noise = np.random.normal(0, 0.1 * multiplier, len(current_state))
            new_state = current_state + noise
            new_state = new_state / np.linalg.norm(new_state)
            
            self.graph.set_node_state(node_id, new_state)
    
    def calculate_portfolio_risk(self, portfolio: List[str], weights: List[float]):
        """Calculate portfolio risk using quantum entanglement."""
        
        if len(portfolio) != len(weights):
            raise ValueError("Portfolio and weights must have same length")
        
        # Normalize weights
        weights = np.array(weights)
        weights = weights / np.sum(weights)
        
        # Calculate quantum portfolio risk
        total_risk = 0.0
        
        # Individual asset risks (diagonal terms)
        for i, asset in enumerate(portfolio):
            if asset in self.graph.nodes:
                node = self.graph.nodes[asset]
                individual_volatility = getattr(node, 'volatility', 0.1)
                total_risk += (weights[i] ** 2) * (individual_volatility ** 2)
        
        # Correlation risks (off-diagonal terms)
        for i, asset1 in enumerate(portfolio):
            for j, asset2 in enumerate(portfolio[i+1:], i+1):
                if asset1 in self.graph.nodes and asset2 in self.graph.nodes:
                    # Use quantum entanglement as correlation measure
                    entanglement = self.graph.measure_entanglement(asset1, asset2)
                    
                    vol1 = getattr(self.graph.nodes[asset1], 'volatility', 0.1)
                    vol2 = getattr(self.graph.nodes[asset2], 'volatility', 0.1)
                    
                    correlation_risk = 2 * weights[i] * weights[j] * vol1 * vol2 * entanglement
                    total_risk += correlation_risk
        
        return np.sqrt(total_risk)
    
    def detect_market_anomalies(self):
        """Detect market anomalies using quantum coherence."""
        
        # Calculate graph coherence
        coherence = self.graph.measure_coherence()
        
        # Low coherence indicates market disruption/anomalies
        if coherence < 0.3:
            anomaly_level = "high"
        elif coherence < 0.6:
            anomaly_level = "medium"
        else:
            anomaly_level = "low"
        
        # Find nodes with highest quantum uncertainty
        uncertain_assets = []
        for node_id in self.graph.nodes:
            state = self.graph.get_node_state(node_id)
            uncertainty = np.std(np.abs(state))
            if uncertainty > 0.2:
                uncertain_assets.append((node_id, uncertainty))
        
        uncertain_assets.sort(key=lambda x: x[1], reverse=True)
        
        return {
            'anomaly_level': anomaly_level,
            'market_coherence': coherence,
            'uncertain_assets': uncertain_assets[:5]
        }
    
    def predict_price_movements(self, asset: str, time_horizon: int = 5):
        """Predict price movements using quantum walks."""
        
        inference = QuantumInference(self.graph)
        
        # Perform quantum walk to explore price space
        walk_result = inference.quantum_walk(asset, steps=time_horizon)
        
        # Interpret walk results as price movement probabilities
        connected_assets = []
        for node_id, probability in walk_result.final_distribution.items():
            if node_id != asset and probability > 0.05:
                connected_assets.append((node_id, probability))
        
        # Calculate momentum based on entangled asset movements
        momentum_score = 0.0
        for connected_asset, probability in connected_assets:
            if connected_asset in self.graph.nodes:
                entanglement = self.graph.measure_entanglement(asset, connected_asset)
                momentum_score += probability * entanglement
        
        # Predict movement direction
        if momentum_score > 0.3:
            direction = "up"
        elif momentum_score < -0.3:
            direction = "down"
        else:
            direction = "sideways"
        
        return {
            'predicted_direction': direction,
            'momentum_score': momentum_score,
            'connected_assets': connected_assets[:3]
        }

# Example financial quantum graph
financial_graph = FinancialQuantumGraph(hilbert_dim=15)

# Add financial entities
financial_entities = [
    ('AAPL', 'stock', {'volatility': 0.25, 'sector': 'technology', 'market_cap': 2000000}),
    ('GOOGL', 'stock', {'volatility': 0.28, 'sector': 'technology', 'market_cap': 1500000}),
    ('JPM', 'stock', {'volatility': 0.30, 'sector': 'banking', 'market_cap': 400000}),
    ('GLD', 'commodity', {'volatility': 0.15, 'sector': 'precious_metals'}),
    ('USD_EUR', 'currency', {'volatility': 0.08}),
    ('10Y_TREASURY', 'bond', {'volatility': 0.05})
]

for entity_id, entity_type, market_data in financial_entities:
    financial_graph.add_financial_entity(entity_id, entity_type, market_data)

# Add market relationships
relationships = [
    ('AAPL', 'GOOGL', 0.7, 'sector_correlation'),
    ('AAPL', 'USD_EUR', -0.3, 'currency_impact'),
    ('JPM', '10Y_TREASURY', 0.6, 'interest_rate_sensitivity'),
    ('GLD', 'USD_EUR', -0.5, 'safe_haven'),
    ('AAPL', 'GLD', -0.2, 'risk_off_correlation')
]

for source, target, correlation, rel_type in relationships:
    financial_graph.add_market_relationship(source, target, correlation, rel_type)

print(f"Financial graph: {len(financial_graph.graph.nodes)} nodes, {len(financial_graph.graph.edges)} edges")

# Portfolio risk analysis
portfolio = ['AAPL', 'GOOGL', 'JPM']
weights = [0.5, 0.3, 0.2]
risk = financial_graph.calculate_portfolio_risk(portfolio, weights)
print(f"Portfolio quantum risk: {risk:.3f}")

# Market anomaly detection
anomalies = financial_graph.detect_market_anomalies()
print(f"Market anomaly level: {anomalies['anomaly_level']}")
print(f"Market coherence: {anomalies['market_coherence']:.3f}")

# Price prediction
prediction = financial_graph.predict_price_movements('AAPL')
print(f"AAPL prediction: {prediction['predicted_direction']} (momentum: {prediction['momentum_score']:.3f})")
```

### 3. Recommendation System

Build a quantum-enhanced recommendation engine:

```python
class QuantumRecommendationSystem:
    """Quantum-enhanced recommendation system."""
    
    def __init__(self, hilbert_dim=10):
        self.graph = EntangledGraph(hilbert_dim)
        self.user_profiles = {}
        self.item_features = {}
        
    def add_user(self, user_id: str, preferences: Dict[str, float],
                demographics: Dict[str, Any] = None):
        """Add user with quantum preference representation."""
        
        if demographics is None:
            demographics = {}
        
        # Create user node
        user_node = QuantumNode(
            user_id,
            node_type='user',
            **demographics
        )
        self.graph.add_node(user_node)
        
        # Store user preferences
        self.user_profiles[user_id] = preferences
        
        # Initialize quantum state based on preferences
        self._initialize_user_quantum_state(user_id, preferences)
    
    def add_item(self, item_id: str, features: Dict[str, float],
                categories: List[str] = None):
        """Add item with quantum feature representation."""
        
        if categories is None:
            categories = []
        
        # Create item node
        item_node = QuantumNode(
            item_id,
            node_type='item',
            categories=categories
        )
        self.graph.add_node(item_node)
        
        # Store item features
        self.item_features[item_id] = features
        
        # Initialize quantum state based on features
        self._initialize_item_quantum_state(item_id, features)
    
    def _initialize_user_quantum_state(self, user_id: str, preferences: Dict[str, float]):
        """Initialize user quantum state from preferences."""
        
        # Map preferences to quantum amplitudes
        amplitudes = np.zeros(self.graph.hilbert_dim, dtype=complex)
        
        for i, (pref_name, pref_value) in enumerate(preferences.items()):
            if i < self.graph.hilbert_dim:
                amplitudes[i] = pref_value
        
        # Fill remaining dimensions with small random values
        for i in range(len(preferences), self.graph.hilbert_dim):
            amplitudes[i] = np.random.normal(0, 0.1)
        
        # Normalize
        amplitudes = amplitudes / np.linalg.norm(amplitudes)
        self.graph.set_node_state(user_id, amplitudes)
    
    def _initialize_item_quantum_state(self, item_id: str, features: Dict[str, float]):
        """Initialize item quantum state from features."""
        
        # Map features to quantum amplitudes
        amplitudes = np.zeros(self.graph.hilbert_dim, dtype=complex)
        
        for i, (feature_name, feature_value) in enumerate(features.items()):
            if i < self.graph.hilbert_dim:
                amplitudes[i] = feature_value
        
        # Fill remaining dimensions
        for i in range(len(features), self.graph.hilbert_dim):
            amplitudes[i] = np.random.normal(0, 0.05)
        
        # Normalize
        amplitudes = amplitudes / np.linalg.norm(amplitudes)
        self.graph.set_node_state(item_id, amplitudes)
    
    def add_interaction(self, user_id: str, item_id: str, 
                       interaction_type: str, rating: float):
        """Add user-item interaction with quantum entanglement."""
        
        # Calculate entanglement strength from rating
        # Higher ratings create stronger entanglement
        if interaction_type == 'like':
            entanglement_strength = min(0.9, rating / 5.0 * 0.8 + 0.1)
        elif interaction_type == 'purchase':
            entanglement_strength = min(0.95, rating / 5.0 * 0.9 + 0.2)
        elif interaction_type == 'view':
            entanglement_strength = min(0.6, rating / 5.0 * 0.4 + 0.1)
        else:
            entanglement_strength = min(0.8, rating / 5.0 * 0.6 + 0.1)
        
        edge = EntangledEdge(
            user_id, item_id,
            relation=interaction_type,
            entanglement_strength=entanglement_strength,
            rating=rating
        )
        
        self.graph.add_edge(edge)
    
    def generate_recommendations(self, user_id: str, num_recommendations: int = 5,
                               filter_seen: bool = True):
        """Generate recommendations using quantum interference."""
        
        if user_id not in self.graph.nodes:
            return []
        
        # Perform quantum walk from user
        inference = QuantumInference(self.graph)
        walk_result = inference.quantum_walk(user_id, steps=8)
        
        # Extract item recommendations
        item_scores = []
        
        for node_id, probability in walk_result.final_distribution.items():
            if (node_id in self.graph.nodes and 
                self.graph.nodes[node_id].node_type == 'item'):
                
                # Skip items user has already interacted with
                if filter_seen and (user_id, node_id) in self.graph.edges:
                    continue
                
                # Calculate quantum recommendation score
                user_state = self.graph.get_node_state(user_id)
                item_state = self.graph.get_node_state(node_id)
                
                # Quantum interference score
                interference = abs(np.vdot(user_state, item_state))**2
                
                # Combined score
                final_score = 0.6 * probability + 0.4 * interference
                
                item_scores.append((node_id, final_score, probability, interference))
        
        # Sort by score and return top recommendations
        item_scores.sort(key=lambda x: x[1], reverse=True)
        
        return item_scores[:num_recommendations]
    
    def find_similar_users(self, user_id: str, num_similar: int = 3):
        """Find similar users using quantum entanglement."""
        
        if user_id not in self.graph.nodes:
            return []
        
        user_state = self.graph.get_node_state(user_id)
        similarities = []
        
        for other_user_id in self.graph.nodes:
            if (other_user_id != user_id and 
                self.graph.nodes[other_user_id].node_type == 'user'):
                
                other_state = self.graph.get_node_state(other_user_id)
                
                # Quantum similarity using state overlap
                similarity = abs(np.vdot(user_state, other_state))**2
                similarities.append((other_user_id, similarity))
        
        similarities.sort(key=lambda x: x[1], reverse=True)
        return similarities[:num_similar]
    
    def explain_recommendation(self, user_id: str, item_id: str):
        """Explain why an item was recommended using quantum reasoning."""
        
        if user_id not in self.graph.nodes or item_id not in self.graph.nodes:
            return {"error": "User or item not found"}
        
        # Calculate quantum similarity
        user_state = self.graph.get_node_state(user_id)
        item_state = self.graph.get_node_state(item_id)
        quantum_similarity = abs(np.vdot(user_state, item_state))**2
        
        # Find reasoning path through quantum walk
        inference = QuantumInference(self.graph)
        walk_result = inference.quantum_walk(user_id, steps=6)
        
        # Find intermediate nodes that led to recommendation
        reasoning_path = []
        for node_id, probability in walk_result.final_distribution.items():
            if (node_id != user_id and node_id != item_id and 
                probability > 0.1):
                
                if node_id in self.graph.nodes:
                    node_type = self.graph.nodes[node_id].node_type
                    reasoning_path.append((node_id, node_type, probability))
        
        reasoning_path.sort(key=lambda x: x[2], reverse=True)
        
        # Check for similar users who liked this item
        similar_users = self.find_similar_users(user_id, 3)
        user_connections = []
        
        for similar_user, similarity in similar_users:
            if (similar_user, item_id) in self.graph.edges:
                edge = self.graph.edges[(similar_user, item_id)]
                user_connections.append((similar_user, similarity, edge.rating))
        
        return {
            'quantum_similarity': quantum_similarity,
            'reasoning_path': reasoning_path[:3],
            'similar_user_connections': user_connections,
            'recommendation_strength': quantum_similarity * 0.7 + 
                                     len(user_connections) * 0.1
        }
    
    def update_user_preferences(self, user_id: str, feedback: Dict[str, float]):
        """Update user quantum state based on feedback."""
        
        if user_id not in self.graph.nodes:
            return
        
        current_state = self.graph.get_node_state(user_id)
        
        # Create feedback vector
        feedback_vector = np.zeros(self.graph.hilbert_dim, dtype=complex)
        for i, (item_id, rating) in enumerate(feedback.items()):
            if i < self.graph.hilbert_dim:
                feedback_vector[i] = rating / 5.0  # Normalize to [0,1]
        
        # Update quantum state using quantum learning rate
        learning_rate = 0.1
        new_state = (1 - learning_rate) * current_state + learning_rate * feedback_vector
        new_state = new_state / np.linalg.norm(new_state)
        
        self.graph.set_node_state(user_id, new_state)

# Example recommendation system
rec_system = QuantumRecommendationSystem(hilbert_dim=12)

# Add users
users_data = [
    ('user1', {'action': 0.8, 'comedy': 0.3, 'drama': 0.6, 'sci_fi': 0.9}),
    ('user2', {'action': 0.2, 'comedy': 0.9, 'drama': 0.4, 'sci_fi': 0.3}),
    ('user3', {'action': 0.7, 'comedy': 0.5, 'drama': 0.8, 'sci_fi': 0.6})
]

for user_id, preferences in users_data:
    rec_system.add_user(user_id, preferences)

# Add items (movies)
movies_data = [
    ('movie1', {'action': 0.9, 'comedy': 0.1, 'drama': 0.3, 'sci_fi': 0.8}, ['action', 'sci-fi']),
    ('movie2', {'action': 0.1, 'comedy': 0.9, 'drama': 0.2, 'sci_fi': 0.1}, ['comedy']),
    ('movie3', {'action': 0.3, 'comedy': 0.2, 'drama': 0.9, 'sci_fi': 0.4}, ['drama']),
    ('movie4', {'action': 0.6, 'comedy': 0.7, 'drama': 0.5, 'sci_fi': 0.3}, ['action', 'comedy'])
]

for movie_id, features, categories in movies_data:
    rec_system.add_item(movie_id, features, categories)

# Add interactions
interactions = [
    ('user1', 'movie1', 'like', 5.0),
    ('user1', 'movie3', 'like', 4.0),
    ('user2', 'movie2', 'like', 5.0),
    ('user2', 'movie4', 'like', 4.5),
    ('user3', 'movie1', 'like', 4.0),
    ('user3', 'movie3', 'like', 5.0)
]

for user_id, item_id, interaction_type, rating in interactions:
    rec_system.add_interaction(user_id, item_id, interaction_type, rating)

print(f"Recommendation system: {len(rec_system.graph.nodes)} nodes, {len(rec_system.graph.edges)} edges")

# Generate recommendations
recommendations = rec_system.generate_recommendations('user1', 3)
print("\nRecommendations for user1:")
for item_id, score, prob, interference in recommendations:
    print(f"  {item_id}: score={score:.3f}, probability={prob:.3f}, interference={interference:.3f}")

# Explain recommendation
explanation = rec_system.explain_recommendation('user1', 'movie2')
print(f"\nExplanation for recommending movie2 to user1:")
print(f"  Quantum similarity: {explanation['quantum_similarity']:.3f}")
print(f"  Recommendation strength: {explanation['recommendation_strength']:.3f}")

# Find similar users
similar_users = rec_system.find_similar_users('user1', 2)
print(f"\nUsers similar to user1:")
for similar_user, similarity in similar_users:
    print(f"  {similar_user}: similarity={similarity:.3f}")
```

## Integration and Deployment

### Creating Production-Ready Applications

```python
import logging
import json
from typing import Optional
from datetime import datetime

class ProductionQuantumGraph:
    """Production-ready quantum graph with monitoring and persistence."""
    
    def __init__(self, config_file: str):
        self.config = self._load_config(config_file)
        self.graph = EntangledGraph(self.config['hilbert_dim'])
        self.query_engine = None
        self.inference = None
        
        # Setup logging
        self._setup_logging()
        
        # Performance monitoring
        self.performance_metrics = {
            'query_count': 0,
            'avg_query_time': 0.0,
            'total_queries': 0,
            'error_count': 0
        }
    
    def _load_config(self, config_file: str) -> Dict[str, Any]:
        """Load configuration from file."""
        with open(config_file, 'r') as f:
            return json.load(f)
    
    def _setup_logging(self):
        """Setup application logging."""
        logging.basicConfig(
            level=getattr(logging, self.config.get('log_level', 'INFO')),
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(self.config.get('log_file', 'quantum_graph.log')),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
    
    def initialize_engines(self):
        """Initialize query and inference engines."""
        try:
            self.query_engine = EntangledQueryEngine(self.graph)
            self.inference = QuantumInference(self.graph)
            self.logger.info("Quantum engines initialized successfully")
        except Exception as e:
            self.logger.error(f"Failed to initialize engines: {e}")
            raise
    
    def health_check(self) -> Dict[str, Any]:
        """Perform system health check."""
        try:
            health_status = {
                'timestamp': datetime.now().isoformat(),
                'graph_nodes': len(self.graph.nodes),
                'graph_edges': len(self.graph.edges),
                'coherence': self.graph.measure_coherence(),
                'engines_ready': self.query_engine is not None,
                'performance_metrics': self.performance_metrics.copy()
            }
            
            # Check for potential issues
            issues = []
            if health_status['coherence'] < 0.3:
                issues.append("Low quantum coherence")
            
            if self.performance_metrics['error_count'] > 10:
                issues.append("High error rate")
            
            health_status['issues'] = issues
            health_status['status'] = 'healthy' if not issues else 'warning'
            
            return health_status
            
        except Exception as e:
            self.logger.error(f"Health check failed: {e}")
            return {
                'status': 'error',
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }
    
    def safe_query(self, query: str, max_results: int = 5) -> Dict[str, Any]:
        """Safe query execution with error handling and monitoring."""
        start_time = time.time()
        
        try:
            if not self.query_engine:
                raise RuntimeError("Query engine not initialized")
            
            # Execute query
            results = self.query_engine.query(query, max_results)
            
            # Update metrics
            query_time = time.time() - start_time
            self._update_performance_metrics(query_time, success=True)
            
            # Format results
            formatted_results = []
            for result in results:
                formatted_results.append({
                    'answer_nodes': result.answer_nodes,
                    'confidence_score': result.confidence_score,
                    'reasoning_path': result.reasoning_path
                })
            
            self.logger.info(f"Query completed: '{query}' -> {len(results)} results in {query_time:.3f}s")
            
            return {
                'status': 'success',
                'query': query,
                'results': formatted_results,
                'execution_time': query_time,
                'timestamp': datetime.now().isoformat()
            }
            
        except Exception as e:
            query_time = time.time() - start_time
            self._update_performance_metrics(query_time, success=False)
            
            self.logger.error(f"Query failed: '{query}' -> {e}")
            
            return {
                'status': 'error',
                'query': query,
                'error': str(e),
                'execution_time': query_time,
                'timestamp': datetime.now().isoformat()
            }
    
    def _update_performance_metrics(self, query_time: float, success: bool):
        """Update performance metrics."""
        self.performance_metrics['total_queries'] += 1
        
        if success:
            self.performance_metrics['query_count'] += 1
            
            # Update average query time
            current_avg = self.performance_metrics['avg_query_time']
            total_successful = self.performance_metrics['query_count']
            
            new_avg = ((current_avg * (total_successful - 1)) + query_time) / total_successful
            self.performance_metrics['avg_query_time'] = new_avg
        else:
            self.performance_metrics['error_count'] += 1
    
    def save_graph(self, filepath: str):
        """Save graph state to file."""
        try:
            graph_data = {
                'nodes': {node_id: {
                    'properties': vars(node),
                    'quantum_state': self.graph.get_node_state(node_id).tolist()
                } for node_id, node in self.graph.nodes.items()},
                'edges': {f"{source}->{target}": {
                    'properties': vars(edge)
                } for (source, target), edge in self.graph.edges.items()},
                'hilbert_dim': self.graph.hilbert_dim,
                'timestamp': datetime.now().isoformat()
            }
            
            with open(filepath, 'w') as f:
                json.dump(graph_data, f, indent=2, default=str)
            
            self.logger.info(f"Graph saved to {filepath}")
            
        except Exception as e:
            self.logger.error(f"Failed to save graph: {e}")
            raise
    
    def load_graph(self, filepath: str):
        """Load graph state from file."""
        try:
            with open(filepath, 'r') as f:
                graph_data = json.load(f)
            
            # Recreate graph
            self.graph = EntangledGraph(graph_data['hilbert_dim'])
            
            # Restore nodes
            for node_id, node_data in graph_data['nodes'].items():
                properties = node_data['properties']
                quantum_state = np.array(node_data['quantum_state'])
                
                node = QuantumNode(node_id, **properties)
                self.graph.add_node(node)
                self.graph.set_node_state(node_id, quantum_state)
            
            # Restore edges
            for edge_key, edge_data in graph_data['edges'].items():
                source, target = edge_key.split('->')
                properties = edge_data['properties']
                
                edge = EntangledEdge(source, target, **properties)
                self.graph.add_edge(edge)
            
            self.logger.info(f"Graph loaded from {filepath}")
            
        except Exception as e:
            self.logger.error(f"Failed to load graph: {e}")
            raise

# Example configuration file (config.json)
config_example = {
    "hilbert_dim": 16,
    "log_level": "INFO",
    "log_file": "quantum_app.log",
    "cache_size": 1000,
    "max_query_time": 30.0,
    "coherence_threshold": 0.3
}

# Save example config
with open('config.json', 'w') as f:
    json.dump(config_example, f, indent=2)

# Example production application
print("Production quantum graph application initialized!")
print("Features:")
print("- Configuration management")
print("- Comprehensive logging")
print("- Performance monitoring") 
print("- Health checks")
print("- Safe query execution")
print("- Graph persistence")
```

## Testing and Validation

### Quantum Graph Testing Framework

```python
import unittest
import numpy as np
from unittest.mock import Mock, patch

class QuantumGraphTestCase(unittest.TestCase):
    """Base test case for quantum graph applications."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.graph = EntangledGraph(hilbert_dim=8)
        self.test_nodes = [
            QuantumNode("node1", node_type="test"),
            QuantumNode("node2", node_type="test"),
            QuantumNode("node3", node_type="test")
        ]
        
        for node in self.test_nodes:
            self.graph.add_node(node)
    
    def tearDown(self):
        """Clean up after tests."""
        self.graph = None
    
    def assert_quantum_state_valid(self, node_id):
        """Assert that a node's quantum state is valid."""
        state = self.graph.get_node_state(node_id)
        
        # Check normalization
        norm = np.linalg.norm(state)
        self.assertAlmostEqual(norm, 1.0, places=6, 
                              msg=f"Node {node_id} state not normalized")
        
        # Check for NaN values
        self.assertFalse(np.any(np.isnan(state)), 
                        msg=f"Node {node_id} contains NaN values")
        
        # Check dimension
        self.assertEqual(len(state), self.graph.hilbert_dim,
                        msg=f"Node {node_id} state dimension mismatch")
    
    def assert_entanglement_valid(self, source, target):
        """Assert that entanglement between nodes is valid."""
        entanglement = self.graph.measure_entanglement(source, target)
        
        self.assertGreaterEqual(entanglement, 0.0,
                               msg="Entanglement cannot be negative")
        self.assertLessEqual(entanglement, 1.0,
                            msg="Entanglement cannot exceed 1.0")
    
    def assert_coherence_maintained(self, min_coherence=0.1):
        """Assert that graph maintains quantum coherence."""
        coherence = self.graph.measure_coherence()
        self.assertGreaterEqual(coherence, min_coherence,
                               msg=f"Graph coherence too low: {coherence}")

class TestBiomedicalGraph(QuantumGraphTestCase):
    """Test biomedical quantum graph functionality."""
    
    def setUp(self):
        super().setUp()
        self.bio_graph = BiomedicalQuantumGraph(hilbert_dim=8)
    
    def test_biomedical_entity_creation(self):
        """Test creating biomedical entities."""
        self.bio_graph.add_biomedical_entity("test_protein", "protein")
        
        self.assertIn("test_protein", self.bio_graph.graph.nodes)
        self.assert_quantum_state_valid("test_protein")
    
    def test_drug_target_prediction(self):
        """Test drug target prediction functionality."""
        # Add test data
        self.bio_graph.add_biomedical_entity("disease1", "disease")
        self.bio_graph.add_biomedical_entity("protein1", "protein")
        self.bio_graph.add_biomedical_relationship("protein1", "disease1", 
                                                  "associated_with", 0.8)
        
        targets = self.bio_graph.find_drug_targets("disease1", 1)
        
        self.assertIsInstance(targets, list)
        self.assertGreater(len(targets), 0)
    
    def test_biomedical_entanglement_calculation(self):
        """Test biomedical-specific entanglement calculation."""
        strength = self.bio_graph._calculate_biomedical_entanglement(
            "protein1", "disease1", "causes", 0.9, 1.0
        )
        
        self.assertGreater(strength, 0.0)
        self.assertLess(strength, 1.0)

class TestFinancialGraph(QuantumGraphTestCase):
    """Test financial quantum graph functionality."""
    
    def setUp(self):
        super().setUp()
        self.financial_graph = FinancialQuantumGraph(hilbert_dim=8)
    
    def test_financial_entity_creation(self):
        """Test creating financial entities."""
        self.financial_graph.add_financial_entity(
            "TEST_STOCK", "stock", 
            {"volatility": 0.2, "market_cap": 1000000}
        )
        
        self.assertIn("TEST_STOCK", self.financial_graph.graph.nodes)
        self.assert_quantum_state_valid("TEST_STOCK")
    
    def test_portfolio_risk_calculation(self):
        """Test portfolio risk calculation."""
        # Add test assets
        assets = ["ASSET1", "ASSET2"]
        for asset in assets:
            self.financial_graph.add_financial_entity(
                asset, "stock", {"volatility": 0.1}
            )
        
        risk = self.financial_graph.calculate_portfolio_risk(assets, [0.5, 0.5])
        
        self.assertIsInstance(risk, float)
        self.assertGreater(risk, 0.0)
    
    def test_market_state_update(self):
        """Test market state updates."""
        # Add test asset
        self.financial_graph.add_financial_entity("TEST", "stock")
        initial_state = self.financial_graph.graph.get_node_state("TEST").copy()
        
        # Update market state
        self.financial_graph.update_market_state("crisis")
        
        updated_state = self.financial_graph.graph.get_node_state("TEST")
        
        # States should be different after market update
        self.assertFalse(np.allclose(initial_state, updated_state, atol=1e-6))

class TestRecommendationSystem(QuantumGraphTestCase):
    """Test quantum recommendation system."""
    
    def setUp(self):
        super().setUp()
        self.rec_system = QuantumRecommendationSystem(hilbert_dim=8)
    
    def test_user_addition(self):
        """Test adding users to recommendation system."""
        preferences = {"action": 0.8, "comedy": 0.3}
        self.rec_system.add_user("test_user", preferences)
        
        self.assertIn("test_user", self.rec_system.graph.nodes)
        self.assert_quantum_state_valid("test_user")
    
    def test_recommendation_generation(self):
        """Test recommendation generation."""
        # Add test data
        self.rec_system.add_user("user1", {"action": 0.8})
        self.rec_system.add_item("item1", {"action": 0.9})
        self.rec_system.add_interaction("user1", "item1", "like", 5.0)
        
        # Add another item to recommend
        self.rec_system.add_item("item2", {"action": 0.7})
        
        recommendations = self.rec_system.generate_recommendations("user1", 1)
        
        self.assertIsInstance(recommendations, list)
        if len(recommendations) > 0:
            self.assertIsInstance(recommendations[0], tuple)
            self.assertEqual(len(recommendations[0]), 4)  # (item_id, score, prob, interference)

# Performance testing
class TestQuantumPerformance(unittest.TestCase):
    """Test quantum graph performance characteristics."""
    
    def test_large_graph_performance(self):
        """Test performance with large graphs."""
        import time
        
        graph = EntangledGraph(hilbert_dim=10)
        
        # Add many nodes
        start_time = time.time()
        for i in range(100):
            node = QuantumNode(f"node_{i}", node_type="test")
            graph.add_node(node)
        node_creation_time = time.time() - start_time
        
        # Add many edges
        start_time = time.time()
        for i in range(50):
            edge = EntangledEdge(f"node_{i}", f"node_{i+1}", 
                               relation="connects", entanglement_strength=0.5)
            graph.add_edge(edge)
        edge_creation_time = time.time() - start_time
        
        # Test coherence measurement
        start_time = time.time()
        coherence = graph.measure_coherence()
        coherence_time = time.time() - start_time
        
        # Performance assertions
        self.assertLess(node_creation_time, 1.0, "Node creation too slow")
        self.assertLess(edge_creation_time, 1.0, "Edge creation too slow")
        self.assertLess(coherence_time, 5.0, "Coherence measurement too slow")
        
        print(f"\nPerformance Results:")
        print(f"  Node creation (100): {node_creation_time:.3f}s")
        print(f"  Edge creation (50): {edge_creation_time:.3f}s")
        print(f"  Coherence measurement: {coherence_time:.3f}s")

# Run tests
if __name__ == "__main__":
    # Create test suite
    suite = unittest.TestSuite()
    
    # Add test cases
    suite.addTest(unittest.makeSuite(TestBiomedicalGraph))
    suite.addTest(unittest.makeSuite(TestFinancialGraph))
    suite.addTest(unittest.makeSuite(TestRecommendationSystem))
    suite.addTest(unittest.makeSuite(TestQuantumPerformance))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print(f"\nTest Results:")
    print(f"  Tests run: {result.testsRun}")
    print(f"  Failures: {len(result.failures)}")
    print(f"  Errors: {len(result.errors)}")
    print(f"  Success rate: {((result.testsRun - len(result.failures) - len(result.errors)) / result.testsRun * 100):.1f}%")
```

Congratulations! You've mastered building custom quantum knowledge graph applications! 🎉⚛️ 

This tutorial covered:

- **Domain-Specific Applications**: Biomedical, financial, and recommendation systems
- **Production Deployment**: Configuration, logging, monitoring, and persistence
- **Testing Framework**: Comprehensive testing for quantum applications
- **Performance Optimization**: Large-scale graph handling and monitoring

You're now equipped to build sophisticated quantum knowledge systems for any domain! Explore the [Use Cases](../use_cases/) section for real-world implementations and best practices.
