from pydantic import BaseModel


class TaxRate(BaseModel):
    price_from: float
    price_to: float
    percentage: float


class TaxRanges(BaseModel):
    ranges: list[TaxRate]


FIRST_TIME_BUYER = TaxRanges(
    ranges=[
        TaxRate(price_from=0, price_to=250000, percentage=0),
        TaxRate(price_from=250000, price_to=600000, percentage=0.05),
        TaxRate(price_from=600000, price_to=2000000, percentage=0.08),
        TaxRate(price_from=2000000, price_to=9999999999, percentage=0.12),
    ]
)

NORMAL_BUYER = TaxRanges(
    ranges=[
        TaxRate(price_from=0, price_to=125000, percentage=0),
        TaxRate(price_from=125000, price_to=250000, percentage=0.02),
        TaxRate(price_from=250000, price_to=500000, percentage=0.05),
        TaxRate(price_from=500000, price_to=1000000, percentage=0.08),
        TaxRate(price_from=1000000, price_to=1500000, percentage=0.10),
        TaxRate(price_from=1500000, price_to=9999999999, percentage=0.12),
    ]
)


def calculate_incremental_tax_rate(ranges: list[TaxRate], amount: float) -> float:
    tax_amount = 0
    if amount is None or amount <= 0:
        return tax_amount

    if amount > 9999999999:
        raise ValueError("Amount must be less than 1 billion")

    for tax_rate in ranges:
        if amount > tax_rate.price_to:
            tax_amount += (tax_rate.price_to - tax_rate.price_from) * tax_rate.percentage
        if tax_rate.price_from <= amount <= tax_rate.price_to:
            tax_amount += (amount - tax_rate.price_from) * tax_rate.percentage
    return tax_amount


def calculate(amount: float):
    return {
        "firstTimeBuyer": calculate_incremental_tax_rate(FIRST_TIME_BUYER.ranges, amount),
        "normalBuyer": calculate_incremental_tax_rate(NORMAL_BUYER.ranges, amount),
    }


def test_stump_duty_calculator():
    assert calculate(100000) == {"firstTimeBuyer": 0.0, "normalBuyer": 0.0}
    assert calculate(200000) == {"firstTimeBuyer": 0.0, "normalBuyer": 1500.0}
    assert calculate(300000) == {"firstTimeBuyer": 2500.0, "normalBuyer": 5000.0}

    assert calculate(500000) == {"firstTimeBuyer": 12500.0, "normalBuyer": 15000.0}
    assert calculate(600000) == {"firstTimeBuyer": 17500.0, "normalBuyer": 23000.0}
    assert calculate(1000000) == {"firstTimeBuyer": 49500.0, "normalBuyer": 55000.0}

    assert calculate(1500000) == {"firstTimeBuyer": 89500.0, "normalBuyer": 105000.0}
    assert calculate(2000000) == {"firstTimeBuyer": 129500.0, "normalBuyer": 165000.0}
    assert calculate(3000000) == {"firstTimeBuyer": 249500.0, "normalBuyer": 285000.0}


if __name__ == "__main__":
    test_stump_duty_calculator()
    print("All tests passed!")
