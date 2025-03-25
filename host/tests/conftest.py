
# tests/conftest.py
import pytest
import pandas as pd
import json
import os

@pytest.fixture
def sample_json(tmp_path):
    """Create a temporary JSON file for testing"""
    data = {
        "id": 1,
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    json_file = tmp_path / "test.json"
    with open(json_file, 'w') as f:
        json.dump(data, f)
    return json_file, data

@pytest.fixture
def sample_dataframe():
    """Create a sample DataFrame"""
    data = [{
        "id": 1,
        "name": "John",
        "age": 30,
        "city": "New York"
    }]
    return pd.DataFrame(data)


@pytest.fixture
def sample_dataframe_other_types():
    """Create a sample DataFrame"""
    data = ({
        "id": [1],
        "float_col": [1.5],
        "bool_col": [True]
    })
    return pd.DataFrame(data)


@pytest.fixture
def json_data():
    """Provide raw JSON data"""
    return {"id": 1, "name": "John", "age": 30, "city": "New York"}

@pytest.fixture
def list_json_data():
    """Provide list of JSON data"""
    return [{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]



@pytest.fixture
def columns():
    return {
        "schema": "dwh_avega_tdd",
        "table_name": "test_table",
        "columns": [
            "id INTEGER CONSTRAINT constraint_dwh_avega_tdd_test_table_id PRIMARY KEY",
            "name VARCHAR(255)",
            "age INTEGER"
        ]
    }



import os

@pytest.fixture
def sample_ddl():
    return """
    CREATE TABLE dwh_avega_tdd.test_table (
        id INTEGER CONSTRAINT constraint_dwh_avega_tdd_test_table_id PRIMARY KEY,
        name VARCHAR(255),
        age INTEGER
    );
    """

@pytest.fixture
def table_name():
    return "test_table"



@pytest.fixture
def sample_json_file(tmp_path):
    file_path = tmp_path / "test_table.json"
    data = [
        {"id": 1, "name": "John"},
        {"id": 2, "name": "Jane"}
    ]
    with open(file_path, 'w') as f:
        json.dump(data, f)
    return str(file_path)


