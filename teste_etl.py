import datetime
from datetime import date

x = date.today()
ini = x.strftime('%Y-%m-01')
fim = x.strftime('%Y-%m-31')

print(f'Usar datas: {ini} até {fim}')