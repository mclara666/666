import requests
import webbrowser

cep = input("Digite o CEP: ").replace("-", "").strip()

url = f"https://viacep.com.br/ws/{cep}/json/"
resposta = requests.get(url)

if resposta.status_code == 200:
    dados = resposta.json()

    if "erro" not in dados:
        html = f"""
        <html>
        <head>
            <title>Consulta de CEP</title>
        </head>
        <body>
            <h1>Resultado do CEP</h1>
            <p><b>CEP:</b> {dados['cep']}</p>
            <p><b>Rua:</b> {dados['logradouro']}</p>
            <p><b>Bairro:</b> {dados['bairro']}</p>
            <p><b>Cidade:</b> {dados['localidade']}</p>
            <p><b>Estado:</b> {dados['uf']}</p>
        </body>
        </html>
        """

        # Salva o arquivo
        with open("resultado.html", "w", encoding="utf-8") as arquivo:
            arquivo.write(html)

        # Abre no navegador (Chrome padrão)
        webbrowser.open("resultado.html")

    else:
        print("CEP não encontrado!")
else:
    print("Erro na requisição:", resposta.status_code)