from sys import argv
from PyPDF2 import PdfFileReader, PdfFileWriter
import re


range_pattern = re.compile(r'(\d+)(\.\.|-)(\d+)')
comma_pattern = re.compile('\d+(,\d+)*')
def pages_args_to_array(pages_str):
	groups = range_pattern.search(pages_str)
	if groups:
		start = int(groups.group(1))
		end = int(groups.group(3))
		return list(range(start, end + 1))
	elif comma_pattern.search(pages_str):
		return [int(d) for d in pages_str.split(',')]
	else:
		raise Exception('pages should be like 1,2,3 or 1-3, but was {}'
			.format(pages_str))


if __name__ == '__main__':
	assert(len(argv) > 1), "usage examle:\npython3 selective_merge_pdf.py file1.pdf 1-3 file2.pdf 3,4,10 file1.pdf 50"
	assert(len(argv) % 2 == 1), "invalid arguments; supply page numbers after each pdf name"

	files_names = argv[1::2]
	pages_args = argv[2::2]


	pdf_writer = PdfFileWriter()
	for file_name, pages in zip(files_names, pages_args):
		pdf_reader = PdfFileReader(file_name)
		last_page_index = pdf_reader.getNumPages()
		pages = pages_args_to_array(pages)
		pages_to_add = list(filter(lambda i: i >= 0 and i <= last_page_index, pages))
		for page in pages_to_add:
		    pdf_writer.addPage(pdf_reader.getPage(page - 1))

	with open("merged.pdf", 'wb') as out:
		pdf_writer.write(out)
