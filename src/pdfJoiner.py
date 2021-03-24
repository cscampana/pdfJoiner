""""
PDF JOINER

Created by Caike Salles Campana - csallesc@ucsd.edu

Description:

    This file contains a single function that is executes the joining process. It uses the
    package PyPDF2 and it was design to act with the file main.py.

Technical information:

    Developed on Python 3.8
    Required dependencies: PyPDF2
    Version: 0.1

License:

    This work is licensed under a Creative Commons Attribution 4.0 International License.

Contact information:

    Caike Salles Campana
    csallesc@ucsd.edu
    @ccampana_ on most social media websites

"""

import PyPDF2


def merger_pdf(pdfone_path, pdftwo_path, file_output):
    """
    Using the information of the first and second pdf locations, we output a merged
    one with the name and location specified in the variable file_output.

    :param: `pdfone_path`: the first pdf path.
    :param: `pdftwo_path`: the second pdf path.
    :param: `file_output`: the output name and location.
    """
    merged = PyPDF2.PdfFileMerger()

    merged.append(PyPDF2.PdfFileReader(open(pdfone_path, 'rb')))
    merged.append(PyPDF2.PdfFileReader(open(pdftwo_path, 'rb')))

    merged.write(open(file_output, 'wb'))
    merged.close()
