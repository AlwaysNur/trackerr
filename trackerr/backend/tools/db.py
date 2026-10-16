import os
import sqlite3
from datetime import datetime
from .logging import log
import uuid
db_path = os.path.join(os.path.dirname(__file__), '../../../data/trackerr.db')

def init_db():
    try:
        os.mkdir(os.path.join(os.path.dirname(__file__), '../../../data/'),)
    except FileExistsError:
        log("data directory already exists, skipping creation")
    conn = sqlite3.connect(os.path.join(os.path.dirname(__file__), '../../../data/trackerr.db'))
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS packages (
            tracking_number TEXT PRIMARY KEY,
            description TEXT,
            id TEXT,
            carrier TEXT DEFAULT 'NZ Post',
            status TEXT DEFAULT 'Added',
            last_updated DATETIME,
            date_added DATETIME
        )
    ''')
    conn.commit()
    conn.close()

def add_package(tracking_number, description):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    id = str(uuid.uuid4)

    try:
        cursor.execute('''
            INSERT INTO packages (tracking_number, description, id, last_updated, date_added)
            VALUES (?, ?, ?, ?, ?)
        ''', (tracking_number, description, id, now, now))
        conn.commit()

        log(f'Added {tracking_number} to db')
        
    except sqlite3.IntegrityError:
        log(f"{tracking_number} already exists in db")
    finally:
        conn.close()

def update_status(tracking_number, new_status):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    cursor.execute('''
        UPDATE packages 
        SET status = ?, last_updated = ? 
        WHERE tracking_number = ?
    ''', (new_status, now, tracking_number))
    
    conn.commit()
    conn.close()

def show_packages():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute("SELECT tracking_number, description, status FROM packages")
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_package(package_id: str):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("""
    DELETE FROM users WHERE id = {package_id};
    """)
    conn.close()


# --- Example Usage ---
# add_package("EE123456789NZ", "New mechanical keyboard")
# update_status("EE123456789NZ", "In Transit")
# show_active_packages()


