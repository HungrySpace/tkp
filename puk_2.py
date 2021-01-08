import os
import classTKP

# определяем текущую деректорию
main_folder = 'C:\\Users\Kirill\Desktop\Test'
os.chdir(main_folder)
# # создаем папки в деректории
# for i in range(5):
#     os.mkdir(str(i).zfill(4))

for i in os.listdir():
    # сбор путей файлов ткп
    path_tut = main_folder + '\\' + i
    os.chdir(path_tut)
    # print(path_tut)
    for file_tkp in os.listdir():
        if file_tkp.find("Карточка ТКП") >= 0:
            path_file = path_tut + '\\' + file_tkp
            print(path_file)
        else:
            print('Левый файл в папке:', file_tkp)

# сбор путей файлов ткп
# path_tut = main_folder + '\\' + os.listdir()[0]
# os.chdir(path_tut)
# path_tkp = path_tut + '\\' + os.listdir()[0]
# number_tkp = path_tkp.split('\\')[-2]
# print(path_tkp, "//", number_tkp)
#
# one_file = classTKP.TKP(path_tkp, number_tkp)
# one_file.print_val()






