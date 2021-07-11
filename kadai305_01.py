from abc import ABCMeta, abstractmethod


class Car:
    def __init__(self, type, nenryo=0, battery=0):
        self.type = type
        self.nenryo = nenryo
        self.battery = battery

    def run(self, gasoline_kaitensu=0, motor_kaitensu=0):
        kaitensu = gasoline_kaitensu + motor_kaitensu
        # 距離　＝　回転するの結果　＊　10㎞
        distanse = kaitensu * 10
        print(f'{self.type}　燃料{self.nenryo}　バッテリー{self.battery}　{distanse:,}km走る。')


class Douryoku(metaclass=ABCMeta):
    @abstractmethod
    def kaiten(self):
        pass


class GasolineEngine(Douryoku):
    def __init__(self, nenryou):
        self.nenryou = nenryou

    def kaiten(self, nenryou):
        kaitensu = nenryou * 100
        return kaitensu

    def kyuyu(self):
        return self.nenryou


class Motor(Douryoku):
    def __init__(self, battery):
        self.battery = battery

    def kaiten(self, battery):
        kaitensu = battery * 500
        return kaitensu

    def jyuden(self):
        return self.battery
    

gasoline_engine = GasolineEngine(100)
gasoline = gasoline_engine.kyuyu()
gasoline_kaitensu = gasoline_engine.kaiten(gasoline)
gasoline_car = Car('Car', nenryo=gasoline)
gasoline_car.run(gasoline_kaitensu)

motor = Motor(100)
denki = motor.jyuden()
motor_kaitensu = motor.kaiten(denki)
ev = Car('EV', battery=100)
ev.run(motor_kaitensu)

gasoline_engine = GasolineEngine(50)
gasoline = gasoline_engine.kyuyu()
gasoline_kaitensu = gasoline_engine.kaiten(gasoline)
motor = Motor(50)
denki = motor.jyuden()
motor_kaitensu = motor.kaiten(denki)
hv = Car('HV', gasoline, denki)
hv.run(gasoline_kaitensu, motor_kaitensu)