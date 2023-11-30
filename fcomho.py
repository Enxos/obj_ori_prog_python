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

    def __repr__(self):
        return '<Foglalas(datum={d}, szobaszam={sz}, utyfel={u})>'.format(d = self.datum,
                                                                          sz = self.szobaszam,
                                                                          u = self.utyfel)
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

    def lemond(self, datum, szobaszam):
        if not isinstance(datum, datetime.date):
            raise Exception('Ez bizony nem datum batyus!')

        for i in range(len(self._foglalasok)):
            f = self._foglalasok[i]
            if f.szobaszam == szobaszam and datum == f.datum:
                self._foglalasok.pop(i)
                return
            pass
        raise Exception('Marpedig ilyen bezony nincs')

    def foglalasok(self):
        return self._foglalasok

    pass

def menu():
    print('0. Foglalas')
    print('1. Lemondas')
    print('2. Listazas')
    print('3. brexit')
    x = int(input('Valassz: '))
    if x<0 or x>3:
        raise Exception('Ez biza nem jo')
    return x

sz = Szalloda('Grand Hostel')
sz.foglal(datetime.date(2023, 12, 2), 2, 'en' )
sz.foglal(datetime.date(2023, 12, 5), 2, 'te' )
sz.foglal(datetime.date(2023, 12, 7), 2, 'o' )
sz.foglal(datetime.date(2023, 12, 11), 2, 'mi' )
sz.foglal(datetime.date(2023, 12, 23), 2, 'ti' )
sz.foglal(datetime.date(2023, 12, 23), 7, 'apache helicopter' )
while True:
    valasztas = menu()
    if valasztas == 3:
        print('Asta la vista, baby!')
        break
    elif valasztas == 0:
        # foglal(self, datum, szobaszam, kicsoda):
        try:
            utyfel = input('Ugyfel: ')
            szobaszam = int(input('Szobaszam: '))
            strdatum = input('Datum(ISO8601): ')

            dt = datetime.datetime.strptime(strdatum, '%Y-%m-%d')
            datum = datetime.date(dt.year, dt.month, dt.day)

            sz.foglal(datum = datum,
                      szobaszam = szobaszam,
                      kicsoda = utyfel)
        except Exception as e:
            print('Ez biza nem jott ossze: {e}'.format(e =str(e)))
            continue
    elif valasztas == 1:
        # lemond(self, datum, szobaszam):
        try:
            szobaszam = int(input('Szobaszam: '))
            strdatum = input('Datum(ISO8601): ')
            dt = datetime.datetime.strptime(strdatum, '%Y-%m-%d')
            datum = datetime.date(dt.year, dt.month, dt.day)

            sz.lemond(datum, szobaszam)
        except Exception as e:
            print('Ez biza nem jott ossze: {e}'.format(e =str(e)))
            continue
            
    elif valasztas == 2:
        print('Foglalasok:')
        for f in sz.foglalasok():
            print('Szoba: {i} Datum: {d} Utyfel: {u}'.format(i = f.szobaszam,
                                                             d = f.datum,
                                                             u = f.utyfel))
            pass
        pass
    pass