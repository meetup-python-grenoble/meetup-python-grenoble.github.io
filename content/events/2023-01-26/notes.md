# Retour ludique sur l’année pythonique 2022

> 2023-01-26

## Question 1

Quel problème de sécurité a eu PyPI à l'été 2022 ?

## Question 2

Quelle est la place du langage Python dans le classement TIOBE 2022 ?

## Question 3

Qu'est-ce que les PDEP apparus en août 2022 ?

## Question 4

À quelle nouvelle fonctionnalité du langage Python introduite dans sa version 3.10 correspond cet exemple :

```python
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
```

- [ ] Le typage statique
- [ ] Les gestionnaires de contextes entre parenthèses
- [x] Le filtrage par motifs structurels
- [ ] La programmation fonctionnelle

Sources :

- https://docs.python.org/3/whatsnew/3.10.html#pep-634-structural-pattern-matching

## Question 5

Quel gain de performance moyen de l'interpréteur CPython a été mesuré dans sa version 3.11 par rapport à la version 3.10 ?

- [x] 25%
- [ ] 50%
- [ ] 75%
- [ ] 100%

Sources :

- https://docs.python.org/3/whatsnew/3.11.html#whatsnew311-faster-cpython

## Question 6

Le code suivant contient une erreur de syntaxe :

```python
expected = {9: 1, 18: 2, 19: 2, 27: 3, 28: 3, 29: 3, 36: 4, 37: 4,
            38: 4, 39: 4, 45: 5, 46: 5, 47: 5, 48: 5, 49: 5, 54: 6,
some_other_code = foo()
```

Quel serait le message d'erreur observé à partir de Python 3.10 :

- [ ]
```python
File "example.py", line 3
    some_other_code = foo()
                    ^
SyntaxError: invalid syntax
```

- [x]
```python
File "example.py", line 1
    expected = {9: 1, 18: 2, 19: 2, 27: 3, 28: 3, 29: 3, 36: 4, 37: 4,
               ^
SyntaxError: '{' was never closed
```

Sources :

- https://docs.python.org/3/whatsnew/3.10.html#better-error-messages

## Question 7

Quel projet de l'écosystème Jupyter permettant l'exécution de notebooks dans le navigateur sans serveur a vu le jour en version beta début 2022 ?

- [ ] JupyterLab
- [ ] JupyterHub
- [x] JupyterLite
- [ ] Voilà

Sources :

- https://jupyterlite.readthedocs.io/en/latest/changelog.html#b0

## Question 8

Dans quelle ville à eu lieu la conférence européenne EuroPython 2022 ?

- [ ] Edimbourg
- [x] Dublin
- [ ] Stockholm
- [ ] Berlin

Sources :

- https://ep2022.europython.eu

## Question 9

Dans quelle ville aura lieu le retour de la conférence française PyConFr en 2023 ?

- [ ] Paris
- [ ] Grenoble
- [ ] Nantes
- [x] Bordeaux

Sources :

- https://www.pycon.fr/2023/

## Question 10

Dans une interview accordée à Lex Friedman en 2022, Guido Van Rossum a répondu que le langage Python "deviendra éventuellement un langage hérité - jouant un rôle important, mais dont la plupart des gens n'ont jamais entendu parler et n'ont pas besoin de connaître". Quelle était la question posée ?

- [ ] Python deviendra-t-il obsolète un jour ?
- [ ] Quelle sera la place de Python dans 10 ans ?
- [x] Quelle sera la place de Python dans 100 ans ?
- [ ] Doit-on enseigner le Python au collège et au lycée ?

Sources :

- https://youtu.be/-DVyjdw4t9I
- https://thenewstack.io/guido-van-rossum-on-types-speed-and-the-future-of-python/