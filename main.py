# PDF Merger Tool 
#importing necessary libraries
import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfMerger
import os

#creating class called PDFMergerApp
#This class will handle the GUI and PDF merging functionality
class PDFMergerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Merger Tool")
        self.pdf_files = []

        # Buttons for selecting and merging PDFs
        tk.Button(root, text="Select PDFs", command=self.select_pdfs, width=30).pack(pady=10)
        tk.Button(root, text="Merge PDFs", command=self.merge_pdfs, width=30).pack(pady=10)
        tk.Button(root, text='EXIT', command=root.quit, width=30).pack(pady=10)

        # Display selected files
        self.files_label = tk.Label(root, text="No files selected", fg="gray", wraplength=300)
        self.files_label.pack(pady=10)

    def select_pdfs(self):
        self.pdf_files = filedialog.askopenfilenames(
            title="Select PDF Files",
            filetypes=[("PDF Files", "*.pdf")]
        )
        
        if self.pdf_files:
            file_names = "\n".join(os.path.basename(f) for f in self.pdf_files)
            self.files_label.config(text=f"Selected:\n{file_names}", fg="black")
        else:
            self.files_label.config(text="No files selected", fg="gray")

    def merge_pdfs(self):
        if not self.pdf_files:
            messagebox.showerror("Error", "No PDF files selected.")
            return

        output_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF Files", "*.pdf")],
            title="Save Merged PDF As"
        )

        if not output_path:
            return  # User cancelled

        try:
            merger = PdfMerger()
            for file in self.pdf_files:
                merger.append(file)
            merger.write(output_path)
            merger.close()
            messagebox.showinfo("Success", f"PDFs merged successfully into:\n{output_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to merge PDFs:\n{e}")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = PDFMergerApp(root)
    root.mainloop()
