"""add cols to orders

Revision ID: 0986ca5337ba
Revises: 984ed45fbfc2
Create Date: 2022-12-09 19:29:16.291381

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0986ca5337ba'
down_revision = '984ed45fbfc2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('orders', schema=None) as batch_op:
        batch_op.add_column(sa.Column('customer_id', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('shop_id', sa.Integer(), nullable=False))
        batch_op.drop_constraint('fk_order_user_id', type_='foreignkey')
        batch_op.create_foreign_key('fk_order_customer_id', 'users', ['customer_id'], ['id'])
        batch_op.create_foreign_key('fk_order_shop_id', 'users', ['shop_id'], ['id'])
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('orders', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.INTEGER(), nullable=False))
        batch_op.drop_constraint('fk_order_shop_id', type_='foreignkey')
        batch_op.drop_constraint('fk_order_customer_id', type_='foreignkey')
        batch_op.create_foreign_key('fk_order_user_id', 'users', ['user_id'], ['id'])
        batch_op.drop_column('shop_id')
        batch_op.drop_column('customer_id')

    # ### end Alembic commands ###
