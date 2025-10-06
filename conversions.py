# === Part II: Celsius conversions ===
def convertCelsiusToKelvin(celsius: float) -> float:
    return celsius + 273.15

def convertCelsiusToFahrenheit(celsius: float) -> float:
    return (celsius * 9/5) + 32

# === Part III: Fahrenheit and Kelvin conversions ===
def convertFahrenheitToCelsius(f: float) -> float:
    return (f - 32) * 5/9

def convertFahrenheitToKelvin(f: float) -> float:
    return (f - 32) * 5/9 + 273.15

def convertKelvinToCelsius(k: float) -> float:
    return k - 273.15

def convertKelvinToFahrenheit(k: float) -> float:
    return (k - 273.15) * 9/5 + 32

# === Part IV: Distance conversions ===
def convertMilesToMeters(miles: float) -> float:
    return miles * 1609.34

def convertMetersToMiles(meters: float) -> float:
    return meters / 1609.34

def convertYardsToMeters(yards: float) -> float:
    return yards * 0.9144

def convertMetersToYards(meters: float) -> float:
    return meters / 0.9144

def convertMilesToYards(miles: float) -> float:
    return miles * 1760

def convertYardsToMiles(yards: float) -> float:
    return yards / 1760