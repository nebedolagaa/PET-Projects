"""
File Organizer in Python (tkinter) — sorting files in a selected folder by categories.
Works with Python 3 on macOS without additional libraries.
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
import shutil
import threading

# ---------------------- File categories configuration ----------------------
# FILE_CATEGORIES dictionary: key — category/folder name, value — list of extensions.
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".flv"],
    "Music": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z", ".dmg"],
    # Other extensions will go to "Others" section
}
# ------------------------------------------------------------------------


class FileOrganizerApp:
    def __init__(self, root):
        self.root = root
        root.title("File Organizer")
        root.geometry("500x250")  # Window size (can be customized)
        root.resizable(False, False)

        try:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            logo_path = os.path.join(script_dir, "logo.png")
            icon = tk.PhotoImage(file=logo_path)
            root.iconphoto(True, icon)
        except Exception as e:
            print(f"Could not load icon: {e}")

        # Flag for canceling sorting
        self.cancelled = False

        # Interface variables
        self.selected_folder = tk.StringVar()
        self.progress_var = tk.DoubleVar()

        # Styling (theme)
        style = ttk.Style()
        style.theme_use('vista')  # Can choose 'alt', 'default', 'clam', etc.
        style.configure("TButton", padding=6)
        style.configure("TLabel", padding=6)
        style.configure("TEntry", padding=6)

        # Building the interface
        self._build_ui()

    def _build_ui(self):
        """Creates and places widgets."""
        # Title label
        title = ttk.Label(self.root, text="File Organizer", font=("Helvetica", 16))
        title.pack(pady=(10, 10))

        # Folder selection button and path field
        select_frame = ttk.Frame(self.root)
        select_frame.pack(pady=5, padx=10, fill='x')
        btn_select = ttk.Button(select_frame, text="Select Folder...", command=self.select_folder)
        btn_select.pack(side="left")
        entry_folder = ttk.Entry(select_frame, textvariable=self.selected_folder, state='readonly')
        entry_folder.pack(side="left", fill='x', expand=True, padx=(5, 0))

        # ProgressBar
        self.progress = ttk.Progressbar(self.root, orient='horizontal', mode='determinate',
                                        variable=self.progress_var, maximum=100)
        self.progress.pack(fill='x', padx=10, pady=10)

        # "Sort" and "Cancel" buttons
        btn_frame = ttk.Frame(self.root)
        btn_frame.pack(pady=5)
        self.btn_sort = ttk.Button(btn_frame, text="Sort", command=self.start_sorting)
        self.btn_sort.pack(side="left", padx=5)
        self.btn_cancel = ttk.Button(btn_frame, text="Cancel", command=self.cancel_sorting, state='disabled')
        self.btn_cancel.pack(side="left", padx=5)

    def select_folder(self):
        """Handler for the folder selection button."""
        folder = filedialog.askdirectory(title="Select folder for sorting")
        if folder:
            # Replace '/' characters with system separator just in case
            folder = os.path.normpath(folder)
            self.selected_folder.set(folder)

    def start_sorting(self):
        """Starts the file sorting process in a separate thread."""
        folder = self.selected_folder.get()
        if not folder or not os.path.isdir(folder):
            messagebox.showwarning("Warning", "Please select a valid folder first.")
            return

        # Prepare list of files (files only, no directories)
        self.files_to_sort = [f for f in os.listdir(folder)
                              if os.path.isfile(os.path.join(folder, f))]
        total = len(self.files_to_sort)
        if total == 0:
            messagebox.showinfo("Information", "No files to sort in the folder.")
            return

        # Disable "Sort" button and enable "Cancel"
        self.btn_sort.config(state='disabled')
        self.btn_cancel.config(state='enabled')
        self.progress_var.set(0)
        self.cancelled = False

        # Start background sorting in a thread
        threading.Thread(target=self._sort_files_thread, args=(folder,), daemon=True).start()

    def _sort_files_thread(self, folder):
        """Background function: sorts files and updates the ProgressBar."""
        total = len(self.files_to_sort)
        done = 0

        for filename in self.files_to_sort:
            if self.cancelled:
                break

            src_path = os.path.join(folder, filename)
            moved = False
            # Determine category by extension
            ext = os.path.splitext(filename)[1].lower()
            for category, extensions in FILE_CATEGORIES.items():
                if ext in extensions:
                    dest_dir = os.path.join(folder, category)
                    os.makedirs(dest_dir, exist_ok=True)  # Create folder if needed
                    shutil.move(src_path, os.path.join(dest_dir, filename))  # Move the file
                    moved = True
                    break
            # If file doesn't match any category — move to Others
            if not moved:
                other_dir = os.path.join(folder, "Others")
                os.makedirs(other_dir, exist_ok=True)
                shutil.move(src_path, os.path.join(other_dir, filename))

            done += 1
            # Update indicator (through the main thread)
            progress_percent = done / total * 100
            self.root.after(0, self.progress_var.set, progress_percent)

        # After completion (or cancellation) return buttons to initial state
        self.root.after(0, self._finish_sorting)

    def cancel_sorting(self):
        """Sets the flag to cancel sorting."""
        self.cancelled = True
        self.btn_cancel.config(state='disabled')

    def _finish_sorting(self):
        """Reset interface after completion."""
        if self.cancelled:
            messagebox.showinfo("Canceled", "Sorting was canceled.")
        else:
            messagebox.showinfo("Done", "Sorting completed successfully.")
        self.btn_sort.config(state='enabled')
        self.btn_cancel.config(state='disabled')
        self.progress_var.set(0)


if __name__ == "__main__":
    root = tk.Tk()
    app = FileOrganizerApp(root)
    root.mainloop()
