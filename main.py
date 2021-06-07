from src.database_connection import Database, User
import src.upload_data
import src.database_schema


def show_databases(db):
    all_databases = "SELECT datname FROM pg_database WHERE datistemplate = false;"
    db.cursor.execute(all_databases)
    print(f"All databases: {db.cursor.fetchall()}")

    current_database = "SELECT current_database()"
    db.cursor.execute(current_database)
    print(f"Current database: {db.cursor.fetchall()[0]}")


if __name__ == '__main__':
    user = User(host="localhost", name="postgres", password="********", database="postgres")
    db = Database(user)

    try:
        db.cursor.execute("CREATE DATABASE olist;")
    except Exception as db_already_exists:
        print("Note:", db_already_exists)

    db.use_database("olist")

    show_databases(db)

    # src.database_schema.make_schema(db)
    # src.upload_data.upload_csv(db)