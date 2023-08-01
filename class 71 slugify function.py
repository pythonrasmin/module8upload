# def slugify(text):
#     slug = text.strip().lower().replace(' ','-')
#     while'--' in slug:
#         slug= slug.replace('--','-')
#     return slug
#
# title = input('Enter your title: ')
# slug = slugify(title)
# print(slug)






# def slugify(text):
#     slug = text.strip().lower().replace(' ','-')
#     while'--' in slug:
#         slug = slug.replace('--','-')
#     return slug
#
# title = input('Enter your title: ')
# slug = slugify(title)
# print(slug)
def slugify(text):
    slug = text.strip().lower().replace(' ','-')
    while '--' in slug:
        slug = slug.replace('--','-')
    return slug
title = input('Enter your title: ')
slug = slugify(title)
# title = input('Enter your title: ')
print(slug)

# title = input('Enter your title: ')

























