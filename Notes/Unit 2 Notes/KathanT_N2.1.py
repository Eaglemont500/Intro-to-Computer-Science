## Truth Tables

## P and Q are propositional statements

## AND -- Conjunction of P and Q

## P | Q | P^Q
## ------------
## T | T |  T
## T | F |  F
## F | T |  F
## F | F |  F

## P: Dr. Cummins is your teacher
## Q: We are in Weeks
## P: True
## Q: True
## So, P^Q: True

## P: Dr. Cummins is your teacher
## Q: We are in the PAC
## P: True
## Q: False
## So, P^Q: False

## P: Mr. Loftin is your teacher
## Q: We are in Weeks
## P: False
## Q: True
## So, P^Q: False

## P: The Moon is larger than Earth
## Q: The Prime divisers of 12 are 2 and 3
## P: False
## Q: True
## So, P^Q: False

## P^Q is True if and only if P and Q are BOTH true

## P: 5 ** 2 + 12 ** 2 = 13 ** 2
## Q: 2 ** 0.5 + 3 ** 0.5 = (2 + 3) ** 0.5
## P: True
## Q: False
## So, P^Q: False


## OR -- Disjunction of P and Q

## P | Q | PVQ
## ------------
## T | T |  T
## T | F |  T
## F | T |  T
## F | F |  F

## P: 12 is Prime
## Q:  16 is an integer power of 2
## P: False
## Q: True
## So, PVQ is True

## P: The Moon is larger than Earth
## Q: The Prime divisers of 12 are 2 and 3
## P: False
## Q: True
## So, PVQ: True

## P: 5 ** 2 + 12 ** 2 = 13 ** 2
## Q: 2 ** 0.5 + 3 ** 0.5 = (2 + 3) ** 0.5
## P: True
## Q: False
## So, PVQ: True


## IF-THEN -- False when P is true and Q is False

## P | Q | P->Q
## ------------
## T | T |  T
## T | F |  F
## F | T |  T
## F | F |  T

## Let x = 10
## P: x > 8
## Q: x > 5
## P: True
## Q: True
## So, P->Q: True

## P: Saturn has Rings
## Q: (2 + 3) ** 2 = 2 ** 2 + 3 ** 2
## P: True
## Q: False
## So, P->Q: False

a = True
b = False
print(a and b)
print(a or b)
print(not a)
print(not a and not b)