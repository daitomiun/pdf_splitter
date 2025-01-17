from cmdline import Cmdline

def main():
    print("----- PDF SPLITS CLI TOOL -----")
    app = Cmdline()

    if app.args.total_pages:
        app.getNumPages()
    if app.args.split:
        app.split_pdf()

if __name__ == "__main__":
    main()
