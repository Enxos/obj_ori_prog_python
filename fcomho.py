from pprint import pprint

class Szoba():
    def __init__(self, ar, szam):
        self._ar = ar
        self._szam = szam
        pass

    @property
    def ar(self):
        return self._ar

    @property
    def szam(self):
        return self._szam

    pass

class EgyagyasSzoba(Szoba):
    def __init__(self, szam):
        super().__init__(42, szam)
        pass

    pass

class KetagyasSzoba(Szoba):
    def __init__(self, szam):
        super().__init__(69, szam)
        pass

    pass

a = EgyagyasSzoba(1)
b = KetagyasSzoba(2)
pprint([a.ar, a.szam])
pprint([b.ar, b.szam])

class Szalloda():
    def __init__(self, nev):
        self._nev = nev
        pass

    @property
    def nev(self):
        return nev
    pass