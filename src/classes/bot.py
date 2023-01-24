import openai

class Bot:
    _TOKEN: str
    _PROMPT: str
    
    def __init__(self, token, prompt) -> None:
        self._TOKEN = token
        self._PROMPT = prompt
        
        if self._TOKEN == "":
            print("You should have an OpenAI token.")
            return
        elif self._PROMPT == "":
            print("You should write a prompt to talk with the bot.")
            return
    
    def respond(self) -> str:
        openai.api_key = self._TOKEN

        response = openai.Completion.create(
            model = "text-davinci-003",
            prompt = self._PROMPT,
            temperature = 0.9,
            max_tokens = 150,
            top_p = 1,
            frequency_penalty = 0.0,
            presence_penalty = 0.6,
            stop = [" Human:", " AI:"]
        )
        
        return response.choices[0].text
    
            