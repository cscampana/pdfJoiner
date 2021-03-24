""""
PDF JOINER

Created by Caike Salles Campana - csallesc@ucsd.edu

Description:

    This program allows two PDF to be joined into one using the module PyPDF2 with a
    graphical user interface built with tkinter.

Usage:

    Click on each input box, select both pdf to be joined. After clicking on the button
    join, a new window asking for the name and location of the new pdf file will be displayed.
    Just select it, and as soon as the user clicks on save, the joining process will automaticly begin.

Technical information:

    Developed on Python 3.8
    Required dependencies: PyPDF2, tkinter
    Class: App
    Version: 0.1

License:

    This work is licensed under a Creative Commons Attribution 4.0 International License.

Contact information:

    Caike Salles Campana
    csallesc@ucsd.edu
    @ccampana_ on most social media websites

"""
import tkinter as tk
import tkinter.filedialog as fd
from tkinter import font
import tkinter.ttk as ttk
import os
import pdfJoiner


class App(tk.Tk):
    """
    This class define the graphical user interface of the program, using the
    package tkinter

    :parameter `tk.Tk`: the constructor of the tkinter package.
    """

    def __init__(self):
        """
        The default constructor of the class App. It defines the basic structure
        of the graphical user interface.

        :parameter `self`: the instance of the class.
        """
        super().__init__()

        self.title("PDF Utility")
        self.configure(background="#000000")
        self.icon = tk.PhotoImage(file="imgs/icon.png")
        self.iconphoto(False, self.icon)

        # Set the font to all the widgets,
        std_font = font.Font(family="Arial", size=14)
        self.option_add("*font", std_font)

        self.geometry("600x400")
        self.style = ttk.Style()
        self.style.configure('TLabel', background="#000000", foreground="#E5E5E5")
        self.style.configure('In.TLabel', foreground="#FCA311")
        self.style.configure('TEntry', foreground="#14213D")

        self.label_greet = ttk.Label(self, text="PDF Utility", style="In.TLabel")
        self.label_firstPDF = ttk.Label(self, text="First PDF File Location")
        self.entry_firstPDF = ttk.Entry(self)
        self.entry_firstPDF.bind("<1>", lambda pdf: self.choose_pdf(pdf, numpdf=1))

        self.label_secondPDF = ttk.Label(self, text="Second PDF File Location")
        self.entry_secondPDF = ttk.Entry(self)
        self.entry_secondPDF.bind("<1>", lambda pdf: self.choose_pdf(pdf, numpdf=2))

        self.btn_join = tk.Button(self, text="Join", command=self.join, background="#14213d", foreground="#FCA311")

        self.status_text = tk.StringVar()
        self.label_status = ttk.Label(self, textvariable=self.status_text)

        self.label_info = ttk.Label(self, text="Created by Caike S. Campana - csallesc@ucsd.edu", style="In.TLabel")

        # Padding options for each individual element in the window.
        options = {'pady': 5, 'padx': 5}
        self.label_greet.pack(pady=15)
        self.label_firstPDF.pack(pady=5)
        self.entry_firstPDF.pack(pady=5, ipady=5, ipadx=5)
        self.label_secondPDF.pack(pady=5)
        self.entry_secondPDF.pack(pady=5, ipady=5, ipadx=5)
        self.btn_join.pack(pady=20, ipady=10, ipadx=45)
        self.label_status.pack(**options)
        self.label_info.pack(**options)

    def choose_pdf(self, args, numpdf):
        """
            This method defines the action of opening the file and the setting the
            location of it to the corresponding entry.
            :parameter: `self`: The instance of the class.
            :parameter: `args`: additional arguments.
            :parameter: `numpdf`: the number of the entry.
        """
        filetypes = (("Portable Document Format (PDF)", "*.pdf"), ("All Files", "*"))
        filename = fd.askopenfilename(title="Choose the PDF file", initialdir=os.path.abspath(os.sep),
                                      filetypes=filetypes)
        if numpdf == 1:
            self.entry_firstPDF.delete(0, tk.END)
            self.entry_firstPDF.insert(0, filename)

        else:
            self.entry_secondPDF.delete(0, tk.END)
            self.entry_secondPDF.insert(0, filename)

    def join(self):
        """
        Gets the file location from the entries and instanciates the class pdfJoiner to
        execute the join of both pdfs. Saves in the specified location.

        :parameter: `self`: the instance of the class
        :return: if both files are not selected.
        """
        if len(self.entry_firstPDF.get()) == 0 or len(self.entry_secondPDF.get()) == 0:
            self.status_text.set("At least one input is empty")
            return

        file_output = fd.asksaveasfile(title="Choose Location and Name to save the merged PDF",
                                       defaultextension='.pdf', filetypes=[("Portable Document Format (PDF)", '*.pdf')],
                                       initialdir=os.path.abspath(os.sep))
        pdfJoiner.merger_pdf(self.entry_firstPDF.get(), self.entry_secondPDF.get(), file_output.name)
        self.status_text.set("")


if __name__ == '__main__':
    app = App()
    app.mainloop()
