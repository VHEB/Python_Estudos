from pathlib import Path
LOG_FILE = Path(__file__).parent / 'log.txt'


# Abstração
class Log:
    def _log(self, msg): #assinatura do método
        raise NotImplementedError('Método log deve ser implementado')

    def log_error(self, msg):
        return self._log(f'ERROR: {msg}')
    
    def log_success(self, msg):
        return self._log(f'SUCCESS: {msg}')

class LogFileMixin(Log):
    def _log(self, msg):
        msg_formatada = f'{msg} ({self.__class__.__name__})'
        print('Salvando no log', msg_formatada)
        with open(LOG_FILE, 'a') as arquivo:
            arquivo.write('\r \n')
            arquivo.write(msg_formatada)
            arquivo.write('\r \n')

        
        
class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'Logando em console: {msg} {self.__class__.__name__}')
        

if __name__ == '__main__':        
    l = LogPrintMixin()
    l.log_error('teste')
    l.log_success('teste')
    l2 = LogFileMixin()
    l2.log_error('teste')
    l2.log_success('teste')