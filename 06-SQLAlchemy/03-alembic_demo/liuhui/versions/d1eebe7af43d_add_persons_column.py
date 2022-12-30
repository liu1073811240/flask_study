"""add persons column

Revision ID: d1eebe7af43d
Revises: 6f0997f9667a
Create Date: 2022-12-27 17:48:41.141539

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd1eebe7af43d'
down_revision = '6f0997f9667a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('persons', sa.String(length=5000), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'persons')
    # ### end Alembic commands ###
