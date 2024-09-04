import tkinter as tk
from tkinter import ttk
import psycopg2

root = tk.Tk()
root.geometry("500x300")
root.title("Offline Software Management")
#list view
#listbox = tk.Listbox(root,font=("Arial", 22, "bold"))
#root.columnconfigure(0, weight=1)

def ADD():
       
    newWindow = tk.Toplevel(root)
 
    # sets the title of the
    # Toplevel widget
    newWindow.title("New Window")
 
    # sets the geometry of toplevel
    newWindow.geometry("200x200")
 
    # A Label widget to show in toplevel
    Label(newWindow, 
          text ="This is a new window").pack()
        


try:
        
        
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="Mansoor@9008",
            host="localhost",
            port="5432"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT name,number FROM Projects;")
        records = cursor.fetchall()
        for record in records:
            #listbox.insert("1", record)
            #listbox.pack(fill="both", expand=True)
            label = tk.Label(root, text=record,font=("Arial", 22, "bold"))
            label.pack(pady=2)

            label = tk.Label(root, text=record)
            label.pack(pady=2)

            connect_button = tk.Button(root, text="New Entry", command=ADD)
            #connect_button.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
            connect_button.pack()

            connect_button = tk.Button(root, text="Cancel")#, command=connect_to_db)
            connect_button.pack()

            
            print(record)
        conn.close()
        
except Exception as e:
        print(f"Error: {e}")



'''       
def connect_to_db():
    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="Mansoor@9008",
            host="localhost",
            port="5432"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Projects;")
        records = cursor.fetchall()
        for record in records:
            listbox.insert("1", 'record')
            listbox.pack(fill="both", expand=True)

            
            print(record)
        conn.close()
        
    except Exception as e:
        print(f"Error: {e}")





root = tk.Tk()
root.geometry("500x300")
root.title("Offline Software Management")
label = tk.Label(root, text="New Project")
label.pack(pady=10)

# label for text box name
label = tk.Label(root, text="Enter Project Name:")
label.pack(pady=5)


#Create a Text widget
text_name = tk.Text(root, height=2, width=40)
text_name.pack(pady=10)

# label for text box number
label = tk.Label(root, text="Enter Number:")
label.pack(pady=5)


#Create a Text widget
text_number = tk.Text(root, height=2, width=40)
text_number.pack(pady=10)

connect_button = tk.Button(root, text="Save", command=connect_to_db)
connect_button.pack(side=tk.RIGHT)

connect_button = tk.Button(root, text="Cancel", command=connect_to_db)
connect_button.pack(side=tk.LEFT)




'''
root.mainloop()