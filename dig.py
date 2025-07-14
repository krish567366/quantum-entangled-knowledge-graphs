# diagnose_qekgr.py
import sys
sys.path.insert(0, '.')

try:
    import qekgr
    from qekgr import EntangledGraph, QuantumInference, EntangledQueryEngine

    print('🚀 QE-KGR Library Test')
    print('=' * 30)

    graph = EntangledGraph(hilbert_dim=4)
    print(f'✅ Created quantum graph with Hilbert dimension: {graph.hilbert_dim}')

    alice = graph.add_quantum_node('Alice', state='researcher',
                                   metadata={'field': 'quantum_physics'})
    bob = graph.add_quantum_node('Bob', state='professor',
                                 metadata={'field': 'computer_science'})

    print('✅ Added quantum nodes: Alice, Bob')

    edge = graph.add_entangled_edge(alice, bob,
                                    relations=['collaborates', 'co_authors'],
                                    amplitudes=[0.8, 0.6])
    print(f'✅ Added entangled edge with strength: {edge.entanglement_strength:.3f}')

    inference = QuantumInference(graph)
    walk_result = inference.quantum_walk(start_node='Alice', steps=5)

    print(f'✅ Quantum walk completed: {len(walk_result.path)} steps')
    print('   Path: ' + ' -> '.join(walk_result.path))

    query_engine = EntangledQueryEngine(graph)
    results = query_engine.query('Who collaborates with Alice?')

    print(f'✅ Query processed: {len(results)} results found')
    if results:
        print(f'   Top result confidence: {results[0].confidence_score:.3f}')

    print()
    print('🎉 All core functionality working!')
    print('📚 QE-KGR is ready for quantum-enhanced knowledge reasoning!')

except Exception as e:
    print(f'❌ Error: {e}')
    import traceback
    traceback.print_exc()
