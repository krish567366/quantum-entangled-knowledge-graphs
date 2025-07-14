"""
Example: Drug Discovery with Quantum Entangled Knowledge Graphs

This example demonstrates how to use QE-KGR for discovering hidden
molecular interaction patterns and predicting novel drug targets.
"""

import numpy as np
import qekgr
from qekgr import EntangledGraph, QuantumInference, EntangledQueryEngine
from qekgr.utils import QuantumGraphVisualizer


def create_drug_discovery_graph():
    """Create a quantum knowledge graph for drug discovery."""
    
    # Create graph with higher dimensional Hilbert space for complex molecular states
    graph = EntangledGraph(hilbert_dim=8)
    
    # Add drug molecules as quantum nodes
    drugs = [
        ("Aspirin", "anti_inflammatory", {"target": "COX", "indication": "pain"}),
        ("Ibuprofen", "anti_inflammatory", {"target": "COX", "indication": "pain"}), 
        ("Metformin", "antidiabetic", {"target": "AMPK", "indication": "diabetes"}),
        ("Statins", "cholesterol_lowering", {"target": "HMG_CoA", "indication": "cardiovascular"}),
        ("ACE_inhibitors", "antihypertensive", {"target": "ACE", "indication": "hypertension"}),
        ("Warfarin", "anticoagulant", {"target": "VKORC1", "indication": "thrombosis"})
    ]
    
    for drug_name, drug_class, metadata in drugs:
        graph.add_quantum_node(drug_name, state=drug_class, metadata=metadata)
    
    # Add protein targets
    proteins = [
        ("COX1", "enzyme", {"function": "prostaglandin_synthesis", "location": "stomach"}),
        ("COX2", "enzyme", {"function": "inflammation", "location": "inflammatory_sites"}),
        ("AMPK", "kinase", {"function": "energy_metabolism", "location": "liver"}),
        ("HMG_CoA_reductase", "enzyme", {"function": "cholesterol_synthesis", "location": "liver"}),
        ("ACE", "enzyme", {"function": "blood_pressure_regulation", "location": "lungs"}),
        ("VKORC1", "enzyme", {"function": "vitamin_K_recycling", "location": "liver"})
    ]
    
    for protein_name, protein_type, metadata in proteins:
        graph.add_quantum_node(protein_name, state=protein_type, metadata=metadata)
    
    # Add diseases/conditions
    conditions = [
        ("Inflammation", "pathological_process", {"category": "immune_response"}),
        ("Pain", "symptom", {"category": "sensory"}),
        ("Diabetes", "metabolic_disorder", {"category": "endocrine"}),
        ("Cardiovascular_disease", "systemic_disorder", {"category": "circulatory"}),
        ("Hypertension", "cardiovascular_condition", {"category": "pressure_disorder"}),
        ("Thrombosis", "blood_disorder", {"category": "coagulation"})
    ]
    
    for condition_name, condition_type, metadata in conditions:
        graph.add_quantum_node(condition_name, state=condition_type, metadata=metadata)
    
    # Add entangled drug-target interactions with quantum superposition
    drug_target_interactions = [
        ("Aspirin", "COX1", ["inhibits", "binds", "acetylates"], [0.9, 0.8, 0.7]),
        ("Aspirin", "COX2", ["inhibits", "binds"], [0.8, 0.7]),
        ("Ibuprofen", "COX1", ["inhibits", "competes"], [0.7, 0.6]),
        ("Ibuprofen", "COX2", ["inhibits", "selective"], [0.9, 0.8]),
        ("Metformin", "AMPK", ["activates", "phosphorylates"], [0.9, 0.7]),
        ("Statins", "HMG_CoA_reductase", ["inhibits", "competitive"], [0.95, 0.9]),
        ("ACE_inhibitors", "ACE", ["inhibits", "blocks_active_site"], [0.9, 0.8]),
        ("Warfarin", "VKORC1", ["inhibits", "interferes"], [0.8, 0.7])
    ]
    
    for drug, target, relations, amplitudes in drug_target_interactions:
        graph.add_entangled_edge(drug, target, relations, amplitudes)
    
    # Add drug-condition relationships
    drug_condition_relations = [
        ("Aspirin", "Pain", ["treats", "reduces"], [0.8, 0.7]),
        ("Aspirin", "Inflammation", ["reduces", "suppresses"], [0.7, 0.6]),
        ("Ibuprofen", "Pain", ["treats", "alleviates"], [0.9, 0.8]),
        ("Ibuprofen", "Inflammation", ["reduces", "anti_inflammatory"], [0.8, 0.9]),
        ("Metformin", "Diabetes", ["treats", "controls_glucose"], [0.9, 0.8]),
        ("Statins", "Cardiovascular_disease", ["prevents", "reduces_risk"], [0.8, 0.7]),
        ("ACE_inhibitors", "Hypertension", ["treats", "lowers_pressure"], [0.9, 0.8]),
        ("Warfarin", "Thrombosis", ["prevents", "anticoagulates"], [0.8, 0.7])
    ]
    
    for drug, condition, relations, amplitudes in drug_condition_relations:
        graph.add_entangled_edge(drug, condition, relations, amplitudes)
    
    # Add target-condition relationships
    target_condition_relations = [
        ("COX1", "Pain", ["mediates", "involved_in"], [0.6, 0.7]),
        ("COX2", "Inflammation", ["mediates", "drives"], [0.8, 0.9]),
        ("AMPK", "Diabetes", ["regulates", "controls_metabolism"], [0.7, 0.8]),
        ("HMG_CoA_reductase", "Cardiovascular_disease", ["contributes", "risk_factor"], [0.6, 0.7]),
        ("ACE", "Hypertension", ["causes", "regulates"], [0.8, 0.9]),
        ("VKORC1", "Thrombosis", ["prevents_when_inhibited", "related"], [0.5, 0.6])
    ]
    
    for target, condition, relations, amplitudes in target_condition_relations:
        graph.add_entangled_edge(target, condition, relations, amplitudes)
    
    return graph


