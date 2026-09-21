import sqlite3
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "data" / "mc_match.db"

def get_db_connection():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    return conn

def load_motorcycles_from_db() -> pd.DataFrame:
    conn = get_db_connection()
    try:
        df = pd.read_sql_query("SELECT * FROM motorcycles", conn)
        return df
    except Exception as e:
        print(f"Error loading motorcycles from database: {e}")
        return pd.DataFrame()
    finally:
        conn.close()

def update_motorcycle(motorcycle_id: int, column_name: str, new_value: str) -> bool:
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        query = f"UPDATE motorcyles SET `{column_name}` = ? WHERE id = ?"
        cursor.execute(query, (new_value, motorcycle_id))
        conn.commit()
        return cursor.rowcount > 0
    except Exception as e:
        print(f"Error updating column {column_name}: {e}")
        return False
    finally:
        conn.close()

def initialize_database():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS motorcycles (
            `id` INTEGER PRIMARY KEY AUTOINCREMENT,
            `Company` CHAR(45),
            `Country of Origin` CHAR(45),
            `Model` CHAR(45),
            `Number of cc` REAL,
            `Horsepower` REAL,
            `Torque` REAL,
            `Transmission Type` CHAR(45),
            `Drivetrain` CHAR(45),
            `Number of Seating` INT,
            `Year` INT,
            `Looks` CHAR(45),
            `Body Type` CHAR(45),
            `Engine Type` CHAR(45),
            `Number of Cylinders` INT,
            `Price (SEK)` REAL,
            `Usage Type` CHAR(45)
        )
    ''')
    conn.commit()
    conn.close()
    