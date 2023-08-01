def heading_two(text):
    """
    return heading two tag of html
    :param text:Any kind of string
    :return:html tag
    """
    html = f'<h2> {text} </h2>'
    return html
data = heading_two('This is heading two')
print(data)
#
# paragraph = heading_two('This is paragraph')
# print(paragraph)
print(heading_two.__doc__)

def html_tag(text,html_tag):
    """
    Return HTML Tag of any text
    :param text:Any kind of string
    :param html_tag:What kind of html tag you want to generate
    :return:HTML Tag of any text
    """
    html = f'<{html_tag}> {text} </{html_tag}>'
    return html
# print(html_tag.__doc__)

print(html_tag('This is heading tag 3','h3'))
print(html_tag('This is heading tag 4','h4'))
print(html_tag('This is heading tag 4',"strong"))
print(html_tag('This is heading tag',"italic"))
