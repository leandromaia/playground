from datetime import date

print("Curso de GIT com código Python")

today = date.today()
format_date = today.strftime("%d-%m-%y")
student = "Adriano Eduardo Trentin Junior"

print(f"{student} está fazendo o curso de GIT no dia {format_date}")
