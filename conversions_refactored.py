class ConversionNotPossible(Exception):
    pass

conversion_factors = {
    'celsius': {'kelvin': lambda x: x + 273.15, 'fahrenheit': lambda x: (x * 9/5) + 32},
    'kelvin': {'celsius': lambda x: x - 273.15, 'fahrenheit': lambda x: (x - 273.15) * 9/5 + 32},
    'fahrenheit': {'celsius': lambda x: (x - 32) * 5/9, 'kelvin': lambda x: (x - 32) * 5/9 + 273.15},
    'miles': {'meters': lambda x: x * 1609.34, 'yards': lambda x: x * 1760},
    'meters': {'miles': lambda x: x / 1609.34, 'yards': lambda x: x / 0.9144},
    'yards': {'miles': lambda x: x / 1760, 'meters': lambda x: x * 0.9144}
}

def convert(fromUnit: str, toUnit: str, value: float) -> float:
    fromUnit = fromUnit.lower()
    toUnit = toUnit.lower()
    if fromUnit == toUnit:
        return float(value)
    try:
        return conversion_factors[fromUnit][toUnit](value)
    except KeyError:
        raise ConversionNotPossible(f"Cannot convert from {fromUnit} to {toUnit}")
