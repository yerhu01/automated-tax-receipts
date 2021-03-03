#!/bin/bash

# chmod +x convert2pdf.sh
# ./convert2pdf.sh

for filename in taxreceipts/*.docx; do
	libreoffice --headless --convert-to pdf --outdir taxreceipts-pdf "$filename" 
done
