import tkinter as tk
from tkinter import ttk

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Society Manager")
        self.root.geometry("800x600")
        
        # Create main menu
        self.create_menu()
        
    def create_menu(self):
        # Create main menu buttons
        staff_btn = ttk.Button(self.root, text="Staff Management", 
                             command=self.open_staff_window)
        staff_btn.pack(pady=10)
        
        residents_btn = ttk.Button(self.root, text="Resident Management", 
                                 command=self.open_residents_window)
        residents_btn.pack(pady=10)
        
        bills_btn = ttk.Button(self.root, text="Bill Management", 
                             command=self.open_bills_window)
        bills_btn.pack(pady=10)
    
    def open_staff_window(self):
        # We'll implement these windows later
        print("Opening staff window")
    
    def open_residents_window(self):
        print("Opening residents window")
    
    def open_bills_window(self):
        print("Opening bills window")