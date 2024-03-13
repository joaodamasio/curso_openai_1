from openai import OpenAI
from dotenv import load_dotenv
import os

'''Permite ler as chaves criadas e traze-las para dentro do python com acesso via
Sistema Operacional'''

load_dotenv()

'''Acessando a chave gerada via SO e buscando dentro do diretório de váriaveis de ambiente a chave
que acabamos de armazenar,  que foi salva dentro do diretório OPEN_API_KEY'''

cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

'''Armezenamos a resposta que vem da OpenAI através da completions.create() que é a troca de mensagens que fizemos
onde enviamos solicitações para a API através de prompts e ela nos devolve uma resposta'''
resposta = cliente.chat.completions.create(
    messages=[
        {
            "role":"system",
            "content": "Listar apenas os nomes dos produtos, sem considerar descrição."
        },
        {
            "role": "user",
            "content" : "Liste 3 produtos sustentáveis"
        }
    ],
    model="gpt-3.5-turbo"
)

print(resposta.choices[0].message.content)