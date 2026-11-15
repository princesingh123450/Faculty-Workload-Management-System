# Employee Leave Management System

A beginner-friendly Python console project for managing employee leave requests.

## Features

- Apply for Casual, Sick, or Earned leave.
- Calculates leave duration inclusively (both start and end dates count).
- Validates date format (`YYYY-MM-DD`) and date order.
- Approves a request only when the employee has enough leave balance.
- Rejects requests when the requested days exceed the available balance.
- Displays an employee's current leave balance.
- Stores employee data in a nested Python dictionary.

## Default employee

| Employee ID | Casual | Sick | Earned |
|---|---:|---:|---:|
| E101 | 12 days | 10 days | 15 days |

Balances are held in memory while the program runs. They reset to the default values when the program is restarted.

## Requirements

- Python 3.9 or later
- No third-party packages required

## Run in Visual Studio Code

1. Extract the ZIP file.
2. Open the extracted `employee_leave_management_system` folder in VS Code.
3. Open `main.py`.
4. Open **Terminal → New Terminal**.
5. Run:

   ```bash
   python main.py
   ```

   If that command is not recognized on Windows, try:

   ```bash
   py main.py
   ```

6. Follow the menu displayed in the terminal.

## Example test cases

### Test 1: Normal input
- Menu option: `1`
- Employee ID: `E101`
- Leave type: `Casual`
- From date: `2026-12-10`
- To date: `2026-12-12`

Expected output (when starting with the default balance):

```text
Leave approved: 3 days Casual | Balance Casual: 9
```

### Test 2: Minimum/boundary balance
- Menu option: `1`
- Employee ID: `E101`
- Leave type: `Casual`
- From date: `2026-11-02`
- To date: `2026-11-13`

Expected output (when starting with the default balance):

```text
Leave approved: 12 days Casual | Balance Casual: 0
```

### Test 3: Invalid date order
- Menu option: `1`
- Employee ID: `E101`
- Leave type: `Sick`
- From date: `2026-12-15`
- To date: `2026-12-10`

Expected output:

```text
Invalid dates. To-date cannot be before from-date.
```

### Test 4(a): Insufficient leave balance
- Menu option: `1`
- Employee ID: `E101`
- Leave type: `Casual`
- From date: `2027-01-01`
- To date: `2027-01-14`

Expected output (when starting with the default balance):

```text
Leave rejected. Requested: 14 days | Available: 12 days Casual
```

### Test 4(b): View balance
- Menu option: `2`
- Employee ID: `E101`

Expected output (before any leave is taken):

```text
Balance: Casual 12 | Sick 10 | Earned 15
```

**Important:** Run each test from a fresh program start if you want the original default balances.

## GitHub upload

1. Sign in to GitHub and create a new repository, for example `employee-leave-management-system`.
2. Extract this ZIP file.
3. Upload `main.py` and `README.md` (or use Git from the VS Code terminal).
4. Add a short repository description, such as: `Python console app for employee leave requests and leave balance management`.

## Project structure

```text
employee_leave_management_system/
├── main.py
└── README.md
```
