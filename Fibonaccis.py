def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b

# Generera de första 10 talen i Fibonaccis talserie
fibonacci(10)


# Generera de första 10 talen i Fibonaccis talserie
print(fibonacci(8))
 
#poäng
task_points = """\
1. Uppgift 1 (Lättast) - 1 poäng
2. Uppgift 5 - 2 poäng
3. Uppgift 10 - 2 poäng
4. Uppgift 2 - 3 poäng
5. Uppgift 6 - 3 poäng
6. Uppgift 3 - 5 poäng
7. Uppgift 7 - 5 poäng
8. Uppgift 9 - 8 poäng
9. Uppgift 4 - 8 poäng
10. Uppgift 8 - 13 poäng
11. Uppgift 12 (Lång men mindre svår än 11) - 13 poäng
12. Uppgift 11 (Svårast) - 13 poäng
"""