# import the entire module once

import utils.convertor as convertor
from pathlib import Path
import utils.find_max as find_max
import ecommerce.shipping as shipping
from openpyxl import Workbook
# import specific module from the module
from utils.convertor import lbs_to_kg
kgToLbs = convertor.kg_to_lbs(62)
print(kgToLbs)
lbsToKg = lbs_to_kg(138)
print(lbsToKg)
numbers = [34, 56, 2, 34]
maxNumber = find_max.find_maxNumber(numbers)
print(maxNumber)
print(max(numbers))
shipping.calc_shipping()
# absolute path
# C:\program File\Microsoft
# relative path
path = Path('ecommerce')
# to check the directories/folder exist or not
print(path.exists())
path = Path('emails')
# to create the directories/folder email
path.mkdir()
# to delete or remove directories/ folder
path.rmdir()

path = Path()
# to list all file that has extensions .py in the directory
for file in path.glob('*.py'):
    print(file)

# to list all file  in the directory
print('All files')
for file in path.glob('*'):
    print(file)

wb = Workbook()
ws = wb.active
print(ws)
