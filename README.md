# FizzBuzz

## Varför?

Tittade på Tom Scott på YouTube och hamnade på en video om FizzBuzz-leken som man använder för att testa en utvecklare under arbetsintervjuer.

Ville därför bara slänga ihop en liten kod för att se hur min lösning ser ut jämfört med Toms och för att utvärdera mitt arbete och hitta förbättringar i mitt sätt att ta itu med en uppgift.

## Reflektioner

Som Tom tog upp i videon så får man många olika lösningar från olika utvecklare beroende på tillvägagångssätt, bland annat hur man planerar och tänker igenom problemet och hur man skriver koden. Jag upptäckte följande om mitt arbetssätt:

### Planering av arbete

Jag tänker ut problemet medan jag skriver koden, ändrar fel efter de dyker upp; jag är dålig på att planera.

### Översätta teori till praktiken

Jag tänkte inte igenom logiken ordenligt och krånglade till den i praktiken; jag bör bli bättre på att fundera ut och utföra praktiska implementeringen av en teoretisk lösning.

För att kontrollera om något är dividerbart med sig själv så gjorde jag följande:

- Dividerade talen (n-värdet och 3, 5 eller 15)
- Kontrollerade typen (float eller integer) av variablen där resultatet av divisionen lagrades och utifrån det...
- så kontrollerade jag om värdet var ett heltal eller inte.

Såhär såg då logiken ut från början.

```python
n_fizz = 3
n_buzz = 5

def is_divisible(n, by_n):
    n_sum = (n / by_n)

    if type(n_sum) is float:
        return n_sum.is_integer()

    if type(n_sum) is int:
        return True

    return False

def is_fizzbuzz(n) -> int:
    n_test = (n_fizz, n_buzz, (n_fizz * n_buzz))
    n_sum = 0

    for n2 in n_test:
        if is_divisible(n, n2):
            n_sum = n2
    
    return n_sum
```

Jag kunde ha förenklat denna kod genom att ha använt mig av enklare artimetik.

```python
def is_fizzbuzz(n) -> int:
    n_test = (n_fizz, n_buzz, (n_fizz * n_buzz))
    n_sum = 0

    for n2 in n_test:
        if n % n2 == 0:
            n_sum = n2
    
    return n_sum
```

Nu behöver jag inte invokera `is_divisble` längre, så kodbasen blir lättare med samma resultat. Värt att fundera på i större projekt i framtiden: planering och utvärdering är superviktigt.