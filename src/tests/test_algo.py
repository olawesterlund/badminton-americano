import pytest
from src.algo import calculate_schedule


def test_calculate_schedule():
    calculate_schedule(8)
    with pytest.raises(ValueError, match="invalid number of players"):
        calculate_schedule(9)