#!/usr/bin/env python3

from pprint import pprint

class Szoba():
    def __init__(self, ar, szam, agyszam):
        self._ar = ar
        self._szam = szam
        self._agyszam = agyszam
        pass

    @property
    def ar(self):
        return self._ar

    @property
    def szam(self):
        return self._szam

    @property
    def agyszam(self):
        return self._agyszam;

    def __repr__(self):
        return '<Szoba {sz}/{agy} {a} zseton>'.format(sz = self.szam,
                                                      agy = self.agyszam,
                                                      a = self.ar)
    pass

class EgyagyasSzoba(Szoba):
    def __init__(self, szam):
        super().__init__(42, szam, 1)
        pass

    pass

class KetagyasSzoba(Szoba):
    def __init__(self, szam):
        super().__init__(69, szam, 2)
        pass

    pass

class Foglalas():
    def __init__(self, datum):
        self._datum = datum
        pass

    @property
    def datum(self):
        return self._datum
    pass

class Szalloda():
    _szobak = []
    def __init__(self, nev, db_egy=5, db_ketto=7):
        self._nev = nev

        szam = 0;
        for i in range(db_egy):
            szam += 1
            self._szobak.append(EgyagyasSzoba(szam))
            pass
        for i in range(db_ketto):
            szam += 1
            self._szobak.append(KetagyasSzoba(szam))
            pass

        pprint(self._szobak)
        pass

    @property
    def nev(self):
        return nev
    pass

s = Szalloda('foobar')