from fastapi import APIRouter
from models import ChatRequest

router = APIRouter()


@router.post("/chat")
def chat(data: ChatRequest):

    message = data.message.lower()

    # Detect gold investment query
    if "gold" in message:

        return {
            "response": "Gold is considered a stable investment and is often used to hedge against inflation. You can also invest in digital gold easily.",
            "suggestion": "Would you like to purchase digital gold? If yes, call /buy-gold API with amount."
        }

    else:

        return {
            "response": "I can help you with investment queries. You can ask about gold investments."
        }