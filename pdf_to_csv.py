import tabula
input_file = '/Users/jazzopardi/Desktop/Traffic_Data.pdf'
tabula.convert_into(input_file, 'output.csv', output_format='csv', pages='all')
