import threading
import tkinter as tk
from tkinter import ttk
from time import sleep


class App:
    """
    Represents a single instance of a stopwatch applicaton.
    """
    def __init__(self):
        """
        Initializes the app window, dimentions and ui elements.
        """
        self.window = tk.Tk()
        self.window.title("Stopwatch")
        self.window.geometry("300x200")
        self.window.resizable(False, False)
        self.FONT = ("Trebuchet MS", 30)

        self.timer_text = ttk.Label(self.window, text="00:00:00", font=self.FONT)
        self.timer_text.place(relx=0.5, rely=0.3, anchor="center")

        self.start_stop_button = ttk.Button(self.window, text="Start", command=self.start_stop)
        self.start_stop_button.place(relx=0.3, rely=0.6, anchor="center")

        self.reset_button = ttk.Button(self.window, text="Reset", command=self.reset)
        self.reset_button.place(relx=0.7, rely=0.6, anchor="center")

        self.timer_running: bool = False
        self.current_time: int = 0

        self.window.mainloop()
    
    def start_stop(self) -> None:
        """
        Starts the timer if it is not running, stops it if it is.
        """
        if self.timer_running:
            self.timer_running = False
            self.start_stop_button.config(text="Start")
        else:
            self.timer_running = True
            self.start_stop_button.config(text="Stop")
            thread = threading.Thread(target=self.start)
            thread.start()

    def update_time_text(self, hour: int, min: int, sec:int) -> None:
        """
        Update the timer text with the given time.

        :param hour: a number of hours
        :param min: a number of minutes
        :param sec: a number of seconds
        """
        time_text: str = f"{hour:02d}:{min:02d}:{sec:02d}"
        self.timer_text.config(text=time_text)

    def start(self) -> None:
        """
        Starts the timer.
        """
        hours, minutes, seconds = 0, 0, 0

        while self.timer_running:
            minutes, seconds = divmod(self.current_time, 60)
            hours, minutes = divmod(minutes, 60)

            self.update_time_text(hours, minutes, seconds)

            sleep(1)
            self.current_time += 1
  
    def reset(self) -> None:
        """
        Resets the timer to zero.
        """
        self.current_time = 0
        self.update_time_text(0, 0, 0)

        self.timer_running = False
        self.start_stop_button.config(text="Start")
     
     
if __name__ == "__main__":
    stopwatch: App = App()
    stopwatch.timer_running = False