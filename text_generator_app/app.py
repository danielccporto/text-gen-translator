from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline

# Inicialização modelo GPT-2
text_generator = pipeline("text-generation", model="gpt2")

# Inicialização FastAPI
app = FastAPI()

# Definição para entrada de dados
class TextInput(BaseModel):
    input_text: str

# Função para geração de texto
@app.post("/generate-text/")
async def generate_text(input_data: TextInput):
    """
    Gera uma continuação de texto a partir de uma frase de entrada.
    """
    try:
        generated = text_generator(input_data.input_text, max_length=50, num_return_sequences=1)
        return {"input": input_data.input_text, "generated_text": generated[0]["generated_text"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Inicialização modelo tradução
translator = pipeline("translation_en_to_fr", model="Helsinki-NLP/opus-mt-en-fr")

@app.post("/translate/")
async def translate_text(input_data: TextInput):
    """
    Traduz texto do inglês para o francês usando o modelo Helsinki-NLP/opus-mt-en-fr.
    """
    try:
        # Tradução do texto de entrada
        translated = translator(input_data.input_text, max_length=500) 
        return {"input": input_data.input_text, "translated_text": translated[0]["translation_text"]}
    except Exception as e:
        # Tratamento de erros com retorno HTTP apropriado
        raise HTTPException(status_code=500, detail=f"Erro ao traduzir o texto: {str(e)}")

