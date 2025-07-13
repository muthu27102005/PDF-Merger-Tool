# # PDF Merger Tool 
# #importing necessary libraries
# import tkinter as tk
# from tkinter import filedialog, messagebox
# from PyPDF2 import PdfMerger
# import os

# #creating class called PDFMergerApp
# #This class will handle the GUI and PDF merging functionality
# class PDFMergerApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("PDF Merger Tool")
#         self.pdf_files = []

#         # Buttons for selecting and merging PDFs
#         tk.Button(root, text="Select PDFs", command=self.select_pdfs, width=30).pack(pady=10)
#         tk.Button(root, text="Merge PDFs", command=self.merge_pdfs, width=30).pack(pady=10)
#         tk.Button(root, text='EXIT', command=root.quit, width=30).pack(pady=10)

#         # Display selected files
#         self.files_label = tk.Label(root, text="No files selected", fg="gray", wraplength=300)
#         self.files_label.pack(pady=10)

#     def select_pdfs(self):
#         self.pdf_files = filedialog.askopenfilenames(
#             title="Select PDF Files",
#             filetypes=[("PDF Files", "*.pdf")]
#         )
        
#         if self.pdf_files:
#             file_names = "\n".join(os.path.basename(f) for f in self.pdf_files)
#             self.files_label.config(text=f"Selected:\n{file_names}", fg="black")
#         else:
#             self.files_label.config(text="No files selected", fg="gray")

#     def merge_pdfs(self):
#         if not self.pdf_files:
#             messagebox.showerror("Error", "No PDF files selected.")
#             return

#         output_path = filedialog.asksaveasfilename(
#             defaultextension=".pdf",
#             filetypes=[("PDF Files", "*.pdf")],
#             title="Save Merged PDF As"
#         )

#         if not output_path:
#             return  # User cancelled

#         try:
#             merger = PdfMerger()
#             for file in self.pdf_files:
#                 merger.append(file)
#             merger.write(output_path)
#             merger.close()
#             messagebox.showinfo("Success", f"PDFs merged successfully into:\n{output_path}")
#         except Exception as e:
#             messagebox.showerror("Error", f"Failed to merge PDFs:\n{e}")

# # Run the app
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = PDFMergerApp(root)
#     root.mainloop()

# import tkinter as tk
# from tkinter import filedialog, messagebox
# from PyPDF2 import PdfMerger
# import os

# class PDFMergerApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("PDF Merger Tool")
#         self.pdf_files = []

#         # Select button
#         tk.Button(root, text="Select PDFs", command=self.select_pdfs, width=30).pack(pady=5)

#         # Listbox to display selected files
#         self.listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=50)
#         self.listbox.pack(pady=5)

#         # Remove button
#         tk.Button(root, text="Remove Selected PDF", command=self.remove_selected, width=30).pack(pady=5)

#         # Merge button
#         tk.Button(root, text="Merge PDFs", command=self.merge_pdfs, width=30).pack(pady=10)
        
#         # Exit button
#         tk.Button(root, text='EXIT', command=root.quit, width=30).pack(pady=5)
#     def select_pdfs(self):
#         files = filedialog.askopenfilenames(title="Select PDF Files", filetypes=[("PDF Files", "*.pdf")])
#         if files:
#             self.pdf_files.extend(files)
#             self.update_listbox()

#     def update_listbox(self):
#         self.listbox.delete(0, tk.END)
#         for file in self.pdf_files:
#             self.listbox.insert(tk.END, os.path.basename(file))

#     def remove_selected(self):
#         selected_index = self.listbox.curselection()
#         if selected_index:
#             del self.pdf_files[selected_index[0]]
#             self.update_listbox()
#         else:
#             messagebox.showwarning("Warning", "Please select a file to remove.")

#     def merge_pdfs(self):
#         if not self.pdf_files:
#             messagebox.showerror("Error", "No PDF files selected.")
#             return

#         output_path = filedialog.asksaveasfilename(defaultextension=".pdf",
#                                                    filetypes=[("PDF Files", "*.pdf")],
#                                                    title="Save Merged PDF As")
#         if not output_path:
#             return

#         try:
#             merger = PdfMerger()
#             for file in self.pdf_files:
#                 merger.append(file)
#             merger.write(output_path)
#             merger.close()
#             messagebox.showinfo("Success", f"PDFs merged into:\n{output_path}")
#         except Exception as e:
#             messagebox.showerror("Error", f"Failed to merge PDFs:\n{e}")

# # Run the app
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = PDFMergerApp(root)
#     root.mainloop()


# import tkinter as tk
# from tkinter import filedialog, messagebox
# from PyPDF2 import PdfMerger
# import os

# class PDFMergerApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("PDF Merger Tool")
#         self.pdf_files = []

#         # Select PDFs
#         tk.Button(root, text="Select PDFs", command=self.select_pdfs, width=30).pack(pady=5)

#         # Listbox
#         self.listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=50)
#         self.listbox.pack(pady=5)

#         # Remove, Up, Down Buttons
#         btn_frame = tk.Frame(root)
#         btn_frame.pack(pady=5)

#         tk.Button(btn_frame, text="Remove Selected", command=self.remove_selected).grid(row=0, column=0, padx=5)
#         tk.Button(btn_frame, text="Move Up", command=self.move_up).grid(row=0, column=1, padx=5)
#         tk.Button(btn_frame, text="Move Down", command=self.move_down).grid(row=0, column=2, padx=5)

