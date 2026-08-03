from tkinter import *
from tkinter import messagebox
import sqlite3
from tkinter import ttk

# ---------------- DATABASE ----------------
conn = sqlite3.connect("gfgc_library.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS books(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_name TEXT,
    author TEXT,
    category TEXT,
    quantity INTEGER
)
""")
conn.commit()

# ---------------- ROOT WINDOW ----------------
root = Tk()
root.title("GFGC Sringeri Smart Library Management System")
root.geometry("1500x1200")
root.config(bg="#E6F7FF")
root.resizable(False, False)

# ---------------- ADD BOOK ----------------
def add_book():
    add = Toplevel(root)
    add.title("Add New Book")
    add.geometry("1500x1500")
    add.config(bg="lightgreen")

    Label(add, text="ADD NEW BOOK", font=("Arial", 18, "bold"), bg="lightgreen", fg="darkblue").pack(pady=15)

    Label(add, text="Book Name", bg="lightgreen").pack()
    book = Entry(add, width=35)
    book.pack(pady=5)

    Label(add, text="Author Name", bg="lightgreen").pack()
    author = Entry(add, width=35)
    author.pack(pady=5)

    Label(add, text="Category", bg="lightgreen").pack()
    category = Entry(add, width=35)
    category.pack(pady=5)

    Label(add, text="Quantity", bg="lightgreen").pack()
    qty = Entry(add, width=35)
    qty.pack(pady=5)

    def save_book():
        if book.get() == "" or author.get() == "" or category.get() == "" or qty.get() == "":
            messagebox.showerror("Error", "Please fill all fields.")
            return
        try:
            quantity = int(qty.get())
        except ValueError:
            messagebox.showerror("Error", "Quantity must be a number.")
            return

        cur.execute("INSERT INTO books (book_name, author, category, quantity) VALUES (?,?,?)",
                    (book.get(), author.get(), category.get(), quantity))
        conn.commit()
        messagebox.showinfo("Success", "Book Added Successfully!")

        book.delete(0, END)
        author.delete(0, END)
        category.delete(0, END)
        qty.delete(0, END)

    Button(add, text="SAVE BOOK", font=("Arial", 12, "bold"), bg="green", fg="white", width=20, command=save_book).pack(pady=20)

# ---------------- VIEW BOOKS ----------------
def view_books():
    view = Toplevel(root)
    view.title("View Books")
    view.geometry("700x400")
    view.config(bg="white")

    Label(view, text="ALL BOOKS", font=("Arial", 18, "bold"), bg="white", fg="darkblue").pack(pady=10)

    columns = ("ID", "Book Name", "Author", "Category", "Quantity")
    tree = ttk.Treeview(view, columns=columns, show="headings")

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=130)

    tree.pack(fill=BOTH, expand=True, padx=10, pady=10)

    cur.execute("SELECT * FROM books")
    rows = cur.fetchall()
    for row in rows:
        tree.insert("", END, values=row)

# ---------------- SEARCH BOOK ----------------
def search_book(): # fixed name
    search = Toplevel(root)
    search.title("Search Book")
    search.geometry("1500x1200")
    search.config(bg="lightyellow")

    Label(search, text="SEARCH BOOK", font=("Arial", 18, "bold"), bg="lightyellow").pack(pady=10)
    Label(search, text="Enter Book Name", bg="lightyellow").pack()

    book = Entry(search, width=35)
    book.pack(pady=5)

    result = Label(search, text="", bg="lightyellow", fg="blue", font=("Arial", 12), justify=LEFT)
    result.pack(pady=15)

    def find():
        cur.execute("SELECT * FROM books WHERE book_name=?", (book.get(),))
        row = cur.fetchone()
        if row:
            result.config(text=f"ID : {row[0]}\nBook : {row[1]}\nAuthor : {row[2]}\nCategory : {row[3]}\nQuantity : {row[4]}")
        else:
            result.config(text="Book Not Found")

    Button(search, text="SEARCH", bg="green", fg="white", command=find).pack()

# ---------------- DELETE BOOK ----------------
def delete_book():
    delete = Toplevel(root)
    delete.title("Delete Book")
    delete.geometry("1500x1300")
    delete.config(bg="lightpink")

    Label(delete, text="DELETE BOOK", font=("Arial", 18, "bold"), bg="lightpink").pack(pady=15)
    Label(delete, text="Book ID", bg="lightpink").pack()
    book_id = Entry(delete)
    book_id.pack()

    def remove():
        if book_id.get() == "":
            messagebox.showerror("Error", "Please enter Book ID")
            return
        cur.execute("DELETE FROM books WHERE id=?", (book_id.get(),))
        conn.commit()
        if cur.rowcount > 0:
            messagebox.showinfo("Success", "Book Deleted Successfully")
        else:
            messagebox.showwarning("Not Found", "No book with that ID")
        delete.destroy()

    Button(delete, text="DELETE", bg="red", fg="white", command=remove).pack(pady=20)

# ---------------- ADMIN DASHBOARD ----------------
def admin_dashboard():
    dash = Toplevel(root)
    dash.title("Library Dashboard")
    dash.geometry("1500x1200")
    dash.config(bg="lightblue")

    Label(dash, text="GFGC SRINGERI LIBRARY", font=("Arial", 20, "bold"), bg="lightblue", fg="darkblue").pack(pady=20)

    Button(dash, text="Add Book", width=25, bg="green", fg="white", command=add_book).pack(pady=8)
    Button(dash, text="View Books", width=25, bg="skyblue", command=view_books).pack(pady=8)
    Button(dash, text=" Search Book", width=25, bg="orange", command=search_book).pack(pady=8) # fixed call
    Button(dash, text=" Delete Book", width=25, bg="red", fg="white", command=delete_book).pack(pady=8)
    Button(dash, text="Issue Book", width=25, bg="lightgreen").pack(pady=8)
    Button(dash, text="Return Book", width=25, bg="lightyellow").pack(pady=8)
    Button(dash, text="Logout", width=25, bg="red", fg="white", command=dash.destroy).pack(pady=20)

# ---------------- ADMIN LOGIN ----------------
def admin_login():
    login = Toplevel(root)
    login.title("Admin Login")
    login.geometry("1500x1200")
    login.config(bg="lightyellow")

    Label(login, text="ADMIN LOGIN", font=("Arial", 18, "bold"), bg="lightyellow", fg="darkblue").pack(pady=20)
    Label(login, text="Username", bg="lightyellow").pack()
    username = Entry(login, width=30)
    username.pack(pady=5)
    Label(login, text="Password", bg="lightyellow").pack()
    password = Entry(login, show="*", width=30)
    password.pack(pady=5)

    def check_login():
        if username.get() == "Prajwal HM" and password.get() == "prajwal@4321":
            messagebox.showinfo("Success", "Welcome Library Admin")
            login.destroy()
            admin_dashboard()
        else:
            messagebox.showerror("Error", "Invalid Username or Password")

    Button(login, text="LOGIN", bg="green", fg="white", width=18, command=check_login).pack(pady=20)

# ---------------- WELCOME PAGE ----------------
Label(root, text="WELCOME TO", font=("Arial", 22, "bold"), fg="darkblue", bg="#E6F7FF").pack(pady=10)
Label(root, text="GFGC SRINGERI\nSMART LIBRARY MANAGEMENT SYSTEM", font=("Arial", 18, "bold"), fg="green", bg="#E6F7FF").pack()
Label(root, text="Knowledge is Power", font=("Arial", 15, "italic"), fg="brown", bg="#E6F7FF").pack(pady=10)
Label(root, text="Government First Grade College, Sringeri", font=("Arial", 14), bg="#E6F7FF").pack()

Button(root, text="ENTER LIBRARY", font=("Arial", 14, "bold"), bg="green", fg="white", width=20, command=admin_login).pack(pady=20)
Button(root, text="EXIT", font=("Arial", 14, "bold"), bg="red", fg="white", width=20, command=root.destroy).pack()

Label(
	root,
	text="DEVOLPED BY PRAJWAL HM(BCA)",
	font=("Arial",10,"italic"),
	fg="green",
	bg="white",
).pack(side=TOP,pady=10)

root.mainloop()