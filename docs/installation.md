# Installation Guide

Welcome to the Quantum Entangled Knowledge Graphs (QE-KGR) installation guide. This page provides comprehensive instructions for installing QE-KGR on various platforms and environments.

## 📋 System Requirements

### Minimum Requirements

- **Python**: 3.8 or higher
- **Memory**: 4GB RAM (8GB+ recommended for large graphs)
- **Storage**: 500MB free space
- **OS**: Windows 10+, macOS 10.14+, or Linux (Ubuntu 18.04+)

### Recommended Requirements

- **Python**: 3.9 or 3.10
- **Memory**: 16GB RAM
- **Storage**: 2GB free space
- **GPU**: CUDA-compatible GPU (optional, for acceleration)

## 🚀 Quick Installation

### Install from PyPI (Recommended)

```bash
pip install quantum-entangled-knowledge-graphs
```

### Verify Installation

```python
import qekgr
print(f"QE-KGR version: {qekgr.__version__}")

# Create a simple test graph
graph = qekgr.EntangledGraph()
print("✅ QE-KGR installed successfully!")
```

## 🛠️ Advanced Installation Options

### Install with All Dependencies

For full functionality including visualization and advanced features:

```bash
pip install quantum-entangled-knowledge-graphs[full]
```

### Install Development Version

To get the latest features from GitHub:

```bash
pip install git+https://github.com/krish567366/quantum-entangled-knowledge-graphs.git
```

### Install in Development Mode

For contributors and developers:

```bash
git clone https://github.com/krish567366/quantum-entangled-knowledge-graphs.git
cd quantum-entangled-knowledge-graphs
pip install -e .
```

## 📦 Optional Dependencies

QE-KGR supports various optional dependencies for enhanced functionality:

### Visualization Dependencies

```bash
pip install plotly>=5.0.0
pip install matplotlib>=3.5.0
pip install seaborn>=0.11.0
pip install networkx>=2.8.0
```

### Machine Learning Dependencies

```bash
pip install scikit-learn>=1.0.0
pip install scipy>=1.7.0
```

### Quantum Computing Dependencies

```bash
pip install qiskit>=0.39.0
pip install pennylane>=0.28.0
```

### Performance Dependencies

```bash
pip install numba>=0.56.0
pip install jax>=0.3.0
```

## 🐳 Docker Installation

### Pull Pre-built Image

```bash
docker pull krishbajpai/qekgr:latest
```

### Run Interactive Container

```bash
docker run -it --rm -p 8888:8888 krishbajpai/qekgr:latest
```

### Build from Source

```bash
git clone https://github.com/krish567366/quantum-entangled-knowledge-graphs.git
cd quantum-entangled-knowledge-graphs
docker build -t qekgr:local .
```

## 🐍 Conda Installation

### Create Conda Environment

```bash
conda create -n qekgr python=3.9
conda activate qekgr
pip install quantum-entangled-knowledge-graphs
```

### Install from Conda-Forge (Coming Soon)

```bash
conda install -c conda-forge quantum-entangled-knowledge-graphs
```

## 🖥️ Platform-Specific Instructions

### Windows

