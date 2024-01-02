from decimal import Decimal, ROUND_HALF_UP

number = Decimal('5.5125')
rounded_number = number.quantize(Decimal('0.001'), rounding=ROUND_HALF_UP)
print(rounded_number)


