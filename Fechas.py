import datetime

now = datetime.datetime.now()
print(now)
print("Año: {now.year}")
print(f"Mes: {now.month}")
print("Dia: {h}:{m}:{s}".format(h=now.hour, m=now.minute, s=now.second))