def discover_drug_repurposing_opportunities(graph, inference_engine, query_engine):
    """Discover drug repurposing opportunities using quantum reasoning."""
    
    print("🔬 Drug Repurposing Discovery using Quantum Entanglement")
    print("=" * 60)
    
    # Query for unexpected drug-condition connections
    repurposing_queries = [
        "What diabetes drugs might help with inflammation?",
        "Could cardiovascular drugs treat other conditions?", 
        "What pain medications might have anti-diabetic effects?",
        "Find drugs that could treat multiple conditions simultaneously"
    ]
    
    discoveries = []
    
    for query in repurposing_queries:
        print(f"\n🔍 Query: {query}")
        results = query_engine.query(query, max_results=3)
        
        for i, result in enumerate(results, 1):
            if result.confidence_score > 0.3:  # Filter for meaningful results
                print(f"  Result {i} (Confidence: {result.confidence_score:.3f}):")
                print(f"    Entities: {', '.join(result.answer_nodes)}")
                print(f"    Reasoning: {' → '.join(result.reasoning_path)}")
                
                discoveries.append({
                    'query': query,
                    'entities': result.answer_nodes,
                    'confidence': result.confidence_score,
                    'path': result.reasoning_path
                })
    
    return discoveries


def find_novel_drug_targets(graph, inference_engine):
    """Use quantum walks to discover novel drug targets."""
    
    print("\n🎯 Novel Drug Target Discovery")
    print("=" * 40)
    
    # Start quantum walks from known drugs to find connected targets
    known_drugs = ["Aspirin", "Metformin", "Statins"]
    
    novel_targets = {}
    
    for drug in known_drugs:
        print(f"\n🚶 Quantum walk from {drug}:")
        
        # Perform quantum walk with bias toward target proteins
        walk_result = inference_engine.quantum_walk(
            start_node=drug,
            steps=10,
            bias_relations=["inhibits", "activates", "binds"]
        )
        
        print(f"  Path: {' → '.join(walk_result.path)}")
        print(f"  Entanglement evolution: {np.array(walk_result.entanglement_trace)[:5]}")
        
        # Analyze path for potential new targets
        proteins_in_path = [node for node in walk_result.path 
                          if node in graph.nodes and 
                          graph.nodes[node].metadata.get('function')]
        
        if len(proteins_in_path) > 1:
            novel_targets[drug] = proteins_in_path[1:]  # Exclude direct targets
            
    return novel_targets


def predict_drug_drug_interactions(graph, inference_engine):
    """Predict potential drug-drug interactions using entanglement analysis."""
    
    print("\n⚠️  Drug-Drug Interaction Prediction")
    print("=" * 45)
    
    drugs = [node for node in graph.nodes.keys() 
             if node in ["Aspirin", "Ibuprofen", "Metformin", "Statins", "ACE_inhibitors", "Warfarin"]]
    
    interactions = []
    
    for i, drug1 in enumerate(drugs):
        for drug2 in drugs[i+1:]:
            # Find common targets or pathways
            drug1_neighbors = set(graph.get_neighbors(drug1))
            drug2_neighbors = set(graph.get_neighbors(drug2))
            common_targets = drug1_neighbors & drug2_neighbors
            
            if common_targets:
                # Calculate quantum interference between drug states
                overlap = graph.get_quantum_state_overlap(drug1, drug2)
                interaction_strength = abs(overlap)
                
                print(f"  {drug1} ↔ {drug2}:")
                print(f"    Common targets: {', '.join(common_targets)}")
                print(f"    Quantum interference: {interaction_strength:.3f}")
                
                if interaction_strength > 0.5:
                    print(f"    ⚠️  High interaction potential!")
                
                interactions.append({
                    'drug1': drug1,
                    'drug2': drug2, 
                    'common_targets': list(common_targets),
                    'interaction_strength': interaction_strength
                })
    
    return interactions


