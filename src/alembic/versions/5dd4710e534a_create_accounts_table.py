"""create accounts table

Revision ID: 5dd4710e534a
Revises: 
Create Date: 2019-09-23 21:17:18.525506

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5dd4710e534a'
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
