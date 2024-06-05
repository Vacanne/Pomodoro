import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
# Define colors and constants for the timer
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# Initialize global variables
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    """Resets the timer and UI elements to their initial state."""
    window.after_cancel(timer)  # Cancel the current timer
    canvas.itemconfig(timer_text, text="00:00")  # Reset timer text
    title_label.config(text="Timer")  # Reset title label
    check_marks.config(text="")  # Clear check marks
    global reps
    reps = 0  # Reset repetitions counter

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    """Starts the timer with work, short break, or long break intervals based on repetitions."""
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # Determine the current session type
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Long Break!", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Short Break!", fg=YELLOW)
    else:
        count_down(work_sec)
        title_label.config(text="Work!", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    """Handles the countdown mechanism and updates the UI."""
    count_min = math.floor(count / 60)
    count_sec = count % 60

    # Ensure seconds are displayed as two digits
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    # Update the timer text
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    
    # Continue countdown or start the next session
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        # Update check marks for completed work sessions
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✓"
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
# Create main application window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=PINK)

# Add a title label
title_label = Label(text="Timer", fg=GREEN, bg=PINK, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

# Create a canvas for the timer
canvas = Canvas(width=200, height=224, bg=PINK, highlightthickness=0)
pomodoro_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=pomodoro_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Add start and reset buttons
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", highlightthickness=0, command=reset)
reset_button.grid(column=2, row=2)

# Add a label to display check marks
check_marks = Label(fg=GREEN, bg=PINK)
check_marks.grid(column=1, row=3)

# Start the main loop
window.mainloop()