def analyze_molecular_networks(graph, inference_engine):
    """Analyze molecular interaction networks using quantum subgraph discovery."""
    
    print("\n🕸️  Molecular Network Analysis")
    print("=" * 35)
    
    # Discover entangled molecular communities
    seed_combinations = [
        ["COX1", "COX2"],  # Inflammation pathway
        ["AMPK", "Diabetes"],  # Metabolic pathway  
        ["ACE", "Hypertension"],  # Cardiovascular pathway
    ]
    
    networks = {}
    
    for i, seeds in enumerate(seed_combinations):
        print(f"\n🔬 Network {i+1} starting from: {', '.join(seeds)}")
        
        discovery = inference_engine.discover_entangled_subgraph(
            seed_nodes=seeds,
            expansion_steps=3,
            min_entanglement=0.4
        )
        
        print(f"  Discovered nodes: {', '.join(discovery.nodes)}")
        print(f"  Network density: {discovery.entanglement_density:.3f}")
        print(f"  Coherence: {discovery.coherence_measure:.3f}")
        print(f"  Confidence: {discovery.discovery_confidence:.3f}")
        
        networks[f"network_{i+1}"] = discovery
    
    return networks


def main():
    """Main drug discovery analysis workflow."""
    
    print("🧬 Quantum Entangled Drug Discovery Analysis")
    print("=" * 50)
    
    # Create the drug discovery knowledge graph
    print("📊 Creating quantum drug discovery knowledge graph...")
    graph = create_drug_discovery_graph()
    
    print(f"✅ Graph created with {len(graph.nodes)} entities and {len(graph.edges)} relationships")
    
    # Initialize reasoning engines
    inference_engine = QuantumInference(graph)
    query_engine = EntangledQueryEngine(graph)
    
    # Run discovery analyses
    repurposing_discoveries = discover_drug_repurposing_opportunities(graph, inference_engine, query_engine)
    novel_targets = find_novel_drug_targets(graph, inference_engine)
    drug_interactions = predict_drug_drug_interactions(graph, inference_engine)
    molecular_networks = analyze_molecular_networks(graph, inference_engine)
    
    # Summary insights
    print("\n📋 Summary of Quantum-Enhanced Discoveries")
    print("=" * 50)
    print(f"💊 Drug repurposing opportunities found: {len(repurposing_discoveries)}")
    print(f"🎯 Novel target suggestions: {sum(len(targets) for targets in novel_targets.values())}")
    print(f"⚠️  Potential drug interactions: {len(drug_interactions)}")
    print(f"🕸️  Molecular networks identified: {len(molecular_networks)}")
    
    # Highlight most promising discoveries
    if repurposing_discoveries:
        best_discovery = max(repurposing_discoveries, key=lambda x: x['confidence'])
        print(f"\n🌟 Most promising repurposing opportunity:")
        print(f"   Query: {best_discovery['query']}")
        print(f"   Entities: {', '.join(best_discovery['entities'])}")
        print(f"   Confidence: {best_discovery['confidence']:.3f}")
    
    # Create visualization
    try:
        print("\n📈 Generating quantum graph visualization...")
        visualizer = QuantumGraphVisualizer(graph)
        
        # Create molecular network visualization
        fig_3d = visualizer.visualize_graph_3d(color_by="entanglement")
        fig_3d.write_html("drug_discovery_network_3d.html")
        
        # Create entanglement heatmap
        fig_heatmap = visualizer.visualize_entanglement_heatmap()
        fig_heatmap.write_html("drug_entanglement_heatmap.html")
        
        print("✅ Visualizations saved: drug_discovery_network_3d.html, drug_entanglement_heatmap.html")
        
    except ImportError:
        print("📊 Visualization libraries not available. Install with: pip install plotly")
    
    return {
        'graph': graph,
        'repurposing': repurposing_discoveries,
        'novel_targets': novel_targets,
        'interactions': drug_interactions,
        'networks': molecular_networks
    }


if __name__ == "__main__":
    results = main()
