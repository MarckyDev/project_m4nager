from google import genai
from dotenv import load_dotenv
import os

class Martin:
    def __init__(self):
        load_dotenv()
        self.client = genai.Client(
            api_key= os.getenv("GEMINI_API_KEY")
        )
        
        
        self.user_input = self.listen()
        self.is_done_listening = True
        
    def run(self) -> None:
        while not self.is_done_listening:
            self.user_input = self.listen()
            self.is_done_listening = True

    def _run_configuration(self) -> None:
        """
        Configures the client with the necessary parameters.
        
        
        The ai should respond when called "Martin"
        """
        ...
        

    def talk(self, response:str) -> str:
        
        ...

    
    def listen(self) -> str:
        """Listens for user input.

        Returns:
            str: The user's input.
        """
        ...