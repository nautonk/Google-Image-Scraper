import re
from slugify import slugify

test = 'Superstore Name Tag Mockup - Cloud 9 Name Tag Clipart Full Paper Product Png,Name Tag Png - free transparent png images -| pngaaa.com'
result = re.sub('[\-\|]','|',test)
result = result.split('|')
if len(result) > 1:
    result.pop()
result = " ".join(result)

print(slugify(result))