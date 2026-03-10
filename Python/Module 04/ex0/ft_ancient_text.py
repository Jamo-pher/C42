print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")

try:
    file = open("ancient_fragment.txt")
except Exception:
    file = None
if not file:
    print("ERROR: Storage vault not found. Run data generator first.")
else:
    print(f"Accessing Storage Vault: {file.name}")
    print("Connection established...\n")
    print("RECOVERED DATA:")

    print(file.read())

    print("\nData recovery complete. Storage unit disconnected")
    file.close()
