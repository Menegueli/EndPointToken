# Flask Bitcoin Price API

Este é um aplicativo Flask simples que fornece uma rota para obter a cotação atual do Bitcoin em relação ao Real (BRL). A cotação é obtida utilizando a API pública CoinGecko.

## Pré-requisitos

Certifique-se de ter o Flask e as dependências necessárias instaladas. Você pode instalá-las usando:

```bash
pip install flask requests python-dotenv
```

## Configuração

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

2. Navegue até o diretório do projeto:

```bash
cd seu-repositorio
```

3. Crie um arquivo `.env` na raiz do projeto e adicione o seu token da API CoinGecko:

```env
API_TOKEN=sua-chave-de-api-aqui
```

## Como Usar

1. Execute o aplicativo:

```bash
python app.py
```

O aplicativo estará disponível em [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

2. Acesse a rota `/cotacao-bitcoin` para obter a cotação atual do Bitcoin em relação ao Real:

```bash
curl http://127.0.0.1:5000/cotacao-bitcoin
```

ou abra a rota no seu navegador.

## Estrutura do Projeto

- `app.py`: Contém o código principal do aplicativo Flask.
- `.env`: Arquivo de configuração para armazenar as variáveis de ambiente, incluindo o token da API CoinGecko.
- `requirements.txt`: Lista de dependências do Python necessárias para o projeto.

## Contribuindo

Sinta-se à vontade para contribuir com melhorias, correções de bugs ou novos recursos. Basta seguir as etapas mencionadas no README.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

Esse README oferece uma visão geral do seu aplicativo Flask para obter a cotação do Bitcoin, instruções de configuração, uso e contribuição, além de informações sobre a estrutura do projeto e a licença. Certifique-se de personalizar as seções conforme necessário para o seu aplicativo específico.
