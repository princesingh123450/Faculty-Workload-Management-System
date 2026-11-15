import unittest
from main import calculate_leave_days, employees, apply_leave
from unittest.mock import patch
from io import StringIO


class LeaveManagementTests(unittest.TestCase):
    def test_inclusive_days(self):
        self.assertEqual(calculate_leave_days("2026-12-10", "2026-12-12"), 3)

    def test_reversed_dates(self):
        with self.assertRaisesRegex(ValueError, "To-date cannot be before from-date"):
            calculate_leave_days("2026-12-15", "2026-12-10")

    def test_invalid_date_format(self):
        with self.assertRaisesRegex(ValueError, "Invalid date format"):
            calculate_leave_days("10-12-2026", "2026-12-12")

    def test_rejects_insufficient_balance(self):
        original = employees["E101"]["Casual"]
        try:
            output = StringIO()
            with patch("sys.stdout", output):
                apply_leave("E101", "Casual", "2027-01-01", "2027-01-14")
            self.assertIn("Leave rejected", output.getvalue())
            self.assertEqual(employees["E101"]["Casual"], original)
        finally:
            employees["E101"]["Casual"] = original


if __name__ == "__main__":
    unittest.main()
