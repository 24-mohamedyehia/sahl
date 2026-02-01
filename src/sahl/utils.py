"""
Utility functions for quick uploads and guides.
"""

import shutil
import tempfile
from pathlib import Path
from typing import Optional, Literal

from .prepare import prepare_kaggle_dataset
from .upload import upload_to_kaggle


def quick_upload(
    source_dir: str,
    username: str,
    dataset_name: str,
    title: Optional[str] = None,
    mode: Literal["new", "version"] = "new",
    version: str = "1.0.0",
    version_notes: Optional[str] = None
):
    """
    Quick one-function upload to Kaggle.
    
    Combines prepare_kaggle_dataset() and upload_to_kaggle() in one call.
    
    Parameters:
        source_dir: Directory containing your files
        username: Your Kaggle username
        dataset_name: Dataset slug
        title: Dataset title (defaults to dataset_name)
        mode: "new" or "version"
        version: Version number
        version_notes: Change notes (required for version mode)
    
    Example:
        >>> quick_upload(
        ...     "./data",
        ...     "researcher",
        ...     "my-dataset",
        ...     mode="new"
        ... )
    """
    if not title:
        title = dataset_name.replace('-', ' ').title()
    
    # Create temporary output directory
    output_dir = Path(tempfile.mkdtemp(prefix="kaggle_dataset_"))
    
    try:
        # Prepare dataset
        dataset_dir = prepare_kaggle_dataset(
            source_dir=Path(source_dir),
            output_dir=output_dir,
            dataset_name=dataset_name,
            username=username,
            title=title,
            version=version
        )
        
        # Upload
        upload_to_kaggle(
            dataset_dir=dataset_dir,
            username=username,
            dataset_name=dataset_name,
            mode=mode,
            version=version,
            version_notes=version_notes
        )
    finally:
        # Cleanup
        if output_dir.exists():
            shutil.rmtree(output_dir)


def print_upload_guide():
    """Print comprehensive upload guide."""
    guide = """
╔════════════════════════════════════════════════════════════════╗
║                  📚 KAGGLE UPLOAD GUIDE                        ║
╚════════════════════════════════════════════════════════════════╝

┌─────────────────────────────────────────────────────────────────┐
│ 🆕 SCENARIO 1: First Time Upload (NEW Dataset)                 │
└─────────────────────────────────────────────────────────────────┘

from sahl import upload_to_kaggle, prepare_kaggle_dataset

# Prepare and upload
dataset_dir = prepare_kaggle_dataset(
    source_dir="./data",
    output_dir="./kaggle_dataset",
    dataset_name="my-dataset",
    username="your-username",
    title="My Dataset"
)

upload_to_kaggle(
    dataset_dir=dataset_dir,
    username="your-username",
    dataset_name="my-dataset",
    mode="new"  # 👈 Creates NEW dataset
)


┌─────────────────────────────────────────────────────────────────┐
│ 🔄 SCENARIO 2: Update Existing (NEW VERSION)                   │
└─────────────────────────────────────────────────────────────────┘

from sahl import upload_to_kaggle, prepare_kaggle_dataset

# Prepare updated data
dataset_dir = prepare_kaggle_dataset(
    source_dir="./data_v2",
    output_dir="./kaggle_dataset_v2",
    dataset_name="my-dataset",  # SAME name!
    username="your-username",
    title="My Dataset",
    version="1.1.0"  # New version
)

upload_to_kaggle(
    dataset_dir=dataset_dir,
    username="your-username",
    dataset_name="my-dataset",  # SAME name!
    mode="version",  # 👈 Creates VERSION
    version="1.1.0",
    version_notes="Fixed bugs and improved quality"
)


┌─────────────────────────────────────────────────────────────────┐
│ ⚡ QUICK ONE-LINER                                              │
└─────────────────────────────────────────────────────────────────┘

from sahl import quick_upload

# NEW dataset
quick_upload("./data", "username", "my-dataset", mode="new")

# VERSION update
quick_upload("./data", "username", "my-dataset", mode="version",
             version="1.1.0", version_notes="Bug fixes")

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
For more details: https://github.com/24-mohamedyehia/sahl
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    print(guide)
