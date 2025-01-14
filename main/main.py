import tkinter as tk
from gui.main_window import MainWindow
from database.database import Database

def main():
    # Initialize database
    db = Database()
    
    # Create main window
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()
    

   