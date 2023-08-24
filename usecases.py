# Parsing and Validating User Input:

def process_command(args):
    match args:
        case ["create", name, size]:
            create_file(name, size)
        case ["delete", name]:
            delete_file(name)
        case _:
            print("Invalid command")


# Handling API Responses:

def handle_response(response):
    match response:
        case {"status": "success", "data": data}:
            process_data(data)
        case {"status": "error", "message": msg}:
            log_error(msg)
        case _:
            log_error("Unexpected response")


# Tokenizing and Parsing Text:

def parse_expression(tokens):
    match tokens:
        case [number] if isinstance(number, int):
            return number
        case ["(", expr, "+", expr, ")"]:
            return parse_expression(expr[0]) + parse_expression(expr[1])
        case _:
            raise ValueError("Invalid expression")


# Implementing Finite State Machines:

class TrafficLight:
    def __init__(self):
        self.state = "red"

    def transition(self, event):
        match (self.state, event):
            case ("red", "timer_expired"):
                self.state = "green"
            case ("green", "timer_expired"):
                self.state = "yellow"
            case ("yellow", "timer_expired"):
                self.state = "red"
            case _:
                print("Invalid transition")

light = TrafficLight()
light.transition("timer_expired")  # Transition to the next state


# Processing Data Records:

def process_record(record):
    match record:
        case {"type": "student", "name": name, "age": age}:
            enroll_student(name, age)
        case {"type": "teacher", "name": name, "subject": subject}:
            hire_teacher(name, subject)
        case _:
            print("Unknown record type")

# Data Quality Monitoring:

def monitor_data_quality(data):
    issues = []
    for record in data:
        match record:
            case {"id": id, "value": value} if value > 1000:
                # Flag high-value records for review
                issues.append(f"High value in record {id}")
            case {"id": id, "timestamp": timestamp} if timestamp is None:
                # Flag missing timestamp records
                issues.append(f"Missing timestamp in record {id}")
            case _:
                # No quality issue with this record
                pass
    return issues


#  Event Stream Processing:

def process_event(event):
    match event:
        case {"type": "click", "user_id": user, "timestamp": time}:
            log_click(user, time)
        case {"type": "purchase", "user_id": user, "amount": amount}:
            process_purchase(user, amount)
        case {"type": "login_attempt", "user_id": user, "success": False}:
            alert_security_team(user)
        case _:
            # Ignore other types of events
            pass


# ETL Process Handling:

def process_data_source(data, source_type):
    match source_type:
        case "csv":
            return process_csv(data)
        case "json":
            return process_json(data)
        case "database":
            return process_database(data)
        case _:
            raise ValueError("Unknown data source type")


# Data Cleaning and Transformation:

def clean_data(data):
    cleaned_data = []
    for record in data:
        match record:
            case {"name": name, "age": age} if age < 0:
                # Handle negative age anomaly
                record["age"] = abs(age)
            case {"name": name, "age": None}:
                # Handle missing age anomaly
                record["age"] = estimate_age(name)
            case _:
                # No anomaly, keep the record as is
                cleaned_data.append(record)
    return cleaned_data
