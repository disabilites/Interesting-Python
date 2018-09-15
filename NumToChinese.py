def NumtoChinese(num):
    zh_char = {0: '零', 1: '壹', 2: '贰', 3: '叁', 4: '肆', 5: '伍', 6: '陆', 7: '柒', 8: '捌', 9: '玖'}
    com = ['', '拾', '佰', '仟']
    num = int(num)
    res = ''
    i = 0

    while num > 0:
        temp = num % 10
        num = num // 10
        if temp != 0:
            res = zh_char[temp] + com[i] + res
        elif res:
            if res[0] != zh_char[0]:
                res = zh_char[temp] + res
        i += 1

    return res

def Conversion(num):
    length = len(num)
    if 0 <= length <= 4:
        res = NumtoChinese(num)
    elif 0 <= length <= 8:
        res = NumtoChinese(num[-4:])
        if res[1] != '仟':
            res = NumtoChinese(num[-len(num): -4]) + '万零' + res
        else:
            res = NumtoChinese(num[-len(num): -4]) + '万' + res
    elif 0 <= length <= 12:
        res = NumtoChinese(num[-4:])
        if res[1] != '仟':
            res = NumtoChinese(num[-8: -4]) + '万零' + res
        else:
            res = NumtoChinese(num[-8: -4]) + '万' + res
        if res[1] != '仟':
            res = NumtoChinese(num[-len(num):-8]) + '亿零' + res
        else:
            res = NumtoChinese(num[-len(num):-8]) + '亿' + res

    return res

num = input()
print(Conversion(num))