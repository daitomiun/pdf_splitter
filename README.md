# Splits: PDF manipulation tool

It's been so god damn hard to get a good tool to split, delete, add and crop pages from a PDF file, so I made my own with PyPDF2 in a CLI env!

## Intstallation

1. Create a venv directory
```bash
python3 -m venv
```

2. install specified requirements
```bash
pip install requirements.txt
```

## Getting started

1. Activate venv

```bash
source venv/bin/activate
```

2. inside the root directory of the project execute:
```bash
python main.py -h
```
> Here it will show the implemented commands that you can use

## Common commands

1. Split a range of pages to then have number of new copies of ranges of the pdf
```bash
python main.py -file file.pdf --split 20-30 3 1-90
```

2. Delete a range of pages and make a copy of the original file
```bash
python main.py -file file.pdf --delete 20-30 3 1-90
```

3. Crops by half on a range of pages to then replace it by the left and right page and make a copy of the original file
```bash
python main.py -file file.pdf --crop-half 20-30 3 1-90
```
