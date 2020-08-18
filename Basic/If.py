#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
pweight = float(input("Please input your weight(kg).\r\n"))
pheight = int(input("please input your height(cm).\r\n"))
pheight = round(pheight / 100,2)
bmi = round(pweight / math.pow(pheight,2),2)
result = "your BMI is %.2f so " % (bmi)

if bmi < 18.5:
    result += "belong to light."
elif bmi <= 25:
    result += "belong to normal."
elif bmi <= 28:
    result += "belong to weight."
elif bmi <= 32:
    result += "belong to obesity."
else:
    result += "belong to too obesity."

print(result)