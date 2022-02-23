from queue import LifoQueue, Empty, Full
from re import A

class CPUSpecificError(Exception):
    pass

class Memory:
    def __init__(self):
        self.data = [0]*256
    def write(self, address, value):
        if address == 666:
            raise CPUSpecificError("Adress must not be equal to the devil number")
        if (address%256) != 0:
            self.data[address%256] = value
    def read(self, address):
        return self.data[address%256]

class Process:
    def __init__(self, offset: int):
        self.PC = offset
        self.tray = LifoQueue(16)
        self.is_alive = True

    def nop(self):
        self.PC +=1

    def pc(self):
        try:
            self.tray.put(self.PC,block=False)
            self.PC +=1
        except Full:
            self.is_alive = False

    def push(self, val):
        try:
            self.tray.put(val,block=False)
            self.PC +=1
        except Full:
            self.is_alive = False

    def pop(self):
        try:
            self.tray.get(block=False)
            self.PC +=1
        except Empty:
            self.is_alive = False
        
    def swap(self):
        if self.tray.qsize() > 1:
            first = self.tray.get(block=False)
            second = self.tray.get(block=False)
            self.tray.put(first,block=False)
            self.tray.put(second,block=False)
            self.PC +=1
        else:
            self.is_alive = False

    def dup(self):
        try:
            val = self.tray.get(block=False)
            self.tray.put(val,block=False)
            self.tray.put(val,block=False)
            self.PC +=1
        except (Full, Empty):
            self.is_alive = False

    def pushsize(self):
        try:
            val = self.tray.qsize()
            self.tray.put(val,block=False)
            self.PC +=1
        except Full:
            self.is_alive = False

    def load(self,mem: Memory):
        try:
            top = self.tray.get(block=False)
            self.tray.put(mem.read(top),block=False)
            self.PC +=1
        except (Full, Empty):
            self.is_alive = False

    def store(self, mem: Memory):
        try:
            addr = self.tray.get(block=False)
            val = self.tray.get(block=False)
            self.PC +=1
            return addr,val
        except (Empty, CPUSpecificError):
            self.is_alive = False

    def add(self):
        try:
            no = self.tray.get(block=False)
            nt = self.tray.get(block=False)
            self.tray.put(no+nt,block=False)
            self.PC +=1
        except Empty:
            self.is_alive = False

    def sub(self):
        try:
            no = self.tray.get(block=False)
            nt = self.tray.get(block=False)
            self.tray.put(no-nt,block=False)
            self.PC +=1
        except Empty:
            self.is_alive = False

    def div(self):
        try:
            no = self.tray.get(block=False)
            nt = self.tray.get(block=False)
            self.tray.put(no/nt,block=False)
            self.PC +=1
        except (Empty, ZeroDivisionError):
            self.is_alive = False

    def pow(self):
        try:
            no = self.tray.get(block=False)
            nt = self.tray.get(block=False)
            self.tray.put(no**nt,block=False)
            self.PC +=1
        except Empty:
            self.is_alive = False

    def brz(self, val):
        try:
            im = self.tray.get(block=False)
            if im == 0:
                self.PC += val
            self.PC +=1
            
        except Empty:
            self.is_alive = False

    def br3(self, val):
        try:
            im = self.tray.get(block=False)
            if im == 3:
                self.PC += val
            self.PC +=1
            
        except Empty:
            self.is_alive = False

    def br7(self, val):
        try:
            im = self.tray.get(block=False)
            if im == 7:
                self.PC += val
            self.PC +=1
            
        except Empty:
            self.is_alive = False

    def brge(self, val):
        try:
            im = self.tray.get(block=False)
            imtwo = self.tray.get(block=False)
            if im >= imtwo:
                self.PC += val
            self.PC +=1
            
        except Empty:
            self.is_alive = False

    def jmp(self, val):
        self.PC = val
        self.PC +=1