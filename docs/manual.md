# Manual
PDF Splitter 

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

