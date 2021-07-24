from abc import ABCMeta, abstractmethod


class Car:
    def __init__(self, type:str, nenryo:int=0, battery:int=0):
        self.type = type
        self.nenryo = nenryo
        self.battery = battery

    def run(self, gasoline_engine, motor):
        gasoline = gasoline_engine.kyuyu(self.nenryo)
        gasoline_kaitensu = gasoline_engine.kaiten(gasoline)
        denki = motor.jyuden(self.battery)
        motor_kaitensu = motor.kaiten(denki)
        kaitensu = gasoline_kaitensu + motor_kaitensu
        # 距離　＝　回転するの結果　＊　10㎞
        distanse = kaitensu * 10
        print(f'{self.type}　燃料{self.nenryo}　バッテリー{self.battery}　{distanse:,}km走る。')


class Douryoku(metaclass=ABCMeta):
    @abstractmethod
    def kaiten(self):
        pass


class GasolineEngine(Douryoku):
    def __init__(self, nenryou:int=0):
        self.nenryou = nenryou

    def kaiten(self, nenryou):
        kaitensu = nenryou * 100
        return kaitensu

    def kyuyu(self, nenryou):
        return nenryou


class Motor(Douryoku):
    def __init__(self, battery:int=0):
        self.battery = battery

    def kaiten(self, battery):
        kaitensu = battery * 500
        return kaitensu

    def jyuden(self, battery):
        return battery
    

gasoline_engine = GasolineEngine()
motor = Motor()

gasoline_car = Car('Car', nenryo=100)
gasoline_car.run(gasoline_engine, motor)

hv = Car('HV', nenryo=50, battery=50)
hv.run(gasoline_engine, motor)

ev = Car('EV', battery=100)
ev.run(gasoline_engine, motor)
