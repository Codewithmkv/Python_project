import tkinter as tk
from tkinter import scrolledtext

class Chatbot:
    def __init__(self):
        self.responses = {
            "hi": "Hello! How can I help you?",
            "how are you": "I'm good, thank you for asking! and How are you?",
            "i am fine": "Ok its great, I am always here to help you",
            "default": "Sorry, I didn't understand that."
        }

    def respond(self, message):
        return self.responses.get(message.lower(), self.responses["default"])

class ChatbotGUI:
    def __init__(self, master):
        self.master = master
        master.title("Chatbot")
        master.config(bg="lightblue")

        self.chatbot = Chatbot()
        

        self.chat_history = scrolledtext.ScrolledText(master, width=150, height=35)
        self.chat_history.grid(row=0, column=0, padx=150, pady=70, columnspan=2)

        self.user_input = tk.Entry(master, width=100,font=13)
        self.user_input.grid(row=1, column=0, padx=130, pady=5)
        self.chat_history.grid(ipadx=30,ipady=20)

        self.send_button = tk.Button(master, text="Send", command=self.send_message, font=30,bg="blue")
        self.send_button.grid(row=1, column=1, padx=5, pady=10, )
        

    def send_message(self):
        message = self.user_input.get()
        self.user_input.delete(0, tk.END)
        response = self.chatbot.respond(message)
        self.update_chat_history(message, response)

    def update_chat_history(self, user_message, bot_response):
        self.chat_history.configure(state='normal')
        self.chat_history.insert(tk.END, "You: " + user_message + "\n")
        self.chat_history.insert(tk.END, "Bot: " + bot_response + "\n\n")
        self.chat_history.configure(state='disabled')
        self.chat_history.yview(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    chatbot_gui = ChatbotGUI(root)
    root.mainloop()
