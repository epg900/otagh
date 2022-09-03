from django import template
from django.utils.html import format_html
import pandas as pd

register = template.Library()


#lst=[[1,'a','aa','ac',0],[2,'b','aa','ac',0],[3,'c','aa','ac',1],[4,'d','aa','ac',3],[5,'e','aa','ac',1]]
#df = pd.DataFrame(lst, columns =['id', 'title', 'link','clas','parent'])
@register.filter
def limenu(value,parent=0):
    data=value.query('parent==%s' % parent)
    if data.empty:
        return
    limenu.txt+='<ul>'
    for i,row in data.iterrows():
            limenu.txt+=format_html("<li class='{}'><a href='{}'>{}</a>",row['clas'],row['link'],row['title'])
            limenu(value,row['id'])
            limenu.txt+='</li>'
    limenu.txt+='</ul>'
    return limenu.txt

limenu.txt=''