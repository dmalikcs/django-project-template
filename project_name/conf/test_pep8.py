# test_pep8 config
TEST_PEP8_DIRS = (
    os.path.dirname(PROJECT_PATH),
)
TEST_PEP8_EXCLUDE = (
    'migrations',
)  # Exclude this paths from tests
TEST_PEP8_IGNORE = (
    'E501',     # 80 chars of line length
)
