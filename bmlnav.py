import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os

SOURCEDATA_TYPES = ["alphaomega", "audio", "ct", "fluoro", "notes", "ripple", "task"]
DERIVATIVE_TYPES = ["annot", "ecoglog", "fieldtrip", "freesurfer", "preproc", "spikesorting"]
DATA_STAGES = ["derivatives", "groupanalyses", "sourcedata"]
EXTENSIONS = [".tsv", ".pdf"]

def browse_folder():
    folder_path = filedialog.askdirectory()
    folder_path_var.set(folder_path)


def open_file(is_folder=False):
    base_folder = folder_path_var.get()
    session_id = session_id_var.get()
    der_folder  = der_foldername_var.get()
    src_folder = sourcedata_type_var.get()
    task = task_id_var.get()
    sub = subject_id_var.get()
    ses = session_id_var.get()
    ext = extension_var.get()
    suf = file_suffix_var.get()

    # try derivatives
    file_names = [f"sub-{sub}_ses-{ses}_task-{task}_{suf}", \
                  f"sub-{sub}_ses-{ses}_{suf}", \
                  f"sub-{sub}_{suf}"]
    file_names = [f"{fn}{ext}" for ext in EXTENSIONS for fn in file_names]

    # derivatives, source data
    folders = [ f"{base_folder}/{data_class_var.get()}/sub-{sub}/ses-{ses}/{src_folder}", \
                f"{base_folder}/{data_class_var.get()}/sub-{sub}/{der_folder}"
                ]

    if is_folder:
        paths = folders
    else: 
        paths = [f"{fol}/{fn}" for fol in folders for fn in file_names]

    for p in paths:
        if os.path.exists(p):  
            print(f"Opening file: {p}")          
            os.system(f"open {p}")
            return
        else:
            print(f"File not found: {p}")    

     

    # # try sourcedata
    # folder = 
    # for f in file_names:
    #     if is_folder: p = folder 
    #     else: p = f"{folder}/{f}" 
    #     if os.path.exists(p):  
    #         print(f"Opening file: {p}")          
    #         os.system(f"open {p}")
    #         return
    #     else:
    #         print(f"File not found: {p}")  


root = tk.Tk()
root.title("Data File Selector")

folder_path_var = tk.StringVar()
subject_id_var = tk.StringVar()
session_id_var = tk.StringVar()
task_id_var = tk.StringVar()
data_class_var = tk.StringVar()
der_foldername_var = tk.StringVar() # the folder name within derivatives that you're looking for
file_suffix_var = tk.StringVar() # the folder name within derivatives that you're looking for
extension_var = tk.StringVar() # the folder name within derivatives that you're looking for

full_path = tk.StringVar() # the folder name within derivatives that you're looking for

sourcedata_type_var = tk.StringVar()

# set defaults for these variables
folder_path_var.set("/Volumes/Nexus4/DBS")
subject_id_var.set("DM1020")
session_id_var.set("intraop")
task_id_var.set("lombard")

data_class_var.set("derivatives")
der_foldername_var.set("")
file_suffix_var.set("channels")
extension_var.set("tsv")

sourcedata_type_var.set("")



ir = 0 # indexes of rows and colums
ic = 0 
ttk.Label(root, text="Select Folder:").grid(column=0, row=ir)
ttk.Entry(root, textvariable=folder_path_var).grid(column=1, row=ir)
ttk.Button(root, text="Browse", command=browse_folder).grid(column=2, row=ir)

# # Create and pack widgets
# entry_subject_id = tk.Entry(root, width=20)
# entry_subject_id.pack(pady=5)
# entry_subject_id.insert(0, "subject_id")
ir+=1 
ttk.Label(root, text="Session ID:").grid(column=0, row=ir)
ttk.Combobox(root, textvariable=session_id_var, values=["preop", "intraop", "training"]).grid(column=1, row=ir)

ir+=1 
ttk.Label(root, text="Task ID:").grid(column=0, row=ir)
ttk.Combobox(root, textvariable=task_id_var, values=["lombard", "smsl"]).grid(column=1, row=ir)

ir+=1 
ttk.Label(root, text="Subject ID:").grid(column=0, row=ir)
ttk.Entry(root, textvariable=subject_id_var).grid(column=1, row=ir)




ir+=2
ttk.Label(root, text="Data Stage:").grid(column=0, row=ir)
ttk.Combobox(root, textvariable=data_class_var, values=DATA_STAGES).grid(column=1, row=ir)

ir+=1 
ttk.Label(root, text="Derivative folder:").grid(column=0, row=ir)
ttk.Combobox(root, textvariable=der_foldername_var, values=DERIVATIVE_TYPES).grid(column=1, row=ir)

ir+=1
ttk.Label(root, text="Sourcedata folder:").grid(column=0, row=ir)
ttk.Combobox(root, textvariable=sourcedata_type_var, values=SOURCEDATA_TYPES).grid(column=1, row=ir)


# ir+=1
# ttk.Label(root, text="Source folder:").grid(column=0, row=ir)
# ttk.Combobox(root, textvariable=sourcedata_type_var, values=SOURCEDATA_TYPES).grid(column=1, row=ir)



ir+=2
ttk.Label(root, text="File suffix:").grid(column=0, row=ir)
ttk.Entry(root, textvariable=file_suffix_var).grid(column=1, row=ir)
 
ir+=1
ttk.Button(root, text="Open File", command=open_file).grid(column=2, row=ir)
ir+=1
ttk.Button(root, text="Open Folder", command=lambda: open_file(is_folder=True)).grid(column=2, row=ir)



col_count, row_count = root.grid_size()
for col in range(col_count):
    root.grid_columnconfigure(col, minsize=200)
for row in range(row_count):
    root.grid_rowconfigure(row, minsize=40)


root.mainloop()
