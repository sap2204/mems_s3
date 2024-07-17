from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column


class Mems(Base):
    """Class for model table in DB"""

    __tablename__ = 'mems'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str | None] = mapped_column()
    url: Mapped[str | None] = mapped_column()

