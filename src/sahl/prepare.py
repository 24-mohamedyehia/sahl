"""
Dataset preparation functionality for Kaggle uploads.
"""

import json
import shutil
from pathlib import Path
from datetime import datetime
from typing import Optional


def prepare_kaggle_dataset(
    source_dir: Path,
    output_dir: Path,
    dataset_name: str,
    username: str,
    title: str,
    description: Optional[str] = None,
    version: str = "1.0.0"
) -> Path:
    """
    Prepare processed data for Kaggle dataset upload.
    
    Parameters:
        source_dir: Directory containing processed files
        output_dir: Directory to prepare dataset (will be created)
        dataset_name: Kaggle dataset slug (e.g., 'my-dataset')
        username: Your Kaggle username
        title: Dataset title
        description: Dataset description (optional)
        version: Version number (e.g., "1.0.0", "1.1.0")
    
    Returns:
        Path to prepared dataset directory
    
    Example:
        >>> dataset_dir = prepare_kaggle_dataset(
        ...     source_dir=Path("./processed"),
        ...     output_dir=Path("./kaggle_dataset"),
        ...     dataset_name="my-awesome-dataset",
        ...     username="researcher",
        ...     title="My Awesome Dataset",
        ...     version="1.0.0"
        ... )
    """
    print(f"\n{'='*60}")
    print("🎁 PREPARING KAGGLE DATASET")
    print(f"{'='*60}\n")
    
    # Create output directory
    output_dir = Path(output_dir)
    if output_dir.exists():
        print(f"⚠️  Output directory exists, cleaning...")
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Copy all files from source
    print("📦 Copying files...")
    source_dir = Path(source_dir)
    
    for item in source_dir.rglob('*'):
        if item.is_file():
            relative_path = item.relative_to(source_dir)
            dest_path = output_dir / relative_path
            dest_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(item, dest_path)
            print(f"  - Copied {relative_path}")
    
    # Create README.md if not exists
    _create_readme(output_dir, title, dataset_name, username, version, description)
    
    # Create dataset-metadata.json for Kaggle
    _create_metadata(output_dir, title, username, dataset_name)
    
    # Print summary
    _print_summary(output_dir, username, dataset_name, title, version)
    
    return output_dir


def _create_readme(
    output_dir: Path,
    title: str,
    dataset_name: str,
    username: str,
    version: str,
    description: Optional[str]
) -> None:
    """Create README.md file if it doesn't exist."""
    readme_path = output_dir / "README.md"
    if not readme_path.exists():
        print("\n📝 Creating README.md...")
        
        if not description:
            description = f"""# {title}

Dataset version: {version}

## Contents

This dataset contains processed data files.

## Usage

```python
# Load your data here
import pandas as pd

# Example
data = pd.read_csv('your_file.csv')
```

## Citation

If you use this dataset, please cite:

```
@dataset{{{dataset_name},
  title = {{{title}}},
  author = {{{username}}},
  year = {{2026}},
  version = {{{version}}}
}}
```

Last updated: {datetime.now().strftime('%Y-%m-%d')}
"""
        
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(description)
        print(f"  ✓ Created README.md")


def _create_metadata(
    output_dir: Path,
    title: str,
    username: str,
    dataset_name: str
) -> None:
    """Create dataset-metadata.json for Kaggle."""
    print("📝 Creating dataset-metadata.json...")
    
    metadata = {
        "title": title,
        "id": f"{username}/{dataset_name}",
        "licenses": [{"name": "CC0-1.0"}],
    }
    
    metadata_path = output_dir / "dataset-metadata.json"
    with open(metadata_path, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, ensure_ascii=False, indent=2)
    
    print(f"  ✓ Created dataset-metadata.json")


def _print_summary(
    output_dir: Path,
    username: str,
    dataset_name: str,
    title: str,
    version: str
) -> None:
    """Print dataset preparation summary."""
    total_size = sum(f.stat().st_size for f in output_dir.rglob('*') if f.is_file())
    total_size_mb = total_size / (1024**2)
    
    print(f"\n{'='*60}")
    print("📊 Dataset Summary")
    print(f"{'='*60}")
    print(f"  Location:     {output_dir}")
    print(f"  Total size:   {total_size_mb:.2f} MB")
    print(f"  Dataset ID:   {username}/{dataset_name}")
    print(f"  Title:        {title}")
    print(f"  Version:      {version}")
    print(f"\n✓ Dataset prepared successfully!")
