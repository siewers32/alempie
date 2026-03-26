from sqlmodel import SQLModel
# BELANGRIJK: Importeer hier je eigen modellenbestand
# Pas 'app.models' aan naar jouw eigen pad/bestandsnaam
try:
    from alempie.models import * 
    print("✅ Modellen succesvol geïmporteerd.")
except ImportError as e:
    print(f"❌ Fout bij importeren van modellen: {e}")

def check_metadata():
    tables = SQLModel.metadata.tables.keys()
    
    print("\n--- Metadata Check ---")
    if not tables:
        print("⚠️  De metadata is LEEG. SQLModel ziet geen tabellen.")
        print("Oplossing: Zorg dat je modellen 'table=True' hebben en dat ze ")
        print("geïmporteerd worden vóórdat je de metadata uitleest.")
    else:
        print(f"Gevonden tabellen ({len(tables)}):")
        for table in tables:
            print(f" - {table}")
    print("----------------------\n")

if __name__ == "__main__":
    check_metadata()