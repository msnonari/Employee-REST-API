import sqlite3

DATABASE = "EmpData.db"

def connect_db():
    """Connect to the SQLite database and return the connection object."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def get_all_emp():
    """Retrieve all employees from the database."""
    try:
        with connect_db() as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM Employee")
            rows = cur.fetchall()
        result = [dict(row) for row in rows]
        return result
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []

def get_emp_by_id(emp_id):
    """Retrieve an employee by their ID."""
    try:
        with connect_db() as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM Employee WHERE employee_id = ?", (emp_id,))
            row = cur.fetchone()
        return dict(row) if row else None
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None

def create_emp(employee):
    """Create a new employee in the database."""
    try:
        with connect_db() as conn:
            cur = conn.cursor()
            val = tuple(employee.values())
            sql = """INSERT INTO Employee (first_name, last_name, age, email, gender, job_title, department, salary, hire_date)
                     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"""
            cur.execute(sql, val)
            conn.commit()
            rowid = cur.lastrowid
        return rowid
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None

def update_emp(first_name, last_name, age, department, emp_id):
    """Update an existing employee's details."""
    try:
        with connect_db() as conn:
            cur = conn.cursor()
            val = (first_name, last_name, age, department, emp_id)
            sql = """UPDATE Employee SET first_name = ?, last_name = ?, age = ?, department = ?
                     WHERE employee_id = ?"""
            cur.execute(sql, val)
            conn.commit()
            rcount = cur.rowcount
        return rcount
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return 0

def delete_emp(emp_id):
    """Delete an employee from the database."""
    try:
        with connect_db() as conn:
            cur = conn.cursor()
            cur.execute("DELETE FROM Employee WHERE employee_id = ?", (emp_id,))
            conn.commit()
            rcount = cur.rowcount
        return rcount
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return 0