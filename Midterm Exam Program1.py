def main():
    class TemperatureConversion:

        def __init__(self, temp=1):
            self._temp = temp

    class FahrenheittoCelcius(TemperatureConversion):

        def conversion(self):
            return (self._temp - 32) * 5 / 9

    class KelvintoCelcius(TemperatureConversion):

        def conversion(self):
            return (self._temp - 273.15)

    class CelsiustoKelvin(TemperatureConversion):

        def conversion(self):
          return self._temp + 273.15

    class CelsiustoFahrenheit(TemperatureConversion):

        def conversion(self):
           return (self._temp * 9) / 5 + 32

    tempInCelsius = float(input("Enter the temperature: "))

    convert = FahrenheittoCelcius(tempInCelsius)

    print(str(convert.conversion()) + " F to C")

    convert = KelvintoCelcius(tempInCelsius)

    print(str(convert.conversion()) + " K to C")

    convert = CelsiustoKelvin(tempInCelsius)

    print(str(convert.conversion()) + " C to K")

    convert = CelsiustoFahrenheit(tempInCelsius)

    print(str(convert.conversion()) + " C to F")


main()
