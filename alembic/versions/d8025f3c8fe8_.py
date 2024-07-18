"""empty message

Revision ID: d8025f3c8fe8
Revises:
Create Date: 2024-07-17 20:34:21.929522

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "d8025f3c8fe8"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "maps",
        sa.Column("id", sa.String(length=100), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_maps")),
    )
    op.create_table(
        "players",
        sa.Column("id", sa.String(length=100), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_players")),
    )
    op.create_table(
        "rounds",
        sa.Column("id", sa.BigInteger(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("map", sa.String(length=100), nullable=False),
        sa.Column("round_end_text", sa.Text(), nullable=False),
        sa.ForeignKeyConstraint(["map"], ["maps.id"], name=op.f("fk_rounds_map_maps")),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_rounds")),
    )
    op.create_table(
        "players_rounds",
        sa.Column("id", sa.BigInteger(), nullable=False),
        sa.Column("player_id", sa.String(length=100), nullable=False),
        sa.Column("round_id", sa.BigInteger(), nullable=False),
        sa.ForeignKeyConstraint(
            ["player_id"],
            ["players.id"],
            name=op.f("fk_players_rounds_player_id_players"),
        ),
        sa.ForeignKeyConstraint(
            ["round_id"], ["rounds.id"], name=op.f("fk_players_rounds_round_id_rounds")
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_players_rounds")),
        sa.UniqueConstraint(
            "player_id", "round_id", name=op.f("uq_players_rounds_player_id")
        ),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("players_rounds")
    op.drop_table("rounds")
    op.drop_table("players")
    op.drop_table("maps")
    # ### end Alembic commands ###
