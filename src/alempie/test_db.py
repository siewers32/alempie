from alempie.database_old import engine
from sqlmodel import select, Session
from alempie.models import Department # Zorg dat dit pad klopt

def test_connection():
    try:
        with Session(engine) as session:
            # Probeer gewoon 1 record op te halen
            statement = select(Department).limit(1)
            session.exec(statement).first()
            print("✅ Database connectie succesvol!")
    except Exception as e:
        print(f"❌ Database fout: {e}")

if __name__ == "__main__":
    test_connection()