from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import ARRAY
import datetime
import sqlalchemy as sa

class Base(DeclarativeBase):
    pass

class Area(Base):
    __tablename__ = 'areas'
    area_id   : Mapped[int]             = mapped_column(sa.BigInteger, primary_key=True)
    name      : Mapped[str]             = mapped_column(sa.String(256))
    url       : Mapped[str]             = mapped_column(sa.String(256))
    vacancies : Mapped[list['Vacancy']] = relationship('Vacancy', back_populates='area')


class Vacancy(Base):
    __tablename__ = 'vacancies'
    vacancy_id      : Mapped[int]               = mapped_column(sa.BigInteger, primary_key=True)
    url             : Mapped[str]               = mapped_column(sa.String(256))
    name            : Mapped[str]               = mapped_column(sa.String(256))
    area_id         : Mapped[int]               = mapped_column(sa.BigInteger, sa.ForeignKey('areas.area_id'))
    salary_from     : Mapped[int  | None]       = mapped_column(sa.BigInteger)
    salary_to       : Mapped[int  | None]       = mapped_column(sa.BigInteger)
    salary_currency : Mapped[str  | None]       = mapped_column(sa.String(10))
    salary_gross    : Mapped[bool | None]       = mapped_column(sa.Boolean)
    salary_mode     : Mapped[str  | None]       = mapped_column(sa.String(256))
    published_at    : Mapped[datetime.datetime] = mapped_column(sa.DateTime)
    created_at      : Mapped[datetime.datetime] = mapped_column(sa.DateTime)
    benefits        : Mapped[list[str] | None]  = mapped_column(ARRAY(sa.String))
    archived        : Mapped[bool]              = mapped_column(sa.Boolean)
    requirement     : Mapped[str | None]        = mapped_column(sa.Text)
    responsibility  : Mapped[str | None]        = mapped_column(sa.Text)
    area            : Mapped['Area']            = relationship('Area', back_populates='vacancies')