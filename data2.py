import re
import xlsxwriter

txt_url = r"C:\Users\Administrator\Desktop\data\data3.txt"
sava_url = r'C:\Users\Administrator\Desktop\data\data6.xlsx'


# 读取txt 并提取指定字符
def readTXT():
    with open(txt_url, 'r', encoding='utf-8') as f:
        content = f.read()

    result1 = re.findall(".*time：(.*)ms.*", content)  # 提取指定字符  表示提取 time: ~ ms之间的字符
    result2 = re.findall(".*TPS:(.*).*", content)  # 提取指定字符 提取TPS:~ *** 号之间的字符

    l1 = len(result1)
    l2 = len(result2)
    print(l1, l2)

    for i in range(l2):
        result2[i] = result2[i].replace("*", "")  # *号 暂时没有好的方法 去除*号
    print(result2)
    return result1, result2


def saveExcel(str1, str2):
    # todo 创建excel文件
    xl = xlsxwriter.Workbook(sava_url)
    # todo 添加sheet
    sheet = xl.add_worksheet('sheet1')
    k = -4
    j = 0
    # todo 往单元格cell添加数据,索引写入
    for i in range(len(str1)):
        if i % 50 == 0:
            k = k + 4
            j = 0
        sheet.write_string(j, k, str1[i])
        sheet.write_string(j, k + 1, str2[i])
        j = j + 1
    # # todo 设置单元格宽度大小
    # sheet.set_column('A:B', 30)
    # todo 关闭文件
    xl.close()


str1, str2 = readTXT()
saveExcel(str1, str2)
