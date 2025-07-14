# Visualization Module

The `qekgr.utils.visualization` module provides comprehensive visualization capabilities for quantum entangled knowledge graphs. The `QuantumGraphVisualizer` class offers 2D/3D interactive visualizations, entanglement heatmaps, and quantum state projections.

## Classes Overview

### `QuantumGraphVisualizer`

Main visualization class for creating interactive quantum graph visualizations.

### Configuration Classes

- `VisualizationConfig` - Configuration options for visualization appearance

---

## QuantumGraphVisualizer

### Class Definition

```python
class QuantumGraphVisualizer:
    """
    Comprehensive visualization toolkit for quantum entangled graphs.
    
    Provides methods for visualizing quantum graphs, entanglement patterns,
    reasoning paths, and quantum state projections.
    """
```

### Constructor

```python
def __init__(
    self,
    graph: EntangledGraph,
    config: Optional[VisualizationConfig] = None
) -> None
```

**Parameters:**

- `graph` (EntangledGraph): The entangled graph to visualize
- `config` (VisualizationConfig, optional): Visualization configuration

**Example:**

```python
from qekgr import EntangledGraph
from qekgr.utils import QuantumGraphVisualizer, VisualizationConfig

# Create graph
graph = EntangledGraph(hilbert_dim=4)
# ... populate graph ...

# Create visualizer with custom config
config = VisualizationConfig(
    width=1200,
    height=800,
    color_scheme="plasma",
    show_quantum_info=True
)
visualizer = QuantumGraphVisualizer(graph, config)
```

### 2D Visualization Methods

#### `visualize_graph_2d`

```python
def visualize_graph_2d(
    self,
    layout: str = "spring",
    highlight_nodes: Optional[List[str]] = None,
    highlight_edges: Optional[List[Tuple[str, str]]] = None,
    color_by: str = "node_type"
) -> go.Figure
```

Create 2D visualization of the quantum graph.

**Parameters:**

- `layout` (str): Layout algorithm ("spring", "circular", "kamada_kawai", "quantum_force")
- `highlight_nodes` (List[str], optional): Nodes to highlight
- `highlight_edges` (List[Tuple[str, str]], optional): Edges to highlight  
- `color_by` (str): Coloring scheme ("node_type", "entanglement", "quantum_state")

**Returns:**

- `go.Figure`: Plotly figure object

**Example:**

```python
# Basic 2D visualization
fig_2d = visualizer.visualize_graph_2d(layout="spring")
fig_2d.show()

# Highlight specific nodes and edges
fig_highlighted = visualizer.visualize_graph_2d(
    layout="quantum_force",
    highlight_nodes=["Alice", "Bob"],
    highlight_edges=[("Alice", "Bob")],
    color_by="entanglement"
)
fig_highlighted.show()
```

#### `visualize_quantum_states_2d`

```python
def visualize_quantum_states_2d(
    self,
    method: str = "tsne",
    perplexity: float = 30.0,
    n_components: int = 2
) -> go.Figure
```

Visualize quantum states projected to 2D space.

**Parameters:**

- `method` (str): Projection method ("tsne", "pca", "umap")
- `perplexity` (float): t-SNE perplexity parameter
- `n_components` (int): Number of output dimensions

**Returns:**

- `go.Figure`: 2D projection of quantum states

**Example:**

```python
# t-SNE projection of quantum states
fig_tsne = visualizer.visualize_quantum_states_2d(
    method="tsne",
    perplexity=20.0
)
fig_tsne.show()

# PCA projection
fig_pca = visualizer.visualize_quantum_states_2d(method="pca")
fig_pca.show()
```

### 3D Visualization Methods

#### `visualize_graph_3d`

```python
def visualize_graph_3d(
    self,
    layout: str = "spring_3d",
    color_by: str = "entanglement",
    size_by: str = "degree",
    show_edge_labels: bool = False
) -> go.Figure
```

Create 3D interactive visualization of the quantum graph.

**Parameters:**

- `layout` (str): 3D layout algorithm ("spring_3d", "sphere", "quantum_embedding")
- `color_by` (str): Node coloring scheme
- `size_by` (str): Node sizing scheme ("degree", "centrality", "entropy")
- `show_edge_labels` (bool): Whether to show edge relation labels

**Returns:**

- `go.Figure`:Interactive 3D plotly figure

**Example:**

```python
# 3D visualization with entanglement coloring
fig_3d = visualizer.visualize_graph_3d(
    layout="quantum_embedding",
    color_by="entanglement",
    size_by="centrality",
    show_edge_labels=True
)
fig_3d.show()

# Save as HTML
fig_3d.write_html("quantum_graph_3d.html")
```

#### `visualize_quantum_hilbert_space`

```python
def visualize_quantum_hilbert_space(
    self,
    selected_nodes: Optional[List[str]] = None,
    projection_method: str = "bloch_sphere"
) -> go.Figure
```

