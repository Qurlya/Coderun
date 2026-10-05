import pytest
import io
from main import main

LARGE_TEST_INPUT = """2
3 0 3000 2500 7000 2700 10000
2 0 3000 2700 10000
"""


@pytest.mark.parametrize("test_input, expected", [
    (LARGE_TEST_INPUT, "Wrong Answer\nAccepted")
])
def test(monkeypatch, capsys, test_input, expected):
    monkeypatch.setattr('sys.stdin', io.StringIO(test_input))

    main()

    captured = capsys.readouterr()
    assert captured.out.strip() == expected