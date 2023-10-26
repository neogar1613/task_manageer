"""Create user profile table

Revision ID: 14dd20d035ce
Revises: 5998ab48f00c
Create Date: 2023-10-26 20:02:05.356030

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "14dd20d035ce"
down_revision: Union[str, None] = "5998ab48f00c"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "userprofiles",
        sa.Column("first_name", sa.String(length=32), nullable=True),
        sa.Column("last_name", sa.String(length=32), nullable=True),
        sa.Column(
            "id",
            sa.Uuid(),
            server_default=sa.text("uuid_generate_v4()"),
            nullable=False,
        ),
        sa.Column("user_id", sa.Uuid(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("user_id"),
    )
    op.drop_constraint("projects_user_id_fkey", "projects", type_="foreignkey")
    op.create_foreign_key(None, "projects", "users", ["user_id"], ["id"])
    op.drop_constraint("tasks_user_id_fkey", "tasks", type_="foreignkey")
    op.create_foreign_key(None, "tasks", "users", ["user_id"], ["id"])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "tasks", type_="foreignkey")
    op.create_foreign_key(
        "tasks_user_id_fkey",
        "tasks",
        "users",
        ["user_id"],
        ["id"],
        onupdate="CASCADE",
        ondelete="CASCADE",
    )
    op.drop_constraint(None, "projects", type_="foreignkey")
    op.create_foreign_key(
        "projects_user_id_fkey",
        "projects",
        "users",
        ["user_id"],
        ["id"],
        onupdate="CASCADE",
        ondelete="CASCADE",
    )
    op.drop_table("userprofiles")
    # ### end Alembic commands ###
