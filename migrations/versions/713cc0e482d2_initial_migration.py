"""Initial migration

Revision ID: 713cc0e482d2
Revises: 
Create Date: 2023-07-26 17:41:07.006459

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '713cc0e482d2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.add_column(sa.Column('discount', sa.Integer(), nullable=True))

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('company', sa.String(length=255), nullable=True))
        batch_op.alter_column('data',
               existing_type=sa.BLOB(),
               nullable=True)
        batch_op.alter_column('registration_status',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('registration_status',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=False)
        batch_op.alter_column('data',
               existing_type=sa.BLOB(),
               nullable=False)
        batch_op.drop_column('company')

    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.drop_column('discount')

    # ### end Alembic commands ###
