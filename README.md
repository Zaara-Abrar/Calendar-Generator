# 📅 Calendar Generator

A Python application that generates a complete calendar for any year, past or future, right in your console.

## Overview

Ever wondered what day of the week a particular date falls on, or wanted to see the full calendar of a year gone by or one still to come? This project takes a year as input and produces a clear, month-by-month calendar. It demonstrates core Python concepts such as loops, conditionals, functions, date calculations, and formatted output.

## Features

- **Any year supported:** generate calendars for past, present, and future years.
- **Accurate dates:** handles leap years and varying month lengths correctly.
- **Clean layout:** displays each month in an easy-to-read grid with days of the week.
- **Efficient logic:** works for any year without hard-coded values.
- **Simple console interface:** just enter a year and view the calendar.

## Tech Stack

- **Language:** Python 3
- **Modules:** `random` module

## Getting Started

### Prerequisites

- Python 3.x installed on your system ([download here](https://www.python.org/downloads/))

### Installation & Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/Zaara-Abrar/<your-repo-name>.git
   ```
2. Navigate to the project folder:
   ```bash
   cd <your-repo-name>
   ```
3. Run the program:
   ```bash
   python main.py
   ```

> Replace `<your-repo-name>` and `main.py` with your actual repository and file names.

## How It Works

1. The program asks you to enter a **year**.
2. It determines whether the year is a **leap year** to set the number of days in February.
3. It calculates which **day of the week** each month starts on.
4. It prints every month in a **grid layout**, aligned under the days of the week.

## Example

```
Enter a year: 2026

        January 2026
Mo Tu We Th Fr Sa Su
             1  2  3  4
 5  6  7  8  9 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 28 29 30 31
...
```

> Replace the sample output above with the real output or a screenshot from your program.

## Future Improvements

- Highlight the current date
- Add support for holidays and important events
- Allow users to generate the calendar for a single month
- Export the calendar to a text or PDF file
- Build a graphical interface (GUI) version

## Author

**Zaara Abrar**
- GitHub: [Zaara-Abrar](https://github.com/Zaara-Abrar)
- LinkedIn: [zaara-abrar](https://linkedin.com/in/zaara-abrar-091186259)
