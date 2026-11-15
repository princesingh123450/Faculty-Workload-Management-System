from datetime import datetime
from typing import Dict

# Employee leave balances (in days)
employees: Dict[str, Dict[str, int]] = {
    "E101": {
        "Casual": 12,
        "Sick": 10,
        "Earned": 15,
    }
}

DATE_FORMAT = "%Y-%m-%d"


def parse_date(date_text: str) -> datetime:
    """Parse a date in YYYY-MM-DD format."""
    try:
        return datetime.strptime(date_text, DATE_FORMAT)
    except ValueError as exc:
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.") from exc


def calculate_leave_days(from_date: str, to_date: str) -> int:
    """Return inclusive leave days after validating the date range."""
    start = parse_date(from_date)
    end = parse_date(to_date)

    if end < start:
        raise ValueError("Invalid dates. To-date cannot be before from-date.")

    return (end - start).days + 1


def view_balance(employee_id: str) -> None:
    """Display all leave balances for an employee."""
    if employee_id not in employees:
        print("Employee ID not found.")
        return

    balance = employees[employee_id]
    print(
        f"Balance: Casual {balance['Casual']} | "
        f"Sick {balance['Sick']} | Earned {balance['Earned']}"
    )


def apply_leave(employee_id: str, leave_type: str, from_date: str, to_date: str) -> None:
    """Validate and process an employee leave request."""
    if employee_id not in employees:
        print("Employee ID not found.")
        return

    # Match leave type without requiring exact capitalization.
    normalized_type = leave_type.strip().title()
    if normalized_type not in employees[employee_id]:
        print("Invalid leave type. Choose Casual, Sick, or Earned.")
        return

    try:
        days = calculate_leave_days(from_date, to_date)
    except ValueError as exc:
        print(str(exc))
        return

    balance = employees[employee_id][normalized_type]
    if days > balance:
        print(
            f"Leave rejected. Requested: {days} days | "
            f"Available: {balance} days {normalized_type}"
        )
        return

    employees[employee_id][normalized_type] -= days
    remaining = employees[employee_id][normalized_type]
    print(
        f"Leave approved: {days} days {normalized_type} | "
        f"Balance {normalized_type}: {remaining}"
    )


def get_non_empty_input(prompt: str) -> str:
    """Read input and reject blank values."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty. Please try again.")


def main() -> None:
    """Run the console menu."""
    while True:
        print("\n=== Employee Leave Management System ===")
        print("1. Apply for leave")
        print("2. View leave balance")
        print("3. Exit")

        choice = input("Enter menu option (1-3): ").strip()

        if choice == "1":
            employee_id = get_non_empty_input("Employee ID: ").upper()
            leave_type = get_non_empty_input("Leave type (Casual/Sick/Earned): ")
            from_date = get_non_empty_input("From date (YYYY-MM-DD): ")
            to_date = get_non_empty_input("To date (YYYY-MM-DD): ")
            apply_leave(employee_id, leave_type, from_date, to_date)
        elif choice == "2":
            employee_id = get_non_empty_input("Employee ID: ").upper()
            view_balance(employee_id)
        elif choice == "3":
            print("Thank you for using the Employee Leave Management System.")
            break
        else:
            print("Invalid menu option. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
