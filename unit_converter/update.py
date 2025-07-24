class Update:
    def __init__(self, varCategory, menuFrom, varFrom, menuTo, varTo):
        self.varCategory = varCategory
        self.menuFrom = menuFrom
        self.varFrom = varFrom
        self.menuTo = menuTo
        self.varTo = varTo

    def updateUnits(self, *args):
        choice = self.varCategory.get()
        if choice == "Length":
            units = ("meters", "kilometers", "centimeters", "millimeters")
        elif choice == "Mass":
            units = ("grams", "pounds", "tons")
        elif choice == "Temperature":
            units = ("Celsius", "Fahrenheit", "Kelvin")
        elif choice == "Time":
            units = ("seconds", "minutes", "hours", "days")
        elif choice == "Area":
            units = ("m²", "cm²", "km²", "hectares")
        elif choice == "Speed":
            units = ("m/s", "km/h", "mi/h")
        elif choice == "Energy":
            units = ("J", "kJ", "Wh")
        else:
            units = ()

        self.menuFrom['values'] = units
        self.menuTo['values'] = units
        self.varFrom.set(units[0])
        self.varTo.set(units[1])
