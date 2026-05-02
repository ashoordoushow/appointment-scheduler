from datetime import datetime


class Appointment:
    def __init__(self, client_name, start_time, end_time):
        self.client_name = client_name
        self.start_time = start_time
        self.end_time = end_time

        if end_time <= start_time:
            raise ValueError("End time must be after start time.")


existing_appointments = [
    Appointment("Alice", datetime(2026, 5, 1, 9, 0), datetime(2026, 5, 1, 10, 0)),
    Appointment("Bob", datetime(2026, 5, 1, 11, 0), datetime(2026, 5, 1, 11, 30)),
]

print("Appointment scheduler loaded successfully.")