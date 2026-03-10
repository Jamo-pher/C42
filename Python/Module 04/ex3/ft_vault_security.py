print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

print("Initiating secure vault access...")

try:
    with open("classified_data.txt", "r") as vault:
        print("Vault connection established with failsafe protocols\n")
        print("SECURE EXTRACTION:")
        print(vault.read())

except FileNotFoundError:
    print("ERROR: Vault not found.")

with open("security_protocols.txt", "a") as vault2:
    print("\nSECURE PRESERVATION:")
    vault2.write("\n[CLASSIFIED] New security protocols archived\n")
    print("[CLASSIFIED] New security protocols archived\n")

print("Vault automatically sealed upon completion\n")
print("All vault operations completed with maximum security.")
