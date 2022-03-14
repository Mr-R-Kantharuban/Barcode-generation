import barcode #lib for response from barcode (pip install python_barcode)
from barcode.writer import ImageWriter
data='data which you want to display'
data1=str(data)
a=barcode.get_barcode_class('code128')
b=a(data,writer=ImageWriter())
c=b.save('Barcode')


