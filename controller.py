import modul_use_telefone_book as mt
from modul_use_telefone_book import  read, delete #add,
import preview as pr

def choise_type(type):
    if type == 1:
        return mt.read()
    elif type == 2:
        return mt.create()
    elif type == 3:
        return mt.delete()
    # elif type == 4:
    #     return mt.add()
    elif type == 5:
        return pr.create()
