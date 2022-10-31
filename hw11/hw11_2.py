'''. Написать регулярное выражение, которое будет
 проверять формат времени. (14:00 - True, 25:66 - False'''
import re
def checkNumber(match):
    if match:
        print(True)
    else:
        print(False)
# date = r"\d\d/\d\d/\d{4}"

date = r"[0-3]\d/[0-1]\d/[0-2]\d{3}"
date = re.fullmatch(date, "10/08/2003")
checkNumber(date)