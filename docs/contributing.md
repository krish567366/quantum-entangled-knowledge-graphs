# Contributing to QE-KGR

Welcome to the Quantum Entangled Knowledge Graphs (QE-KGR) project! We're excited that you're interested in contributing to the world's first open-source quantum-enhanced knowledge graph library. This guide will help you get started with contributing to our project.

## 🎯 Vision & Mission

QE-KGR aims to revolutionize knowledge representation and reasoning by applying quantum mechanics principles to graph structures. Our mission is to create a robust, scalable, and scientifically grounded library that enables breakthrough applications in AI, data science, and complex systems analysis.

## 🚀 Getting Started

### Prerequisites

Before contributing, ensure you have:

- **Python 3.8+** installed
- **Git** for version control
- **Basic understanding** of quantum mechanics concepts
- **Knowledge graph** experience (helpful but not required)
- **Open source** contribution experience (helpful but not required)

### Development Environment Setup

1. **Fork and Clone**
   ```bash
   git clone https://github.com/yourusername/quantum-entangled-knowledge-graphs.git
   cd quantum-entangled-knowledge-graphs
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv qekgr_env
   source qekgr_env/bin/activate  # On Windows: qekgr_env\Scripts\activate
   ```

3. **Install Development Dependencies**
   ```bash
   pip install -e ".[dev]"
   # Or if the above doesn't work:
   pip install -r requirements.txt
   pip install -e .
   ```

4. **Install Additional Development Tools**
   ```bash
   pip install pytest pytest-cov black flake8 mypy
   pip install pre-commit
   pre-commit install
   ```

5. **Verify Installation**
   ```bash
   python -c "import qekgr; print('QE-KGR installed successfully!')"
   pytest tests/ -v
   ```

## 📋 Contribution Types

We welcome various types of contributions:

### 🐛 Bug Reports
- Found a bug? Create an issue with detailed reproduction steps
- Include Python version, QE-KGR version, and error messages
- Provide minimal code example that demonstrates the issue

### 💡 Feature Requests
- Suggest new quantum algorithms or graph operations
- Propose new visualization capabilities
- Request additional quantum mechanics implementations

### 📝 Documentation
- Improve existing documentation
- Add new examples and tutorials
- Translate documentation to other languages
- Fix typos and clarify explanations

### 🔧 Code Contributions
- Implement new quantum algorithms
- Add visualization features
- Optimize performance
- Improve test coverage
- Fix bugs and issues

### 📊 Examples & Use Cases
- Create new application examples
- Develop domain-specific implementations
- Build educational tutorials
- Showcase real-world applications

## 🔄 Development Workflow

### 1. Issue Creation/Assignment
- Check existing issues before creating new ones
- Use issue templates when available
- Assign yourself to issues you want to work on
- Discuss approach in issue comments before starting large changes

### 2. Branch Management
```bash
# Create feature branch
git checkout -b feature/quantum-walk-optimization
# Or for bug fixes:
git checkout -b fix/entanglement-calculation-bug
```

### 3. Development Process
- Write code following our coding standards (see below)
- Add appropriate tests for new functionality
- Update documentation as needed
- Ensure all tests pass locally

### 4. Testing Your Changes
```bash
# Run all tests
pytest tests/ -v

# Run specific test file
pytest tests/test_entangled_graph.py -v

# Run with coverage
pytest tests/ --cov=qekgr --cov-report=html

# Run performance tests
pytest tests/test_performance.py -v --benchmark-only
```

### 5. Code Quality Checks
```bash
# Format code
black qekgr/ tests/

# Check code style
flake8 qekgr/ tests/

# Type checking
mypy qekgr/

# Run pre-commit hooks
pre-commit run --all-files
```

### 6. Commit Guidelines
We follow conventional commit format:
```bash
git commit -m "feat: add quantum interference pattern calculation"
git commit -m "fix: resolve entanglement strength normalization"
git commit -m "docs: add advanced usage examples"
git commit -m "test: add comprehensive quantum walk tests"
```

Commit types:
- `feat`: New features
- `fix`: Bug fixes
- `docs`: Documentation changes
- `test`: Test additions or modifications
- `refactor`: Code refactoring
- `perf`: Performance improvements
- `style`: Code style changes
- `chore`: Maintenance tasks

### 7. Pull Request Process
1. **Push your branch** to your fork
2. **Create pull request** against `main` branch
3. **Fill out PR template** completely
4. **Ensure CI passes** (tests, linting, etc.)
5. **Request review** from maintainers
6. **Address feedback** promptly
7. **Squash commits** if requested

## 📏 Coding Standards

### Python Style Guide
We follow PEP 8 with some modifications:

```python
# Good: Clear, descriptive names
def calculate_quantum_state_overlap(state_a: np.ndarray, state_b: np.ndarray) -> complex:
    """Calculate overlap between two quantum states."""
    return np.vdot(state_a, state_b)

# Good: Type hints for all functions
class EntangledGraph:
    def __init__(self, hilbert_dim: int = 8) -> None:
        self.hilbert_dim = hilbert_dim
        self.nodes: Dict[str, QuantumNode] = {}

# Good: Comprehensive docstrings
def quantum_walk(
    self, 
    start_node: str, 
    steps: int,
    bias_relations: Optional[List[str]] = None
) -> QuantumWalkResult:
    """Perform quantum walk on the entangled graph.
    
    Args:
        start_node: Starting node for the walk
        steps: Number of quantum walk steps
        bias_relations: Relations to bias the walk towards
        
    Returns:
        QuantumWalkResult containing path and probabilities
        
    Raises:
        ValueError: If start_node not in graph
    """
```

