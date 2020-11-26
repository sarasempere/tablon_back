"""empty message

Revision ID: 29e4fbaaa66e
Revises: 8550844f28c7
Create Date: 2020-11-24 16:31:36.171738

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '29e4fbaaa66e'
down_revision = '8550844f28c7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('photo', sa.Column('latitude', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('photo', 'latitude')
    # ### end Alembic commands ###
