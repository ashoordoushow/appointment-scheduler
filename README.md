# Appointment Scheduler

This is a simple Python program that checks whether a requested appointment can be added to an existing schedule.

## How to Run

Make sure you have Python 3 installed.

Then run:

python3 scheduler.py

## What It Does

Each appointment includes:

- a client name
- a start time
- an end time

I used a Python class to represent each appointment.

The program compares a requested appointment against a list of existing appointments to see if there are any conflicts.

If the requested appointment overlaps with an existing one, it will return that it is not available and show which appointment it conflicts with.

If there is no overlap, the appointment can be scheduled.

## Example Output

--- Test Case 1: Conflicting Appointment ---
Requested appointment: Dana, May 1 from 9:30 AM to 10:30 AM  
Result: Not available  
Reason: Conflicts with Alice  

--- Test Case 2: Available Appointment ---
Requested appointment: Charlie, May 1 from 10:00 AM to 10:30 AM  
Result: Available  
Reason: Appointment can be scheduled  

## Notes

Back-to-back appointments are allowed. For example, if one appointment ends at 10:00 AM, another can start at 10:00 AM.

I used Python’s built-in datetime module to handle and compare times.