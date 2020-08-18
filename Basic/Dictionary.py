#!/usr/bin/env python3
# -*- coding: utf-8 -*-
classmates = {"Kerwin":38,"Lee":20,"Vick":15,"Angela":21,"Fei":22,"Eric":31}
print(classmates)
print(classmates.get("Zhoukeke","not found"))
print("zhoukeke" in classmates)
classmates.pop("Kerwin")
print(classmates)
classmates["Derek"] = 23
print(classmates)

set1 = set(list(range(100)))
set1.add(100)
set1.remove(0)
print(set1)