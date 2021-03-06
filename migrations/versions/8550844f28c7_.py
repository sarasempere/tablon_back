"""empty message

Revision ID: 8550844f28c7
Revises: f6073e7b4247
Create Date: 2020-11-16 17:43:20.376039

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8550844f28c7'
down_revision = 'f6073e7b4247'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('photo', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'photo', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'photo', type_='foreignkey')
    op.drop_column('photo', 'user_id')
    # ### end Alembic commands ###
