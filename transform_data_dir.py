#############################################################################################
# Параметры программы:                                                                      #
#   1 - Путь к папке, в которой находятся директории Annatations и Images                   #
#   2 - Путь к папке, куда скопировать файлы                                                #
#   3 - (не обязательно) Значение параметра отображения вывода 'vis', который описан ниже   #
#                                                                                           #
# Пример запуска : transform_data_dir.py 'D:\Input Dir' 'D:\Output Dir' 1                   #
#############################################################################################

import sys
import os
import shutil

input_folder = 'D:\\WORK'
output_folder = 'D:\\WORK\\OUT'
cout_files = 0
vis = 1  # Параметр отображения вывода

# Значения параметра отображения вывода.
#   0 - Вывести только сообщение о завершении,
#   1 - Вывести информацию о том, какие файлы копируются,
#   2 - Вывести подробную информацию по каждому файлу

if len(sys.argv) == 3:
    input_folder = sys.argv[1]
    output_folder = sys.argv[2]
else:
    if len(sys.argv) == 4:
        input_folder = sys.argv[1]
        output_folder = sys.argv[2]
        vis = sys.argv[3]
    else:
        if len(sys.argv) < 3:
            print("ERROR! Параметров слишком мало")
            sys.exit(1)
        else:
            print("ERROR! Параметров слишком много")
            sys.exit(1)

folder_ann = 'Annatations'
folder_img = 'Images'

try:
    os.mkdir(output_folder + '\\annotations')
    os.mkdir(output_folder + '\\annotations\\xmls')
    os.mkdir(output_folder + '\\images')
except OSError:
    print("Создать директорию %s не удалось. Возможно она уже существует." % output_folder)
else:
    if vis != 0:
        print("Успешно создана директория %s " % output_folder)

Files = os.listdir(input_folder + '/' + folder_ann)

xml_folder = os.path.join(output_folder, "annotations\\xmls")
trainval_path = os.path.join(output_folder, "annotations")
img_folder = os.path.join(output_folder, "images")

f = open(trainval_path + '\\' + 'trainval.txt', 'w')

for xml_file in Files:
    if xml_file.endswith('.xml'):
        cout_files += 1
        ann_path_in = os.path.join(input_folder, folder_ann + '\\' + xml_file)
        if vis == 2:
            print("Файл xml на входе - " + ann_path_in)
        ann_path_out = os.path.join(xml_folder, xml_file)
        if vis == 2:
            print("Файл xml скопирован - " + ann_path_out)
        file_name = xml_file[:-4]
        if vis == 2:
            print("Название файла - " + str(file_name))
        f.write(str(file_name) + '\n')

        img_path_in = os.path.join(input_folder, folder_img + '\\' + file_name + '.jpeg')
        if vis == 2:
            print("Файл jpeg на входе - " + img_path_in)
        img_path_out = os.path.join(img_folder, file_name + '.jpeg')
        if vis == 2:
            print("Файл jpeg скопирован - " + img_path_out)
        shutil.copyfile(ann_path_in, ann_path_out)
        shutil.copyfile(img_path_in, img_path_out)
        if vis == 2 or vis == 1:
            print("файл %s (xml и jpeg) скопирован!" % file_name)

        if vis == 2:
            print("==================")

print("Копирование завершено!\n Количество файлов : " + str(cout_files))
f.close()

# with open(trainval_path + '/' + 'text.txt') as f:
#     text = f.readlines()
#
# with open(trainval_path + '/' + 'text.txt', 'w') as f:
#     f.writelines(text[:cout_files-1])
