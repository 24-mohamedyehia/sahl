# Contributing to Sahl

Thank you for your interest in contributing to Sahl! This document provides guidelines and instructions for contributing.

## 🚀 Getting Started

### Prerequisites

- Python 3.11 or higher
- Git
- A GitHub account

### Development Setup

1. **Fork and clone the repository:**
```bash
git clone https://github.com/YOUR_USERNAME/sahl.git
cd sahl
```

2. **Create a virtual environment:**
```bash
# Using venv
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# OR using conda
conda create -n sahl python=3.11 -y
conda activate sahl
```

3. **Install development dependencies:**
```bash
pip install -e ".[dev]"
```

4. **Verify installation:**
```bash
python -c "from sahl import __version__; print(__version__)"
pytest tests/ -v
```

## 📝 Development Workflow

### 1. Create a Feature Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/bug-description
```

### 2. Make Your Changes

- Write clean, readable code
- Follow PEP 8 style guidelines
- Add docstrings to functions and classes
- Update tests if needed

### 3. Run Tests

```bash
# Run all tests
pytest tests/

# Run with coverage
pytest tests/ --cov=sahl --cov-report=html
```

### 4. Format Your Code

```bash
# Format with black
black sahl/

# Sort imports
isort sahl/

# Check linting
flake8 sahl/

# Type checking
mypy sahl/
```

### 5. Commit Your Changes

```bash
git add .
git commit -m "feat: add amazing feature"
```

**Commit Message Format:**
- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `style:` Code style changes (formatting, etc.)
- `refactor:` Code refactoring
- `test:` Test changes
- `chore:` Build/config changes

### 6. Push and Create Pull Request

```bash
git push origin feature/your-feature-name
```

Then create a Pull Request on GitHub.

## 🧪 Testing Guidelines

- Write tests for new features
- Maintain or improve code coverage
- Test edge cases and error conditions
- Use descriptive test names

Example:
```python
def test_prepare_kaggle_dataset_creates_output_directory():
    """Test that prepare_kaggle_dataset creates the output directory."""
    # Test implementation
    pass
```

## 📚 Documentation

- Update README.md if adding new features
- Add docstrings to all public functions/classes
- Update CHANGELOG.md
- Add examples for new functionality

## 🐛 Reporting Bugs

When reporting bugs, please include:

1. **Description:** Clear description of the bug
2. **Steps to reproduce:** Detailed steps
3. **Expected behavior:** What should happen
4. **Actual behavior:** What actually happens
5. **Environment:**
   - Python version
   - Operating system
   - Sahl version

## 💡 Suggesting Features

Feature requests are welcome! Please include:

1. **Use case:** Why is this feature needed?
2. **Description:** Detailed description
3. **Examples:** Usage examples if possible
4. **Alternatives:** Have you considered alternatives?

## ✅ Pull Request Checklist

Before submitting a PR, make sure:

- [ ] Code follows project style guidelines
- [ ] Tests pass (`pytest tests/`)
- [ ] Code is formatted (`black` and `isort`)
- [ ] Docstrings are added/updated
- [ ] README.md is updated (if needed)
- [ ] CHANGELOG.md is updated
- [ ] Commit messages follow format
- [ ] PR description is clear and detailed

## 📄 Code of Conduct

- Be respectful and inclusive
- Welcome newcomers
- Focus on constructive feedback
- Help others learn and grow

## 📞 Questions?

If you have questions:

1. Check existing issues and documentation
2. Open a new issue with the "question" label
3. Be specific and provide context

## 🙏 Thank You!

Your contributions make Sahl better for everyone. Thank you for taking the time to contribute!

---

**Happy Coding!** 🚀
