popa = 80000
popb = 200000
#valor da taxa em percentual de crescimento
taxaa = 0.03
taxab = 0.015

while popa <= popb:
    popa += popa*taxaa
    popa = popa +( popa * taxaa)