import uuid
import pytest

# Ensure the User model is imported so SQLAlchemy can resolve the relationship
from app.models.user import User  # noqa: F401

from app.models.calculation import (
    Addition,
    Subtraction,
    Multiplication,
    Division,
)


def test_addition_get_result():
    c = Addition(user_id=uuid.uuid4(), inputs=[1, 2, 3])
    assert c.get_result() == 6


def test_subtraction_get_result():
    c = Subtraction(user_id=uuid.uuid4(), inputs=[10, 3, 2])
    assert c.get_result() == 5


def test_multiplication_get_result():
    c = Multiplication(user_id=uuid.uuid4(), inputs=[2, 3, 4])
    assert c.get_result() == 24


def test_division_get_result():
    c = Division(user_id=uuid.uuid4(), inputs=[100, 2, 5])
    assert c.get_result() == 10


def test_division_by_zero_raises():
    c = Division(user_id=uuid.uuid4(), inputs=[10, 0])
    with pytest.raises(ValueError):
        c.get_result()
