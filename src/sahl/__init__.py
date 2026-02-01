"""
Sahl - Easy Kaggle Dataset Upload Helper
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A simple Python package for uploading datasets to Kaggle with proper versioning.

Basic usage:

   >>> from sahl import upload_to_kaggle, prepare_kaggle_dataset
   >>> dataset_dir = prepare_kaggle_dataset(
   ...     source_dir="./data",
   ...     output_dir="./kaggle_dataset",
   ...     dataset_name="my-dataset",
   ...     username="username",
   ...     title="My Dataset"
   ... )
   >>> upload_to_kaggle(
   ...     dataset_dir=dataset_dir,
   ...     username="username",
   ...     dataset_name="my-dataset",
   ...     mode="new"
   ... )

:copyright: (c) 2026 by Mohamed Yehia.
:license: MIT, see LICENSE for more details.
"""

__version__ = "0.1.0"
__author__ = "Mohamed Yehia"
__email__ = "mo.yehia.824@gmail.com"
__license__ = "MIT"

from .prepare import prepare_kaggle_dataset
from .upload import upload_to_kaggle
from .utils import quick_upload, print_upload_guide

__all__ = [
    "prepare_kaggle_dataset",
    "upload_to_kaggle",
    "print_upload_guide",
    "quick_upload",
    "__version__",
]
