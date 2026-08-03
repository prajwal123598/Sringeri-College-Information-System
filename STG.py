from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Sringeri Tourism Guide")
root.geometry("1500x1000")
root.config(bg="lightblue")

Label(
    root,
    text="WELCOME TO SRINGERI\nTHE LAND OF TEMPLES & NATURE",
    font=("Arial", 12, "bold"),
    fg="darkblue",
    bg="lightblue"
).pack(pady=20)

# -------- Temple Data --------
temple_details = {
    "Sri Sharadamba Temple": {
        "Timings": "6:00 AM - 2:00 PM, 5:00 PM - 9:00 PM",
        "Details": "Main deity of Sringeri. One of the 4 cardinal mathas established by Adi Shankaracharya. Abhisheka and poojas done daily."
    },
    "Sri Srungageri Temple": {
        "Timings": "7:00 AM - 12:00 PM, 4:00 PM - 8:00 PM",
        "Details": "Ancient temple located on the banks of Tunga river. Famous for its peaceful atmosphere."
    },
    "Sri Kalabhairaveshwara Temple": {
        "Timings": "6:30 AM - 1:00 PM, 5:00 PM - 8:30 PM",
        "Details": "Dedicated to Lord Bhairava. Special poojas on Ashtami and Sundays."
    },
    "Sri Torana Rushyasrunga Temple": {
        "Timings": "8:00 AM - 6:00 PM",
        "Details": "Temple with unique stone gateway. Named after sage Rushyasrunga."
    },
    "Sri Durga Temple": {
        "Timings": "6:00 AM - 12:00 PM, 4:00 PM - 9:00 PM",
        "Details": "Goddess Durga temple. Navaratri celebrations are grand here with special alankara."
    },
    "Sri Kalikamba Temple": {
        "Timings": "7:00 AM - 1:00 PM, 5:00 PM - 8:00 PM",
        "Details": "Dedicated to Goddess Kali. Fridays and Tuesdays are considered very auspicious."
    },
    "Sri Anjaneya Temple": {
        "Timings": "6:00 AM - 8:00 PM",
        "Details": "Hanuman temple with 15ft tall idol. Devotees offer vadas on Saturdays."
    },
    "Sri Raktheshwari Temple": {
        "Timings": "7:00 AM - 1:00 PM, 5:00 PM - 8:00 PM",
        "Details": "Goddess temple known for special abhishekas and evening deepa pooja."
    },
    "Sri Sharadamba Temple, Hariharapura": {
        "Timings": "8:00 AM - 1:00 PM, 4:00 PM - 7:00 PM",
        "Details": "Branch matha of Sringeri. Located 20km from Sringeri on the way to Koppa."
    },
    "Sri Annapoorneshwari Temple": {
        "Timings": "5:30 AM - 2:00 PM, 4:00 PM - 9:00 PM",
        "Details": "Goddess of food. Free meals 'Anna Dasoha' are served to all devotees daily."
    }
}

# -------- Tourist Places Data --------
tourist_details = {
    "Sirimane Falls": {"Timings": "6:00 AM - 6:00 PM", "Details": "Beautiful waterfall, 15km from Sringeri. Jeep ride available through forest."},
    "Tunga River": {"Timings": "Open 24 Hours", "Details": "Holy river flowing through Sringeri. Boating and coracle rides available."},
    "Hanging Bridge": {"Timings": "7:00 AM - 7:00 PM", "Details": "Iconic 330ft bridge over Tunga river. Great photo spot and sunset view."},
    "Kigga": {"Timings": "Open 24 Hours", "Details": "Hill station with coffee plantations. 10km from Sringeri. Misty weather all year."},
    "Agumbe": {"Timings": "6:00 AM - 6:00 PM", "Details": "Known as 'Cherrapunji of South India'. Famous for sunset point and rainforests."},
    "Suthanabhi Falls": {"Timings": "6:00 AM - 6:00 PM", "Details": "Hidden waterfall in forest area. 2km trek required. Best in monsoon."},
    "Narasimha Mountain": {"Timings": "6:00 AM - 5:00 PM", "Details": "Trekking spot with Narasimha temple on top. 400 steps to climb."},
    "Suji Mountain": {"Timings": "6:00 AM - 5:00 PM", "Details": "Scenic viewpoint. Popular for sunrise and paragliding activities."},
    "Kundhadri": {"Timings": "6:00 AM - 6:00 PM", "Details": "Hill with 17th century Jain temple. 360 degree view of Western Ghats."},
    "Magebil Falls": {"Timings": "7:00 AM - 5:00 PM", "Details": "Seasonal waterfall during monsoon. Surrounded by dense forest."},
    "Buddha Homestay": {"Timings": "Check-in: 12 PM, Check-out: 11 AM", "Details": "Peaceful homestay with garden view. Authentic Malnad food available."},
    "Lakya Dam": {"Timings": "8:00 AM - 6:00 PM", "Details": "Dam with boating and garden. Good picnic spot with family."},
    "Kudremukh Garden": {"Timings": "8:00 AM - 6:00 PM", "Details": "Botanical garden with rare plants and flowers. Entry fee Rs.20."}
}

