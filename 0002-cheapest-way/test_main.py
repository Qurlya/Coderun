import pytest
import io
from main import main

LARGE_TEST_INPUT = """5 5
1 1 1 1 1
3 100 100 100 100
1 1 1 1 1
2 2 2 2 1
1 1 1 1 1
"""


@pytest.mark.parametrize("test_input, expected", [
    (LARGE_TEST_INPUT, "11")
])
def test(monkeypatch, capsys, test_input, expected):
    monkeypatch.setattr('sys.stdin', io.StringIO(test_input))

    main()

    captured = capsys.readouterr()
    assert captured.out.strip() == expected