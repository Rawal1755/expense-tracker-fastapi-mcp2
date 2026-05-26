from backend_api.database.connection import init_db


if __name__ == "__main__":
    init_db()
    print("Backend API database tables created successfully.")