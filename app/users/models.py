from datetime import datetime
from sqlalchemy import (
    Boolean,
    Column,
    Integer,
    String,
    DateTime,
)

from app.config.database import DBBase


class UserBalances(DBBase):
    __tablename__ = "user_balances"

    address = Column(String(255), primary_key=True)
    onChainBal = Column(String(255), nullable=False)
    localBal = Column(String(255), nullable=False)
    inPlay = Column(String(255), nullable=False)