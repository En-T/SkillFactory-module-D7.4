from django import template


register = template.Library()
censors = ['Джонни', 'Тест', 'Томми']

@register.filter(name='censor') 
def censor(value):
    for st in censors:     
        value = value.replace(st, str(len(st)*'*'))
    return value        