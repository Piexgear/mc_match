import pandas as pd
from data.database import get_db_connection, initialize_database
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
DATA_PATH = BASE_DIR / "dataset" / "motorcycles_clean.csv"

def migrate_data():
    df = pd.read_csv(DATA_PATH)
    # Ensure the database is initialized
    if initialize_database():
        conn = get_db_connection()
        try:
            # Using dataframe's columns to insert data
            df.to_sql("motorcycles", conn, if_exists="append", index=False)
            print("Migration successful!")
        except Exception as e:
            print(f"Error during migration: {e}")
        finally:
            conn.close()

if __name__ == "__main__":
    migrate_data()
