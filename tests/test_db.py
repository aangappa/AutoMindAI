import sys
from pathlib import Path

project_root = (
    Path(__file__)
    .resolve()
    .parent.parent
)

sys.path.append(
    str(project_root / "src" / "automind")
)

from mvc.database.config import (
    DatabaseConfig,
)
from mvc.database.engine import (
    DatabaseEngine,
)

print("Connection URL:")
print(DatabaseConfig.url())

print()

print("Connection Test:")
print(DatabaseEngine.test_connection())