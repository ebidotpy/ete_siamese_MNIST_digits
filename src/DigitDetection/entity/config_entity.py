from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path

@dataclass(frozen=True)
class DataPrepareConfig:
    train_images: Path
    train_labels: Path
    test_images: Path
    test_labels: Path
    batch_size: int
    image_shape: list
