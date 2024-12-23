      <!-- STUDENT GRADE TRACKER -->

A command line application to manage and track studets's grades using SQLite.


# Features
1. Add, view, and update student records (ID, name, and grades).
2. Stores data in an SQLite database for persistence.
3. Simple and intuitive CLI interface.

# Running the Application
Launch the CLI:
python lib/cli.py

Follow the prompts to:
Add new students
View the list of students
Update student grades

# Project Structure
lib/db/: Database setup and seed data.
lib/cli.py: Command-line interface.
students.db: SQLite database file.

# Requirments
python 3.8+
SQLite 3

# Database Information
All data is stored in an SQLite database file named students.db, which is created automatically if it doesn't already exist. You can inspect this file using any SQLite viewer or by using the command-line tool sqlite3.

# Contribution Guidelines
We welcome contributions to enhance this project! Here’s how you can contribute:

Fork the repository.
Create a new branch for your features.