import dataclasses

import pytest

from normalize_phone import norm_phone


@dataclasses.dataclass
class Case:
    phone: str
    result: (str, None)

    def __str__(self) -> str:
        return f"{self.phone}"


TEST_CASES = [
    Case(phone="+1 223-456-7890", result="1-223-456-7890"),
    Case(phone="(223) 456-7890", result="1-223-456-7890"),
    Case(phone="1-223-456-7890", result="1-223-456-7890"),
    Case(phone="1 223 456 7890", result="1-223-456-7890"),
    Case(phone="+1 223 456-7890", result="1-223-456-7890"),
    Case(phone="223.456.7890", result="1-223-456-7890")

]

TEST_CASES_ERR = [
    Case(phone="+3 223-456-7890", result=None),
    Case(phone="+1 123-456-7890", result=None),
    Case(phone="+1 293-456-7890", result=None),
    Case(phone="+1 223-156-7890", result=None),
    Case(phone="Not a number at all", result=None)
]


@pytest.mark.parametrize("t", TEST_CASES, ids=str)
def test_norm_phone(t: Case) -> None:
    assert norm_phone(t.phone) == t.result


@pytest.mark.parametrize("t", TEST_CASES_ERR, ids=str)
def test_norm_phone_err(t: Case) -> None:
    try:
        norm_phone(t.phone)
        err = False
    except ValueError:
        err = True

    assert err
