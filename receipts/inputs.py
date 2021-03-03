import csv
from collections import namedtuple
import logging
import pandas as pd
from pandas import read_excel

SUPPORTED_FILETYPES = [('Excel 2007+: xlsx', '*.xlsx'),
                   ('Excel 1997-2003: xls', '*.xls'),
                   ('xlsm', '*.xlsm'), ('xlsb', '*.xlsb'),
                   ('odf', '*.odf'), ('ods','*.ods'), ('odt','*.odt')]

Receipt = namedtuple('Receipt', ['Name', 'Address', 'Amount', 'ReceiptNumber']) 

class Inputs:
    def __init__(self, file_location, sheet_name, receipt_start):
        self.file_location = file_location
        self.sheet = sheet_name
        self.receipt_start = receipt_start

    def receipt_data(self):
        df = read_excel(self.file_location,
                        sheet_name = self.sheet,
                        usecols = ['FirstName', 'LastName', 'Address', 'Total'])
        logging.info(df)
        receiptnumber = self.receipt_start
        for index, row in df.iterrows():
            first, last = row[0], row[1]
            name = ''
            if pd.isnull(first):
                first = ''
            if pd.isnull(last):
                last = ''
            if not first or not last:
                name = first or last 
            else:
                name = ' '.join((first, last))
            address = row[2].upper() if not pd.isnull(row[2]) else ''
            total = format(row[3], '.2f')
            yield Receipt(name, address, total, receiptnumber)
            receiptnumber += 1
        
    def to_csv(self):
        with open('receipts.csv', 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            for receipt in self.receipt_data():
                csvwriter.writerow(receipt)
