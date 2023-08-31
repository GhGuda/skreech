from django import template

register = template.Library()

@register.filter
def censor(value, num_asterisks):
    if num_asterisks < 1:
        return value
    hidden_text = num_asterisks * '*'
    return str(value)[num_asterisks:] + hidden_text
