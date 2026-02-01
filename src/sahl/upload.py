"""
Kaggle upload functionality with versioning support.
"""

import os
from pathlib import Path
from typing import Optional, Literal


def upload_to_kaggle(
    dataset_dir: Path,
    username: str,
    dataset_name: str,
    mode: Literal["new", "version"] = "new",
    version: str = "1.0.0",
    version_notes: Optional[str] = None
):
    """
    Upload dataset to Kaggle as NEW dataset or VERSION update.
    
    Parameters:
        dataset_dir: Directory containing prepared dataset
        username: Your Kaggle username
        dataset_name: Dataset slug (must match existing for 'version' mode)
        mode: "new" for new dataset, "version" for updating existing
        version: Version number (e.g., "1.1.0") - used for version notes
        version_notes: Description of changes (required for 'version' mode)
    
    Raises:
        ValueError: If version_notes not provided when mode='version'
    
    Examples:
        Create NEW dataset:
        >>> upload_to_kaggle(
        ...     dataset_dir=Path("./kaggle_dataset"),
        ...     username="researcher",
        ...     dataset_name="my-dataset",
        ...     mode="new"
        ... )
        
        Update existing dataset:
        >>> upload_to_kaggle(
        ...     dataset_dir=Path("./kaggle_dataset_v2"),
        ...     username="researcher",
        ...     dataset_name="my-dataset",
        ...     mode="version",
        ...     version="1.1.0",
        ...     version_notes="Fixed data quality issues"
        ... )
    """
    print(f"\n{'='*60}")
    print(f"📤 UPLOADING TO KAGGLE ({mode.upper()} MODE)")
    print(f"{'='*60}\n")
    
    # Validate parameters
    if mode == "version" and not version_notes:
        raise ValueError("version_notes is required when mode='version'")
    
    # Change to dataset directory
    original_dir = os.getcwd()
    dataset_dir = Path(dataset_dir)
    os.chdir(dataset_dir)
    
    try:
        if mode == "new":
            _upload_new_dataset(username, dataset_name)
        elif mode == "version":
            _upload_new_version(username, dataset_name, version, version_notes)
    finally:
        os.chdir(original_dir)


def _upload_new_dataset(username: str, dataset_name: str) -> None:
    """Upload a new dataset to Kaggle."""
    print("🆕 Creating NEW dataset...")
    print(f"   Dataset: {username}/{dataset_name}")
    print(f"   This will be version 1")
    print()
    
    result = os.system("kaggle datasets create -p . --dir-mode zip")
    
    if result == 0:
        print(f"\n✅ NEW Dataset created successfully!")
        print(f"   View at: https://www.kaggle.com/datasets/{username}/{dataset_name}")
        print(f"\n💡 Next time, use mode='version' to update this dataset")
    else:
        print(f"\n❌ Upload failed with code {result}")
        print("   Common issues:")
        print("   - Dataset name already exists (use mode='version' instead)")
        print("   - Kaggle API not configured")
        print("   - Invalid dataset name (must be URL-friendly)")


def _upload_new_version(
    username: str,
    dataset_name: str,
    version: str,
    version_notes: str
) -> None:
    """Upload a new version of an existing dataset."""
    print("🔄 Creating NEW VERSION of existing dataset...")
    print(f"   Dataset: {username}/{dataset_name}")
    print(f"   Version: {version}")
    print(f"   Notes: {version_notes}")
    print()
    
    # Kaggle CLI for versioning
    version_message = f"v{version}: {version_notes}"
    cmd = f'kaggle datasets version -p . -m "{version_message}" --dir-mode zip'
    result = os.system(cmd)
    
    if result == 0:
        print(f"\n✅ NEW VERSION created successfully!")
        print(f"   View at: https://www.kaggle.com/datasets/{username}/{dataset_name}")
        print(f"   Version: {version}")
        print(f"\n📝 Remember to:")
        print(f"   1. Update CHANGELOG.md with this version")
        print(f"   2. Tag in Git: git tag v{version}")
    else:
        print(f"\n❌ Upload failed with code {result}")
        print("   Common issues:")
        print("   - Dataset doesn't exist (use mode='new' first)")
        print("   - No changes detected")
        print("   - Kaggle API not configured")
