# selective_merge_pdf
A command line script to merge specific pages of pdf documents

## Installing
install pip:
`sudo apt install python3-pip`

install virtualenv:
`pip3 install virtualenv`

create a virtual environment:
`python3 -m virtualenv venv`

activate the environment:
`source venv/bin/activate`

install the dependencies:
`pip install -r requirements.txt`

## Using
pass as arguments file names each immediately followed by the pages

pages can be specified as 1,2,3 or as a range 1-3

example:
`python3 selective_merge_pdf.py file1.pdf 1-3 file2.pdf 3,4,10 file1.pdf 50`
