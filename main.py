from tkinter import *
from tkinter import scrolledtext
from datetime import datetime

root = Tk()
root.title("Keyboard Activity Logger")
root.geometry("700x500")
root.resizable(False, False)

logging = False


def log_key(event):
    if not logging:
        return

    if event.keysym in ["Shift_L", "Shift_R", "Control_L", "Control_R", "Alt_L", "Alt_R"]:
        return

    if event.keysym == "space":
        key = "SPACE"
    elif event.keysym == "Return":
        key = "ENTER"
    elif event.keysym == "BackSpace":
        key = "BACKSPACE"
    else:
        key = event.keysym

    current_time = datetime.now().strftime("%H:%M:%S")

    message = f"{current_time}  ->  {key}\n"

    log_area.insert(END, message)
    log_area.see(END)

    with open("keystrokes.txt", "a") as file:
        file.write(message)


def start_logging():
    global logging
    logging = True
    status_label.config(
        text="Status: Logging ON",
        fg="green"
    )


def stop_logging():
    global logging
    logging = False
    status_label.config(
        text="Status: Logging OFF",
        fg="red"
    )


def clear_log():
    log_area.delete("1.0", END)

    with open("keystrokes.txt", "w") as file:
        file.write("")


heading = Label(
    root,
    text="Keyboard Activity Logger",
    font=("Arial", 18, "bold")
)
heading.pack(pady=10)

status_label = Label(
    root,
    text="Status: Logging OFF",
    fg="red",
    font=("Arial", 12, "bold")
)
status_label.pack(pady=5)

log_area = scrolledtext.ScrolledText(
    root,
    width=80,
    height=20,
    font=("Consolas", 10)
)
log_area.pack(padx=10, pady=10)

log_area.bind("<Key>", log_key)

button_frame = Frame(root)
button_frame.pack(pady=10)

start_button = Button(
    button_frame,
    text="Start Logging",
    width=15,
    command=start_logging
)
start_button.grid(row=0, column=0, padx=10)

stop_button = Button(
    button_frame,
    text="Stop Logging",
    width=15,
    command=stop_logging
)
stop_button.grid(row=0, column=1, padx=10)

clear_button = Button(
    button_frame,
    text="Clear Log",
    width=15,
    command=clear_log
)
clear_button.grid(row=0, column=2, padx=10)

root.mainloop()