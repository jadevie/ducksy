"""create categories table

Revision ID: 08957bb0dc5c
Revises: 0986ca5337ba
Create Date: 2022-12-11 11:10:20.024566

"""
from alembic import op
import sqlalchemy as sa

import os
environment = os.getenv("FLASK_ENV")
SCHEMA = os.environ.get("SCHEMA")
# revision identifiers, used by Alembic.
revision = '08957bb0dc5c'
down_revision = '0986ca5337ba'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # with op.batch_alter_table('orders', schema=None) as batch_op:
        # batch_op.drop_constraint('fk_order_seller_id', type_='foreignkey')
        # batch_op.drop_column('seller_id')

    with op.batch_alter_table('order_details', schema=None) as batch_op:
        batch_op.create_foreign_key('fk_order_detail_seller_id', 'users', ['seller_id'], ['id'])

    # ### end Alembic commands ###
    if environment == "production":
        op.execute(f"ALTER TABLE categories SET SCHEMA {SCHEMA};")

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order_details', schema=None) as batch_op:
        batch_op.drop_constraint('fk_order_detail_seller_id', type_='foreignkey')

    # with op.batch_alter_table('orders', schema=None) as batch_op:
        # batch_op.add_column(sa.Column('seller_id', sa.INTEGER(), nullable=False))
        # batch_op.create_foreign_key('fk_order_seller_id', 'users', ['seller_id'], ['id'])

    op.drop_table('categories')
    # ### end Alembic commands ###
