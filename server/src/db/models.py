from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
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
    name            : Mapped[str]               = mapped_column(sa.String(256))
    area_id         : Mapped[int]               = mapped_column(sa.BigInteger, sa.ForeignKey('areas.area_id'))
    selary_from     : Mapped[int  | None]       = mapped_column(sa.BigInteger)
    selary_to       : Mapped[int  | None]       = mapped_column(sa.BigInteger)
    selary_currency : Mapped[str  | None]       = mapped_column(sa.String(10))
    selary_gross    : Mapped[bool | None]       = mapped_column(sa.Boolean)
    selary_mode     : Mapped[str  | None]       = mapped_column(sa.String(10))
    published_at    : Mapped[datetime.datetime] = mapped_column(sa.DateTime)
    created_at      : Mapped[datetime.datetime] = mapped_column(sa.DateTime)
    archived        : Mapped[bool]              = mapped_column(sa.Boolean)
    requirement     : Mapped[str]               = mapped_column(sa.Text)
    responsibility  : Mapped[str]               = mapped_column(sa.Text)
    area            : Mapped['Area']            = relationship('Area', back_populates='vacancies')