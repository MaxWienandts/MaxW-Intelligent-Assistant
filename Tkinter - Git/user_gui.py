# cd "C:\Users\014206631\Python\Llama chat\Tkinter"
# conda activate llamaChat
# python user_gui.py

import sys, os

import time
import threading
import webbrowser
from PIL import ImageTk, Image

from class_llama2chat import llama2Chat
import tkinter as tk
from tkinter import ttk
import tkinter.scrolledtext as tkscrolled

from class_llama2chat import llama2Chat

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def callback(url):
    # To make hyperlinks
    webbrowser.open_new(url)

def on_configure(event):
    # Update the scroll region of the canvas to include the whole content frame
    canvas.configure(scrollregion=canvas.bbox('all'))
    # Ensure the content frame is the same width as the canvas
    canvas_width = event.width
    canvas.itemconfig(canvas_window, width = canvas_width)

def on_mouse_wheel(event):
    if event.delta:
        canvas.yview_scroll(-1 * int(event.delta / 120), "units")
    elif event.num == 4:
        canvas.yview_scroll(-1, "units")
    elif event.num == 5:
        canvas.yview_scroll(1, "units")

# Create a divisor
def create_horizontal_lines():
    # Make a horizontal line to separate elements
    separator = ttk.Separator(content_frame, orient = 'horizontal')
    separator.pack(fill = 'x', pady = 10)

# Clean chat history
def clean_chat_history():
    text_chat_history_1.configure(state = "normal")
    text_chat_history_1.delete('1.0', tk.END)
    text_chat_history_1.configure(state = "disabled")

# Create the main window
root = tk.Tk()
root.state('zoomed') # Open with maximized screen
# Change window icon and title
root.iconbitmap(resource_path('META & Microsoft Team Up on LlaMA 2.ico'))
root.title('Chat with Your PC Llama2')

# Make the root window's grid expand to fit the window size
root.grid_rowconfigure(0, weight = 1)
root.grid_columnconfigure(0, weight = 1)

# Create a frame to hold the scrollbar and canvas
frame = tk.Frame(root)
frame.grid(row = 0, column = 0, sticky='nsew')
frame.grid_rowconfigure(0, weight = 1)
frame.grid_columnconfigure(0, weight = 1)
frame.grid_columnconfigure(1, weight = 0)

# Create a scrollbar and place it on the right side of the frame
scrollbar = tk.Scrollbar(frame, orient = tk.VERTICAL)
scrollbar.grid(row = 0, column = 1, sticky = 'ns')

# Create a canvas and place it next to the scrollbar
canvas = tk.Canvas(frame, yscrollcommand = scrollbar.set)
canvas.grid(row = 0, column = 0, sticky = 'nsew')

# Configure the scrollbar to control the canvas
scrollbar.config(command=canvas.yview)

# Create another frame inside the canvas to hold the content
content_frame = tk.Frame(canvas)
canvas_window = canvas.create_window((0, 0), window=content_frame, anchor='nw')

# Configure the canvas scrolling region
content_frame.bind("<Configure>", on_configure)
canvas.bind("<Configure>", on_configure)
# Bind mouse wheel events
canvas.bind_all("<MouseWheel>", on_mouse_wheel)
canvas.bind_all("<Button-4>", on_mouse_wheel)
canvas.bind_all("<Button-5>", on_mouse_wheel)

# Both elements will be used to show chat history
history_frame = tk.Frame(content_frame)
text_chat_history_1 = tkscrolled.ScrolledText(history_frame, 
    height = 30, 
    state='disabled'
)

# Load model
def instantiate_chat(system_prompt):
    clean_chat_history()
    llamaChatObj.instantiate_llm()
    llamaChatObj.setup_chain(system_prompt)
    return llamaChatObj

# Define model object
default_system_prompt = """You are a helpful, respectful and honest assistant. 
Always answer as helpfully as possible.  
If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. 
If you don't know the answer to a question, please don't share false information."""
llamaChatObj = llama2Chat(default_system_prompt)
llamaChatObj = instantiate_chat(default_system_prompt)

# Header
label_header_1 = tk.Label(content_frame, text='Chat with your computer.', font=("Arial", 15))
label_header_2 = tk.Label(content_frame, text='AI powered by Llama 2.\n', font=("Arial", 10))
label_header_1.pack(pady = 10)
label_header_2.pack(pady = 0)

# Create a divisor
create_horizontal_lines()

# System Message
text_system_message = """System message is used to prime the chat with context, instructions, or other information relevant to your use case. \nYou can use the system message to describe the assistant’s personality, define what it should and shouldn’t answer, and define the format of the responses.
\nSystem message:"""

label_system_message_1 = tkscrolled.ScrolledText(content_frame, height = 12)
label_system_message_1.insert(tk.INSERT, f"{text_system_message} \n{default_system_prompt}")
label_system_message_1.configure(state = "disabled")

