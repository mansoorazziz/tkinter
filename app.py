import tkinter as tk

class CRUDApp:
    def __init__(self, root):
        self.root = root
        self.data = []

        # Create frame
        self.create_frame = tk.Frame(root)
        self.create_frame.pack()

        # Create entry fields
        self.name_label = tk.Label(self.create_frame, text="Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(self.create_frame)
        self.name_entry.pack()

        self.email_label = tk.Label(self.create_frame, text="Email:")
        self.email_label.pack()
        self.email_entry = tk.Entry(self.create_frame)
        self.email_entry.pack()

        # Create button
        self.create_button = tk.Button(self.create_frame, text="Create", command=self.create_data)
        self.create_button.pack()

        # Read frame
        self.read_frame = tk.Frame(root)
        self.read_frame.pack()

        # Read text box
        self.read_text = tk.Text(self.read_frame)
        self.read_text.pack()

        # Read button
        self.read_button = tk.Button(self.read_frame, text="Read", command=self.read_data)
        self.read_button.pack()

        # Update frame
        self.update_frame = tk.Frame(root)
        self.update_frame.pack()

        # Update entry fields
        self.update_name_label = tk.Label(self.update_frame, text="Name:")
        self.update_name_label.pack()
        self.update_name_entry = tk.Entry(self.update_frame)
        self.update_name_entry.pack()

        self.update_email_label = tk.Label(self.update_frame, text="Email:")
        self.update_email_label.pack()
        self.update_email_entry = tk.Entry(self.update_frame)
        self.update_email_entry.pack()

        # Update button
        self.update_button = tk.Button(self.update_frame, text="Update", command=self.update_data)
        self.update_button.pack()

        # Delete frame
        self.delete_frame = tk.Frame(root)
        self.delete_frame.pack()

        # Delete button
        self.delete_button = tk.Button(self.delete_frame, text="Delete", command=self.delete_data)
        self.delete_button.pack()

    def create_data(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        self.data.append({"name": name, "email": email})
        self.name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)

    def read_data(self):
        self.read_text.delete(1.0, tk.END)
        for item in self.data:
            self.read_text.insert(tk.END, f"Name: {item['name']}, Email: {item['email']}\n")

    def update_data(self):
        name = self.update_name_entry.get()
        email = self.update_email_entry.get()
        for item in self.data:
            if item["name"] == name:
                item["email"] = email
        self.update_name_entry.delete(0, tk.END)
        self.update_email_entry.delete(0, tk.END)

    def delete_data(self):
        name = self.update_name_entry.get()
        for item in self.data:
            if item["name"] == name:
                self.data.remove(item)
        self.update_name_entry.delete(0, tk.END)

root = tk.Tk()
app = CRUDApp(root)
root.mainloop()