import tkinter as tk
from tkinter import messagebox
pip install Pillow



def get_float_input(entry):
    try:
        return float(entry.get())
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number for your weight.")
        return None

def get_age_input(entry):
    try:
        return float(entry.get())
    except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid number for your age.")
            return None

def get_gender_input():
    if gender_var.get() not in ['M', 'F']:
         messagebox.showerror("Invalid input", "Please select 'Male' or 'Female'.")
         return None
    return gender_var.get()

def get_activity_level():
    if activity_var.get() not in ['A', 'B', 'C', 'D', 'E']:
        messagebox.showerror("Invalid input", "Please select an activity level.")
        return None
    return activity_var.get()

def calculate_bmr(weight, height, age, gender,):
    if gender == 'M':
        weight1 = 66 + (13.7 * weight) + (5 * height) - (6.8 * age)
        return weight1
    else:
        weight1 = 655 + (9.6 * weight) + (1.8 * height) - (4.7 * age)
        return weight1


def calculate_daily_calories(bmr, activity_level):
    activity_multipliers = {
        "A": 1.2, "B": 1.375, "C": 1.55, "D": 1.725, "E": 1.9
    }

    return bmr * activity_multipliers.get(activity_level, 1)
def calculate_nutrition():
    height = get_float_input(height_entry)
    weight = get_float_input(weight_entry)
    age = get_age_input(age_entry)
    gender = get_gender_input()
    activity_level = get_activity_level()





    if height is None or weight is None or age is None or gender is None or activity_level is None:
        return

    bmr = calculate_bmr(weight, height, age, gender)
    daily_calories = calculate_daily_calories(bmr, activity_level)

    protein = 0.7 * weight




    result_text = (f"Your BMR: {bmr:.2f}\n"
                   f"Calories you should eat: {daily_calories:.2f}\n"
                   f"Grams of protein needed: {protein:.2f}\n"
                   f"If BMR is Over 2500 You are classified as overweight, If BMR is 2500 you are healthy weight, If BMR is under 2500 you are classified as underweight.")
    messagebox.showinfo("Your specialized nutrition information", result_text)

def gender_choice():
    choice = gender_var.get()
    if choice == "M":
        output = "Male"
    elif choice == "F":
        output = "Female"
    else:
        output = "Invalid selection"
    return output


# Create main window
root = tk.Tk()
root.title("Calorie Calculator")
root.geometry("1200x200")

tk.Label(root, text="Welcome! This is a Calorie Calculator made by Youdahe!!!.").grid(row=10, column=10, columnspan=20)

tk.Label(root, text="Height (feet, e.g., 5.2):").grid(row=1, column=0)
height_entry = tk.Entry(root)
height_entry.grid(row=1, column=1)

tk.Label(root, text="Weight (lbs):").grid(row=2, column=0)
weight_entry = tk.Entry(root)
weight_entry.grid(row=2, column=1)

tk.Label(root, text="Age:").grid(row=3, column=0)
age_entry = tk.Entry(root)
age_entry.grid(row=3, column=1)

tk.Label(root, text="Gender:").grid(row=4, column=0)
gender_var = tk.StringVar()
tk.Radiobutton(root, text="M - Male", variable=gender_var, value='M', indicatoron=False).grid(row=4, column=1)
tk.Radiobutton(root, text="F - Female", variable=gender_var, value='F', indicatoron=False).grid(row=4, column=2)


tk.Label(root, text="Activity Level:").grid(row=5, column=0)
activity_var = tk.StringVar()
tk.Radiobutton(root, text="Sedentary (A)", variable=activity_var, value='A', indicatoron=False).grid(row=5, column=1)
tk.Radiobutton(root, text="Lightly Active (B)", variable=activity_var, value='B', indicatoron=False).grid(row=5, column=2)
tk.Radiobutton(root, text="Moderately Active (C)", variable=activity_var, value='C', indicatoron=False).grid(row=5, column=3)
tk.Radiobutton(root, text="Very Active (D)", variable=activity_var, value='D', indicatoron=False).grid(row=5, column=4)
tk.Radiobutton(root, text="Extra Active (E)", variable=activity_var, value='E', indicatoron=False).grid(row=5, column=5)
tk.Label(root, text="Goal:").grid(row=6, column=0)
decision_var = tk.StringVar()
tk.Radiobutton(root, text='Loose Weight', variable= decision_var,value="Loose",indicatoron=False).grid(row=6, column=1)
tk.Radiobutton(root, text='Maintain Weight', variable=decision_var,value="Maintain",indicatoron=False).grid(row=6, column=2)
tk.Radiobutton(root, text='Gain Weight', variable=decision_var,value="Gain",indicatoron=False).grid(row=6, column=3)
tk.Button(root, text="Calculate", command=calculate_nutrition).grid(row=7, column=0, columnspan=4)

# Start the GUI event loop
root.mainloop()