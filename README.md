
# Text Generator and Translator API"""

## Este projeto consiste em uma API desenvolvida com FastAPI, utilizando modelos da HuggingFace para:

1. Gerar textos a partir de uma frase de entrada (usando o modelo GPT-2).
2. Traduzir textos do inglês para o francês (usando o modelo Helsinki-NLP/opus-mt-en-fr).

## Requisitos

### Antes de executar o projeto, certifique-se de ter o seguinte instalado no seu sistema:
1. Python 3.8 ou superior
2. Pip (gerenciador de pacotes do Python)
3. Virtualenv (opcional, mas recomendado)

## Configuração do Ambiente

1. Clone este repositório:
git clone <URL_DO_REPOSITORIO>
cd TP2_DATA_DRIVEN
2. Crie e ative um ambiente virtual:
- python -m venv venv
- venv\Scripts\activate ou source venv/bin/activate
3. Instale as dependências:
- pip install -r requirements.txt

## Como Executar a API

1. Execute o servidor FastAPI:
- uvicorn text_generator_app.app:app --reload
2. A API estará disponível em: http://127.0.0.1:8000
3. Acesse a documentação interativa (Swagger UI) em:
- http://127.0.0.1:8000/docs

## Endpoints Disponíveis 

1. Geração de Texto:
- Endpoint: POST/generate-text/
Descrição:
Gera uma continuação de texto com base em uma frase fornecida como entrada.
obs: modelo possui melhor funcionamento com entrada em inglês.

*Corpo da Requisição:
{
  "input_text": "One day, me and my brother"
}
*Exemplo de Resposta:
{
  "input": "One day, me and my brother",
  "generated_text": "One day, me and my brother got up and we went to the station and we knew the place was getting ready for tomorrow. We were about to go into the station when it turned around and when we looked up at where the door was, the"
}

2. Tradução de Texto:
- Endpoint: POST/translate/
Descrição:
Traduz um texto do inglês para o francês usando o modelo Helsinki-NLP/opus-mt-en-fr.

*Corpo da Requisição:
{
  "input_text": "This is an example of a text in English."
}

*Exemplo de Resposta:
{
  "input": "This is an example of a text in English.",
  "translated_text": "Ceci est un exemple de texte en anglais."
}

obs: Caso o texto de entrada não esteja em inglês, o resultado pode ser inconsistente.


## Possíveis Problemas 

1. Erro sentencepiece:
- Caso o erro ValueError: This tokenizer cannot be instantiated... apareça, 
instale o pacote sentencepiece: pip install sentencepiece

2. Modelos não encontrado:
- Certifique-se de que você tem conexão com a internet ao inicializar os modelos, 
pois eles serão baixados automaticamente na primeira execução.





