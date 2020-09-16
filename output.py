Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 2 + 2

4
>>> 100 - 10
90
>>> 25 / 5
5.0
>>> 10 / 3
3.3333333333333335
>>> 10 // 3
3
>>> print('Mijn naam is <stefan>')
Mijn naam is <stefan>
>>> print(naam)

Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print(naam)
NameError: name 'naam' is not defined
>>> naam = "stefan"
>>> print(naam)

stefan
>>> print(naam.upper())

STEFAN
>>> print(naam[0:2])

st
>>> print(naam[::-1])

nafets
>>> leeftijd = 15

>>> print('Hallo ' + naam + ' ben je al ' + str(leeftijd) + ' jaar?')

Hallo stefan ben je al 15 jaar?
>>> 
KeyboardInterrupt
>>> leeftijd = leeftijd + 1

>>> leeftijd
16
>>> leeftijd-=1
leeftijd-=1
leeftijd-=1

SyntaxError: multiple statements found while compiling a single statement
>>> leeftijd
16
>>> leeftijd-=1

>>> leeftijd
15
>>> hoelang_tot18jaar = 18 - leeftijd
>>> print('Over ' + str(hoelang_tot18jaar) + ' jaar wordt je 18')
Over 3 jaar wordt je 18
>>> hoelang_al18jaar = leeftijd - 18
>>>     print('Het is alweer ' + str(hoelang_al18jaar) + ' jaar geleden dat je 18 werd ;-)')

SyntaxError: unexpected indent
>>> print('Het is alweer ' + str(hoelang_al18jaar) + ' jaar geleden dat je 18 werd ;-)')
Het is alweer -3 jaar geleden dat je 18 werd ;-)
>>> print('Je bent precies ' + str(leeftijd) + ' jaar')
Je bent precies 15 jaar
>>> from random import randint
>>> randint(0,1000)
932
>>> willekeurig_getal = randint(0,1000)
>>> willekeurig_getal
284
>>> print('Willekeurig getal tussen 0 en 1000: ' + str(willekeurig_getal))
Willekeurig getal tussen 0 en 1000: 284
>>> from datetime import datetime
>>> datum = datetime.now()

>>> print(datum)
2020-09-16 14:24:43.500207
>>> datum.strftime('%A %d %B %Y')
'Wednesday 16 September 2020'
>>> import locale
>>> locale.setlocale(locale.LC_TIME, 'nl_NL')
'nl_NL'
>>> datum.strftime('%A %d %B %Y')
'woensdag 16 september 2020'
>>> locale.setlocale(locale.LC_TIME, 'it_IT')
'it_IT'
>>> datum.strftime('%A %d %B %Y')
'mercoledì 16 settembre 2020'
>>> 