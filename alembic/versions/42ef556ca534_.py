"""empty message

Revision ID: 42ef556ca534
Revises: 896a01ccd574
Create Date: 2024-07-18 16:23:18.983525

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '42ef556ca534'
down_revision: Union[str, None] = '896a01ccd574'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('rounds', 'round_end_text')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('rounds', sa.Column('round_end_text', sa.TEXT(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###