#!/usr/bin/env python3

import datetime

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
    def __init__(self, datum, utyfel, szobaszam):

        if not isinstance(datum, datetime.date):
            raise Exception('Ez bizony nem datum batyus!')
        self._datum = datum
        self._utyfel = utyfel
        self._szobaszam = szobaszam
        pass

    @property
    def datum(self):
        return self._datum

    @property
    def utyfel(self):
        return self._utyfel

    @property
    def szobaszam(self):
        return self._szobaszam
    pass

class Szalloda():
    _szobak = []
    _foglalasok = []
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

        #pprint(self._szobak)
        pass

    @property
    def nev(self):
        return nev

    def foglal(self, datum, szobaszam, kicsoda):
        if not isinstance(datum, datetime.date):
            raise Exception('Ez bizony nem datum batyus!')

        if datum <= datetime.date.today():
            raise Exception('A mult nem a jovendo')

        szoba = None
        for sz in self._szobak:
            if sz.szam == szobaszam:
                szoba = sz
                break
            pass
        if szoba is None:
            raise Exception('Szoba {sz} not found'.format(sz = szobaszam))

        for f in self._foglalasok:
            if f.szobaszam == szoba.szam and datum == f.datum:
                raise Exception('E mar foglalt e!')
            pass

        self._foglalasok.append(Foglalas(datum = datum,
                                         utyfel = kicsoda,
                                         szobaszam = szobaszam))
        return sz.ar

    pass

s = Szalloda('foobar')
x = s.foglal(datetime.date(2023, 12, 13), 1, 'en')
pprint(x)
x = s.foglal(datetime.date(2023, 12, 14), 11, 'te')
pprint(x)