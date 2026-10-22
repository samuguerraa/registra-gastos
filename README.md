# Registra-gastos

A Python-based personal expense tracker developed incrementally as a learning project.

## About

Registra-gastos is a console-based application for recording and managing personal expenses.

The project is being developed incrementally, with each version introducing new functionality while reinforcing Python programming fundamentals, data structures, input validation, testing, and software development practices.

## Current version

**v1.5.4**

### Features

- Register expenses with an automatic registration date
- Predefined expense categories
- Expense descriptions with input validation
- COP value validation
- Display registered expenses
- Calculate total expenses
- Edit existing expenses
- Delete expenses with confirmation
- Search expenses by category
- Search expenses by description
- Search expenses by date:
  - Exact date
  - After a specified date
  - Before a specified date
  - Between two dates, including both endpoints
- Input validation and error handling

## Testing

The project includes automated regression tests for date-based expense searches.

The test suite uses a simulated system date to create reproducible test data without modifying the production code.

### Run the tests

From the repository root, run:

```bash
python3 tests/test_fechas_mock_1.5.4.py
```

The test suite checks exact-date searches, strict before/after comparisons, inclusive date intervals, boundary conditions, and searches with no matching expenses.

It also verifies that the test data is correctly prepared and compares the actual search results against the expected expenses.

## Technologies

- Python
- Git
- GitHub

## Project roadmap

- [x] v1.0 — Basic expense registration
- [x] v1.1 — Input validation and menu improvements
- [x] v1.2 — Category and description improvements
- [x] v1.3 — Monetary value validation
- [x] v1.4 — Automatic expense dates
- [x] v1.5 — Expense editing, deletion, and search functionality
- [ ] v1.5.x — Search usability improvements and additional features
- [ ] v2.0 — Data persistence
- [ ] Future — Data analysis and visualization
- [ ] Future — Graphical user interface

## Purpose

This project is primarily a learning and portfolio project focused on improving Python programming, data structures, input validation, automated testing, Git, and software development practices.