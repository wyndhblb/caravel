"""Enable Filter Select on Tables and Datasources

Revision ID: ae0f4d3a9ea9
Revises: 41f6a59a61f2
Create Date: 2016-09-02 11:37:10.154630

"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'ae0f4d3a9ea9'
down_revision = '41f6a59a61f2'


def upgrade():
    op.add_column('datasources', sa.Column('filter_select_enabled',
                                           sa.Boolean(), default=False))
    op.add_column('tables', sa.Column('filter_select_enabled',
                                      sa.Boolean(), default=False))


def downgrade():
    op.drop_column('tables', 'filter_select_enabled')
    op.drop_column('datasources', 'filter_select_enabled')
