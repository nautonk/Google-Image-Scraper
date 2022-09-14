import re
from slugify import slugify

test = 'Superstore 88888 Name Tag Mockup - Cloud 9 Name Tag Clipart Full Paper Product Png,Name Tag Png - free transparent png images -| pngaaa.com'
result = re.sub('[\d]','',test)

print(slugify(result))