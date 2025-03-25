
import os


from tdd_json_parser.tdd_simple_json_to_postgres.host.json_to_postgres import save_ddl_to_file



def test_save_ddl_to_file_creates_file(sample_ddl, table_name):
    ddl_path = save_ddl_to_file(sample_ddl, table_name)
    assert os.path.exists(ddl_path)


def test_save_ddl_to_file_correct_content(sample_ddl, table_name):
    ddl_path = save_ddl_to_file(sample_ddl, table_name)
    with open(ddl_path, 'r') as f:
        content = f.read()
    assert content == sample_ddl


def test_save_ddl_to_file_returns_correct_path(sample_ddl, table_name):
    ddl_path = save_ddl_to_file(sample_ddl, table_name)
    expected_path = f"ddls/{table_name}.sql"
    assert ddl_path == expected_path