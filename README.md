# Automated Tax Receipts

# Contents
1. [Introduction](#introduction)
1. [GUI](#gui)
1. [Template Format](#template-format)
1. [Spreadsheet Format](#spreadsheet-format)
1. [PDF Conversion](#pdf-conversion)
1. [Development Setup](#development-setup)

# Introduction
This application automates the making of tax receipts by copying data from a spreadsheet
into a receipt template of `.docx` format.

# GUI
Graphical user interface created using tkinter.
![alt text](images/gui.png?raw=true "gui")

# Template Format
The receipt template must be of `.docx` format and have the following template labels
in the file as placeholders for the data.  

**Template Labels:**
* [NAME]
* [ADDRESS]
* [AMOUNT]
* [RECEIPT#]

# Spreadsheet Format
The spreadsheet file must be of `.xlsx`, `.xls`, `.xlsm`, `.xlsb`, `.odf`, `.ods`, or `.odt` and 
must have the following column names.

**Column Names:**
* FirstName
* LastName
* Address
* Total

# PDF Conversion on Linux
The receipts can be converted into PDF on Linux by running the given Bash script.
This requires `Libreoffice` application to do the conversion.
    ```
    ./convert2pdf.sh
    ```

# Development Setup
## Python environment setup
1. Create and activate a venv
    ```
    python3 -m venv env
    source env/bin/activate 
    ```
1. Install the required python packages:
    ```
    pip3 install pandas
    pip3 install xlrd
    pip3 install openpyxl
    pip install python-docx  NOTE: pip not pip3
    pip3 install ttkthemes
    ```
1. Run the app:
    ```
    python3 receipts.py
    ```
