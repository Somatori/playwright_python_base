from pathlib import Path

# repo_root / tests / test_data
TEST_DATA_DIR = Path(__file__).resolve().parents[1] / "tests" / "test_data"

def get_test_data_path(*parts: str) -> Path:
    """Return a Path inside tests/test_data, e.g. get_test_data_path('uploads','sample.pdf')"""
    return TEST_DATA_DIR.joinpath(*parts)