1. **Install Python** from [python.org](https://python.org) or Microsoft Store
2. **Open Command Prompt** as Administrator
3. **Install QE-KGR**:

   ```cmd
   pip install quantum-entangled-knowledge-graphs
   ```

### macOS

1. **Install Homebrew** (if not already installed):

   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. **Install Python**:

   ```bash
   brew install python@3.9
   ```

3. **Install QE-KGR**:

   ```bash
   pip3 install quantum-entangled-knowledge-graphs
   ```

### Linux (Ubuntu/Debian)

1. **Update system packages**:

   ```bash
   sudo apt update && sudo apt upgrade -y
   ```

2. **Install Python and pip**:

   ```bash
   sudo apt install python3.9 python3-pip -y
   ```

3. **Install QE-KGR**:

   ```bash
   pip3 install quantum-entangled-knowledge-graphs
   ```

### Linux (CentOS/RHEL)

1. **Install Python**:

   ```bash
   sudo dnf install python3.9 python3-pip -y
   ```

2. **Install QE-KGR**:

   ```bash
   pip3 install quantum-entangled-knowledge-graphs
   ```

## 🔧 Virtual Environment Setup

### Using venv (Recommended)

```bash
python -m venv qekgr-env
source qekgr-env/bin/activate  # On Windows: qekgr-env\Scripts\activate
pip install quantum-entangled-knowledge-graphs
```

### Using virtualenv

```bash
pip install virtualenv
virtualenv qekgr-env
source qekgr-env/bin/activate  # On Windows: qekgr-env\Scripts\activate
pip install quantum-entangled-knowledge-graphs
```

### Using pipenv

```bash
pip install pipenv
pipenv install quantum-entangled-knowledge-graphs
pipenv shell
```

## 🧪 Testing Your Installation

### Basic Functionality Test

```python
#!/usr/bin/env python3
"""Test script for QE-KGR installation."""

import qekgr
import numpy as np

def test_installation():
    print("🧪 Testing QE-KGR Installation...")
    print(f"   Version: {qekgr.__version__}")
    
    # Test 1: Create graph
    print("   ✅ Creating EntangledGraph...")
    graph = qekgr.EntangledGraph(hilbert_dim=4)
    
    # Test 2: Add nodes
    print("   ✅ Adding quantum nodes...")
    alice = graph.add_quantum_node("Alice", state="physicist")
    bob = graph.add_quantum_node("Bob", state="engineer")
    
    # Test 3: Add entangled edge
    print("   ✅ Creating entangled edges...")
    graph.add_entangled_edge(alice, bob, 
                           relations=["collaborates"], 
                           amplitudes=[0.8])
    
    # Test 4: Quantum inference
    print("   ✅ Testing quantum inference...")
    inference = qekgr.QuantumInference(graph)
    walk_result = inference.quantum_walk("Alice", steps=5)
    
    # Test 5: Query engine
    print("   ✅ Testing query engine...")
    query_engine = qekgr.EntangledQueryEngine(graph)
    results = query_engine.query("Who collaborates with Alice?")
    
    print("🎉 All tests passed! QE-KGR is working correctly.")
    return True

if __name__ == "__main__":
    test_installation()
```

### Performance Benchmark

```python
import time
import qekgr

def benchmark_installation():
    """Benchmark QE-KGR performance."""
    print("⚡ Benchmarking QE-KGR Performance...")
    
    start_time = time.time()
    
    # Create larger graph
    graph = qekgr.EntangledGraph(hilbert_dim=8)
    
    # Add 100 nodes
    for i in range(100):
        graph.add_quantum_node(f"node_{i}", state=f"state_{i%10}")
    
    # Add 200 edges
    for i in range(200):
        source = f"node_{i%100}"
        target = f"node_{(i+1)%100}"
        graph.add_entangled_edge(source, target,
                               relations=["connects"],
                               amplitudes=[0.7])
    
    # Run inference
    inference = qekgr.QuantumInference(graph)
    walk_result = inference.quantum_walk("node_0", steps=20)
    
    end_time = time.time()
    duration = end_time - start_time
    
    print(f"   Benchmark completed in {duration:.2f} seconds")
    print(f"   Graph size: {len(graph.nodes)} nodes, {len(graph.edges)} edges")
    
    if duration < 10:
        print("   🚀 Excellent performance!")
    elif duration < 30:
        print("   ✅ Good performance!")
    else:
        print("   ⚠️  Consider upgrading hardware for better performance")

if __name__ == "__main__":
    benchmark_installation()
```

## 🚨 Troubleshooting

### Common Installation Issues

#### Issue: "No module named 'qekgr'"

**Solution**: Ensure you're using the correct Python environment:

```bash
which python
pip list | grep quantum
```

#### Issue: Import errors with dependencies

**Solution**: Install with full dependencies:

```bash
pip install quantum-entangled-knowledge-graphs[full]
```

#### Issue: "Microsoft Visual C++ 14.0 is required" (Windows)

**Solution**: Install Visual Studio Build Tools:

1. Download from [Microsoft Visual Studio](https://visualstudio.microsoft.com/downloads/)
2. Install "C++ build tools"
3. Retry installation

#### Issue: Permission denied (Linux/macOS)

**Solution**: Use virtual environment or install with --user:

```bash
pip install --user quantum-entangled-knowledge-graphs
```

#### Issue: Slow performance

**Solutions**:

1. Install with performance dependencies:

   ```bash
   pip install numba jax
   ```

2. Use smaller Hilbert dimensions for testing
3. Consider GPU acceleration if available

### Getting Help

If you encounter issues not covered here:

1. **Check GitHub Issues**: [GitHub Issues](https://github.com/krish567366/quantum-entangled-knowledge-graphs/issues)
2. **Create New Issue**: Provide system info, error messages, and minimal reproduction case
3. **Email Support**: bajpaikrishna715@gmail.com
4. **Discord Community**: [Join our Discord](https://discord.gg/qekgr) (coming soon)

### System Information Script

Use this script to gather system information for bug reports:

```python
import sys
import platform
import pkg_resources

def system_info():
    """Gather system information for debugging."""
    print("🖥️  System Information")
    print("=" * 30)
    print(f"Python Version: {sys.version}")
    print(f"Platform: {platform.platform()}")
    print(f"Architecture: {platform.architecture()}")
    print(f"Processor: {platform.processor()}")
    
    print("\n📦 Installed Packages")
    print("=" * 20)
    installed = [d.project_name for d in pkg_resources.working_set]
    qe_related = [pkg for pkg in installed if 'quantum' in pkg.lower() or 'qekgr' in pkg.lower()]
    
    for pkg in qe_related:
        try:
            version = pkg_resources.get_distribution(pkg).version
            print(f"{pkg}: {version}")
        except:
            print(f"{pkg}: unknown version")

if __name__ == "__main__":
    system_info()
```

## 🔄 Upgrading QE-KGR

### Check Current Version

```python
import qekgr
print(qekgr.__version__)
```

### Upgrade to Latest Version

```bash
pip install --upgrade quantum-entangled-knowledge-graphs
```

### Upgrade to Specific Version

```bash
pip install quantum-entangled-knowledge-graphs==0.2.0
```

### Uninstall QE-KGR

```bash
pip uninstall quantum-entangled-knowledge-graphs
```

---

## ✅ Next Steps

After successful installation:

1. 📖 **Read the [Quick Start Guide](quickstart.md)**
2. 🧪 **Try the [Examples](examples.md)**
3. 📚 **Explore [API Reference](modules.md)**
4. 🎓 **Follow [Tutorials](tutorials/basic_usage.md)**

Congratulations! You now have QE-KGR installed and ready to explore quantum-enhanced knowledge graphs! 🎉
