#!/usr/bin/python

a={"name":"mirenping","age":30,"sex":"man","like":("color","read") }

for key,value in a.items():
    print key,value



print "--------------------------------------------"

for key in a.keys():
    print a[key]

