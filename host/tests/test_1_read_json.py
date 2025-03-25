import pytest
from tdd_json_parser.tdd_simple_json_to_postgres.host.json_to_postgres import read_json_file

def test_read_json_file_valid(sample_json):
    file_path, expected_data = sample_json
    result = read_json_file(file_path)
    assert result == expected_data

def test_read_json_file_invalid_path():
    with pytest.raises(FileNotFoundError):
        read_json_file("nonexistent.json")