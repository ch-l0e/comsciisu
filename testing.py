import tkinter as tk

root = tk.Tk()
root.title("Textbox Example")
root.geometry("400x200")

# Create an Entry widget
entry = tk.Entry(root, width=30)
entry.pack(pady=20)

# Function to display the entered text
def display_text():
    input_text = entry.get()  # Get the text from the Entry widget
    print(f"Entered text: {input_text}")

# Button to get the input text
btn = tk.Button(root, text="Submit", command=display_text)
btn.pack(pady=10)

root.mainloop()
