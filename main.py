'''
Main focus for the pdf splitter cli tool

---
1. Show number of pages inside the CLI
ex:
> python3 main.py --file ./doc.pdf --total-pages 

output:
total pages: 100

## Show total pages
- Just show number of pages in the document given
---

2. Based on the pages create multiple splits from a simple arguments from the CLI
ex:
python3 main.py --file ./G1_P1_horeb.pdf --split 1-30 24-50 51-70 --output ../output

output:
files created at ../output 

list files created
G1_P1_horeb_1-30.pdf
G1_P1_horeb_24-50.pdf
G1_P1_horeb_51-70.pdf

# conditions
both conditions will only accept pdf files
## splitting
- It can be 1 page --> --split 1 2 3

- it can't go in the reverse --> 40-1

- it can't have a number over the size limit at the start or end of the range --> 101-103 Error: page 101 and 103 not found
    - as it's a loop from every files splitter it will just error the split change 
        ex: 
            51-70 Succes: pages splitted
            101-103 Error: page 101 and 103 not found
            
- Should output to current or selected directory
    --output ../output or --output without params for current directory
'''
import argparse
from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter

# parsing splits
def parse_split(value):
    if "-" in value:
        start, end = map(int, value.split("-"))
        return list(range(start, end + 1))
    return [int(value)]


parser = argparse.ArgumentParser(description="Split and list num of pages of a PDF")
parser.add_argument(
    "-f", "--file",
    dest="file_path",
    type=str,
    help="Get the PDF file location"
)
parser.add_argument(
    "-tp", "--total-pages", 
    help="From the file location get total pages of the PDF",
    action="store_true"
)
parser.add_argument(
    "-s", "--split",
    help="Split a file from the given path, takes a param to '--split 1' a single page on the document or '--split 1-30' a range of pages given by the user",
    nargs="+",
    type=parse_split
)
args = parser.parse_args()

def main():
    print("----- PDF CUTTER -----")
    input_pdf = PdfReader(args.file_path)
    
    if args.total_pages:
        print(f"There are {len(input_pdf.pages)} pages at document {args.file_path}")

    if len(args.split) > 0:
        for i, page_range in enumerate(args.split, 1):
            writer = PdfWriter()
            for page in page_range:
                writer.add_page(input_pdf.pages[page])

            split = args.split[i - 1]
            file_name = Path(args.file_path).stem
            start_split = split[0]
            end_split = split[len(split) - 1]
            pdf_path = f"./output/{file_name}_from_{start_split}_to_{end_split}.pdf"
            with open(pdf_path, "wb") as fp:
                writer.write(fp)
            print(f"--- PDF split number {i} ---")

if __name__ == "__main__":
    main()
