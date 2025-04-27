"""
File Organizer на Python (tkinter) — сортировка файлов в выбранной папке по категориям.
Работает под Python 3 на macOS без дополнительных библиотек.
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
import shutil
import threading

# ---------------------- Настройка категорий файлов ----------------------
# Словарь FILE_CATEGORIES: ключ — название категории/папки, значение — список расширений.
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".flv"],
    "Music": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z", ".dmg"],
    # Прочие расширения попадут в раздел "Others"
}
# ------------------------------------------------------------------------


class FileOrganizerApp:
    def __init__(self, root):
        self.root = root
        root.title("File Organizer")
        root.geometry("500x250")  # Размер окна (можно настроить)
        root.resizable(False, False)

        try:
            icon = tk.PhotoImage(file="logo.png")
            root.iconphoto(True, icon)
        except Exception as e:
            print(f"Could not load icon: {e}")

        # Флаг для отмены сортировки
        self.cancelled = False

        # Переменные интерфейса
        self.selected_folder = tk.StringVar()
        self.progress_var = tk.DoubleVar()

        # Стилизация (тема)
        style = ttk.Style()
        style.theme_use('vista')  # Можно выбрать 'alt', 'default', 'clam' и т.д.
        style.configure("TButton", padding=6)
        style.configure("TLabel", padding=6)
        style.configure("TEntry", padding=6)

        # Построение интерфейса
        self._build_ui()

    def _build_ui(self):
        """Создаёт и размещает виджеты."""
        # Метка заголовка
        title = ttk.Label(self.root, text="Файловый органайзер", font=("Helvetica", 16))
        title.pack(pady=(10, 10))

        # Кнопка выбора папки и поле с путём
        select_frame = ttk.Frame(self.root)
        select_frame.pack(pady=5, padx=10, fill='x')
        btn_select = ttk.Button(select_frame, text="Выбрать папку...", command=self.select_folder)
        btn_select.pack(side="left")
        entry_folder = ttk.Entry(select_frame, textvariable=self.selected_folder, state='readonly')
        entry_folder.pack(side="left", fill='x', expand=True, padx=(5, 0))

        # ProgressBar
        self.progress = ttk.Progressbar(self.root, orient='horizontal', mode='determinate',
                                        variable=self.progress_var, maximum=100)
        self.progress.pack(fill='x', padx=10, pady=10)

        # Кнопки «Сортировать» и «Отменить»
        btn_frame = ttk.Frame(self.root)
        btn_frame.pack(pady=5)
        self.btn_sort = ttk.Button(btn_frame, text="Сортировать", command=self.start_sorting)
        self.btn_sort.pack(side="left", padx=5)
        self.btn_cancel = ttk.Button(btn_frame, text="Отменить", command=self.cancel_sorting, state='disabled')
        self.btn_cancel.pack(side="left", padx=5)

    def select_folder(self):
        """Обработчик кнопки выбора папки."""
        folder = filedialog.askdirectory(title="Выберите папку для сортировки")
        if folder:
            # Заменим символы '/' на системный разделитель на всякий случай
            folder = os.path.normpath(folder)
            self.selected_folder.set(folder)

    def start_sorting(self):
        """Запускает процесс сортировки файлов в отдельном потоке."""
        folder = self.selected_folder.get()
        if not folder or not os.path.isdir(folder):
            messagebox.showwarning("Предупреждение", "Сначала выберите корректную папку.")
            return

        # Готовим список файлов (только файлы, без директорий)
        self.files_to_sort = [f for f in os.listdir(folder)
                              if os.path.isfile(os.path.join(folder, f))]
        total = len(self.files_to_sort)
        if total == 0:
            messagebox.showinfo("Информация", "В папке нет файлов для сортировки.")
            return

        # Блокируем кнопку «Сортировать» и активируем «Отменить»
        self.btn_sort.config(state='disabled')
        self.btn_cancel.config(state='enabled')
        self.progress_var.set(0)
        self.cancelled = False

        # Запускаем фоновую сортировку в потоке
        threading.Thread(target=self._sort_files_thread, args=(folder,), daemon=True).start()

    def _sort_files_thread(self, folder):
        """Фоновая функция: сортирует файлы и обновляет ProgressBar."""
        total = len(self.files_to_sort)
        done = 0

        for filename in self.files_to_sort:
            if self.cancelled:
                break

            src_path = os.path.join(folder, filename)
            moved = False
            # Определяем категорию по расширению
            ext = os.path.splitext(filename)[1].lower()
            for category, extensions in FILE_CATEGORIES.items():
                if ext in extensions:
                    dest_dir = os.path.join(folder, category)
                    os.makedirs(dest_dir, exist_ok=True)  # Создать папку, если нужно&#8203;:contentReference[oaicite:9]{index=9}
                    shutil.move(src_path, os.path.join(dest_dir, filename))  # Переместить файл&#8203;:contentReference[oaicite:10]{index=10}
                    moved = True
                    break
            # Если в ни одной категории не попал — в Others
            if not moved:
                other_dir = os.path.join(folder, "Others")
                os.makedirs(other_dir, exist_ok=True)
                shutil.move(src_path, os.path.join(other_dir, filename))

            done += 1
            # Обновляем индикатор (через главную нить)
            progress_percent = done / total * 100
            self.root.after(0, self.progress_var.set, progress_percent)

        # После завершения (или отмены) вернуть кнопки в исходное состояние
        self.root.after(0, self._finish_sorting)

    def cancel_sorting(self):
        """Устанавливает флаг отмены сортировки."""
        self.cancelled = True
        self.btn_cancel.config(state='disabled')

    def _finish_sorting(self):
        """Сброс интерфейса после завершения."""
        if self.cancelled:
            messagebox.showinfo("Отменено", "Сортировка была отменена.")
        else:
            messagebox.showinfo("Готово", "Сортировка завершена успешно.")
        self.btn_sort.config(state='enabled')
        self.btn_cancel.config(state='disabled')
        self.progress_var.set(0)


if __name__ == "__main__":
    root = tk.Tk()
    app = FileOrganizerApp(root)
    root.mainloop()
