# Sahl - Easy Kaggle Dataset Upload Helper

[![PyPI version](https://badge.fury.io/py/sahl.svg)](https://badge.fury.io/py/sahl)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)

🚀 A simple Python package to upload datasets to Kaggle with proper versioning support.

## ✨ Features

- 🎯 **Clear distinction** between NEW dataset and VERSION updates
- 📝 **Semantic versioning** support (MAJOR.MINOR.PATCH)
- 📋 **Automatic metadata** generation
- 🔄 **Version notes** tracking
- ⚡ **Easy to use** - 3 lines of code!

## 📦 Installation

### For Users

```bash
pip install sahl
```

### For Development

#### Prerequisites
- Python 3.11 or higher
- Git

#### Setup Steps

1. **Clone the repository:**
```bash
git clone https://github.com/24-mohamedyehia/sahl.git
cd sahl
```

2. **Create a virtual environment:**

**Option A: Using venv (Recommended)**
```bash
# Create virtual environment
python -m venv .venv

# Activate it
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

**Option B: Using conda**
```bash
# Create conda environment
conda create -n sahl python=3.11 -y

# Activate it
conda activate sahl
```

3. **Install dependencies:**
```bash
# Install package in editable mode with dev dependencies
pip install -e ".[dev]"
```

4. **Verify installation:**
```bash
python -c "from sahl import __version__; print(f'Sahl version: {__version__}')"
```

## 🚀 Quick Start

### First Time Upload (NEW Dataset)

```python
from sahl import upload_to_kaggle, prepare_kaggle_dataset

# Step 1: Prepare your dataset
dataset_dir = prepare_kaggle_dataset(
    source_dir="./processed_data",
    output_dir="./kaggle_dataset",
    dataset_name="my-awesome-dataset",
    username="your-username",
    title="My Awesome Dataset"
)

# Step 2: Upload as NEW dataset
upload_to_kaggle(
    dataset_dir=dataset_dir,
    username="your-username",
    dataset_name="my-awesome-dataset",
    mode="new"  # 👈 Creates new dataset
)
```

### Update Existing Dataset (NEW VERSION)

```python
from sahl import upload_to_kaggle, prepare_kaggle_dataset

# Step 1: Prepare updated data
dataset_dir = prepare_kaggle_dataset(
    source_dir="./processed_data_v2",
    output_dir="./kaggle_dataset_v2",
    dataset_name="my-awesome-dataset",  # Same name!
    username="your-username",
    title="My Awesome Dataset",
    version="1.1.0"  # New version
)

# Step 2: Upload as VERSION update
upload_to_kaggle(
    dataset_dir=dataset_dir,
    username="your-username",
    dataset_name="my-awesome-dataset",  # Same name!
    mode="version",  # 👈 Creates new version
    version="1.1.0",
    version_notes="Fixed data quality issues"
)
```

### One-Liner Quick Upload

```python
from sahl import quick_upload

# NEW dataset
quick_upload("./data", "username", "dataset-name", mode="new")

# VERSION update
quick_upload("./data", "username", "dataset-name", mode="version", 
             version="1.1.0", version_notes="Bug fixes")
```

## 📖 API Reference

### `prepare_kaggle_dataset()`

Prepare dataset files for Kaggle upload.

**Parameters:**
- `source_dir` (Path): Directory containing your processed files
- `output_dir` (Path): Where to prepare dataset (will be created)
- `dataset_name` (str): Kaggle dataset slug (URL-friendly)
- `username` (str): Your Kaggle username
- `title` (str): Dataset title
- `description` (str, optional): Dataset description
- `version` (str, optional): Version number (default: "1.0.0")

**Returns:** `Path` to prepared dataset directory

### `upload_to_kaggle()`

Upload dataset to Kaggle.

**Parameters:**
- `dataset_dir` (Path): Directory containing prepared dataset
- `username` (str): Your Kaggle username
- `dataset_name` (str): Dataset slug
- `mode` (Literal["new", "version"]): Upload mode
  - `"new"`: Create new dataset (first time)
  - `"version"`: Update existing dataset
- `version` (str, optional): Version number (required for mode="version")
- `version_notes` (str, optional): Change description (required for mode="version")

### `quick_upload()`

Quick one-function upload to Kaggle.

**Parameters:**
- `source_dir` (str): Directory containing your files
- `username` (str): Your Kaggle username
- `dataset_name` (str): Dataset slug
- `title` (str, optional): Dataset title
- `mode` (Literal["new", "version"]): Upload mode
- `version` (str, optional): Version number
- `version_notes` (str, optional): Change notes

## 🔧 Configuration

### Kaggle API Credentials

Make sure you have Kaggle API credentials configured:

1. Go to https://www.kaggle.com/settings
2. Click "Create New Token"
3. Save `kaggle.json` to:
   - **Windows:** `C:\Users\<username>\.kaggle\kaggle.json`
   - **Linux/Mac:** `~/.kaggle/kaggle.json`

Or in Kaggle Notebooks:
```python
from kaggle_secrets import UserSecretsClient
user_secrets = UserSecretsClient()
KAGGLE_KEY = user_secrets.get_secret("KAGGLE_KEY")
```

## 📝 Semantic Versioning

This package follows [Semantic Versioning](https://semver.org/):

```
MAJOR.MINOR.PATCH

1.0.0 → 1.0.1  = Bug fix (backward compatible)
1.0.0 → 1.1.0  = New feature (backward compatible)
1.0.0 → 2.0.0  = Breaking change (not backward compatible)
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Development Workflow

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests: `pytest tests/`
5. Format code: `black sahl/` and `isort sahl/`
6. Commit your changes (`git commit -m 'Add amazing feature'`)
7. Push to the branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

### Running Tests

```bash
# Run all tests
pytest tests/

# Run with coverage
pytest tests/ --cov=sahl --cov-report=html
```

### Code Style

This project uses:
- **black** for code formatting
- **isort** for import sorting
- **flake8** for linting
- **mypy** for type checking

```bash
# Format code
black sahl/
isort sahl/

# Check linting
flake8 sahl/

# Type checking
mypy sahl/
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎓 Citation

If you use this package in your research, please cite:

```bibtex
@software{sahl,
  title = {Sahl: Easy Kaggle Dataset Versioning},
  author = {Mohamed Yehia},
  year = {2026},
  url = {https://github.com/24-mohamedyehia/sahl}
}
```

## 🔗 Links

- **GitHub**: [https://github.com/24-mohamedyehia/sahl](https://github.com/24-mohamedyehia/sahl)
- **PyPI**: [https://pypi.org/project/sahl](https://pypi.org/project/sahl)
- **Issues**: [https://github.com/24-mohamedyehia/sahl/issues](https://github.com/24-mohamedyehia/sahl/issues)

## 🙏 Acknowledgments

- Inspired by [Kaggle API](https://github.com/Kaggle/kaggle-api)

## 📊 Comparison with Kaggle API

| Feature | Kaggle API | Sahl |
|---------|-----------|------|
| Upload datasets | ✅ | ✅ |
| Clear versioning | ❌ | ✅ |
| Semantic versioning | ❌ | ✅ |
| Version notes | ❌ | ✅ |
| Easy to use | 😐 | ✅ |

## 🐛 Troubleshooting

### Error: "Dataset already exists"
**Solution**: Use `mode="version"` instead of `mode="new"`

### Error: "No changes detected"
**Solution**: Make sure files in `dataset_dir` are different from current version

### Error: "Kaggle API not configured"
**Solution**: Set up `~/.kaggle/kaggle.json` with your credentials

---

**Made with ❤️ by Mohamed Yehia**