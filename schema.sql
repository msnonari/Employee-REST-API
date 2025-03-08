CREATE TABLE Employee (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER,
    email TEXT,
    gender TEXT,
    job_title TEXT,
    department TEXT,
    salary REAL,
    hire_date TEXT
);