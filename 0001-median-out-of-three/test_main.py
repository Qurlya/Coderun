import pytest
import io
from main import main


@pytest.mark.parametrize("test_input, expected", [
    ("1 2 3", "2"),
    ("10 5 7", "7"),
    ("-1 -5 -3", "-3"),
    ("100 0 50", "50")
])
def test_median_out_of_three(monkeypatch, capsys, test_input, expected):
    monkeypatch.setattr('sys.stdin', io.StringIO(test_input))

    main()

    captured = capsys.readouterr()

    assert captured.out.strip() == expected