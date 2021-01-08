import openpyxl


class TKP:
    def __init__(self, path_tkp_file, number_tkp):
        self.path_tkp_file = path_tkp_file
        self.number_tkp = number_tkp
        book = openpyxl.open(path_tkp_file, read_only=True)
        # выбор первого листа докумета
        sheet = book.active
        self.dict_value_file = {"number_tkp": str(sheet['B1'].value).zfill(4),
                           "gip_tkp": sheet['B2'].value,
                           "name_tkp": sheet['D1'].value,
                           "object_tkp": sheet['D2'].value,
                           "brand_1": sheet['A8'].value,
                           "brand_2": sheet['B8'].value,
                           "brand_3": sheet['C8'].value,
                           "brand_4": sheet['D8'].value,
                           "brand_5": sheet['E8'].value,
                           "brand_6": sheet['F8'].value,
                           "brand_7": sheet['G8'].value,
                           "brand_8": sheet['H8'].value,
                           "brand_9": sheet['I8'].value,
                           "brand_10": sheet['J8'].value,
                           "status_stp_1C": sheet['A11'].value,
                           "status_stp": sheet['B11'].value}

    def print_val(self):
        print(self.dict_value_file)
