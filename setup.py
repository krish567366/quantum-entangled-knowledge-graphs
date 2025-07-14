"""
Setup configuration for quantum-entangled-knowledge-graphs package.
"""

from setuptools import setup, find_packages
import os

# Read README for long description
def read_readme():
    readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            return f.read()
    return ""

# Read requirements
def read_requirements():
    req_path = os.path.join(os.path.dirname(__file__), 'requirements.txt')
    if os.path.exists(req_path):
        with open(req_path, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip() and not line.startswith('#')]
    return []

setup(
    name="quantum-entangled-knowledge-graphs",
    version="0.1.0",
    author="Krishna Bajpai",
    author_email="bajpaikrishna715@gmail.com",
    description="World's first open-source library for quantum-enhanced knowledge graph reasoning using entanglement principles",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/krish567366/quantum-entangled-knowledge-graphs",
    project_urls={
        "Bug Tracker": "https://github.com/krish567366/quantum-entangled-knowledge-graphs/issues",
        "Documentation": "https://krish567366.github.io/quantum-entangled-knowledge-graphs/",
        "Source Code": "https://github.com/krish567366/quantum-entangled-knowledge-graphs",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    install_requires=read_requirements() or [
        "numpy>=1.21.0",
        "scipy>=1.7.0",
        "networkx>=2.6.0",
        "matplotlib>=3.4.0",
        "plotly>=5.0.0",
        "pandas>=1.3.0",
        "scikit-learn>=1.0.0",
        "seaborn>=0.11.0",
    ],
    extras_require={
        "quantum": [
            "pennylane>=0.28.0",
            "qiskit>=0.39.0",
        ],
        "visualization": [
            "pyvis>=0.3.0",
            "graphviz>=0.20.0",
        ],
        "dev": [
            "pytest>=6.0.0",
            "pytest-cov>=3.0.0",
            "black>=22.0.0",
            "flake8>=4.0.0",
            "mypy>=0.950",
            "mkdocs>=1.4.0",
            "mkdocs-material>=8.0.0",
            "mkdocstrings[python]>=0.19.0",
        ],
        "examples": [
            "jupyter>=1.0.0",
            "streamlit>=1.15.0",
            "gradio>=3.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "qekgr=qekgr.cli:main",
        ],
    },
    keywords=[
        "quantum computing",
        "knowledge graphs", 
        "quantum entanglement",
        "graph neural networks",
        "quantum machine learning",
        "semantic reasoning",
        "artificial intelligence",
    ],
    include_package_data=True,
    zip_safe=False,
)
