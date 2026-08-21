"""Rename ticket category table

Revision ID: b23c82a4a128
Revises: 63378451b19d
Create Date: 2026-08-20 11:19:58.301290

"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'b23c82a4a128'
down_revision = '63378451b19d'
branch_labels = None
depends_on = None


from alembic import op


def upgrade():
    op.rename_table("ticket_category", "ticket_categories")


def downgrade():
    op.rename_table("ticket_categories", "ticket_category")