### Quantum Computing Conventions
- Use complex numbers for quantum amplitudes
- Normalize quantum states appropriately
- Include uncertainty measures in results
- Document quantum mechanics assumptions clearly

### Documentation Standards
- Every public function/class needs docstring
- Include type hints for all parameters and returns
- Provide usage examples for complex functions
- Document quantum mechanics concepts used

## 🧪 Testing Guidelines

### Test Structure
```python
import pytest
import numpy as np
from qekgr import EntangledGraph, QuantumInference

class TestQuantumInference:
    """Test suite for quantum inference algorithms."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.graph = EntangledGraph(hilbert_dim=4)
        self.inference = QuantumInference(self.graph)
    
    def test_quantum_walk_basic(self):
        """Test basic quantum walk functionality."""
        # Setup
        self.graph.add_quantum_node("A", "state_a")
        self.graph.add_quantum_node("B", "state_b")
        self.graph.add_entangled_edge("A", "B", ["connects"], [0.8])
        
        # Execute
        result = self.inference.quantum_walk("A", steps=5)
        
        # Assert
        assert result.path[0] == "A"
        assert len(result.path) == 6  # steps + 1
        assert 0 <= result.final_probability <= 1
    
    def test_quantum_state_normalization(self):
        """Test quantum state normalization."""
        state = np.array([1+2j, 3-1j, 2+0j])
        normalized = self.inference._normalize_quantum_state(state)
        
        # State should be normalized
        assert np.isclose(np.linalg.norm(normalized), 1.0)
```

### Test Coverage Requirements
- **Minimum 80%** test coverage for new code
- **Unit tests** for all quantum algorithms
- **Integration tests** for complete workflows
- **Performance tests** for computationally intensive operations
- **Edge case tests** for boundary conditions

### Quantum Testing Considerations
- Test with various Hilbert space dimensions
- Verify quantum state normalization
- Check entanglement consistency
- Test numerical stability with complex numbers
- Validate quantum mechanics principles

## 📚 Documentation Contribution

### Documentation Types
1. **API Documentation**: Auto-generated from docstrings
2. **User Guides**: Step-by-step tutorials
3. **Theory Documentation**: Quantum mechanics explanations
4. **Examples**: Complete working examples
5. **Use Cases**: Real-world applications

### Documentation Standards
- Write in clear, accessible language
- Include mathematical formulations when necessary
- Provide runnable code examples
- Use consistent terminology
- Include visualizations where helpful

### Building Documentation Locally
```bash
# Install documentation dependencies
pip install mkdocs mkdocs-material

# Serve documentation locally
mkdocs serve

# Build documentation
mkdocs build
```

## 🤝 Community Guidelines

### Code of Conduct
- Be respectful and inclusive
- Welcome newcomers and help them learn
- Focus on constructive feedback
- Acknowledge contributions from others
- Maintain professional communication

### Communication Channels
- **GitHub Issues**: Bug reports, feature requests
- **GitHub Discussions**: General questions, ideas
- **Pull Request Reviews**: Code-specific discussions
- **Documentation**: Technical explanations

### Getting Help
- Check existing documentation first
- Search closed issues for similar problems
- Ask specific, well-formed questions
- Provide context and examples
- Be patient with responses

## 🏆 Recognition

We value all contributions and recognize contributors through:

- **Contributors list** in README and documentation
- **Release notes** acknowledging significant contributions
- **Issue/PR mentions** for helpful participation
- **Special recognition** for outstanding contributions

## 📈 Roadmap Participation

Help shape QE-KGR's future by participating in:

- **Feature planning** discussions
- **Architecture decisions** for major changes
- **Performance optimization** initiatives
- **New domain applications** exploration
- **Research collaboration** opportunities

## 🔬 Research Contributions

We especially welcome research-oriented contributions:

- **New quantum algorithms** for graph analysis
- **Theoretical improvements** to existing methods
- **Performance benchmarks** and comparisons
- **Scientific applications** and case studies
- **Publications** using QE-KGR

## 🚀 Quick Start Checklist

- [ ] Fork and clone repository
- [ ] Set up development environment
- [ ] Run tests to verify setup
- [ ] Read through existing code
- [ ] Choose an issue to work on
- [ ] Create feature branch
- [ ] Make your changes
- [ ] Add tests for new functionality
- [ ] Update documentation
- [ ] Run all quality checks
- [ ] Submit pull request

## 📞 Contact

Questions about contributing? Reach out through:

- **GitHub Issues**: For technical questions
- **GitHub Discussions**: For general inquiries
- **Email**: [maintainer@qekgr.org](mailto:maintainer@qekgr.org)

Thank you for contributing to QE-KGR! Together, we're building the future of quantum-enhanced knowledge graphs. 🚀⚛️