# -------- Function to show details window --------
def show_details(title, data):
    win = Toplevel(root)
    win.title(title)
    win.geometry("1500x1200")
    win.config(bg="white")

    Label(win, text=title, font=("Arial", 10, "bold"), fg="darkblue", bg="white").pack(pady=10)
    Label(win, text="Timings: " + data["Timings"], font=("Arial", 10, "bold"), fg="green", bg="white", wraplength=350, justify="left").pack(pady=5, padx=10, anchor="w")
    Label(win, text="About:", font=("Arial", 10, "bold"), fg="black", bg="white").pack(pady=5, padx=10, anchor="w")
    Label(win, text=data["Details"], font=("Arial", 10), fg="black", bg="white", wraplength=350, justify="left").pack(pady=5, padx=10)

# -------- Temple Window --------
def temples():
    win = Toplevel(root)
    win.title("Temples in Sringeri")
    win.geometry("1500x1200")
    win.config(bg="lightyellow")

    Label(win, text="FAMOUS TEMPLES IN SRINGERI", font=("Arial", 14, "bold"), fg="blue", bg="lightyellow").pack(pady=10)

    canvas = Canvas(win, bg="lightyellow")
    scrollbar = Scrollbar(win, orient="vertical", command=canvas.yview)
    scrollable_frame = Frame(canvas, bg="lightyellow")

    scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    colors = ["orange","lightgreen","lightblue","pink","khaki","violet","green","white","red","yellow"]
    for i, name in enumerate(temple_details.keys()):
        Button(scrollable_frame, text=name, width=35, bg=colors[i % len(colors)],
               command=lambda n=name: show_details(n, temple_details[n])).pack(pady=5)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

# -------- Tourist Places Window --------
def tourist_places():
    win = Toplevel(root)
    win.title("Tourist Places")
    win.geometry("2000x2000")
    win.config(bg="lightcyan")

    Label(win, text="TOURIST PLACES IN SRINGERI", font=("Arial", 14, "bold"), fg="darkblue", bg="lightcyan").pack(pady=10)

    canvas = Canvas(win, bg="lightcyan")
    scrollbar = Scrollbar(win, orient="vertical", command=canvas.yview)
    scrollable_frame = Frame(canvas, bg="lightcyan")

    scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    colors = ["skyblue","lightgreen","orange","pink","khaki","violet","lightblue","lightgrey","lightpink","coral","lavender","beige","mistyrose"]
    for i, name in enumerate(tourist_details.keys()):
        Button(scrollable_frame, text=name, width=35, bg=colors[i % len(colors)],
               command=lambda n=name: show_details(n, tourist_details[n])).pack(pady=5)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

# -------- Explore Button --------
def explore():
    temple_btn.pack(pady=10)
    tourist_btn.pack(pady=10)

Button(
    root,
    text="EXPLORE SRINGERI",
    font=("Arial", 18, "bold"),
    bg="green",
    fg="white",
    command=explore
).pack(pady=20)

temple_btn = Button(root, text="TEMPLES", font=("Arial", 15), bg="orange", width=20, command=temples)
tourist_btn = Button(root, text="TOURIST PLACES", font=("Arial", 13), bg="skyblue", width=20, command=tourist_places)

Label(
	root,
	text="DEVELOPED BY PRAJWAL HM(BCA)",
	font=("Arial",10,"italic"),
	fg="orange",
	bg="white"
).pack(side=TOP,pady=10)

Label(
	root,
	text="DEVELOPED BY SWASTHIK D(BCA)",
	font=("Arial",10,"italic"),
	fg="red",
	bg="blue"
).pack(side=TOP,pady=10)

Label(
	root,
	text="DEVELOPED BY DHANUSH BC(BCA)",
	font=("Arial",10,"italic"),
	fg="pink",
	bg="yellow"
).pack(side=TOP,pady=10)

root.mainloop()