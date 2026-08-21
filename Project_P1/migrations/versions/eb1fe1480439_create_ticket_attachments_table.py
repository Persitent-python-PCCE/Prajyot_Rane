"""Create ticket attachments table

Revision ID: eb1fe1480439
Revises: 7c41e270fcf1
Create Date: 2026-08-20 12:55:37.897897

"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'eb1fe1480439'
down_revision = '7c41e270fcf1'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'ticket_assignments',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('ticket_id', sa.Integer(), nullable=False),
        sa.Column('agent_id', sa.Integer(), nullable=False),
        sa.Column(
            'assigned_at',
            sa.DateTime(),
            server_default=sa.text('now()'),
            nullable=False,
        ),
        sa.Column('assigned_by', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['ticket_id'], ['tickets.id']),
        sa.ForeignKeyConstraint(['agent_id'], ['users.id']),
        sa.ForeignKeyConstraint(['assigned_by'], ['users.id']),
        sa.PrimaryKeyConstraint('id'),
    )
    # ### end Alembic commands ###


def downgrade():
    op.drop_table('ticket_attachments')
    # ### end Alembic commands ###
