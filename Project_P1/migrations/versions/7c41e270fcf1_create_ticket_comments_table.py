"""Create ticket comments table

Revision ID: 7c41e270fcf1
Revises: b23c82a4a128
Create Date: 2026-08-20 12:28:53.540413

"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '7c41e270fcf1'
down_revision = 'b23c82a4a128'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'ticket_comments',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('ticket_id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('comment', sa.Text(), nullable=False),
        sa.Column(
            'created_at',
            sa.DateTime(),
            server_default=sa.text('CURRENT_TIMESTAMP'),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ['ticket_id'],
            ['tickets.id'],
        ),
        sa.ForeignKeyConstraint(
            ['user_id'],
            ['users.id'],
        ),
        sa.PrimaryKeyConstraint('id'),
    )


def downgrade():
    op.drop_table('ticket_comments')
    # ### end Alembic commands ###
