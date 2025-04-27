# File Organizer

A simple program to organize files in a selected folder into categories (images, documents, videos, music, archives, and others).  
Developed using **Python** and the standard **tkinter** library for the graphical user interface.

## About the Project

I created this project to practice building GUI applications with Python and to help organize file systems.  
The program allows you to quickly tidy up any folder by automatically sorting files into subfolders based on their extensions.

Features:

- Select a folder through a dialog window.
- Automatically sort files into predefined categories.
- Move files into corresponding folders (Images, Documents, Videos, Music, Archives, Others).
- Progress bar indicating the sorting progress.
- Ability to cancel sorting at any time.
- Clean and simple graphical interface using `tkinter` and `ttk`.
- Works without any third-party libraries (only Python's standard modules are used).

## Technologies

- Python 3.x
- tkinter / ttk
- os, shutil, threading

## How to Use

1. Download or clone the repository.
2. Make sure Python 3 is installed.
3. Run the file:

```bash
python file_organizer.py
```

4. In the opened window, click "Select Folder...", choose a folder to organize, and click "Organize".

> ⚡ You can cancel the process anytime by clicking "Cancel".

## Notes

- The program moves files into new folders. Make sure you select the correct directory.
- If a file’s extension doesn’t match any predefined category, it will be moved to the `Others` folder.
- On macOS, you might need to grant Python permission to access files and folders through your system settings.

## Screenshots

*(Add screenshots of the interface here if you want)*

## License

This project is released without a license (free to use). You are free to use and modify the code for your own needs.
