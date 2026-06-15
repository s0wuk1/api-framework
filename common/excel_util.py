from openpyxl import load_workbook
import os
class ExcelUtil:
    def read_excel(self, file_path):

        root_dir = os.path.dirname(
            os.path.dirname(__file__)
        )
        excel_path = os.path.join(
            root_dir,
            file_path
        )

        print("Excel路径：", excel_path)

        wb = load_workbook(excel_path)

        sheet = wb.active

        rows = list(sheet.rows)

        headers = [cell.value for cell in rows[0]]

        data = []

        for row in rows[1:]:
            row_data = {}

            for header, cell in zip(headers, row):
                row_data[header] = cell.value

            data.append(row_data)

        return data


excel_util = ExcelUtil()