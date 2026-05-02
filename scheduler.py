from datetime import datetime


class Appointment:
    def __init__(self, client_name, start_time, end_time):
        self.client_name = client_name
        self.start_time = start_time
        self.end_time = end_time

        if end_time <= start_time:
            raise ValueError("End time must be after start time.")

    def formatted_time(self):
        start = self.start_time.strftime("%B %-d from %-I:%M %p")
        end = self.end_time.strftime("%-I:%M %p")
        return f"{self.client_name}, {start} to {end}"


def can_schedule_appointment(requested_appointment, existing_appointments):
    for appointment in existing_appointments:
        overlaps = (
            requested_appointment.start_time < appointment.end_time
            and requested_appointment.end_time > appointment.start_time
        )

        if overlaps:
            return {
                "available": False,
                "reason": f"Conflicts with {appointment.client_name}"
            }

    return {
        "available": True,
        "reason": "Appointment can be scheduled"
    }


def print_result(requested_appointment, result):
    print(f"Requested appointment: {requested_appointment.formatted_time()}")

    if result["available"]:
        print("Result: Available")
    else:
        print("Result: Not available")

    print(f"Reason: {result['reason']}")


existing_appointments = [
    Appointment("Alice", datetime(2026, 5, 1, 9, 0), datetime(2026, 5, 1, 10, 0)),
    Appointment("Bob", datetime(2026, 5, 1, 11, 0), datetime(2026, 5, 1, 11, 30)),
]


print("\n--- Test Case 1: Conflicting Appointment ---")

requested_appointment_1 = Appointment(
    "Dana",
    datetime(2026, 5, 1, 9, 30),
    datetime(2026, 5, 1, 10, 30)
)

result_1 = can_schedule_appointment(requested_appointment_1, existing_appointments)
print_result(requested_appointment_1, result_1)


print("\n--- Test Case 2: Available Appointment ---")

requested_appointment_2 = Appointment(
    "Charlie",
    datetime(2026, 5, 1, 10, 0),
    datetime(2026, 5, 1, 10, 30)
)

result_2 = can_schedule_appointment(requested_appointment_2, existing_appointments)
print_result(requested_appointment_2, result_2)