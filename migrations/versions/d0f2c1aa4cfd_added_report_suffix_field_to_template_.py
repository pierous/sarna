"""Added 'report_suffix' field to Template table.

Revision ID: d0f2c1aa4cfd
Revises: 951b8ed9a8e1
Create Date: 2020-08-04 14:00:36.411851

"""
from alembic import op
from sqlalchemy import orm
from sarna.model.client import Template

import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd0f2c1aa4cfd'
down_revision = '951b8ed9a8e1'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('template', sa.Column('report_suffix', sa.String(length=128), nullable=True))

    session = orm.Session(bind=op.get_bind())

    for template in session.query(Template):
        template.report_suffix = template.name

    session.commit()

    op.alter_column('template', 'report_suffix', nullable=False)


def downgrade():
# ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('template', 'report_suffix')
    # ### end Alembic commands ###
