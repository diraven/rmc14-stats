"""empty message

Revision ID: 1677d542b0f7
Revises: 6d89509c0304
Create Date: 2024-07-18 16:12:52.232847

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1677d542b0f7'
down_revision: Union[str, None] = '6d89509c0304'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('rounds', 'winning_faction',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('rounds', 'winning_faction',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
    # ### end Alembic commands ###
