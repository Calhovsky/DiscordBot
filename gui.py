import asyncio
import tkinter as tk

class GUI:
    def __init__(self, bot):
        self.bot = bot
        self.root = tk.Tk()
        self.root.title("Bot Control")
        
        self.stop_button = tk.Button(self.root, text="Stop Bot", command=self.stop_bot)
        self.stop_button.pack()

    def run(self):
        self.root.mainloop()

    def stop_bot(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self.bot.close())
        loop.close()