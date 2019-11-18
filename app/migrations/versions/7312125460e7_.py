"""empty message

Revision ID: 7312125460e7
Revises: 32dfe82aeb04
Create Date: 2019-11-17 17:10:45.932786

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7312125460e7'
down_revision = '32dfe82aeb04'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('crash_location_point',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('latitude', sa.String(length=140), nullable=True),
    sa.Column('longitude', sa.String(length=140), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_crash_location_point_timestamp'), 'crash_location_point', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_crash_location_point_timestamp'), table_name='crash_location_point')
    op.drop_table('crash_location_point')
    # ### end Alembic commands ###
