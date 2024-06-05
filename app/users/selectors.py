from sqlalchemy import text
from sqlalchemy.orm import Session

from app.users import models


def get_users_balances(db: Session):
    """This function returns a list of users from the database

    Args:
        db (Session): The DB session

    Returns:
        list[models.UserBalances]: The user obj list
    """

    return db.query(models.User).all()
