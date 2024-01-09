from datetime import datetime as _dt

import sqlalchemy as _sql
import sqlalchemy.orm as _orm

from . import schemas as _schemas
from .database import Base as _Base


class Notification(_Base):
    id: _orm.Mapped[int] = _orm.mapped_column(_sql.Integer, primary_key=True)

    created: _orm.Mapped[_dt] = _orm.mapped_column(
        _sql.DateTime, index=True, nullable=False, default=_dt.utcnow
    )

    name: _orm.Mapped[str] = _orm.mapped_column(
        _sql.String, index=True, nullable=False
    )

    description: _orm.Mapped[str] = _orm.mapped_column(
        _sql.String, nullable=False, default=""
    )

    hitpoints: _orm.Mapped[int] = _orm.mapped_column(
        _sql.Integer,
        index=True,
        nullable=True,
    )


class NotificationRotaion(_Base):
    notification_id: _orm.Mapped[int] = _orm.mapped_column(
        _sql.Integer, _sql.ForeignKey("Notification.id"), primary_key=True
    )

    type_: _orm.Mapped[_schemas.RotationType] = _orm.mapped_column(
        _sql.Enum(_schemas.RotationType), index=True, nullable=False
    )
