# import the entire module once

import utils.convertor as convertor

import utils.find_max as find_max
import ecommerce.shipping as shipping
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
