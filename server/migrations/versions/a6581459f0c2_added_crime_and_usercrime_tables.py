"""added crime and usercrime tables

Revision ID: a6581459f0c2
Revises: 1c5b3c1e2ecd
Create Date: 2023-03-24 15:10:12.354795

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a6581459f0c2'
down_revision = '1c5b3c1e2ecd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('crimes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('lethal', sa.Boolean(), nullable=True),
    sa.Column('misdemeanor', sa.Boolean(), nullable=True),
    sa.Column('felony', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_crimes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('crime_id', sa.Integer(), nullable=True),
    sa.Column('date', sa.String(), nullable=True),
    sa.Column('caught', sa.Boolean(), nullable=True),
    sa.Column('convicted', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['crime_id'], ['crimes.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_crimes')
    op.drop_table('crimes')
    # ### end Alembic commands ###