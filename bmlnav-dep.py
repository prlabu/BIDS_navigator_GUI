import tkinter as tk
from tkinter import filedialog
import os

def open_file():
    subject_id = entry_subject_id.get()
    session_id = entry_session_id.get()
    task_id = entry_task_id.get()
    run_id = entry_run_id.get()

    base_path = "/Volumes/Nexus4/DBS"
    file_name = f"sub-{subject_id}_ses-{session_id}_task-{task_id}_run-{run_id}"
    
    # Set your preferred file extensions here
    file_extensions = [".tsv", ".pdf"]

    for ext in file_extensions:
        file_path = os.path.join(base_path, file_name + ext)
        if os.path.isfile(file_path):
            os.system(f"open {file_path}")
            break

# Create the main window
root = tk.Tk()
root.title("BIDS File Navigator")

# Create and pack widgets
entry_subject_id = tk.Entry(root, width=20)
entry_subject_id.pack(pady=5)
entry_subject_id.insert(0, "subject_id")

entry_session_id = tk.Entry(root, width=20)
entry_session_id.pack(pady=5)
entry_session_id.insert(0, "session_id")

entry_task_id = tk.Entry(root, width=20)
entry_task_id.pack(pady=5)
entry_task_id.insert(0, "task_id")

entry_run_id = tk.Entry(root, width=20)
entry_run_id.pack(pady=5)
entry_run_id.insert(0, "run_id")

open_button = tk.Button(root, text="Open", command=open_file)
open_button.pack(pady=5)

# Start the main loop
root.mainloop()
