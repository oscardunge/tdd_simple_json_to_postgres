
import pytest
import pandas as  pd
from tdd_json_parser.tdd_simple_json_to_postgres.host.json_to_postgres import to_dataframe

def test_to_dataframe_single_dict(json_data):
    df = to_dataframe(json_data)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 1
    assert df.iloc[0]["name"] == "John"

def test_to_dataframe_list(list_json_data):
    df = to_dataframe(list_json_data)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 2
    assert df.iloc[1]["name"] == "Jane"


def test_to_dataframe_invalid_int():
    with pytest.raises(ValueError, match="json_data must be a dict or list of dicts"):
        to_dataframe(42)

def test_to_dataframe_invalid_string():
    with pytest.raises(ValueError, match="json_data must be a dict or list of dicts"):
        to_dataframe("id,name\n1,John")