Visualize quantum states in Hilbert space.

**Parameters:**

- `selected_nodes` (List[str], optional): Specific nodes to visualize
- `projection_method` (str): Visualization method ("bloch_sphere", "state_space", "poincare")

**Returns:**

- `go.Figure`: Hilbert space visualization

**Example:**

```python
# Bloch sphere representation (for 2D Hilbert space)
fig_bloch = visualizer.visualize_quantum_hilbert_space(
    selected_nodes=["Alice", "Bob"],
    projection_method="bloch_sphere"
)
fig_bloch.show()
```

### Heatmap Visualizations

#### `visualize_entanglement_heatmap`

```python
def visualize_entanglement_heatmap(
    self,
    normalize: bool = True,
    cluster: bool = True
) -> go.Figure
```

Create entanglement strength heatmap between all node pairs.

**Parameters:**

- `normalize` (bool): Whether to normalize entanglement values
- `cluster` (bool): Whether to cluster similar nodes together

**Returns:**

- `go.Figure`: Heatmap visualization

**Example:**

```python
# Entanglement heatmap
fig_heatmap = visualizer.visualize_entanglement_heatmap(
    normalize=True,
    cluster=True
)
fig_heatmap.show()
```

#### `visualize_quantum_correlation_matrix`

```python
def visualize_quantum_correlation_matrix(
    self,
    correlation_type: str = "quantum_mutual_information"
) -> go.Figure
```

Visualize quantum correlations between nodes.

**Parameters:**

- `correlation_type` (str): Type of correlation ("quantum_mutual_information", "entanglement_entropy", "fidelity")

**Returns:**

- `go.Figure`: Correlation matrix heatmap

**Example:**

```python
# Quantum mutual information matrix
fig_corr = visualizer.visualize_quantum_correlation_matrix(
    correlation_type="quantum_mutual_information"
)
fig_corr.show()
```

### Dynamic Visualizations

#### `animate_quantum_walk`

```python
def animate_quantum_walk(
    self,
    walk_result: QuantumWalkResult,
    frame_duration: int = 500,
    show_amplitudes: bool = True
) -> go.Figure
```

Create animated visualization of quantum walk.

**Parameters:**

- `walk_result` (QuantumWalkResult): Result from quantum walk
- `frame_duration` (int): Duration of each frame in milliseconds
- `show_amplitudes` (bool): Whether to show quantum amplitudes

**Returns:**

- `go.Figure`: Animated quantum walk visualization

**Example:**

```python
from qekgr import QuantumInference

# Perform quantum walk
inference = QuantumInference(graph)
walk_result = inference.quantum_walk("Alice", steps=15)

# Animate the walk
fig_animation = visualizer.animate_quantum_walk(
    walk_result=walk_result,
    frame_duration=800,
    show_amplitudes=True
)
fig_animation.show()
```

#### `animate_query_reasoning`

```python
def animate_query_reasoning(
    self,
    query_results: List[QueryResult],
    highlight_path: bool = True
) -> go.Figure
```

Animate the reasoning process for query results.

**Parameters:**

- `query_results` (List[QueryResult]): Results from query engine
- `highlight_path` (bool): Whether to highlight reasoning paths

**Returns:**

- `go.Figure`: Animated reasoning visualization

### Specialized Visualizations

#### `visualize_interference_patterns`

```python
def visualize_interference_patterns(
    self,
    source_nodes: List[str],
    interference_type: str = "constructive"
) -> go.Figure
```

Visualize quantum interference patterns in the graph.

**Parameters:**

- `source_nodes` (List[str]): Nodes to start interference from
- `interference_type` (str): Type of interference to visualize

**Returns:**

- `go.Figure`: Interference pattern visualization

**Example:**

```python
# Visualize interference from multiple sources
fig_interference = visualizer.visualize_interference_patterns(
    source_nodes=["Alice", "Bob", "Charlie"],
    interference_type="constructive"
)
fig_interference.show()
```

#### `visualize_entanglement_network`

```python
def visualize_entanglement_network(
    self,
    threshold: float = 0.5,
    layout: str = "force_directed"
) -> go.Figure
```

Visualize network of highly entangled connections.

**Parameters:**

- `threshold` (float): Minimum entanglement strength to show
- `layout` (str): Network layout algorithm

**Returns:**

- `go.Figure`: Entanglement network visualization

**Example:**

```python
# Show only strong entanglements
fig_network = visualizer.visualize_entanglement_network(
    threshold=0.7,
    layout="force_directed"
)
fig_network.show()
```

#### `visualize_community_structure`

```python
def visualize_community_structure(
    self,
    communities: Dict[str, int],
    method: str = "sankey"
) -> go.Figure
```

Visualize community structure in the quantum graph.

