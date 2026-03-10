def crisis_protocols(file_name) -> None:
    try:
        with open(file_name, "r") as file:
            print(f"ROUTINE ACCESS: Attempting access to '{file_name}'...")
            print(f"SUCCESS: Archive recovered - ''{file.read()}''")
            print("STATUS: Normal operations resumed\n")
    except FileNotFoundError:
        print(f"CRISIS ALERT: Attempting access to '{file_name}'")
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, security maintained\n")
    except PermissionError:
        print(f"CRISIS ALERT: Attempting access to '{file_name}'")
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained\n")
    except Exception as e:
        print(f"CRISIS ALERT: Attempting access to '{file_name}'")
        print(f"RESPONSE: Non registered error detected: {e}")
        print("STATUS: Crisis handled, security maintained\n")


def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    crisis_protocols("lost_archive.txt")
    crisis_protocols("classified_vault.txt")
    crisis_protocols("standard_archive.txt")
    print("\nAll crisis scenarios handled successfuly. Archives secure.")


if __name__ == "__main__":
    main()
