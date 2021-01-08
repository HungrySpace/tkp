import os
import classTKP

# определяем текущую деректорию
main_folder = 'C:\\Users\Kirill\Desktop\Test'
os.chdir(main_folder)
list_class_tkp = []
for i in os.listdir():
    # сбор путей файлов ткп
    path_tut = main_folder + '\\' + i
    os.chdir(path_tut)
    # print(path_tut[1])
    for file_tkp in os.listdir():
        if file_tkp.find("Карточка ТКП") >= 0 and file_tkp[0] != '~':
            path_file = path_tut + '\\' + file_tkp
            number_tkp = path_file.split('\\')[-2]
            one_file = classTKP.TKP(path_file, number_tkp, main_folder)
            list_class_tkp.append(one_file)
        elif file_tkp.find("Карточка ТКП") == -1 and file_tkp[0] != '~':
            print('Левый файл в папке:', file_tkp)
        elif file_tkp[0] == '~':
            print('наткнулись на открытый файл')

for puk in list_class_tkp:
    puk.gip_shortcut()

# # создаем папки в деректории
# for i in range(5):
#     os.mkdir(str(i).zfill(4))




