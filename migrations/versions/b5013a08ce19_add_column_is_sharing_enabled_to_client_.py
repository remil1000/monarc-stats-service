"""add column is_sharing_enabled to client model

Revision ID: b5013a08ce19
Revises:
Create Date: 2021-02-14 23:44:38.622748

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "b5013a08ce19"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "client",
        sa.Column(
            "is_sharing_enabled",
            sa.Boolean(),
            nullable=False,
            server_default=sa.schema.DefaultClause("True"),
        ),
    )
    try:
        op.create_unique_constraint(None, "stats", ["uuid"])
    except:
        pass
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    try:
        op.drop_constraint(None, "stats", type_="unique")
    except:
        pass
    op.drop_column("client", "is_sharing_enabled")
    # ### end Alembic commands ###
