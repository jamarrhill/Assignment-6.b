# Name: Jamar Hill
# Date: 11/3/2020
# Description: Assignment 6.b

def add_surname(first_names_lst):
    """Adds Kardashian to names with K in the 0 position of the string"""
    full_names_lst = [name + ' Kardashian' for name in first_names_lst if name[0] == 'K']
    """Returns full name including Kardashian to the value of first name"""
    return full_names_lst
"""Defines name values"""
first_names_lst = ["Kiki", "Krystal", "Pavel", "Annie", "Koala"]
""" Prints first name + Kardashian = full_name"""
print(add_surname(first_names_lst))