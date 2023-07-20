"""create example and user table

Revision ID: 1e2a572f99d6
Revises: 
Create Date: 2023-07-20 20:35:48.479055

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1e2a572f99d6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=191), nullable=True),
    sa.Column('username', sa.String(length=191), nullable=False),
    sa.Column('email', sa.String(length=191), nullable=False),
    sa.Column('password', sa.String(length=191), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('update_at', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_index(op.f('ix_users_name'), 'users', ['name'], unique=False)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.create_table('examples',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=191), nullable=True),
    sa.Column('description', sa.String(length=191), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('update_at', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_examples_description'), 'examples', ['description'], unique=False)
    op.create_index(op.f('ix_examples_id'), 'examples', ['id'], unique=False)
    op.create_index(op.f('ix_examples_title'), 'examples', ['title'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_examples_title'), table_name='examples')
    op.drop_index(op.f('ix_examples_id'), table_name='examples')
    op.drop_index(op.f('ix_examples_description'), table_name='examples')
    op.drop_table('examples')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_name'), table_name='users')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###