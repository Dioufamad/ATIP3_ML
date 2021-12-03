##### script to convert the readme written in markdown (.md) to pdf file for more plush distribution oriented files :
from markdown import markdown
import pdfkit

input_filename = '/home/diouf/ClassHD_work/ML/ClassHD/Full_documentation.md' # put here the name of the doc to convert # .md only
output_filename = '/home/diouf/ClassHD_work/ML/ClassHD/Full_documentation.pdf' # put here the name of the doc to obtain # .pdf only

with open(input_filename, 'r') as f:
    html_text = markdown(f.read(), output_format='html4')

pdfkit.from_string(html_text, output_filename)


# test for ATIP3_ML (not working)

input_filename = '/home/amad/PALADIN_2/3CEREBRO/garage/projects/ATIP3_ML/Documentation/Quick_start_guide.md' # put here the name of the doc to convert # .md only
output_filename = '/home/amad/PALADIN_2/3CEREBRO/garage/projects/ATIP3_ML/Documentation/Quick_start_guide.pdf' # put here the name of the doc to obtain # .pdf only

with open(input_filename, 'r') as f:
    html_text = markdown(f.read(), output_format='html4')

pdfkit.from_string(html_text, output_filename)