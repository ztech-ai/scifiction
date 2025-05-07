import os
from dotenv import load_dotenv
from prompts import PROMPT_CONFIG

load_dotenv()

PROMPT_CONFIG = PROMPT_CONFIG

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
MAX_RETRIES = 3
RETRY_DELAY = 1.5
MAX_TOKENS = int(os.getenv('MAX_TOKENS', 5000))