**Parameters:**

- `communities` (Dict[str, int]): Community assignments for nodes
- `method` (str): Visualization method ("sankey", "chord", "hierarchical")

**Returns:**

- `go.Figure`: Community structure visualization

### Statistical Visualizations

#### `plot_degree_distribution`

```python
def plot_degree_distribution(
    self,
    degree_type: str = "quantum"
) -> go.Figure
```

Plot degree distribution of the graph.

**Parameters:**

- `degree_type` (str): Type of degree ("quantum", "classical", "weighted")

**Returns:**

- `go.Figure`: Degree distribution plot

#### `plot_entanglement_distribution`

```python
def plot_entanglement_distribution(self) -> go.Figure
```

Plot distribution of entanglement strengths.

**Returns:**

- `go.Figure`: Entanglement distribution histogram

#### `plot_quantum_coherence_over_time`

```python
def plot_quantum_coherence_over_time(
    self,
    evolution_data: List[Dict[str, Any]]
) -> go.Figure
```

Plot evolution of quantum coherence over time.

**Parameters:**

- `evolution_data` (List[Dict]): Time evolution data

**Returns:**

- `go.Figure`: Coherence evolution plot

---

## VisualizationConfig

### Class Definition

```python
@dataclass
class VisualizationConfig:
    """Configuration for graph visualization."""
    width: int = 1000                    # Figure width in pixels
    height: int = 800                    # Figure height in pixels  
    node_size_factor: float = 20.0       # Node size scaling factor
    edge_width_factor: float = 5.0       # Edge width scaling factor
    color_scheme: str = "viridis"        # Color scheme name
    show_labels: bool = True             # Whether to show node labels
    show_quantum_info: bool = True       # Whether to show quantum information
    animation_duration: int = 500        # Animation frame duration (ms)
```

**Example:**

```python
# Custom visualization configuration
custom_config = VisualizationConfig(
    width=1400,
    height=1000,
    node_size_factor=30.0,
    edge_width_factor=8.0,
    color_scheme="plasma",
    show_labels=True,
    show_quantum_info=True,
    animation_duration=750
)

visualizer = QuantumGraphVisualizer(graph, custom_config)
```

## Color Schemes and Styling

### Available Color Schemes

```python
# Built-in color schemes
color_schemes = {
    "viridis": "Green-blue gradient",
    "plasma": "Purple-pink-yellow gradient", 
    "inferno": "Black-red-yellow gradient",
    "quantum": "Custom quantum-inspired colors",
    "entanglement": "Blue-red entanglement colors",
    "coherence": "Coherence-based coloring"
}

# Use specific color scheme
fig = visualizer.visualize_graph_2d(color_by="entanglement")
```

### Custom Styling

```python
def apply_custom_styling(fig, style_dict):
    """Apply custom styling to visualization."""
    
    fig.update_layout(
        title=style_dict.get("title", "Quantum Graph"),
        title_font_size=style_dict.get("title_size", 20),
        paper_bgcolor=style_dict.get("bg_color", "white"),
        plot_bgcolor=style_dict.get("plot_bg", "white"),
        font=dict(
            family=style_dict.get("font_family", "Arial"),
            size=style_dict.get("font_size", 12),
            color=style_dict.get("font_color", "black")
        )
    )
    
    return fig

# Apply custom styling
custom_style = {
    "title": "Quantum Drug Discovery Network",
    "title_size": 24,
    "bg_color": "#f8f9fa",
    "font_family": "Source Sans Pro",
    "font_size": 14
}

fig = visualizer.visualize_graph_2d()
fig = apply_custom_styling(fig, custom_style)
```

## Export and Sharing

### Export Methods

```python
# Export as HTML (interactive)
fig.write_html("quantum_graph.html")

# Export as static image
fig.write_image("quantum_graph.png", width=1200, height=800)
fig.write_image("quantum_graph.pdf")
fig.write_image("quantum_graph.svg")

# Export data for other tools
plot_data = fig.to_dict()
with open("plot_data.json", "w") as f:
    json.dump(plot_data, f)
```

### Integration with Jupyter

```python
# Jupyter notebook integration
import plotly.offline as pyo
pyo.init_notebook_mode(connected=True)

# Display inline
fig.show()

# Create widget
from plotly.widgets import FigureWidget
widget = FigureWidget(fig)
widget
```

## Advanced Visualization Examples

### Multi-Panel Dashboard