#         # Merge button
#         tk.Button(root, text="Merge PDFs", command=self.merge_pdfs, width=30).pack(pady=10)

#     def select_pdfs(self):
#         files = filedialog.askopenfilenames(title="Select PDF Files", filetypes=[("PDF Files", "*.pdf")])
#         if files:
#             self.pdf_files.extend(files)
#             self.update_listbox()

#     def update_listbox(self):
#         self.listbox.delete(0, tk.END)
#         for file in self.pdf_files:
#             self.listbox.insert(tk.END, os.path.basename(file))

#     def remove_selected(self):
#         index = self.listbox.curselection()
#         if index:
#             del self.pdf_files[index[0]]
#             self.update_listbox()
#         else:
#             messagebox.showwarning("Warning", "Please select a file to remove.")

#     def move_up(self):
#         index = self.listbox.curselection()
#         if index and index[0] > 0:
#             i = index[0]
#             self.pdf_files[i - 1], self.pdf_files[i] = self.pdf_files[i], self.pdf_files[i - 1]
#             self.update_listbox()
#             self.listbox.select_set(i - 1)

#     def move_down(self):
#         index = self.listbox.curselection()
#         if index and index[0] < len(self.pdf_files) - 1:
#             i = index[0]
#             self.pdf_files[i + 1], self.pdf_files[i] = self.pdf_files[i], self.pdf_files[i + 1]
#             self.update_listbox()
#             self.listbox.select_set(i + 1)

#     def merge_pdfs(self):
#         if not self.pdf_files:
#             messagebox.showerror("Error", "No PDF files selected.")
#             return

#         output_path = filedialog.asksaveasfilename(defaultextension=".pdf",
#                                                    filetypes=[("PDF Files", "*.pdf")],
#                                                    title="Save Merged PDF As")
#         if not output_path:
#             return

#         try:
#             merger = PdfMerger()
#             for file in self.pdf_files:
#                 merger.append(file)
#             merger.write(output_path)
#             merger.close()
#             messagebox.showinfo("Success", f"PDFs merged into:\n{output_path}")
#         except Exception as e:
#             messagebox.showerror("Error", f"Failed to merge PDFs:\n{e}")

# # Run the app
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = PDFMergerApp(root)
#     root.mainloop()


import tkinter as tk
from tkinter import filedialog, messagebox
from tkinterdnd2 import DND_FILES, TkinterDnD
from PyPDF2 import PdfMerger
import os

class PDFMergerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Merger Tool")
        self.pdf_files = []

        # Drag-and-drop support
        self.root.drop_target_register(DND_FILES)
        self.root.dnd_bind('<<Drop>>', self.drop_files)

        # Buttons and listbox
        tk.Button(root, text="Select PDFs", command=self.select_pdfs, width=30).pack(pady=5)

        self.listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=50)
        self.listbox.pack(pady=5)

        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=5)

        tk.Button(btn_frame, text="Remove Selected", command=self.remove_selected).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Move Up", command=self.move_up).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Move Down", command=self.move_down).grid(row=0, column=2, padx=5)

        tk.Button(root, text="Merge PDFs", command=self.merge_pdfs, width=30).pack(pady=10)

    def select_pdfs(self):
        files = filedialog.askopenfilenames(title="Select PDF Files", filetypes=[("PDF Files", "*.pdf")])
        if files:
            self.pdf_files.extend(files)
            self.update_listbox()

    def drop_files(self, event):
        dropped_files = self.root.tk.splitlist(event.data)
        for file in dropped_files:
            if file.lower().endswith(".pdf"):
                self.pdf_files.append(file)
        self.update_listbox()

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for file in self.pdf_files:
            self.listbox.insert(tk.END, os.path.basename(file))

    def remove_selected(self):
        index = self.listbox.curselection()
        if index:
            del self.pdf_files[index[0]]
            self.update_listbox()
        else:
            messagebox.showwarning("Warning", "Please select a file to remove.")

    def move_up(self):
        index = self.listbox.curselection()
        if index and index[0] > 0:
            i = index[0]
            self.pdf_files[i - 1], self.pdf_files[i] = self.pdf_files[i], self.pdf_files[i - 1]
            self.update_listbox()
            self.listbox.select_set(i - 1)

    def move_down(self):
        index = self.listbox.curselection()
        if index and index[0] < len(self.pdf_files) - 1:
            i = index[0]
            self.pdf_files[i + 1], self.pdf_files[i] = self.pdf_files[i], self.pdf_files[i + 1]
            self.update_listbox()
            self.listbox.select_set(i + 1)

    def merge_pdfs(self):
        if not self.pdf_files:
            messagebox.showerror("Error", "No PDF files selected.")
            return

        output_path = filedialog.asksaveasfilename(defaultextension=".pdf",
                                                   filetypes=[("PDF Files", "*.pdf")],
                                                   title="Save Merged PDF As")
        if not output_path:
            return

        try:
            merger = PdfMerger()
            for file in self.pdf_files:
                merger.append(file)
            merger.write(output_path)
            merger.close()
            messagebox.showinfo("Success", f"PDFs merged into:\n{output_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to merge PDFs:\n{e}")

# Run the app with drag-and-drop support
if __name__ == "__main__":
    root = TkinterDnD.Tk()
    app = PDFMergerApp(root)
    root.mainloop()
