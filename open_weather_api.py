# -*- coding: utf-8 -*-
"""Open_Weather_API.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/GlenLuiz/FIAP/blob/main/Open_Weather_API.ipynb

# Consumindo a API do OPEN WEATHER

OpenWeatherMap é um serviço online, de propriedade da OpenWeather Ltd, que fornece dados meteorológicos globais via API, incluindo dados meteorológicos atuais, previsões, previsões e dados meteorológicos históricos para qualquer localização geográfica

https://openweathermap.org/

## Exercício

Consuma a API OPEN WEATHER de uma cidade que comece com a mesma letra do seu nome, normalize a saida para que seja amigavel para o usuário, e converta as unidades para os padrões que usamos no Brasil.

Para isso consulte a documentação do openweather, doc da biblioteca "requests" do python e materiais onlines

Após terminar o exercicio, disponibilize um link do **github** em um repositorio da sua escolha para a correção

*Arquivo > Salvar uma cópia no Github*

Insira seu nome e RM abaixo
"""

nome = input('Insira seu nome: ')
rm = input('Insira seu rm: ')

"""# Utilize a **Current weather data** para acessar o clima local da cidade

Exemplo de endpoint utilizado na doc da api

https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}
"""

#Lembre-se de importar a biblioteca
import requests

API_KEY = "f6a7f6b1bb99db0698cbdf6eaed6deee"
cidade = "London"
endpoint = f"https://api.openweathermap.org/data/2.5/weather?q=London&appid=f6a7f6b1bb99db0698cbdf6eaed6deee"

resposta = requests.get(endpoint).json()

"""A saida da sua API deve conter 2 informações essenciais:



1.   Descrição ( description )
2.   Temperatura em Celsius ( temp )

Insira abaixo a saida normalizada:

"""

desc = resposta["weather"][0]["description"]
temp = resposta["main"]['temp']
print(desc,temp)

temp_c = temp - 273
print(f"Grau Celsius: {temp_c:.2f}")

