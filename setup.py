from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="esm2-epistasis-pipeline",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A computational pipeline for epistatic interaction prediction using ESM2",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/YOUR_USERNAME/esm2-epistasis-pipeline",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "black>=22.0.0",
            "flake8>=4.0.0",
            "pre-commit>=2.15.0",
            "pytest>=6.0.0",
        ],
        "notebook": [
            "jupyter>=1.0.0",
            "ipykernel>=6.0.0",
            "ipywidgets>=7.6.0",
        ],
    },
    entry_points={
        "console_scripts": [
            # Future CLI commands can be added here
            # "esm2-epistasis=esm2_epistasis.cli:main",
        ],
    },
    keywords=[
        "protein",
        "epistasis",
        "ESM2",
        "language model",
        "bioinformatics",
        "computational biology",
        "machine learning",
        "transformers",
        "pytorch",
    ],
    project_urls={
        "Bug Reports": "https://github.com/YOUR_USERNAME/esm2-epistasis-pipeline/issues",
        "Source": "https://github.com/YOUR_USERNAME/esm2-epistasis-pipeline",
        "Documentation": "https://github.com/YOUR_USERNAME/esm2-epistasis-pipeline#readme",
    },
)
