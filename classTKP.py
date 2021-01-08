import openpyxl
import os, winshell
from win32com.client import Dispatch




class TKP:
    def __init__(self, path_tkp_file, number_tkp, main_folder):
        self.main_folder = main_folder
        self.path_tkp_file = path_tkp_file
        self.number_tkp = number_tkp
        book = openpyxl.open(path_tkp_file, read_only=True)
        # выбор первого листа докумета
        sheet = book.active
        self.dict_value_file = {"Номер ТКП": str(sheet['B1'].value).zfill(4),
                                "ГИП": sheet['B2'].value,
                                "Краткое наименование ТКП": sheet['D1'].value,
                                "Объект": sheet['D2'].value,
                                "Бренд 1": sheet['A8'].value,
                                "Бренд 2": sheet['B8'].value,
                                "Бренд 3": sheet['C8'].value,
                                "Бренд 4": sheet['D8'].value,
                                "Бренд 5": sheet['E8'].value,
                                "Бренд 6": sheet['F8'].value,
                                "Бренд 7": sheet['G8'].value,
                                "Бренд 8": sheet['H8'].value,
                                "Бренд 9": sheet['I8'].value,
                                "Бренд 10": sheet['J8'].value,
                                "Статус ТКП 1С": sheet['A11'].value,
                                "Статус ТКП в отделе": sheet['B11'].value,
                                "Название направления 1": sheet['H1'].value,
                                "Название направления 2": sheet['H2'].value,
                                "Название направления 3": sheet['J1'].value,
                                "Название направления 4": sheet['J1'].value,
                                }
        pass

    def print_val(self):
        print(self.dict_value_file)
        pass

    def gip_shortcut(self):
        path_main_gip = str(self.main_folder) + '\\' + 'GIP'
        # создаем папку если такой нет
        if not os.path.isdir(path_main_gip):
            os.mkdir(path_main_gip)
        if str(self.dict_value_file.get('ГИП')) != 'None':
            path_gip = path_main_gip + '\\' + str(self.dict_value_file.get('ГИП'))
            if not os.path.isdir(path_gip):
                os.mkdir(path_gip)
            # путь где ярлык будет создан
            desktop = path_gip
            # создаем сам ярлык
            path = os.path.join(desktop, str(self.number_tkp)+".lnk")
            target = self.main_folder + '\\' + str(self.number_tkp)
            # wDir = ''
            # icon = path
            shell = Dispatch('WScript.Shell')
            shortcut = shell.CreateShortCut(path)
            shortcut.Targetpath = target
            # shortcut.WorkingDirectory = wDir
            # shortcut.IconLocation = icon
            shortcut.save()
        pass