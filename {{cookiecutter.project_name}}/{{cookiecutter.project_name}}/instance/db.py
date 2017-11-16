"""Database related helpers and variables."""
import re

import sqlalchemy as sa
import sqlalchemy.ext.declarative as declarative
import sqlalchemy.schema as schema

# Recommended naming convention used by Alembic, as various different database
# providers will autogenerate vastly different names making migrations more
# difficult. See: http://alembic.zzzcomputing.com/en/latest/naming.html
NAMING_CONVENTION = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}


class ModelBase(object):
    """Base class for ORM tables.
    Any ORM table model should inherit the `model.meta.Base`
    declarative base. This base class provides -
        1. id for any entry
        2. table name in table_name syntax
        3. _created and _updated columns for eve
        4. a _etag column for eve 
    """

    id = sa.Column(sa.Integer, primary_key=True)
    _created = sa.Column(sa.DateTime, server_default=sa.func.now())
    _updated = sa.Column(sa.DateTime, server_default=sa.func.now(),
                         onupdate=sa.func.now())
    _etag = sa.Column(sa.Text, nullable=False)

    @declarative.declared_attr
    def __tablename__(cls):
        name = cls.__name__
        return (
            name[0].lower() +
            re.sub(
                r'([A-Z])',
                lambda m: '_' + m.group(0).lower(),
                name[1:]
            )
        )

    def __repr__(self):
        """Reresent an instance as `str`.

        Override it to better represent your model.
        """
        return '{}<{}>'.format(self.__class__.__name__, self.id)


metadata = schema.MetaData(naming_convention=NAMING_CONVENTION)
Base = declarative.declarative_base(metadata=metadata, cls=ModelBase)