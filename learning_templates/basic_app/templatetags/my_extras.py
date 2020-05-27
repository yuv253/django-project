from django import template

register=template.Library()
@register.filter(name='cut')  # name='cut' used in the index.html file
def cut(value,arg):
#value will be Hello World or text in the views.py file and agr is what you provide in the index.html file after pipe operator

    '''
    This cuts out all values of "arg" from the string!

    '''

    return value.replace(arg,'')

#register.filter('cut',cut)
# 1st cut 'will be used in index.html file and other is cut isthe name of the function
@register.filter
def lower(value): # Only one argument.
    """Converts a string into all lowercase"""
    return value.lower()