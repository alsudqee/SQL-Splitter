
# SQL Splitter

A simple Python-based tool that splits a large SQL file containing `CREATE TABLE` statements into smaller files, each containing a specified number of tables. The tool is designed to be easy to use and is suitable for scenarios where large SQL dump files need to be split for easier management and processing.

## Features
- Reads a single SQL file containing `CREATE TABLE` statements.
- Splits the SQL content into multiple output files, each containing a user-defined number of tables.
- Saves each chunk as a new `.sql` file, with an output file name that includes a part number.

## Installation

To use this tool, you'll need Python 3.x installed on your system. It can be run locally.

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/SQL-Splitter.git
   cd SQL-Splitter
   ```

## Dependencies
The script doesn't require any external dependencies other than Python's built-in `re` module for regular expressions. Ensure you have Python 3.x installed.

## Running the Script Locally
To use the tool locally, simply run the Python script with the following command:
```bash
python split_sql.py
```

## Usage

### Locally:
Run the script by entering the following command in your terminal or command prompt:
```bash
python split_sql.py
```

The script will prompt you to enter:
- The path to the SQL file you want to split.
- A prefix for the output files.
- The number of tables each output file should contain.
