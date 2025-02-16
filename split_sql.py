import re

def split_sql_file(input_file, output_prefix, tables_per_file):
    with open(input_file, 'r') as file:
        sql_content = file.read()

    # Use regex to find all CREATE TABLE statements
    create_table_pattern = re.compile(r'CREATE TABLE.*?;', re.DOTALL)
    tables = create_table_pattern.findall(sql_content)

    # Split the tables into chunks
    for i in range(0, len(tables), tables_per_file):
        chunk = tables[i:i + tables_per_file]
        output_file = f"{output_prefix}_part_{i // tables_per_file + 1}.sql"
        
        with open(output_file, 'w') as out_file:
            out_file.write('\n\n'.join(chunk))

        print(f"Created {output_file} with {len(chunk)} tables.")

if __name__ == "__main__":
    input_file = input("Enter the path to the SQL file: ")
    output_prefix = input("Enter the prefix for output files: ")
    tables_per_file = int(input("Enter the number of tables per file: "))

    split_sql_file(input_file, output_prefix, tables_per_file)
