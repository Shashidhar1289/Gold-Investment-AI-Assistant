from fastapi import APIRouter
from models import PurchaseRequest
from database import insert_purchase

router = APIRouter()

GOLD_PRICE_PER_GRAM = 6100


@router.post("/buy-gold")
def buy_gold(data: PurchaseRequest):

    gold_grams = data.amount / GOLD_PRICE_PER_GRAM

    insert_purchase(data.user_id, data.amount, gold_grams)

    return {
        "status": "success",
        "message": "Digital gold purchased successfully",
        "gold_grams": round(gold_grams, 3)
    }