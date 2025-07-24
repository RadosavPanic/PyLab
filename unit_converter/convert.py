class Convert:
    def __init__(self, inputValue, varCategory, varFrom, varTo, lblResult, lblFunFact):
        self.inputValue = inputValue
        self.varCategory = varCategory
        self.varFrom = varFrom
        self.varTo = varTo
        self.lblResult = lblResult
        self.lblFunFact = lblFunFact

    def convert(self):
        try:
            value = float(self.inputValue.get())
            category = self.varCategory.get()
            fromUnit = self.varFrom.get()
            toUnit = self.varTo.get()

            if category == "Length":
                result = self.convertLength(value, fromUnit, toUnit)
                funFact = "The longest snake ever: 10 meters!"
            elif category == "Mass":
                result = self.convertMass(value, fromUnit, toUnit)
                funFact = "An adult elephant weighs about 6,000 kg!"
            elif category == "Temperature":
                result = self.convertTemperature(value, fromUnit, toUnit)
                funFact = "Highest Earth Temperature: 56.7°C (Death Valley)"
            elif category == "Time":
                result = self.convertTime(value, fromUnit, toUnit)
                funFact = "A day lasts exactly 86,400 seconds!"
            elif category == "Area":
                result = self.convertArea(value, fromUnit, toUnit)
                funFact = "One hectare is 10,000 m² – about the size of two football fields!"
            elif category == "Speed":
                result = self.convertSpeed(value, fromUnit, toUnit)
                funFact = "The fastest car in the world: over 500 km/h!"
            elif category == "Energy":
                result = self.convertEnergy(value, fromUnit, toUnit)
                funFact = "A single banana has about 105 calories, which is around 440 kJ."
            else:
                result = "Unsupported category"
                funFact = ""

            rounded = round(result, 2)
            if rounded.is_integer():
                output = f"Result: {int(rounded)}"
            else:
                output = f"Result: {rounded}"

            self.lblResult.config(text=f"{output} {toUnit}")
            self.lblFunFact.config(text=funFact)
        except ValueError:
            self.lblResult.config(text="Insert correct digit value.")
            self.lblFunFact.config(text="")


    def convertLength(self, value, fromUnit, toUnit):
        metersUnits = {
            "meters": 1,
            "kilometers": 1000,
            "centimeters": 0.01,
            "millimeters": 0.001
        }
        meters = value * metersUnits[fromUnit]
        return meters / metersUnits[toUnit]


    def convertMass(self, value, fromUnit, toUnit):
        gramsUnits = {
            "grams": 1,
            "pounds": 1000,
            "tons": 1_000_000,
        }

        grams = value * gramsUnits[fromUnit]
        return grams / gramsUnits[toUnit]

    def convertTemperature(self, value, fromUnit, toUnit):
        if fromUnit == toUnit:
            return value
        if fromUnit == "Celsius":
            if toUnit == "Fahrenheit":
                return (value * 9 / 5) + 32
            elif toUnit == "Kelvin":
                return value + 273
        elif fromUnit == "Fahrenheit":
            if toUnit == "Celsius":
                return (value - 32) * 5 / 9
            elif toUnit == "Kelvin":
                return (value - 32) * 5 / 9 + 273
        elif fromUnit == "Kelvin":
            if toUnit == "Celsius":
                return value - 273
            elif toUnit == "Fahrenheit":
                return (value - 273) * 9 / 5 + 32

    def convertTime(self, value, fromUnit, toUnit):
        secondsUnits = {
            "seconds": 1,
            "minutes": 60,
            "hours": 3600,
            "days": 86400
        }
        seconds = value * secondsUnits[fromUnit]
        return seconds / secondsUnits[toUnit]

    def convertArea(self, value, fromUnit, toUnit):
        msquareUnits = {
            "m²": 1,
            "cm²": 0.0001,
            "km²": 1_000_000,
            "hectares": 10_000
        }
        msquare = value * msquareUnits[fromUnit]
        return msquare / msquareUnits[toUnit]

    def convertSpeed(self, value, fromUnit, toUnit):
        mpsUnits = {
            "m/s": 1,
            "km/h": 1 / 3.6,
            "mi/h": 0.44704,
        }
        mps = value * mpsUnits[fromUnit]
        return mps / mpsUnits[toUnit]

    def convertEnergy(self, value, fromUnit, toUnit):
        joulesUnits = {
            "J": 1,
            "kJ": 1_000,
            "Wh": 3_600,
        }
        joules = value * joulesUnits[fromUnit]
        return joules / joulesUnits[toUnit]