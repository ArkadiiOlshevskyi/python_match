def process_data(data):
    match data:
        case {"type": "csv", "filename": filename}:
            return process_csv(filename)
        case {"type": "json", "filename": filename}:
            return process_json(filename)
        case {"type": "database", "connection": connection}:
            return process_database(connection)
        case _:
            raise ValueError("Unknown data type")

def process_csv(filename):
    print(f"Processing CSV file: {filename}")
    # ... process CSV file ...

def process_json(filename):
    print(f"Processing JSON file: {filename}")
    # ... process JSON file ...

def process_database(connection):
    print(f"Processing database connection: {connection}")
    # ... process database connection ...

# Example usage
data1 = {"type": "csv", "filename": "data.csv"}
process_function1 = process_data(data1)
process_function1()

data2 = {"type": "json", "filename": "data.json"}
process_function2 = process_data(data2)
process_function2()

data3 = {"type": "database", "connection": "db_connection"}
process_function3 = process_data(data3)
process_function3()
