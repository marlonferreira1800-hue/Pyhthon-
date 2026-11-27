"""Module 3 — Chapter 14: Dictionaries (dict).

Demonstrates multi-line formatting for readability, nested list values,
len(), .get(), .keys(), .values(), .items(), updating values, and adding keys.
"""


def create_and_update_person() -> dict:
    """Build a person profile dictionary and demonstrate common operations."""
    # Breaking lines after each comma keeps larger dictionaries readable
    person = {
        "name": "Fernando",
        "age": 43,
        "profession": "Programmer",
        "education": ["Systems Analysis", "Python"],
    }

    initial_key_count = len(person)

    # Safe lookup with .get() avoids KeyError on missing keys
    phone = person.get("phone", "Not provided")
    safe_name = person.get("name")

    # Updating an existing key
    person["age"] = 44

    # Appending to a list stored inside the dictionary
    person["education"].append("Data Science")

    # Adding a brand-new key dynamically
    person["city"] = "Curitiba"

    return {
        "person": person,
        "initial_key_count": initial_key_count,
        "final_key_count": len(person),
        "phone": phone,
        "safe_name": safe_name,
        "keys": list(person.keys()),
        "values": list(person.values()),
        "items": list(person.items()),
    }


def main() -> None:
    """Run Chapter 14 demonstration."""
    result = create_and_update_person()
    print("=== CH. 14: DICTIONARIES ===")
    for key, value in result["person"].items():
        print(f"  {key}: {value}")
    print("Phone (.get):", result["phone"])
    print("Total keys:", result["final_key_count"])


if __name__ == "__main__":
    main()
