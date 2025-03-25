import os
import json
import pandas as pd

from tdd_json_parser.tdd_simple_json_to_postgres.host.json_to_postgres import main



def test_main_creates_correct_table_structure(sample_json_file):
    ddl, _ = main(sample_json_file)
    assert "CREATE TABLE dwh_avega_tdd.test_table" in ddl


def test_main_includes_id_column(sample_json_file):
    ddl, _ = main(sample_json_file)
    assert "id INTEGER" in ddl

def test_main_includes_name_column(sample_json_file):
    ddl, _ = main(sample_json_file)
    assert "name VARCHAR(255)" in ddl

def test_main_saves_file_correctly(sample_json_file):
    _, ddl_path = main(sample_json_file)
    assert os.path.exists(ddl_path)

def test_main_saved_file_contains_correct_ddl(sample_json_file):
    _, ddl_path = main(sample_json_file)
    with open(ddl_path, 'r') as f:
        content = f.read()
    assert "CREATE TABLE dwh_avega_tdd.test_table" in content

def test_main_returns_correct_path(sample_json_file):
    _, ddl_path = main(sample_json_file)
    assert ddl_path == "ddls/test_table.sql"
