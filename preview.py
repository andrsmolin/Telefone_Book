from cgitb import html
from tkinter.ttk import Style
import modul_use_telefone_book as mt
from modul_use_telefone_book import return_data


def create():
    style = "style = 'font-size: 22px;'"
    html = '<html>\n <head></head>\n <body>\n'
    tel_dect = mt.return_data()
    for i in range(1, len(tel_dect)+1):
        # f.write( + ' ')
        # f.write(tel_dect[i]['name']+ ' ')
        # f.write(tel_dect[i]['telefon'] + ' ')
        # f.write(tel_dect[i]['status'] + '\n')
        html += '<p{}> id {} {} {} {} {} </p> \n' \
        .format(style, str(tel_dect[i]['idd']), tel_dect[i]['surname'], tel_dect[i]['name'], tel_dect[i]['telefon'], tel_dect[i]['status'] )
    html += ' </body >\n </html>'

    with open('E:/IT_HomeWork/tel.html', 'w', encoding ='utf-8') as page:
        page.write(html)
    return html
