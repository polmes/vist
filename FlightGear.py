from telnetlib import Telnet
import time

class Interface(Telnet):
	def __init__(self, host, port):
		super().__init__(host, port)
		self._write('data') # switch to data mode

	def get(self, key):
		self._write(f'get {key}')
		return self._read()

	def set(self, key, val):
		self._write(f'set {key} {val}')

	def _write(self, cmd):
		self.write(f'{cmd}\r\n'.encode('utf-8'))
		time.sleep(0.5)

	def _read(self):
		return self.read_very_eager().decode('utf-8').strip('\r\n')

	def __del__(self):
		self._write('quit')
		self.close()
