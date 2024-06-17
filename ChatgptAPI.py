import openai

openai.api_key ='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'

question = 'what is the capital of france'

response = openai.Completion.create(
    engine = 'text-davinci-003',
    prompt = question,
    max_tokem = 50
)
print(response)

