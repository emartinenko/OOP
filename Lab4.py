class Car:
    def __init__(self,
                 name: str,
                 weight: float,
                 length: float,
                 wheel_drive: str = "rear-wheel",
                 engine_volume: float = 1.6,
                 ):
        self.name = name
        if not isinstance(weight, float):
            raise TypeError("Вес машины должен быть вещественным числом")
        if weight <= 0.6:
            raise ValueError("Вес машины должен быть больше 0.6 т")
        self.weight = weight
        if not isinstance(length, float):
            raise TypeError("Длина машины должна быть вещественным числом")
        if length <= 2:
            raise ValueError("Длина машины должна быть больше 2 м")
        self.length = length
        if wheel_drive not in ["rear-wheel", "front-wheel", "all-wheel"]:
            raise ValueError("Привод машины может быть только rear-wheel, front-wheel или all-wheel")
        self.wheel_drive = wheel_drive
        if not isinstance(engine_volume, float):
            raise TypeError("Объем двигателя машины должен быть вещественным числом")
        if engine_volume <= 1:
            raise ValueError("Объем двигателя машины должен быть больше 1 л")
        self.engine_volume = engine_volume
        self._speed = 0.0

    def __str__(self):
        return f"Машина {self.name}. Масса {self.weight}. Длина {self.length}." \
               f" Привод {self.wheel_drive}. Объем двигателя {self.engine_volume}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, weight={self.weight}," \
               f" length={self.length}, wheel_drive={self.wheel_drive!r}, engine_volume={self.engine_volume})"

    def drive(self) -> None:
        """
        Метод отвечающий за движение машины

        :return: None
        """
        ...

    def slow_down(self) -> None:
        """
        Метод отвечающий за торможение машины

        :return: None
        """
        ...

    @property
    def speed(self) -> float:
        """
        Геттер для аттрибута speed
        Аттрибут защищен от изменения, так как скорость должна меняться только черем методы dirve() и slow_down()

        :return: self.speed типа float
        """
        return self._speed


class PassengerCar(Car):
    def __init__(self,
                 name: str,
                 weight: float,
                 length: float,
                 wheel_drive: str = "rear-wheel",
                 engine_volume: float = 1.6,
                 ):
        if weight >= 3.5:
            raise ValueError("Легковая машина должна весить менее 3.5 т")
        super().__init__(name=name, weight=weight, length=length, wheel_drive=wheel_drive, engine_volume=engine_volume)

    def __str__(self):
        return super().__str__

    def __repr__(self):
        return f"{super.__repr__}"

    def open_sunroof(self) -> bool:
        """
        Метод отвечающий за открытие люка в крыше машины

        :return: True - люк открылся, False - люк не открылся
        """
        ...


class Truck(Car):
    def __init__(self,
                 name: str,
                 weight: float,
                 length: float,
                 wheel_drive: str = "rear-wheel",
                 engine_volume: float = 1.6,
                 height: float = 2.0,
                 ):
        if weight < 3.5:
            raise ValueError("Грузовая машина должна весить более 3.5 т")
        super().__init__(name=name, weight=weight, length=length, wheel_drive=wheel_drive, engine_volume=engine_volume)
        if not isinstance(height, float):
            raise TypeError("Высота машины должна быть вещественным числом")
        if height <= 1.5:
            raise ValueError("Высота машины должна быть больше 1.5 м")
        self.height = height
        self._status_cruise_control = False

    def __str__(self):
        return f"{super().__str__}. Высота {self.height}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, weight={self.weight}, length={self.length}, " \
               f"wheel_drive={self.wheel_drive!r}, engine_volume={self.engine_volume}, height={self.height})"

    def activate_cruise_control(self) -> bool:
        """
        Метод отвечающий за включение круиз-контроля.
        При включении учитывется набранная скорость, обстановка на дороге

        :return: True - круиз-контроль включился, False - не включился
        """
        ...

    @property
    def status_cruise_control(self) -> bool:
        """
        Геттер для статуса круиз-контроля
        self._status_cruise_control инкапсулирован, так как предпологается,
        что не всегда можно включить круиз-контроль

        :return: True - включен, False - выключен
        """
        return self._status_cruise_control


if __name__ == "__main__":
    truck = Truck("Volvo", 4.0, 3.0)
    print(truck.speed)
    print(repr(truck))
