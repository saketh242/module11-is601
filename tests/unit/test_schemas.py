import pytest
from uuid import UUID

from app.schemas.calculation import (
    CalculationBase,
    CalculationCreate,
    CalculationType,
)


def test_calculationbase_valid():
    data = {"type": "addition", "inputs": [1, 2, 3]}
    obj = CalculationBase.model_validate(data)
    assert obj.type == CalculationType.ADDITION
    assert obj.inputs == [1, 2, 3]


def test_calculationbase_short_inputs_raises():
    data = {"type": "addition", "inputs": [1]}
    with pytest.raises(ValueError):
        CalculationBase.model_validate(data)


def test_calculationbase_invalid_type_raises():
    data = {"type": "pow", "inputs": [2, 3]}
    with pytest.raises(ValueError):
        CalculationBase.model_validate(data)


def test_division_inputs_cannot_have_zero_after_first():
    data = {"type": "division", "inputs": [10, 0]}
    with pytest.raises(ValueError):
        CalculationBase.model_validate(data)


def test_calculationcreate_accepts_uuid():
    uid = "123e4567-e89b-12d3-a456-426614174000"
    data = {"type": "addition", "inputs": [1, 2], "user_id": uid}
    obj = CalculationCreate.model_validate(data)
    assert isinstance(obj.user_id, UUID)
