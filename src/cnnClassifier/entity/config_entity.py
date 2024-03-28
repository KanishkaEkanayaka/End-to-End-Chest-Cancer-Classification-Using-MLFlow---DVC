from dataclasses import dataclass
from pathlib import Path

#dataclass is a class that introduced to specially deal with data. frozen=True means this class is frozen to only take defined parameters
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path