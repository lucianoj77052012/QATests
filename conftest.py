# Make sure conftest.py is in root. By loading it from root, directory changes such that the following lines are no longer required per test_execute file:

# Make the test_steps files accessible from current file.
# import os
# import sys
# root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# sys.path.append(root_path)

import pytest

@pytest.fixture
def some_value():
    return 8