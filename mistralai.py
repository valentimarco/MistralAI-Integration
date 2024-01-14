from typing import List, Optional, Type
from cat.mad_hatter.decorators import tool, hook, plugin
from pydantic import BaseModel, ConfigDict, SecretStr
from datetime import datetime, date
from cat.factory.llm import LLMSettings
from langchain_mistralai.chat_models import ChatMistralAI

class MistralAIConfig(LLMSettings):
    """The configuration for the MistralAI plugin."""

    """The API key for TogetherAI."""
    mistral_api_key: Optional[SecretStr]
    model: str = "mistral-small"
    max_tokens: Optional[int] = 4096
    top_p: float = 1
    
    _pyclass: Type = ChatMistralAI

    model_config = ConfigDict(
        json_schema_extra={
            "humanReadableName": "MistralAI",
            "description": "Configuration for MistralAI",
            "link": "https://www.together.ai",
        }
    )
    

@hook
def factory_allowed_llms(allowed, cat) -> List:
    allowed.append(MistralAIConfig)
    return allowed