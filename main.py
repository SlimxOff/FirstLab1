import os
import xml.etree.ElementTree as ET
import pandas as pd
import psutil
import os
import xml.etree.ElementTree as ET
import pandas as pd
import psutil
import zipfile

print("Выберете, что хотите сделать:")
print("1.Запись в TXT файл")
print("2.Вывод информации о диске")
print("3.Чтение XMl файла")
print("4.Архивировать и разорхивировать файл")
n = int(input())
if n == 1:
    Name = input("Введите имя файла:")
    file = open(Name, 'w')
    Message = input("Введите текст в файл:")
    file.write(Message)
    file.close()
    temp=open(Name)
    print(temp.read())
    os.remove(Name)

if n == 2:
    d = psutil.disk_partitions()
    print('Информация о диске:', d[0])
    print('Тип данных:', type(d), '\ n')

if n == 3:
    p=ET.Element(str(input("Enter name of column")))
    ET.SubElement(p,'hello')
    tree = ET.ElementTree(p)
    tree.write('test.xml')
    print(ET.dump(p))
    os.remove('test.xml')
if n == 4:
    file = input("Введите имя файла c расширением: ")
    zipFileName = input("Введите имя файла zip: ")
    jungle_zip = zipfile.ZipFile(f'{zipFileName}.zip', 'w')
    jungle_zip.write(f'{file}', compress_type=zipfile.ZIP_DEFLATED)
    jungle_zip.close()
    fantasy_zip = zipfile.ZipFile(f'{zipFileName}.zip')
    fantasy_zip.extractall('/Users/ivangoyda/PycharmProjects/OperSisFirstLab')
    fantasy_zip.close()
    file_name = f"{file}"

    file_stats = os.stat(file_name)
    print("File size: "+ str(file_stats.st_size)+" b")
    print("File name"+ file)
