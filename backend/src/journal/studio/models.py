from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from ...database import Model


class Studio(Model):
    __tablename__ = 'studio'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    is_active: Mapped[bool] = mapped_column(default=True)
