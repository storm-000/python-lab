from tkinter import *

def save_resume():
    name = name_entry.get()
    age = age_entry.get()

    # DOB from dropdowns
    dob = f"{day_var.get()}-{month_var.get()}-{year_var.get()}"

    gender = gender_var.get()
    qualification = qual_var.get()
    address = addr_entry.get("1.0", END)

    # Resume content
    resume_text = (
        "------ RESUME ------\n\n"
        f"Name: {name}\n"
        f"Age: {age}\n"
        f"Date of Birth: {dob}\n"
        f"Gender: {gender}\n"
        f"Qualification: {qualification}\n"
        f"Address: {address}\n"
    )

    # Save as .doc (simple text file)
    with open("resume.doc", "w") as f:
        f.write(resume_text)

    status_label.config(text="Resume saved as resume.doc")


root = Tk()
root.title("Resume Builder")

# ------------------------------
# Name
Label(root, text="Name").grid(row=0, column=0, sticky="w")
name_entry = Entry(root, width=40)
name_entry.grid(row=0, column=1)

# Age
Label(root, text="Age").grid(row=1, column=0, sticky="w")
age_entry = Entry(root, width=40)
age_entry.grid(row=1, column=1)

# ------------------------------
# DOB Dropdowns
Label(root, text="Date of Birth").grid(row=2, column=0, sticky="w")

# Day dropdown
day_var = StringVar(value="1")
day_choices = [str(i) for i in range(1, 32)]
OptionMenu(root, day_var, *day_choices).grid(row=2, column=1, sticky="w")

# Month dropdown
month_var = StringVar(value="Jan")
month_choices = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
OptionMenu(root, month_var, *month_choices).grid(row=2, column=1)

# Year dropdown
year_var = StringVar(value="2000")
year_choices = [str(i) for i in range(1970, 2026)]
OptionMenu(root, year_var, *year_choices).grid(row=2, column=1, sticky="e")

# ------------------------------
# Gender
Label(root, text="Gender").grid(row=3, column=0, sticky="w")
gender_var = StringVar(value="Male")
Radiobutton(root, text="Male", value="Male", variable=gender_var).grid(row=3, column=1, sticky="w")
Radiobutton(root, text="Female", value="Female", variable=gender_var).grid(row=3, column=1, sticky="e")

# ------------------------------
# Qualification dropdown
Label(root, text="Qualification").grid(row=4, column=0, sticky="w")
qual_var = StringVar(value="10th")
qual_choices = ["10th", "12th", "Diploma", "Undergraduate", "Postgraduate", "PhD"]
OptionMenu(root, qual_var, *qual_choices).grid(row=4, column=1)

# ------------------------------
# Address Textbox
Label(root, text="Address").grid(row=5, column=0, sticky="nw")
addr_entry = Text(root, width=30, height=5)
addr_entry.grid(row=5, column=1)

# ------------------------------
# Save Button
Button(root, text="Save Resume", command=save_resume).grid(row=6, column=1, pady=10)

status_label = Label(root, text="", fg="green")
status_label.grid(row=7, column=1)

root.mainloop()
