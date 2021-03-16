n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número '))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2
r = n1%n2
print('A soma é {}\n, o produto é {}\n e a divisão é\n {:.3f}.'.format(s, m, d))
print('Divisão inteira {}, potência {} e resto {}.'.format(di, e, r))