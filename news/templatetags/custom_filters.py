from django import template

register = template.Library()

banned_word_list = [
    'Редиска',
    'канай',
    'дурак',
    'дура',
    'Петух',
    'Моргалы'
]


@register.filter(name='Censor')
def censor(text):
    for bw in banned_word_list:
        text = text.lower().replace(bw.lower(), f'{bw[0:2]}...')
    return text

