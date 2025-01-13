from django import template


register = template.Library()


@register.filter()
def censor(s: str):
    var = ["бля", "хуй", "пизд", "еба", "еби", "хуе", "хуи"]
    ln = len(var)
    filter = ''
    string = ''
    p = '*'
    for i in s:
        string += i
        string2 = string.lower()
        f = 0
        for j in var:
            if not string2 in j:
                f += 1
            if string2 == j:
                filter += f'{string[0]}{p*(len(string)-1)}'
                f -= 1

        if f == ln:
            filter += string
            string = ''

    if string2 != '' and string2 not in var:
        filter += string
    elif string2 != '':
        filter += string[0]+p*(len(string)-1)

    return filter
