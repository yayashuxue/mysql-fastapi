from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.users import schemas, services, selectors

router = APIRouter()


# GET
@router.get("/", summary="list user balnces", response_model=list[schemas.UserBalances])
async def list_users(db=Depends(get_db)):
    return selectors.get_users_balances(db=db)


# POST
@router.post(
    "/create",
    summary="create user balances",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.UserCreate,
)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return services.create_user(user=user, db=db)


# PUT

# DELETE
