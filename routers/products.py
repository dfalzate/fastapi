
from fastapi import APIRouter

router =APIRouter(prefix="/products", tags=["Products"])

products=["product1","product2","product3"]

@router.get('/')
async def getProducts():
  return products