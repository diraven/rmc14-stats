"""empty message

Revision ID: bd11716afc6a
Revises: c11a00e35128
Create Date: 2024-07-18 14:42:25.220401

"""

from typing import Sequence, Union

import sqlalchemy as sa

from src import models

# revision identifiers, used by Alembic.
revision: str = "bd11716afc6a"
down_revision: Union[str, None] = "c11a00e35128"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with models.Session.begin() as session:
        session.add(models.Faction(id=models.DEFAULT_WINNING_FACTION))
        session.add(models.Faction(id="xenoids"))
        session.execute(
            sa.update(models.Round).values(
                winning_faction=models.DEFAULT_WINNING_FACTION
            )
        )


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
