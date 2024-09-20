import math

# 1) Beräkna hypotenusan
a = 3
b = 4
c = math.sqrt(a**2 + b**2)
print(f"Hypotenusan är {c:.1f} längdenheter.")  # Svar: 5

# b) Beräkna den andra kateten
c = 7.0
a = 5.0
b = math.sqrt(c**2 - a**2)
print(f"Den andra kateten är {b:.1f} längdenheter.")  # Svar: 4.9

# 2) 365 prediktioner, 300 korrekta
correct_predictions = 300
total_predictions = 365
accuracy = correct_predictions / total_predictions
print(f"Modellens noggrannhet är {accuracy:.3f}.")  # Svar: 0.822


# 3) Beräkna noggrannhet för branddetektionsmodellen
TP = 2
FP = 2
FN = 11
TN = 985
accuracy = (TP + TN) / (TP + TN + FP + FN)
print(f"Modellens noggrannhet är {accuracy:.3f}.")  # Svar: 0.987


# 4) Beräkna k och m
x1, y1 = 4, 4
x2, y2 = 0, 1
k = (y2 - y1) / (x2 - x1)
m = y1 - k * x1
print(f"Linjens ekvation är y = {k:.2f}x + {m:.2f}.")  # Svar: y = 0.75x + 1



# 5)Koordinater för punkterna
P1 = (2, 1, 4)
P2 = (3, 1, 0)

# 6)Beräkna det euklidiska avståndet
distance = math.sqrt((P2[0] - P1[0])**2 + (P2[1] - P1[1])**2 + (P2[2] - P1[2])**2)

# Visa resultatet
print(f"Avståndet mellan punkterna P1 och P2 är {distance:.2f} längdenheter.")  # Svar: 4.12 l.u.
