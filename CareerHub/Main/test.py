import pyodbc

def test_connection():
    server = 'HP-15EF2XXX'  # Your SQL Server instance
    database = 'CareerHub'   # Your Database Name

    try:
        connection = pyodbc.connect(
            f'DRIVER={{ODBC Driver 17 for SQL Server}};'
            f'SERVER={server};'
            f'DATABASE={database};'
            f'Trusted_Connection=yes;'  # This enables Windows Authentication
        )
        print("Database connected successfully!")
        connection.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_connection()
