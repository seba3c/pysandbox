from pydantic import BaseModel

"""
In the UK, when you buy a property you pay tax on the purchase of the home called stamp duty.
The amount of tax you pay depends on two factors, the type of buyer you are and the value of the home.

Stamp duty is calculated based on tax bands and each buyer type has their own set of tax bands.
A tax band is represented by a value range that is taxed.

Each tax rate is applied to the value of the property that fits within each band.
The tax rate increases as the taxable amount increases.

For the purposes of this test we will assign the following tax bands:

First time buyer:
+----------------+-------------+------------+
| From           | To          | Tax Rate   |
+----------------+-------------+------------+
| £0             | £250,000    | 0%         |
| £250,000       | £600,000    | 5%         |
| £600,000       | £2,000,000  | 8%         |
| £2,000,000     | And Above   | 12%        |
+----------------+-------------+------------+

Normal buyer:
+----------------+-------------+------------+
| From           | To          | Tax Rate   |
+----------------+-------------+------------+
| £0             | £125,000    | 0%         |
| £125,000       | £250,000    | 2%         |
| £250,000       | £500,000    | 5%         |
| £500,000       | £1,000,000  | 8%         |
| £1,000,000     | £1,500,000  | 10%        |
| £1,500,000     | And Above   | 12%        |
+----------------+-------------+------------+

For example for a £2,000,000 normal buyer purchase, the bands work out like this:

£0 to £125,000 at 0% = £0
£125,000 to £250,000 at 2% = £2,500
£250,000 to £500,000 at 5% = £12,500
£500,000 to £1,000,000 at 8% = £40,000
£1,000,000 to £1,500,000 at 10% = £50,000
£1,500,000 to £2,000,000 at 12% = £60,000

Total = £165,000

Assignment
Write a calculator that returns the tax for both categories of buyers for a given property value,
you can use any programming language.

Example:
	calculate(300000) would return something like {firstTimeBuyer: 2500, normalBuyer: 5000}

To test if your calculator works correctly, here are some sample answers below.

+------------------+--------------------+--------------+
| Property Amount  | First time buyer   | Normal       |
+------------------+--------------------+--------------+
| £100,000         | £0                 | £0           |
| £200,000         | £0                 | £1,500       |
| £300,000         | £2,500             | £5000        |
| £500,000         | £12,500            | £15,000      |
| £600,000         | £17,500            | £23,000      |
| £1,000,000       | £49,500            | £55,000      |
| £1,500,000       | £89,500            | £105,000     |
| £2,000,000       | £129,500           | £165,000     |
| £3,000,000       | £249,500           | £285,000     |
+------------------+--------------------+--------------+

"""


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
