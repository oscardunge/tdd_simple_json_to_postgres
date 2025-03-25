
import os
import json
import pandas as pd
from pathlib import Path

def read_json_file(file_path: str | Path):
    file_path = Path(file_path)  
    with file_path.open('r', encoding='utf-8') as f:
        json_in_memory = json.load(f)  
    return json_in_memory


def to_dataframe(json_data: dict | list):
    """Convert JSON data to pandas DataFrame"""
    if not isinstance(json_data, (dict, list)):
        raise ValueError("json_data must be a dict or list of dicts")
    if isinstance(json_data, dict):
        json_data = [json_data]
    return pd.DataFrame(json_data)


def infer_schema(df: pd.DataFrame, table_name: str, constraint: str | None = None, schema: str = "dwh_avega_tdd"):
    """Infer SQL column definitions directly from DataFrame."""
    type_mapping = {
        'int64': 'INTEGER',
        'float64': 'FLOAT',
        'object': 'VARCHAR(255)',
        'bool': 'BOOLEAN'
    }
    
    columns = []
    for column, dtype in df.dtypes.items():
        sql_type = type_mapping.get(str(dtype), 'VARCHAR(255)')
        if constraint and column == constraint:
            column_def = f"{column} {sql_type} CONSTRAINT constraint_{schema}_{table_name}_{constraint} PRIMARY KEY"
        else:
            column_def = f"{column} {sql_type}"
        columns.append(column_def)

    return columns


def generate_ddl(columns: list, table_name: str, schema: str = "dwh_avega_tdd"):
    """Generate SQL DDL statement for creating the table."""
    full_table_name = f"{schema}.{table_name}" if schema else table_name
    
    ddl = f"CREATE TABLE {full_table_name} (\n    " + ",\n    ".join(columns) + "\n);\n"
    return ddl



def save_ddl_to_file(ddl: str, table_name: str):
    """Save the generated DDL to a file."""
    os.makedirs("ddls", exist_ok=True)
    ddl_path = f"ddls/{table_name}.sql"
    with open(ddl_path, 'w') as f:
        f.write(ddl)
    return ddl_path



def main(json_file_name: str, constraint: str = None, schema="dwh_avega_tdd"):
    """Process a JSON file into a DDL file."""
    table_name = os.path.splitext(os.path.basename(json_file_name))[0]
    data = read_json_file(json_file_name)
    df = to_dataframe(data)
    
    # Inferera och skapa DDL i ett steg
    columns = infer_schema(df, schema, constraint, table_name)
    ddl = generate_ddl(columns, table_name, schema)
    ddl_path = save_ddl_to_file(ddl, table_name)
    
    return ddl, ddl_path






































# # # # # # # # # # json_to_postgres.py
# # # # # # # # # import json
# # # # # # # # # import pandas as pd
# # # # # # # # # import psycopg2
# # # # # # # # # from sqlalchemy import create_engine

# # # # # # # # # def read_json_file(file_path):
# # # # # # # # #     """Read JSON file and return dictionary"""
# # # # # # # # #     with open(file_path, 'r') as f:
# # # # # # # # #         data = json.load(f)
# # # # # # # # #     return data

# # # # # # # # # def to_dataframe(json_data):
# # # # # # # # #     """Convert JSON data to pandas DataFrame"""
# # # # # # # # #     if isinstance(json_data, dict):
# # # # # # # # #         json_data = [json_data]
# # # # # # # # #     return pd.DataFrame(json_data)

# # # # # # # # # def infer_schema(df, table_name):
# # # # # # # # #     """Infer SQL schema from DataFrame and return DDL"""
# # # # # # # # #     type_mapping = {
# # # # # # # # #         'int64': 'INTEGER',
# # # # # # # # #         'float64': 'FLOAT',
# # # # # # # # #         'object': 'VARCHAR(255)',
# # # # # # # # #         'bool': 'BOOLEAN'
# # # # # # # # #     }
    
# # # # # # # # #     columns = []
# # # # # # # # #     for column, dtype in df.dtypes.items():
# # # # # # # # #         sql_type = type_mapping.get(str(dtype), 'VARCHAR(255)')
# # # # # # # # #         if column == 'id':
# # # # # # # # #             columns.append(f"{column} {sql_type} CONSTRAINT id_user_pk PRIMARY KEY")
# # # # # # # # #         else:
# # # # # # # # #             columns.append(f"{column} {sql_type}")
    
# # # # # # # # #     ddl = f"CREATE TABLE {table_name} (\n    " + ",\n    ".join(columns) + "\n);"
# # # # # # # # #     with open(f"{table_name}.sql", 'w') as f:
# # # # # # # # #         f.write(ddl)
# # # # # # # # #     return ddl

# # # # # # # # # def execute_ddl_and_insert(ddl, df, table_name):
# # # # # # # # #     """Execute DDL and insert data into PostgreSQL"""
# # # # # # # # #     conn = psycopg2.connect(
# # # # # # # # #         dbname="your_db",
# # # # # # # # #         user="your_user",
# # # # # # # # #         password="your_password",
# # # # # # # # #         host="localhost"
# # # # # # # # #     )
    
# # # # # # # # #     try:
# # # # # # # # #         with conn.cursor() as cursor:
# # # # # # # # #             cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
# # # # # # # # #             cursor.execute(ddl)
        
# # # # # # # # #         engine = create_engine('postgresql://your_user:your_password@localhost/your_db')
# # # # # # # # #         df.to_sql(table_name, engine, if_exists='append', index=False)
        
# # # # # # # # #         conn.commit()
# # # # # # # # #     finally:
# # # # # # # # #         conn.close()