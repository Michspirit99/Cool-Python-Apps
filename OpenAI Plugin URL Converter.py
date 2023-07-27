import tkinter as tk
from tkinter import Entry, Label, Button, Text

def convert_url():
    user_url = url_entry.get()
    if user_url.endswith("/.well-known/openapi.yaml"):
        converted_url = user_url.replace("/.well-known/openapi.yaml", "/.well-known/ai-plugin.json")
    else:
        converted_url = "Invalid URL format."

    result_text.delete(1.0, tk.END)  # Clear the previous result
    result_text.insert(tk.END, converted_url)

def copy_to_clipboard():
    app.clipboard_clear()
    app.clipboard_append(result_text.get(1.0, tk.END).strip())
    app.update()  # Now it stays in the clipboard after the window is closed

# Create the main window
app = tk.Tk()
app.title("URL Converter")

# Add a label
label = Label(app, text="Enter URL:")
label.pack(padx=20, pady=5)

# Add an input field
url_entry = Entry(app, width=50)
url_entry.pack(padx=20, pady=5)

# Add a button to convert the URL
convert_button = Button(app, text="Convert URL", command=convert_url)
convert_button.pack(padx=20, pady=5)

# Text widget to display the result
result_text = Text(app, height=2, width=50, wrap=tk.WORD)
result_text.pack(padx=20, pady=5)

# Add a button to copy the result
copy_button = Button(app, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(padx=20, pady=20)

app.mainloop()
