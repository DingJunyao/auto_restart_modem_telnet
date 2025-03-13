import telnetlib
import time
import dotenv
import os

dotenv.load_dotenv()



port = 23
timeout = 100
USER_MANE = os.getenv("USER_MANE")
PASSWORD = os.getenv("PASSWORD")
ROUTER_ADDR = os.getenv("ROUTER_ADDR")
SU_PASSWORD = os.getenv("SU_PASSWORD")


def restart_modem():
    with telnetlib.Telnet(ROUTER_ADDR, port, timeout) as session:
        session.read_until(b'Login: ')
        session.write((USER_MANE + '\n').encode('ascii'))
        session.read_until(b'Password: ')
        session.write((PASSWORD + '\n').encode('ascii'))
        session.read_until(b'$ ')
        session.write(b'su\n')
        session.read_until(b'Password: ')
        session.write((SU_PASSWORD + '\n').encode('ascii'))
        session.read_until(b'# ')
        session.write(b'reboot\n')
        time.sleep(2)


if __name__ == '__main__':
    restart_modem()