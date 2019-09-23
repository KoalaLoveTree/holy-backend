"""create account table

Revision ID: 1ae8d3c45521
Revises:
Create Date: 2019-09-18 20:02:54.782249

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1ae8d3c45521'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'account',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String(50), nullable=False),
        sa.Column('password', sa.String(60)),
    )


def downgrade():
    op.drop_table('account')
