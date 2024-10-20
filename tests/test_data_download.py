import os
import pytest
from patientinsight.data.download import download_dataset

@pytest.fixture
def temp_output_dir(tmp_path):
    return tmp_path / "test_output"

def test_download_dataset(temp_output_dir):
    download_dataset(output_dir=str(temp_output_dir))
    
    # Check if files are created
    assert (temp_output_dir / "train.csv").exists()
    assert (temp_output_dir / "test.csv").exists()
    assert (temp_output_dir / "validation.csv").exists()

    # Check if files are not empty
    assert (temp_output_dir / "train.csv").stat().st_size > 0
    assert (temp_output_dir / "test.csv").stat().st_size > 0
    assert (temp_output_dir / "validation.csv").stat().st_size > 0

