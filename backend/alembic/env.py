from alembic import context
import os, sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

config = context.config
target_metadata = None

