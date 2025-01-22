from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter

class Cmdline():
    def __init__(self, args) -> None:
        self.args = args
        self.input_pdf = PdfReader(self.args.file_path)

    def check_valid_pos_num(self):
        position = self.args.after if self.args.after is not None else self.args.before
        position_type = "after" if self.args.after is not None else "before"
        pdf_to_add = PdfReader(self.args.insert)

        print(f"page to add {self.args.insert}")
        print(f"{position_type} the position {position} with a total of total pages {len(pdf_to_add.pages)}")
        if position < 0 or position > len(self.input_pdf.pages):
            raise ValueError(f"ERR: Invalid {position_type} Position {position}")

        position = position if position_type == "after" else position - 1
        return position

    def check_valid_range(self, page):
        num_pages = len(self.input_pdf.pages)
        if page > num_pages:
            raise ValueError(f"ERR: page {page} range is higher than num of pages {num_pages}")

    def parse_input(self, value):
       if "-" in value:
            start, end = map(int, value.split("-"))
            if  start > end:
                raise ValueError(f"ERR: Start range {start} is higher than end range {end}")

            if start < 1 or end < 1:
                raise ValueError(f"ERR: start {start} or end {end} range must be positive numbers")
            return list(range(start - 1, end))
       single_page = int(value) 
       if single_page < 1:
           raise ValueError(f"ERR: Page {single_page} has to be positive")
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

    def add_pdf(self):
        print("--- add action ---")
        pos = self.check_valid_pos_num()

        reader_pdf_to_insert = PdfReader(self.args.insert)
        writer = PdfWriter()
        writer.append_pages_from_reader(self.input_pdf)
        writer.merge(position=pos, fileobj=reader_pdf_to_insert)

        file_name = Path(self.args.file_path).stem
        pdf_path = f"./output/{file_name}_added_pages.pdf"
        with open(pdf_path, "wb") as fp:
            writer.write(fp)
        print(f"--- PDF files added from file: {self.args.insert}  ---")
        print(f"--- DONE: PDF addition done at file  {pdf_path} ---")

