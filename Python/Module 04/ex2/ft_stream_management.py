import sys


print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
id_input = input("Input Stream active: Enter archivist ID: ")
Status_input = input("Input Stream active. Enter status report: ")
print(f"\n[STANDARD] Archive status from {id_input}: {Status_input}")
sys.stderr.write("[ALERT] System diagnostic: Communication "
                 "channels verified\n")

print("[STANDARD] Data transmission complete")
print("\nThree-channel communication test successful.")
