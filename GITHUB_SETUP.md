# GitHub Setup Guide

This guide walks you through setting up your ESM2 Epistasis Pipeline repository on GitHub.

## 📋 Prerequisites

1. **GitHub account**: [Sign up here](https://github.com) if you don't have one
2. **Git installed**: Download from [git-scm.com](https://git-scm.com)
3. **Files ready**: All project files downloaded to your local computer

## 🚀 Method 1: GitHub Web Interface (Easiest)

### Step 1: Create Repository
1. Go to [GitHub](https://github.com)
2. Click the **"+"** button in top-right → **"New repository"**
3. Fill in repository details:
   - **Repository name**: `esm2-epistasis-pipeline`
   - **Description**: `Computational epistasis prediction using ESM2 protein language model`
   - **Visibility**: Choose **Public** (recommended for open science)
   - ✅ **Add a README file** (we'll replace it)
   - **Add .gitignore**: Choose **Python**
   - **Choose a license**: **MIT License**
4. Click **"Create repository"**

### Step 2: Upload Files
1. In your new repository, click **"uploading an existing file"** link
2. **Drag and drop** or **choose files** to upload:
   ```
   esm2_epistasis_pipeline.ipynb
   README.md
   requirements.txt
   CHANGELOG.md
   setup.py
   ```
3. **Commit message**: "Initial commit: ESM2 epistasis pipeline v1.0.0"
4. Click **"Commit changes"**

### Step 3: Update Repository Settings
1. Go to **Settings** → **General**
2. Under **Features**, enable:
   - ✅ **Issues** (for bug reports)
   - ✅ **Discussions** (for Q&A)
3. Under **Social preview**, add a description and topics:
   - **Topics**: `protein`, `epistasis`, `esm2`, `bioinformatics`, `pytorch`, `transformers`

## 🔧 Method 2: Command Line (Advanced)

### Step 1: Create Repository on GitHub
Follow Step 1 from Method 1, but **don't add** README, .gitignore, or license (we have our own).

### Step 2: Initialize Local Repository
```bash
# Navigate to your project folder
cd /path/to/your/project/folder

# Initialize git repository
git init

# Add all files
git add .

# Make initial commit
git commit -m "Initial commit: ESM2 epistasis pipeline v1.0.0"

# Add remote origin (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/esm2-epistasis-pipeline.git

# Push to GitHub
git branch -M main
git push -u origin main
```

## 📝 Method 3: GitHub Desktop (User-Friendly)

### Step 1: Install GitHub Desktop
Download from [desktop.github.com](https://desktop.github.com)

### Step 2: Create Repository
1. Open GitHub Desktop
2. **File** → **New Repository**
3. **Name**: `esm2-epistasis-pipeline`
4. **Local path**: Choose where to create the folder
5. **Initialize with README**: ✅
6. **Git ignore**: **Python**
7. **License**: **MIT**
8. Click **"Create Repository"**

### Step 3: Add Files
1. Copy all your project files into the created folder
2. In GitHub Desktop, you'll see all files listed
3. **Summary**: "Initial commit: ESM2 epistasis pipeline v1.0.0"
4. Click **"Commit to main"**
5. Click **"Publish repository"**
6. Choose **Public** and click **"Publish Repository"**

## 🎯 Post-Setup Tasks

### 1. Update README with Your Info
Replace placeholders in `README.md`:
- `YOUR_USERNAME` → your GitHub username
- `your.email@example.com` → your email
- `[Your Name]` → your name

### 2. Enable GitHub Pages (Optional)
1. **Settings** → **Pages**
2. **Source**: **Deploy from a branch**
3. **Branch**: `main` **Folder**: `/docs` (create a docs folder if needed)

### 3. Add Repository Secrets (For CI/CD later)
1. **Settings** → **Secrets and variables** → **Actions**
2. Useful secrets to add later:
   - `HUGGINGFACE_TOKEN` (for model access)
   - `PYTORCH_TOKEN` (if needed)

### 4. Set Up Branch Protection (Optional)
1. **Settings** → **Branches**
2. **Add rule** for `main` branch
3. ✅ **Require pull request reviews**
4. ✅ **Require status checks**

## 🔗 Getting the Colab Badge Working

### Option 1: Update README after publishing
1. Replace this line in README.md:
   ```markdown
   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR_USERNAME/esm2-epistasis-pipeline/blob/main/esm2_epistasis_pipeline.ipynb)
   ```
   
   With your actual username:
   ```markdown
   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yourusername/esm2-epistasis-pipeline/blob/main/esm2_epistasis_pipeline.ipynb)
   ```

### Option 2: Test the Colab link
After uploading, test: `https://colab.research.google.com/github/yourusername/esm2-epistasis-pipeline/blob/main/esm2_epistasis_pipeline.ipynb`

## 📊 Setting Up Repository Analytics

### 1. Enable Insights
1. **Insights** → **Community Standards**
2. Add missing items:
   - ✅ **Code of conduct** (use GitHub template)
   - ✅ **Contributing guidelines**

### 2. Add Topics and Description
1. Main repository page → **⚙️** gear icon next to "About"
2. **Description**: "Computational epistasis prediction using ESM2 protein language model"
3. **Topics**: `protein`, `epistasis`, `esm2`, `bioinformatics`, `pytorch`, `transformers`, `computational-biology`, `machine-learning`
4. **Website**: Link to documentation or paper (if available)

## 🎉 Final Checklist

- ✅ Repository created and files uploaded
- ✅ README.md updated with your information
- ✅ Requirements.txt includes all dependencies  
- ✅ License file is present (MIT)
- ✅ .gitignore configured for Python
- ✅ Topics and description added
- ✅ Issues and Discussions enabled
- ✅ Colab badge working
- ✅ All placeholder text replaced

## 🆘 Troubleshooting

### Common Issues

**Problem**: "Git not recognized" error
**Solution**: Install Git from [git-scm.com](https://git-scm.com) and restart terminal

**Problem**: Permission denied when pushing
**Solution**: Use HTTPS with token or set up SSH keys ([guide](https://docs.github.com/en/authentication))

**Problem**: Colab badge not working
**Solution**: Ensure your repository is public and the file path is correct

**Problem**: Large files rejected
**Solution**: ESM2 models are auto-downloaded; don't commit model files

### Getting Help

1. **GitHub Documentation**: [docs.github.com](https://docs.github.com)
2. **Git Tutorial**: [git-scm.com/docs/gittutorial](https://git-scm.com/docs/gittutorial)
3. **GitHub Community**: [github.community](https://github.community)

---

**🎯 Once setup is complete, share your repository URL with the community!**

Example final URL: `https://github.com/yourusername/esm2-epistasis-pipeline`
