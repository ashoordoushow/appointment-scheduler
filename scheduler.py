from datetime import datetime


class Appointment:
    def __init__(self, client_name, start_time, end_time):
        self.client_name = client_name
        self.start_time = start_time
        self.end_time = end_time

        if end_time <= start_time:
            raise ValueError("End time must be after start time.")


def can_schedule_appointment(requested_appointment, existing_appointments):
    for appointment in existing_appointments:
        overlaps = (
            requested_appointment.start_time < appointment.end_time
            and requested_appointment.end_time > appointment.start_time
        )

        if overlaps:
            return False

    return True


existing_appointments = [
    Appointment("Alice", datetime(2026, 5, 1, 9, 0), datetime(2026, 5, 1, 10, 0)),
    Appointment("Bob", datetime(2026, 5, 1, 11, 0), datetime(2026, 5, 1, 11, 30)),
]

requested_appointment = Appointment(
    "Dana",
    datetime(2026, 5, 1, 9, 30),
    datetime(2026, 5, 1, 10, 30)
)

result = can_schedule_appointment(requested_appointment, existing_appointments)

print(result)