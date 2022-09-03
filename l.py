import pandas as pd
from django.utils.html import format_html

lst=[[1,'a','aa','ac',0],[2,'b','aa','ac',0],[3,'c','aa','ac',1],[4,'d','aa','ac',3],[5,'e','aa','ac',1]]
df = pd.DataFrame(lst, columns =['id', 'title', 'link','clas','parent'])

def menu(val,parent=0):
    data=val.query('parent=={}'.format(parent))
    if data.empty:
        return
    menu.txt+='<ul>'
    for i,row in data.iterrows():
            menu.txt+=format_html("<li class='{}'><a href='{}'>{}</a>",row['clas'],row['link'],row['title'])
            menu(val,row['id'])
            menu.txt+='</li>'
    menu.txt+='</ul>'
    return menu.txt


menu.txt=''
print(menu(df))