# Add possibility to change system message
entry_system_message = tkscrolled.ScrolledText(content_frame, height = 3)
entry_system_message.insert(
    tk.INSERT,
    "Type a new system message. If you change it, the chat history will be lost.",
)
new_system_prompt = default_system_prompt
def set_new_system_message(): 
    # use global variable. Functions insode a button cannot receive variables.
    global new_system_prompt
    clean_chat_history() # When you change the system message, you lose the chat history. 
    new_system_prompt = entry_system_message.get("1.0",'end-1c')
    llamaChatObj.setup_chain(new_system_prompt)
    label_system_message_1.configure(state = "normal")
    label_system_message_1.delete('1.0',tk.END)
    label_system_message_1.insert(tk.INSERT, f"{text_system_message} \n{llamaChatObj.system_prompt}")
    label_system_message_1.configure(state = "disabled")
# The system message will change only if the button is pressed.
button_set_new_system_message = tk.Button(
    content_frame, 
    text = "Set new system message", 
    command = set_new_system_message
)
label_system_message_1.pack(
    anchor = 'center',
    fill = 'x',
    padx = 30,
    pady = 15,
)
entry_system_message.pack(
    anchor = 'center',
    fill = 'x',
    padx = 30,
    pady = 15
)
button_set_new_system_message.pack(anchor = 'center')

# Create a divisor
create_horizontal_lines()

# Question and answer
label_question_answer_1 = tk.Label(
    content_frame, 
    text = "\nLet's talk!",
    font = ("Arial", 10),
)
label_question_answer_1.pack()
entry_question_answer = tkscrolled.ScrolledText(content_frame, height = 3)
entry_question_answer.insert(
    tk.INSERT,
    "What is in your mind?",
)
label_question_answer_2 = tk.Label(
    content_frame,
    text = "Llama 2's answer:",   # The model's result will be put here.
    font = ("Arial", 10)
)
text_question_answer_1 = tkscrolled.ScrolledText(content_frame, height = 5, state = "disabled")

def send_question():
    def process_prompt():
        # Get answer
        user_prompt = entry_question_answer.get("1.0",'end-1c')
        
        # Update the UI to show "PROCESSING!!!"
        text_question_answer_1.configure(state="normal")
        text_question_answer_1.delete('1.0', tk.END)
        text_question_answer_1.insert(tk.INSERT, "PROCESSING!!!")
        text_question_answer_1.configure(state="disabled")

        # Simulate processing time
        time.sleep(1)

        # Get the answer from llamaChatObj (assuming it's a global object)
        llamaChatObj.answer_prompt(user_prompt)

        # Update the UI with the response
        text_question_answer_1.configure(state="normal")
        text_question_answer_1.delete('1.0', tk.END)
        text_question_answer_1.insert(tk.INSERT, llamaChatObj.answer["text"])
        text_question_answer_1.configure(state="disabled")
        
        # Update chat history
        text_chat_history_1.configure(state="normal")
        text_chat_history_1.insert(tk.END, f"User: {user_prompt}\n")
        text_chat_history_1.insert(tk.END, f"{llamaChatObj.answer['text']}\n---\n\n")
        text_chat_history_1.configure(state="disabled")

    # Run the prompt processing in a separate thread to avoid blocking the UI
    threading.Thread(target=process_prompt).start()

# The answer will appear only when the button is pressed.
button_set_question_answer = tk.Button(
    content_frame, 
    text = "Send", 
    command = send_question
)
label_question_answer_1.pack(anchor = 'center')
entry_question_answer.pack(
    anchor = 'center',
    fill = 'x',
    padx = 30,
)
button_set_question_answer.pack(anchor = 'center', pady = 5)
text_question_answer_1.pack(
    anchor = 'center',
    fill = 'x',
    padx = 30,
)


# Create a divisor
create_horizontal_lines()

# Show chat history
def show_hide_chat_history(): 
    if history_frame.winfo_ismapped():
        history_frame.pack_forget()
        hide_help_the_developer()
        show_help_the_developer()
    else:
        history_frame.pack(fill = "x",
            pady = 10
        )
        hide_help_the_developer()
        show_help_the_developer()
# The chat history will be shown or hidden when the button is pressed.
button_show_hide_chat_history = tk.Button(
    content_frame, 
    text = "Show/Hide Chat History", 
    command = show_hide_chat_history
)
button_show_hide_chat_history.pack()
# Elements in history_frame
label_chat_history_1 = tk.Label(
    history_frame, 
    text = "Chat history:",
    font = ("Arial", 10),
)

label_chat_history_1.pack()
text_chat_history_1.pack(
    anchor = 'center',
    fill = 'x',
    padx = 30,
    pady = 10,
)

# Help the developer
def show_help_the_developer():
    label_help_the_developer_3.pack(padx = 30, pady = 0)
    label_help_the_developer_4.pack(padx = 30, pady = 10)
def hide_help_the_developer():
    label_help_the_developer_3.pack_forget()
    label_help_the_developer_4.pack_forget()

label_help_the_developer_3 = tk.Label(content_frame, text='Help the developer: PayPal Donation.', font=("Arial", 10), fg="blue", cursor="hand2")
label_help_the_developer_3.bind("<Button-1>", lambda e: callback("https://www.paypal.com/donate/?hosted_button_id=2F444HZGJBNX6"))
paypal_qr_code = ImageTk.PhotoImage(Image.open(resource_path("QR Code PayPal.png")))
label_help_the_developer_4 = tk.Label(content_frame, image = paypal_qr_code)
show_help_the_developer()

root.mainloop()

