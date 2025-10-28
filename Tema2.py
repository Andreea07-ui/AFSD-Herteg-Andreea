elevi = ["Ana", "Bogdan", "Carmen", "Darius", "Elena"]
note  = [9,       7,        10,       4,        8]

elev_nou        = "Felix"
nota_elev_nou   = 6
elev_de_sters   = "Darius"

interogari_nume = ["Ana", "Mara", "Elena", "stop"]

absente = [1, 0, 2, 3, 0]

#A
for i in range(len(elevi)):
    print(elevi[i], end=", ")
    print(note[i])

nota_maxima=(max(note))
nota_minima=(min(note))
max_elevi = elevi[note.index(nota_maxima)]
print(max_elevi, nota_maxima)
min_elevi = elevi[note.index(nota_minima)]
print(min_elevi, nota_minima)

ma=sum(note)/len(note)
print(round(ma,2))

for i in range(len(elevi)):
    if note[i] >= 5:
        print(elevi[i])

#B
for i in range(len(note)):
    note[i] = note[i] + 1
    if note[i] > 10:
        note[i] = 10
print(note)

elevi1=elevi.pop(3)
elevii=elevi.append(elev_nou)
print(elevi)

Note=note.append(nota_elev_nou)
print(note)

for i in range(len(elevi)):
    print(elevi[i], end=", ")
    print(note[i])
#C
i = 0
while i < len(interogari_nume):
    nume = interogari_nume[i]
    if nume == "stop":
        break  # oprește procesarea
    if nume in elevi:
        poz = elevi.index(nume)
        print(f"{nume} are nota {note[poz]}.")
    else:
        print(f"{nume} nu există în listă.")
    i += 1

numar_trecuti = 0
numar_picati  = 0
for i in range(len(note)):
    if note[i] >= 5:
        numar_trecuti += 1
    else:
        numar_picati += 1
print(f"Elevi cu notă ≥ 5: {numar_trecuti}")
print(f"Elevi cu notă < 5: {numar_picati}")

note_trecuti = []
for n in note:
    if n >= 5:
        note_trecuti.append(n)
if len(note_trecuti) > 0:
    media = sum(note_trecuti) / len(note_trecuti)
    print(f"Note ≥ 5: {note_trecuti}")
    print(f"Media notelor ≥ 5: {media:.2f}")





