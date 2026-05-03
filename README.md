# ESM2 Epistasis Pipeline

A three-layer computational pipeline for identifying epistatic interactions in protein sequences using Facebook's ESM2 protein language model.

![Python](https://img.shields.io/badge/python-v3.10+-blue.svg)
![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=flat&logo=PyTorch&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 🧬 Overview

This pipeline identifies epistatic interactions (non-additive mutation effects) in proteins using ESM2's attention patterns and masked language modeling capabilities. Specifically designed for influenza A hemagglutinin (HA) analysis, but adaptable to any protein sequence.

### Pipeline Architecture

```
Layer 1: Attention Contact Map → Layer 2: Embedding Perturbation → Layer 3: Masked Marginal Epistasis
     ↓                              ↓                                ↓
Co-dependent pairs              Bidirectional mutation           Statistical epistasis
(ESM2 contacts)                 impact analysis                  scores with validation
```

## 🚀 Quick Start

### Google Colab (Recommended)

1. **Open in Colab**: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR_USERNAME/esm2-epistasis-pipeline/blob/main/esm2_epistasis_pipeline.ipynb)

2. **Runtime Setup**: 
   - Runtime → Change runtime type → Hardware accelerator: **GPU (T4)**
   - Runtime → Run all (⏱️ ~10-15 minutes for demo mode)

3. **Results**: Automatically downloads CSV files and PNG visualizations

### Local Installation

```bash
git clone https://github.com/YOUR_USERNAME/esm2-epistasis-pipeline.git
cd esm2-epistasis-pipeline
pip install -r requirements.txt
jupyter notebook esm2_epistasis_pipeline.ipynb
```

## 📊 Example Results

### Demo Mode: pH1N1 HA residues 150-220

| Mutation Pair | Epistasis Score | Type | Contact Score |
|---------------|-----------------|------|---------------|
| `S156L × T200A` | -0.0234 | Synergistic | 0.1456 |
| `N158D × S195P` | +0.0189 | Antagonistic | 0.1289 |
| `K160R × N193S` | -0.0167 | Synergistic | 0.1134 |

**Statistical Validation**: Top pairs show 2.3x stronger median |epistasis| than random (Mann-Whitney p = 1.2e-5)

## 📋 Configuration

### Sequence Modes

```python
# Demo mode (fast): HA residues 150-220, covers antigenic regions
USE_FULL_SEQUENCE = False
MODEL_NAME = 'facebook/esm2_t6_8M_UR50D'    # ~5-10 min
TOP_K = 50

# Full mode (comprehensive): Complete 566-residue sequence  
USE_FULL_SEQUENCE = True
MODEL_NAME = 'facebook/esm2_t12_35M_UR50D'  # ~60-90 min
TOP_K = 500
```

### Key Parameters

| Parameter | Demo | Full | Description |
|-----------|------|------|-------------|
| `MIN_SEQ_SEP` | 12 | 12 | Minimum sequence separation for contacts |
| `TOP_MUTATIONS_PER_PAIR` | 3 | 3 | Candidates per perturbation direction |
| `N_RANDOM_BASELINE` | 50 | 50 | Random pairs for statistical validation |

## 🔬 Scientific Background

### Layer 1: ESM2 Contact Prediction
- Uses ESM2's trained logistic regression head for contact probability
- Fallback to manual attention averaging with APC correction
- Filters for long-range contacts (|i-j| ≥ 12)

### Layer 2: Embedding Perturbation Analysis  
- **Bidirectional**: Tests both i→j and j→i mutation effects
- **Metric**: Cosine distance between wild-type and mutant embeddings
- **Output**: Top-K mutation candidates per contact pair

### Layer 3: Masked Marginal Epistasis
- **Formula**: `Epistasis = S(A+B) - S(A) - S(B)`
- **S(X)**: `log P(mut|masked) - log P(wt|masked)`
- **Interpretation**: Negative = synergistic, Positive = antagonistic

> ⚠️ **Important**: Uses masked marginal approximation, not exact joint likelihood (standard in ESM epistasis studies)

## 📁 Output Files

| File | Description |
|------|-------------|
| `esm2_epistasis_results_*.csv` | Complete results (top + random pairs) |
| `esm2_top_epistatic_pairs_*.csv` | Top epistatic interactions only |
| `esm2_epistasis_summary_*.csv` | Statistical summary & validation |
| `epistasis_comprehensive_results.png` | 3-panel analysis figure |
| `layer1_contact_map.png` | ESM2 contact probability heatmap |
| `layer2_perturbation.png` | Bidirectional embedding perturbation |

## 📈 Validation & Interpretation

### Statistical Validation
- **Mann-Whitney U test**: Compares |epistasis| distributions (top vs random pairs)
- **Correlation analysis**: Layer 1 contact probability ↔ Layer 3 epistasis magnitude
- **Fold enrichment**: Quantifies improvement over random baseline

### Biological Relevance (Influenza HA)
- **Antigenic sites**: Sa, Sb, Ca1, Ca2, Cb (immune escape)
- **Receptor binding site**: Host adaptation mutations
- **Fusion domain**: Membrane fusion efficiency

### Position Numbering
- **Python indices**: 0-based, matches sequence slicing
- **HA numbering**: 1-based mature protein (signal peptide removed)
- **UniProt coordinates**: Includes 17-residue signal peptide

## 🛠️ Technical Requirements

### Compute Resources
| Mode | GPU Memory | Runtime | Forward Passes |
|------|------------|---------|----------------|
| Demo | 4-6 GB | 10-15 min | ~2,000 |
| Full | 8-12 GB | 60-90 min | ~20,000 |

### Dependencies
```
torch >= 2.0
transformers >= 4.30  
numpy, pandas, matplotlib, seaborn, tqdm, scipy
```

### Hardware Compatibility
- **GPU**: Recommended (CUDA-compatible)
- **CPU**: Supported but 10x slower
- **Colab**: T4 GPU sufficient for both modes

## 📚 Citation & References

If you use this pipeline in your research, please cite:

```bibtex
@software{esm2_epistasis_pipeline,
  title={ESM2 Epistasis Pipeline: Computational Epistasis Prediction using Protein Language Models},
  author={[Your Name]},
  year={2024},
  url={https://github.com/YOUR_USERNAME/esm2-epistasis-pipeline}
}
```

### Key References
- **ESM2**: [Lin et al. "Language models of protein sequences at the scale of evolution" (2023)](https://doi.org/10.1126/science.ade2574)
- **Masked Marginal Epistasis**: [Meier et al. "Language models enable zero-shot prediction of mutation effects" (2021)](https://doi.org/10.1101/2021.07.09.450648)
- **Contact Prediction**: [Rao et al. "MSA Transformer" (2021)](https://doi.org/10.1101/2021.02.12.430858)

## 🤝 Contributing

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** changes (`git commit -m 'Add amazing feature'`)
4. **Push** to branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Development Setup
```bash
git clone https://github.com/YOUR_USERNAME/esm2-epistasis-pipeline.git
cd esm2-epistasis-pipeline
pip install -e .
pre-commit install  # Optional: code formatting
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🚨 Limitations & Caveats

### Model Limitations
- ESM2 trained on evolutionary data, not functional assays
- May not correlate with experimental fitness effects
- Biased toward evolutionarily conserved interactions

### Method Limitations  
- Masked marginal approximation (not true joint probability)
- No structural constraints incorporated
- Limited to single amino acid mutations

### Computational Limitations
- Memory requirements scale quadratically with sequence length
- GPU recommended for reasonable runtime
- Full mode requires significant computational resources

## 💡 Future Directions

- [ ] **Multi-protein complexes**: Extend to protein-protein interfaces
- [ ] **Deep mutational scanning**: Integration with experimental data
- [ ] **Structural constraints**: Incorporate 3D structure information
- [ ] **Higher-order epistasis**: Beyond pairwise interactions
- [ ] **Real-time analysis**: Optimize for faster inference


**⭐ Star this repo if it helped your research!**

Made with ❤️ for the computational biology community
