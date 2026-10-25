import helpers as hp

h_total = (1, 2, 3, 4, 5)
print("=== PAPER REGRESSION TEST: n=5 Total Order [e_{4,1}] X_G ===")
for shape in hp.partitions(5):
    terms = hp.djt_terms(shape)
    if (4, 1) in terms:
        tabs = list(hp.tableaux(h_total, shape))
        print(f"Shape {shape}: coeff={terms[(4,1)]}, count={len(tabs)}")
        for t in tabs:
            print(f"   {t}")
