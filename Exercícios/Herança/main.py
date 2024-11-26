from log import LogFileMixin, LogPrintMixin

from eletronico import Smartphone

galaxy = Smartphone('Galaxy S10')
iphone = Smartphone('iPhone X')

galaxy.ligar()
iphone.desligar()
