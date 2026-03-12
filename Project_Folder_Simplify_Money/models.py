from pydantic import BaseModel


class ChatRequest(BaseModel):
    user_id: int
    message: str


class PurchaseRequest(BaseModel):
    user_id: int
    amount: float