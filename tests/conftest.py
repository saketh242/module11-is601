import os
import sys


def _add_project_root_to_path():
    # tests are in tests/, project root is one level up
    here = os.path.dirname(__file__)
    project_root = os.path.abspath(os.path.join(here, ".."))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)


_add_project_root_to_path()
