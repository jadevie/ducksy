"""add_cols_to_order_detail

Revision ID: b3d9f19bcc8f
Revises: 186d6856094d
Create Date: 2022-12-14 20:07:02.363038

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b3d9f19bcc8f'
down_revision = '186d6856094d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order_details', schema=None) as batch_op:
        batch_op.add_column(sa.Column('buyer_id', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('quantity', sa.Integer(), nullable=False))
        batch_op.create_foreign_key('fk_order_detail_buyer_id', 'users', ['buyer_id'], ['id'], ondelete='CASCADE')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order_details', schema=None) as batch_op:
        batch_op.drop_constraint('fk_order_detail_buyer_id', type_='foreignkey')
        batch_op.drop_column('quantity')
        batch_op.drop_column('buyer_id')

    # ### end Alembic commands ###
