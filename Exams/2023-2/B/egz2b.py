#Rozwiązanie dynamiczne przy pomocy funkcji f, gdzie f(i,j) oznacza minimalną sumę odległości pierwszych i biurowców 
#przy założeniu, że biurowiec i ma przydzieloną działkę co najwyżej z pozycji j
#Rozwiązani O(nm) - wyliczanie wartości tablicy n x m
from egz2btesty import runtests

def parking(X,Y):
  n = len(X)
  m = len(Y)
  F = [[-1 for i in range(m)] for i in range(n)]
  F[0][0] = abs(X[0] - Y[0]) #pierwsza wartość oczywista - jedyna możliwość

  #obliczenie pierwszego rzędu 
  for j in range(1, m):
    F[0][j] = min(F[0][j - 1], abs(X[0] - Y[j])) #wzięcie j-tego parkingu - abs(X[0] - Y[j]) lub nie i wtedy najlepsza do tej pory - (F[0][j - 1])

  #obliczenie reszty tablicy
  for i in range(1, n):
    #jedyna możliwość - i-ty biurowiec ma i-ty parking
    F[i][i] = F[i - 1][i] + abs(X[i] - Y[i])
    #gdyby j < i to złamanie zasad bezpiecznego ruchu, więc nie trzeba liczyć
    for j in range(i + 1, m):
      F[i][j] = min(F[i][j - 1], F[i - 1][j - 1] + abs(X[i] - Y[j])) #wzięcie j-tego parkingu - F[i - 1][j - 1] + abs(X[i] - Y[j]), czyli najlepsza opcja dla i-1 biurowców do j-1 parkingu 
                                                                     #lub najlepsza do tej pory - F[i][j - 1]

  return F[n - 1][m - 1] #wynik

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( parking, all_tests = True )