```python
def create_quantum_dashboard(graph):
    """Create comprehensive quantum graph dashboard."""
    
    visualizer = QuantumGraphVisualizer(graph)
    
    # Create subplots
    from plotly.subplots import make_subplots
    
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=("Graph Network", "Entanglement Heatmap", 
                       "Quantum States", "Degree Distribution"),
        specs=[[{"type": "scatter"}, {"type": "heatmap"}],
               [{"type": "scatter"}, {"type": "histogram"}]]
    )
    
    # Add 2D graph
    graph_2d = visualizer.visualize_graph_2d()
    for trace in graph_2d.data:
        fig.add_trace(trace, row=1, col=1)
    
    # Add entanglement heatmap
    heatmap = visualizer.visualize_entanglement_heatmap()
    for trace in heatmap.data:
        fig.add_trace(trace, row=1, col=2)
    
    # Add quantum state projection
    states_2d = visualizer.visualize_quantum_states_2d()
    for trace in states_2d.data:
        fig.add_trace(trace, row=2, col=1)
    
    # Add degree distribution
    degree_dist = visualizer.plot_degree_distribution()
    for trace in degree_dist.data:
        fig.add_trace(trace, row=2, col=2)
    
    fig.update_layout(height=800, title_text="Quantum Graph Dashboard")
    return fig

# Create dashboard
dashboard = create_quantum_dashboard(graph)
dashboard.show()
```

### Real-time Visualization

```python
import asyncio
import time

async def real_time_quantum_evolution():
    """Real-time visualization of quantum graph evolution."""
    
    visualizer = QuantumGraphVisualizer(graph)
    
    # Create initial plot
    fig = visualizer.visualize_graph_2d()
    
    # Setup for real-time updates
    import plotly.graph_objects as go
    
    for step in range(50):
        # Simulate quantum evolution
        evolve_quantum_graph(graph, evolution_rate=0.1)
        
        # Update visualization
        updated_fig = visualizer.visualize_graph_2d()
        
        # In a real application, you'd update the existing figure
        # Here we show the concept
        await asyncio.sleep(0.1)  # 100ms update rate
    
    return fig

# Run real-time visualization
# asyncio.run(real_time_quantum_evolution())
```

### Interactive Query Visualization

```python
def interactive_query_explorer(graph):
    """Interactive tool for exploring query results."""
    
    from ipywidgets import interact, widgets
    import ipywidgets as widgets
    
    visualizer = QuantumGraphVisualizer(graph)
    query_engine = EntangledQueryEngine(graph)
    
    # Create interactive widgets
    query_input = widgets.Text(
        value="What treats inflammation?",
        placeholder="Enter your query",
        description="Query:"
    )
    
    max_results_slider = widgets.IntSlider(
        value=5,
        min=1,
        max=20,
        description="Max Results:"
    )
    
    highlight_button = widgets.Button(
        description="Highlight Results",
        button_style="info"
    )
    
    output = widgets.Output()
    
    def on_query_change(change):
        with output:
            output.clear_output()
            
            # Process query
            results = query_engine.query(
                change['new'], 
                max_results=max_results_slider.value
            )
            
            # Extract result nodes
            result_nodes = []
            for result in results:
                result_nodes.extend(result.answer_nodes)
            
            # Create visualization with highlighted results
            fig = visualizer.visualize_graph_2d(
                highlight_nodes=result_nodes,
                color_by="entanglement"
            )
            fig.show()
            
            # Display results
            print(f"Found {len(results)} results:")
            for i, result in enumerate(results[:3]):
                print(f"{i+1}. {', '.join(result.answer_nodes)} "
                      f"(confidence: {result.confidence_score:.3f})")
    
    query_input.observe(on_query_change, names='value')
    
    # Display interface
    return widgets.VBox([query_input, max_results_slider, output])

# Create interactive explorer
# explorer = interactive_query_explorer(graph)
# explorer
```

## Performance Optimization

### Large Graph Visualization

```python
def optimize_for_large_graphs(visualizer, max_nodes=1000, max_edges=2000):
    """Optimize visualization for large graphs."""
    
    graph = visualizer.graph
    
    if len(graph.nodes) > max_nodes:
        # Sample nodes based on centrality
        from qekgr import QuantumInference
        inference = QuantumInference(graph)
        centrality = inference.measure_quantum_centrality()
        
        # Keep top central nodes
        top_nodes = sorted(centrality.items(), key=lambda x: x[1], reverse=True)
        selected_nodes = [node for node, _ in top_nodes[:max_nodes]]
        
        # Create subgraph
        subgraph = create_subgraph(graph, selected_nodes)
        visualizer.graph = subgraph
    
    if len(graph.edges) > max_edges:
        # Filter edges by entanglement strength
        edges_by_strength = sorted(
            graph.edges.items(),
            key=lambda x: x[1].entanglement_strength,
            reverse=True
        )
        
        # Keep strongest edges
        strong_edges = dict(edges_by_strength[:max_edges])
        visualizer.graph.edges = strong_edges
    
    return visualizer
```

The visualization module makes quantum knowledge graphs accessible and interpretable through beautiful, interactive visualizations that reveal the hidden quantum structure of knowledge! 🎨⚛️
