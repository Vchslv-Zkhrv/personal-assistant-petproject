from datetime import date as _date
from datetime import time as _time
from datetime import datetime as _dt

import sqlalchemy as _sql
import sqlalchemy.orm as _orm

from .database import Base as _Base
from . import schemas as _schemas


class Notification(_Base):

    id: _orm.Mapped[int] = _orm.mapped_column(
        _sql.Integer,
        primary_key=True
    )

    created: _orm.Mapped[_dt] = _orm.mapped_column(
        _sql.DateTime,
        index=True,
        nullable=False,
        default=_dt.utcnow
    )

    name: _orm.Mapped[str] = _orm.mapped_column(
        _sql.String,
        index=True,
        nullable=False
    )

    description: _orm.Mapped[str] = _orm.mapped_column(
        _sql.String,
        nullable=False,
        default=""
    )

    hitpoints: _orm.Mapped[int] = _orm.mapped_column(
        _sql.Integer,
        index=True,
        nullable=True,
    )


class NotificationRotaion(_Base):

    notification_id: _orm.Mapped[int] = _orm.mapped_column(
        _sql.Integer,
        _sql.ForeignKey("Notification.id"),
        primary_key=True
    )

    type_: _orm.Mapped[_schemas.RotationType] = _orm.mapped_column(
        _sql.Enum(_schemas.RotationType),
        index=True,
        nullable=False
    )
