# JSON to DDL Converter

This script takes a JSON file as input, infers its schema, and generates a SQL Data Definition Language (DDL) statement to create a corresponding table.

## Requirements

This script addresses the need to quickly generate database table schemas from JSON data, which is useful in scenarios such as:

* **Rapid prototyping:** Quickly setting up database tables based on initial data structures.
* **Data integration:** Creating target tables for data loaded from JSON sources.
* **Schema discovery:** Understanding the structure of JSON data for database design.

## Usage

1.  Save the provided Python code as a `.py` file (e.g., `json_to_ddl.py`).
2.  Ensure you have the `pandas` library installed. You can install it using pip:
    ```bash
    pip install pandas
    ```
3.  Place your JSON data file in the same directory as the script, or provide the full path to the file.
4.  Run the script from your terminal, providing the JSON file name as a command-line argument:
    ```bash
    python json_to_ddl.py your_data.json
    ```
5.  Optionally, you can specify a column to be used as a primary key and the target schema:
    ```bash
    python json_to_ddl.py your_data.json --constraint id --schema my_schema
    ```

## Script Description

The script performs the following steps:

1.  **Reads JSON file:** The `read_json_file` function reads the JSON data from the specified file.
2.  **Converts to DataFrame:** The `to_dataframe` function converts the JSON data (which can be a dictionary or a list of dictionaries) into a pandas DataFrame.
3.  **Infers Schema:** The `infer_schema` function analyzes the DataFrame's data types and generates corresponding SQL column definitions. It maps Python data types to common SQL data types (INTEGER, FLOAT, VARCHAR, BOOLEAN). It also allows specifying a primary key constraint.
4.  **Generates DDL:** The `generate_ddl` function constructs the `CREATE TABLE` SQL statement using the inferred column definitions and the provided table name and schema.
5.  **Saves DDL to File:** The `save_ddl_to_file` function saves the generated DDL statement to a `.sql` file in a `ddls` subdirectory. The filename is based on the JSON file name.
6.  **Main Function:** The `main` function orchestrates the entire process, taking the JSON file name, optional constraint column, and schema as input.

## TODO

* **Schema Evolution:**
    * Implement functionality to compare a new JSON schema with an existing table schema.
    * Generate `ALTER TABLE` statements to add new columns, modify existing column types (with considerations for data loss), or handle removed columns.
    * Consider different strategies for schema evolution (e.g., adding new columns as nullable by default, providing options for default values).
    * Explore using database introspection to fetch the existing schema for comparison.
* **More Granular Type Mapping:** Allow for more specific SQL data type mappings (e.g., specifying VARCHAR length, DECIMAL precision and scale).
* **Handling Nested JSON:** Currently, the script flattens the JSON structure into a tabular format. Explore options for handling nested JSON structures, potentially creating related tables or using JSON/JSONB data types in the database.
* **Command-Line Argument Parsing:** Use a library like `argparse` for more robust command-line argument handling.
* **Error Handling:** Implement more comprehensive error handling, such as handling invalid JSON files or unsupported data types.
* **Support for Other Database Dialects:** Currently, the generated DDL is generic. Consider adding support for specific database dialects (e.g., PostgreSQL, MySQL, SQL Server) with their specific syntax and data types.
* **More Sophisticated Constraint Inference:** Explore inferring other constraints like NOT NULL or UNIQUE based on the data.
* **Documentation and Examples:** Add more detailed documentation and examples on how to use the script and its options.