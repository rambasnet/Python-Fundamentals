#! /bin/bash

# Script to convert jupyter notebooks to PDF files. The pdfs are saved in ./pdfs folder

files=$(find . -name '*.ipynb')
for f in $files; do
    echo Converting: $f
    jupyter nbconvert --log-level=0 --output-dir='./pdfs' --to pdf $f > /dev/null
done
