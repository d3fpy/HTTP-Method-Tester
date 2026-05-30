# HTTP Method Tester

A simple educational project demonstrating how `Flask` (server) and `Requests` (client) interact using different HTTP methods (`GET`, `POST`, `DELETE`).

## Features
* **Flask Server**: Detects incoming request methods and returns text confirmation.
* **Client Script**: Sends a loop of automated requests and prints formatted responses.

## Quick Start

### 1. Install dependencies
```bash
pip install flask requests
```

### 2. Run the Server
Start your Flask application file:
```bash
python server.py
```

### 3. Run the Client
Update `BASE_URL` inside `main.py` with your server address (e.g., `http://127.0.0.1:5000`) and run:
```bash
python main.py
```

## Expected Output
```text
DELETE Request ✓
GET Request ✓
POST Request ✓
```
