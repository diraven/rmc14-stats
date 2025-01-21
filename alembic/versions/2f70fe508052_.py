"""empty message

Revision ID: 2f70fe508052
Revises: 86e97f3be678
Create Date: 2024-09-07 19:44:32.457689

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "2f70fe508052"
down_revision: Union[str, None] = "86e97f3be678"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "rounds",
        "winning_score",
        existing_type=sa.DOUBLE_PRECISION(precision=53),
        nullable=False,
    )
    op.alter_column(
        "rounds", "summary_message", existing_type=sa.TEXT(), nullable=False
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("rounds", "summary_message", existing_type=sa.TEXT(), nullable=True)
    op.alter_column(
        "rounds",
        "winning_score",
        existing_type=sa.DOUBLE_PRECISION(precision=53),
        nullable=True,
    )
    # ### end Alembic commands ###
