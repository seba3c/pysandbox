from pysandbox.stump_duty_calculator import calculate


def test_calculate():
    assert calculate(100000) == {"firstTimeBuyer": 0.0, "normalBuyer": 0.0}
    assert calculate(200000) == {"firstTimeBuyer": 0.0, "normalBuyer": 1500.0}
    assert calculate(300000) == {"firstTimeBuyer": 2500.0, "normalBuyer": 5000.0}

    assert calculate(500000) == {"firstTimeBuyer": 12500.0, "normalBuyer": 15000.0}
    assert calculate(600000) == {"firstTimeBuyer": 17500.0, "normalBuyer": 23000.0}
    assert calculate(1000000) == {"firstTimeBuyer": 49500.0, "normalBuyer": 55000.0}

    assert calculate(1500000) == {"firstTimeBuyer": 89500.0, "normalBuyer": 105000.0}
    assert calculate(2000000) == {"firstTimeBuyer": 129500.0, "normalBuyer": 165000.0}
    assert calculate(3000000) == {"firstTimeBuyer": 249500.0, "normalBuyer": 285000.0}
