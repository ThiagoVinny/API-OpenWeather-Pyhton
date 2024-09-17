import requests

cidade = input("Digite a sua cidade: ")
chaveAPI = 'SUA_CHAVE_VALIDA_AQUI'  # Substitua pela sua chave de API válida
link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chaveAPI}"

# Faz a requisição e verifica se ocorreu um erro
requisicao = requests.get(link)

# Verifica se a resposta da requisição foi bem-sucedida
if requisicao.status_code == 200:
    requisicao = requisicao.json()

    nomeCidade = requisicao['name']
    paisCidade = requisicao['sys']['country']
    pressaoCidade = requisicao['main']['pressure']
    temperaturaCidade = requisicao['main']['temp'] - 273.15  # Corrigindo a conversão de Kelvin para Celsius
    umidadeCidade = requisicao['main']['humidity']
    velocidadeVentoCidade = requisicao['wind']['speed'] * 1.609  # Convertendo de m/s para km/h

    print(f"\nCidade: {nomeCidade}\nPaís: {paisCidade}\nTemperatura: {temperaturaCidade:.2f} C°")
    print(f"Umidade: {umidadeCidade}%\nVelocidade do vento: {velocidadeVentoCidade:.2f} km/h")
    print(f"Pressão: {pressaoCidade} hPA")
else:
    print(f"Erro ao acessar a API. Código de status: {requisicao.status_code}")
