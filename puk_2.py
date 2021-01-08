import os
import classTKP

# определяем текущую деректорию
main_folder = 'C:\\Users\Kirill\Desktop\Test'
os.chdir(main_folder)
# # создаем папки в деректории
# for i in range(5):
#     os.mkdir(str(i).zfill(4))

# for i in os.listdir():
#     print(i)


# сбор путей файлов ткп
path_tut = main_folder + '\\' + os.listdir()[0]
os.chdir(path_tut)
path_tkp = path_tut + '\\' + os.listdir()[0]
number_tkp = path_tkp.split('\\')[-2]
print(path_tkp, "//", number_tkp)

one_file = classTKP.TKP(path_tkp, number_tkp)
one_file.print_val()






