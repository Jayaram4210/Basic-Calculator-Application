import tkinter as tk
import math

def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            expression = entry.get().replace("x", "*")  # Replace 'x' with '*'
            result.set(eval(expression))
        except Exception as e:
            result.set("Error")
    elif text == "C":
        result.set("")
    elif text == "←":
        result.set(result.get()[:-1])  # Delete last character
    elif text == "√":
        try:
            result.set(math.sqrt(float(entry.get())))
        except Exception as e:
            result.set("Error")
    elif text == "^2":
        try:
            result.set(float(entry.get()) ** 2)
        except Exception as e:
            result.set("Error")
    elif text == "^":
        result.set(result.get() + "**")  # Using '**' for exponentiation
    else:
        result.set(result.get() + text)

root = tk.Tk()
root.title("Advanced Calculator")

result = tk.StringVar()
entry = tk.Entry(root, textvariable=result, font=("Arial", 20), justify="right")
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "x"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"],
    ["√", "^2", "^", "←"]
]

for i, row in enumerate(buttons):
    for j, button_text in enumerate(row):
        button = tk.Button(root, text=button_text, font=("Arial", 20), width=5, height=2)
        button.grid(row=i+1, column=j)
        button.bind("<Button-1>", on_click)

root.mainloop()
