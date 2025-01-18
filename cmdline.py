import argparse
from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter
import itertools

class Cmdline():
    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser(description="Split and list num of pages of a PDF")
        self.parser.add_argument(
            "-f", "--file",
            dest="file_path",
            type=str,
            help="Get the PDF file location",
            required=True
        )
        self.parser.add_argument(
            "-tp", "--total-pages", 
            help="From the file location get total pages of the PDF",
            action="store_true"
        )
        self.parser.add_argument(
            "-s", "--split",
            help="It splits a file to multiple files with a range of pages '--split 1-30 31-40' or single pages '--split 1 4 6' given by the user",
            nargs="+",
            type=self.parse_split
        )
        self.parser.add_argument(
            "-d", "--delete",
            help="It deletes a range of pages '--del 1-5' or a single page '--del 1 3 5' from a PDF and makes a copy with the deleted pages",
            nargs="+",
            type=self.parse_split
        )
        self.args = self.parser.parse_args()
        self.input_pdf = PdfReader(self.args.file_path)

    def check_valid_range(self, page):
        num_pages = len(self.input_pdf.pages)
        if page > num_pages:
            self.parser.error(f"ERR: page {page} range is higher than num of pages {num_pages}")

    def parse_split(self, value):
       if "-" in value:
            start, end = map(int, value.split("-"))
            if  start > end:
                self.parser.error(f"ERR: Start range {start} is higher than end range {end}")

            if start < 1 or end < 1:
                self.parser.error(f"ERR: start {start} or end {end} range must be positive numbers")
            return list(range(start - 1, end))
       single_page = int(value) 
       if single_page < 1:
           self.parser.error(f"ERR: Page {single_page} has to be positive")
       return [int(value) - 1]

    def get_num_pages(self):
        print(f"There are {len(self.input_pdf.pages)} pages at document {self.args.file_path}")

    def split_pdf(self):
        print("--- split action ---")
        for i, page_range in enumerate(self.args.split, 1):
            writer = PdfWriter()
            for page in page_range:
                self.check_valid_range(page)
                writer.add_page(self.input_pdf.pages[page])

                split = self.args.split[i - 1]
                file_name = Path(self.args.file_path).stem
                start_split = split[0]
                end_split = split[len(split) - 1]
                pdf_path = f"./output/{file_name}_from_{start_split + 1}_to_{end_split + 1}.pdf"
                with open(pdf_path, "wb") as fp:
                    writer.write(fp)
            print(f"--- DONE: PDF split on File {i} ---")

    def del_range_pdf(self):
        print("--- delete action ---")
        writer = PdfWriter()
        flattened_omit_list = [item for sublist in self.args.delete for item in sublist]
        total_pages = list(range(0, len(self.input_pdf.pages)))
        pages_to_keep = [i for i in total_pages if i not in flattened_omit_list]

        for page in pages_to_keep:
           writer.add_page(self.input_pdf.pages[page])

        file_name = Path(self.args.file_path).stem
        pdf_path = f"./output/{file_name}_del_selected_pages.pdf"
        with open(pdf_path, "wb") as fp:
            writer.write(fp)
        print(f"--- PDF deletion at pages {flattened_omit_list}  ---")
        print(f"--- DONE: PDF deletion done at file  {pdf_path} ---")




if __name__ == '__main__':
    app = Cmdline()
