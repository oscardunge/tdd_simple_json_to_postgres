
# import os
import pandas as  pd 

from tdd_json_parser.tdd_simple_json_to_postgres.host.json_to_postgres import generate_ddl





def test_generate_ddl_creates_table(columns):
    schema = columns["schema"]
    table_name = columns["table_name"]
    ddl = generate_ddl(columns["columns"], table_name, schema)

    assert f"CREATE TABLE {schema}.{table_name}" in ddl


def test_generate_ddl_handles_primary_key(columns):
    schema = columns["schema"]
    table_name = columns["table_name"]
    ddl = generate_ddl(columns["columns"], table_name, schema)

    assert "id INTEGER CONSTRAINT constraint_dwh_avega_tdd_test_table_id PRIMARY KEY" in ddl


def test_generate_ddl_includes_name_column(columns):
    schema = columns["schema"]
    table_name = columns["table_name"]
    ddl = generate_ddl(columns["columns"], table_name, schema)

    assert "name VARCHAR(255)" in ddl


def test_generate_ddl_includes_age_column(columns):
    schema = columns["schema"]
    table_name = columns["table_name"]
    ddl = generate_ddl(columns["columns"], table_name, schema)

    assert "age INTEGER" in ddl


def test_generate_ddl_ends_properly(columns):
    schema = columns["schema"]
    table_name = columns["table_name"]
    ddl = generate_ddl(columns["columns"], table_name, schema)

    assert ddl.endswith(");\n")
