# My Public IP App

A Python command-line application that fetches and displays your public 
IPv4/IPv6 information using the [ipapi.co](https://ipapi.co) REST API.

Built as a team project to demonstrate REST API integration, error 
handling, unit testing, and Git collaboration.

---

## Features

- Displays your public IP address (IPv4 or IPv6)
- Shows city, region, country, timezone, and ISP
- Shows latitude and longitude
- Handles network errors gracefully
- Includes unit tests (no internet required to run tests)

---

## Requirements

- Python 3.7 or higher
- `requests` library (see install instructions below)

---

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/YOUR-USERNAME/my-public-ip-app.git
cd my-public-ip-app
```

### 2. Create and activate a virtual environment
```bash
# Mac/Linux
python -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

---

## Usage

```bash
python ip_app.py
```

### Sample Output
```
Fetching your IP information...

────────────────────────────────────────
  MY PUBLIC IP INFORMATION
────────────────────────────────────────
  IP Address : 203.0.113.42
  IP Version : IPv4
  City       : Manila
  Region     : Metro Manila
  Country    : Philippines
  Timezone   : Asia/Manila
  ISP / Org  : AS9299 Philippine Long Distance
  Latitude   : 14.5995
  Longitude  : 120.9842
────────────────────────────────────────
```

---

## Running the Tests

```bash
# Using unittest (built-in)
python -m unittest test_ip_app -v

# Using pytest
pip install pytest
python -m pytest test_ip_app.py -v
```

---

## Project Structure

```
my-public-ip-app/
├── ip_app.py          # Main application
├── test_ip_app.py     # Unit tests
├── requirements.txt   # Python dependencies
├── README.md          # This file
└── .gitignore         # Files excluded from Git
```

---

## API Reference

This app uses the free [ipapi.co](https://ipapi.co) API.
- Endpoint: `https://ipapi.co/json/`
- Returns: JSON with IP, location, timezone, and ISP data
- No API key required for basic usage

---

## Team Members

| Name | Role |
|------|------|
| [Name 1] | Scrum Leader |
| [Name 2] | Recorder |
| [Name 3] | Developer |
| [Name 4] | Developer |

---

## License

This project is for educational purposes only.
