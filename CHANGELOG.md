# Changelog

All notable changes to the ESM2 Epistasis Pipeline will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2024-12-09

### Added
- Initial release of ESM2 Epistasis Pipeline
- Three-layer computational pipeline for epistatic interaction prediction
- Support for both demo (residues 150-220) and full sequence modes
- ESM2 contact prediction with automatic fallback to manual attention+APC
- Bidirectional embedding perturbation analysis (i→j and j→i)
- Masked marginal epistasis computation with statistical validation
- Random baseline comparison with Mann-Whitney U test
- Comprehensive visualization suite (contact maps, perturbation plots, integrated analysis)
- Complete Jupyter notebook with detailed documentation
- Automated CSV export for all results and summary statistics
- pH1N1 A/California/04/2009 HA sequence integration
- Position numbering conversion (Python 0-indexed ↔ HA 1-indexed)
- GPU memory management and error handling
- Support for both T4 (Colab) and larger GPU environments

### Technical Features
- ESM2 model support: `esm2_t6_8M_UR50D` (demo), `esm2_t12_35M_UR50D` (full)
- Reproducible results with fixed random seeds
- Robust error handling with fallback mechanisms
- Efficient computation with periodic GPU memory cleanup
- Standard amino acid filtering (20 canonical residues only)
- Sequence separation filtering to focus on long-range interactions

### Documentation
- Comprehensive README with quick start guide
- Detailed scientific background and method descriptions
- Technical requirements and hardware recommendations
- Example results and interpretation guide
- Citations and references to key literature
- Contributing guidelines and development setup

### Files Structure
```
esm2_epistasis_pipeline.ipynb    # Main analysis notebook
README.md                        # Documentation and usage guide
requirements.txt                 # Python dependencies
LICENSE                         # MIT license
CHANGELOG.md                    # Version history
.gitignore                      # Git ignore patterns
```

### Performance Benchmarks
- Demo mode: ~10-15 minutes on T4 GPU (71 residues, 50 pairs)
- Full mode: ~60-90 minutes on T4 GPU (566 residues, 500 pairs)
- Memory usage: 4-6 GB (demo), 8-12 GB (full)
- Forward passes: ~2,000 (demo), ~20,000 (full)

## [Planned - 1.1.0]

### Planned Additions
- [ ] Command-line interface (CLI) for non-interactive use
- [ ] Custom sequence input support (beyond pH1N1 HA)
- [ ] Batch processing for multiple proteins
- [ ] Integration with structural data (PDB files)
- [ ] Performance optimizations for larger sequences
- [ ] Docker containerization
- [ ] Conda package distribution

### Planned Improvements
- [ ] More sophisticated contact prediction methods
- [ ] Higher-order epistasis analysis (triplets, quadruplets)
- [ ] Real-time progress visualization
- [ ] Memory optimization for very long sequences
- [ ] Support for additional ESM model variants
- [ ] Enhanced statistical testing options

## [Future Releases]

### Research Extensions
- [ ] Multi-protein complex analysis
- [ ] Integration with deep mutational scanning data
- [ ] Phylogenetic epistasis analysis
- [ ] Machine learning predictive models
- [ ] Web interface for broader accessibility
- [ ] API for programmatic access

---

**Note**: This project is actively maintained. Please report issues or feature requests through GitHub Issues.
