k = 'ноутбук'
score = 0

for item in k:
    if item.upper() in ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R']:
        score += 1
    elif item.upper() in ['D', 'G']:
        score += 2
    elif item.upper() in ['B', 'C', 'M', 'P']:
        score += 3
    elif item.upper() in ['F', 'H', 'V', 'W', 'Y']:
        score += 4
    elif item.upper() in ['K']:
        score += 5
    elif item.upper() in ['J', 'X']:
        score += 8
    elif item.upper() in ['Q', 'Z']:
        score += 10
    if item.upper() in ['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т']:
        score += 1
    elif item.upper() in ['Д', 'К', 'Л', 'М', 'П', 'У']:
        score += 2
    elif item.upper() in ['Б', 'Г', 'Ё', 'Ь', 'Я']:
        score += 3
    elif item.upper() in ['Й', 'Ы']:
        score += 4
    elif item.upper() in ['Ж', 'З', 'Х', 'Ц', 'Ч']:
        score += 5
    elif item.upper() in ['Ш', 'Э', 'Ю']:
        score += 8
    elif item.upper() in ['Ф', 'Щ', 'Ъ']:
        score += 10
print(score)