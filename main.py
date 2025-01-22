from cmdline import Cmdline
from parseargs import PDFArgumentParser

def main():
    print("----------------- SPLITS: PDF CLI editor -----------------")
    parser = PDFArgumentParser()
    args = parser.get_args()
    app = Cmdline(args)

    if app.args.total_pages:
        app.get_num_pages()
    if app.args.split:
        app.split_pdf()
    if app.args.delete:
        app.del_range_pdf()
    if app.args.command == "add":
        app.add_pdf()



if __name__ == "__main__":
    main()
