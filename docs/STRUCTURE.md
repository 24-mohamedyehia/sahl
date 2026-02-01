# Project Structure

```
sahl/
├── .git/                      # Git repository
├── .gitignore                 # Git ignore file
├── CHANGELOG.md               # Version history
├── CONTRIBUTING.md            # Contribution guidelines
├── LICENSE                    # MIT License
├── README.md                  # Main documentation
├── pyproject.toml             # Project configuration
├── requirements.txt           # Production dependencies
├── requirements-dev.txt       # Development dependencies
├── setup.py                   # Setup file
├── MANIFEST.in                # Package manifest
│
├── src/                       # Source directory ✨
│   └── sahl/                 # Main package
│       ├── __init__.py       # Package initialization
│       ├── prepare.py        # Dataset preparation module
│       ├── upload.py         # Upload functionality
│       └── utils.py          # Utility functions
│
├── tests/                     # Test suite (to be created)
│   └── test_*.py
│
└── docs/                      # Additional documentation
    ├── STRUCTURE.md           # This file
    ├── DEVELOPER.md           # Developer guide
    └── SRC_LAYOUT.md          # Explanation of src/ layout
```

## Module Structure

### `src/sahl/__init__.py`
- Package entry point
- Exports main functions
- Version information

### `src/sahl/prepare.py`
- `prepare_kaggle_dataset()` - Main preparation function
- Helper functions for README and metadata creation

### `src/sahl/upload.py`
- `upload_to_kaggle()` - Main upload function
- `_upload_new_dataset()` - New dataset upload
- `_upload_new_version()` - Version update

### `src/sahl/utils.py`
- `quick_upload()` - One-liner convenience function
- `print_upload_guide()` - Help/guide display

