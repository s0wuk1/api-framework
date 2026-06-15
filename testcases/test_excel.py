from common.excel_util import excel_util
def test_excel():

    data = excel_util.read_excel(
        "../data/order_data.xlsx"
    )
    print(data)