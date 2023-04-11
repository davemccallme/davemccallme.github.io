
import os
import openai
import urllib3
import requests

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

openai.organization = "org-AC2RGMuaXfFEbRfhmmkJ74Ef"

#Dim6 personal OpenAI API key - $$$ 
os.environ["OPENAI_API_KEY"] = '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'   


openai.api_key = os.getenv("OPENAI_API_KEY")


response = requests.get('https://api.openai.com/v1/completions', verify=False)

###
# Update TLS/SSL certs
#cafile = r"C:\Users\DIM6\OneDrive - PGE\Documents\GitHub\davemccallme.github.io\scratch\LLM\cacert.pem"
#url = 'https://api.openai.com/v1/completions'
#response = requests.get(url, verify=cafile)
#os.environ['REQUESTS_CA_BUNDLE'] = cafile
###

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="I am a highly intelligent question answering bot. If you ask me a question that is rooted in truth, I will give you the answer. If you ask me a question that is nonsense, trickery, or has no clear answer, I will respond with \"Unknown\".\n\nQ: What is human life expectancy in the United States?\nA: Human life expectancy in the United States is 78 years.\n\nQ: Who was president of the United States in 1955?\nA: Dwight D. Eisenhower was president of the United States in 1955.\n\nQ: Which party did he belong to?\nA: He belonged to the Republican Party.\n\nQ: What is the square root of banana?\nA: Unknown\n\nQ: How does a telescope work?\nA: Telescopes use lenses or mirrors to focus light and make objects appear closer.\n\nQ: Where were the 1992 Olympics held?\nA: The 1992 Olympics were held in Barcelona, Spain.\n\nQ: How many squigs are in a bonk?\nA: Unknown\n\nQ: Where is the Valley of Kings?\nA:",
  temperature=0,
  max_tokens=100,
  top_p=1,
  frequency_penalty=0.0,
  presence_penalty=0.0,
  stop=["\n"]
)