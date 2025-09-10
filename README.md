# Idle Hero TD API

This is a backend API for Idle Hero TD, providing endpoints and an admin interface for managing heroes, synergies, and bonuses.

## Features
- Displaying of heroes and level up stats
- Displaying of heroes and synergies

## Getting Started

### Prerequisites
- Python 3.12+
- Flask (and other dependencies listed in your requirements)

### Setup
1. **Clone the repository**
2. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```
3. **Seed the database**
   Before running the app, you must seed the database with initial data:
   ```
   python db_setup.py
   ```
   This will populate `idleherotd.db` with the required tables and data from data.py

4. **Run the app**
   ```
   python app.py
   ```
   The app will start on `http://127.0.0.1:5000/`.

## Notes
- If you make changes to the database schema, rerun `db_setup.py` and reseed with `data.py`.
- The database file is `idleherotd.db` (in root and `instance/`).

## License
MIT
