import pandas as  pd 
import os
from tdd_json_parser.tdd_simple_json_to_postgres.host.json_to_postgres import infer_schema



def test_infer_schema_basic(sample_dataframe, table_name =  "test_table", schema= "dwh_avega_tdd"):
    ddl = infer_schema(sample_dataframe, table_name, schema= schema)
    assert "name VARCHAR(255)" in ddl
    assert "age INTEGER" in ddl
    assert os.path.exists("ddls/test_table.sql")

def test_infer_schema_basic_with_constraint(sample_dataframe, table_name =  "test_table2", constraint="id", schema= "dwh_avega_tdd"):
    ddl = infer_schema(sample_dataframe, table_name =  "test_table2", constraint="id", schema= schema)
    assert f"{constraint} INTEGER CONSTRAINT constraint_{schema}_{table_name}_{constraint} PRIMARY KEY" in ddl
    assert "name VARCHAR(255)" in ddl
    assert "age INTEGER" in ddl
    assert os.path.exists("ddls/test_table2.sql")

def test_infer_schema_different_types(sample_dataframe_other_types):

    ddl = infer_schema(sample_dataframe_other_types, "test_table")
    assert "float_col FLOAT" in ddl
    assert "bool_col BOOLEAN" in ddl




