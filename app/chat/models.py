from sqlalchemy import ForeignKey,Text
from sqlalchemy.orm import Mapped,mapped_column
from app.database import Base


class Message(Base):
    __tablename__ = 'messages'

    id: Mapped[int] = mapped_column(primary_key=True,index=True)
    sender_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    recipient_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    content: Mapped[str] = mapped_column(Text)