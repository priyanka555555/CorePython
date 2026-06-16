import pickle
import os

class Contact:
    """Represents a contact with a name and email."""
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        """Returns a string representation for printing."""
        return f"Contact: {self.name} <{self.email}>"

class ContactManager:
    """Manages contacts using pickle for data persistence."""
    def __init__(self, filename="contacts.pkl"):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        """Loads contacts from the file using pickle."""
        if os.path.exists(self.filename):
            try:
                # Open in binary read mode ('rb')
                with open(self.filename, "rb") as file:
                    return pickle.load(file)
            except (IOError, pickle.UnpicklingError) as e:
                print(f"Error loading data: {e}. Starting with an empty list.")
                return []
        return []

    def save_contacts(self):
        """Saves current contacts to the file using pickle."""
        try:
            # Open in binary write mode ('wb')
            with open(self.filename, "wb") as file:
                pickle.dump(self.contacts, file)
            print("Contacts saved successfully!")
        except IOError as e:
            print(f"Error saving contacts: {e}")

    def add_contact(self, contact):
        """Adds a new contact to the list and saves."""
        self.contacts.append(contact)
        self.save_contacts()

    def view_contacts(self):
        """Displays all stored contacts."""
        if not self.contacts:
            print("\nNo contacts found.")
        else:
            print("\n--- My Contacts ---")
            for contact in self.contacts:
                print(contact)
            print("-------------------")

# --- Example Usage ---
if __name__ == "__main__":
    manager = ContactManager()

    # Add some sample contacts (if not already loaded)
    if not manager.contacts:
        manager.add_contact(Contact("John Doe", "john@example.com"))
        manager.add_contact(Contact("Jane Smith", "jane@example.com"))

    # View all contacts
    manager.view_contacts()

    """
    import pickle

# The Python object to be pickled
data = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}

# Pickling (serializing) the data to a file
with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)
print("Data pickled and saved to data.pkl")

# Unpickling (deserializing) the data from the file
with open('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)

print("Data unpickled:")
print(loaded_data)

    """
