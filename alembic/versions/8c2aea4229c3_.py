"""empty message

Revision ID: 8c2aea4229c3
Revises: fa2683367f41
Create Date: 2024-07-18 21:44:50.341317

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "8c2aea4229c3"
down_revision: Union[str, None] = "fa2683367f41"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "rounds", sa.Column("winning_faction_id", sa.BigInteger(), nullable=True)
    )
    op.drop_constraint(
        "fk_rounds_winning_faction_factions", "rounds", type_="foreignkey"
    )
    op.create_foreign_key(
        op.f("fk_rounds_winning_faction_id_factions"),
        "rounds",
        "factions",
        ["winning_faction_id"],
        ["id"],
    )
    op.drop_column("rounds", "winning_faction")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "rounds",
        sa.Column("winning_faction", sa.BIGINT(), autoincrement=False, nullable=True),
    )
    op.drop_constraint(
        op.f("fk_rounds_winning_faction_id_factions"), "rounds", type_="foreignkey"
    )
    op.create_foreign_key(
        "fk_rounds_winning_faction_factions",
        "rounds",
        "factions",
        ["winning_faction"],
        ["id"],
    )
    op.drop_column("rounds", "winning_faction_id")
    # ### end Alembic commands ###
