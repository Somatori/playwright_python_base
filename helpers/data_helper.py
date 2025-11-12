import random
import datetime
import uuid
from model.employee import Employee

# Centralized departments list as a tuple
DEPARTMENTS = (
    "Engineering",
    "QA",
    "Sales",
    "Marketing",
    "HR",
    "Finance",
    "Operations",
    "Support",
)

def _timestamp_str() -> str:
    """
    e.g. "20251111153045" (UTC, seconds precision).
    """
    now = datetime.datetime.now(datetime.timezone.utc)
    return now.strftime("%Y%m%d%H%M%S")  # seconds precision

def generate_random_employee() -> Employee:
    """
    Create an Employee with random and unique data
    """
    ts = _timestamp_str()
    first_name = f"Forename_{ts}"
    last_name = "Test"
    email = f"{ts}@example.com"
    age = str(random.randint(18, 90))
    salary = str(random.randint(50000, 100000))
    department = random.choice(DEPARTMENTS)
    return Employee(
        first_name=first_name,
        last_name=last_name,
        email=email,
        age=age,
        salary=salary,
        department=department,
    )
