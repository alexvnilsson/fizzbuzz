# FizzBuzz

## Varför?

Tittade på Tom Scott på YouTube och hamnade på en video om FizzBuzz-leken som man använder för att testa en utvecklare under arbetsintervjuer. Ville därför bara slänga ihop en liten kod för att se hur min lösning ser ut jämfört med Toms.

## Reflektioner

Som Tom tog upp i videon så får man många olika lösningar från olika utvecklare beroende på tillvägagångssätt, bland annat hur man planerar och tänker igenom problemet och hur man skriver koden. Jag upptäckte följande om mitt arbetssätt:

### Planering av arbete

Jag tänker ut problemet medan jag skriver koden, ändrar fel efter de dyker upp; jag är dålig på att planera.



### Översätta teori till praktiken

Jag tänkte inte igenom artimetiken ordenligt, krånglade till logiken därefter; jag bör bli bättre på att fundera ut och utföra praktiska implementeringen av en teoretisk lösning.

För att kontrollera om något är dividerbart med sig själv så gjorde jag följande:

- Dividerade talen (n-värdet och 3, 5 eller 15)
- Kontrollerade typen (float eller integer) av variablen där resultatet av divisionen lagrades och utifrån det...
- så kontrollerade jag om värdet var ett heltal eller inte.

Såhär ser då funktionen ut för att utföra division och kontroller.

```python
def is_divisible(n, by_n):
    n_sum = (n / by_n)

    if type(n_sum) is float:
        return n_sum.is_integer()

    if type(n_sum) is int:
        return True

    return False
```

Jag kunde ha förenklat denna kod genom att ha använt mig av kvadrater, d.v.s. enligt följande:

Invokerar den funktionen från `is_fizzbuzz`.

```python
def is_fizzbuzz(n) -> int:
    n_test = (n_fizz, n_buzz, (n_fizz * n_buzz))
    n_sum = 0

    for n2 in n_test:
        if is_divisible(n, n2):
            n_sum = n2
    
    return n_sum
```

Returvärdet från denna funktionen är 0, 3, 5 eller 15 (0, Fizz, Buzz eller FizzBuzz). Rätt enkel och tydlig kod.