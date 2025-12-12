from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

Builder.load_file("kv/aksioma.kv") 

class Aksioma(MDScreen):
    def hitung(self):
        try:
            u = list(map(float, self.ids.u.text.split()))
            v = list(map(float, self.ids.v.text.split()))
            w = list(map(float, self.ids.w.text.split()))
            k = float(self.ids.k.text)

            # cek panjang vektor sama
            if not (len(u) == len(v) == len(w)):
                self.ids.hasil.text = "[color=#ff0000]Semua vektor harus memiliki panjang sama![/color]"
                return

            # fungsi dot product
            def dot(a, b):
                return sum(x * y for x, y in zip(a, b))

            # 1. Komutatif
            kom1 = dot(u, v)
            kom2 = dot(v, u)

            # 2. Linearitas
            u_plus_v = [u[i] + v[i] for i in range(len(u))]
            lin1 = dot(u_plus_v, w)
            lin2 = dot(u, w) + dot(v, w)

            # 3. Homogenitas
            ku = [k * x for x in u]
            hom1 = dot(ku, v)
            hom2 = k * dot(u, v)

            # 4. Positif definit
            vv = dot(v, v)
            if vv == 0:
                pos = "Vektor v adalah vektor nol."
            else:
                pos = "Vektor v bukan vektor nol."

            # Menampilkan hasil di label
            self.ids.hasil.text = f"""
1. Komutatif <u, v> = {kom1}
2. Linearitas <u + v, w> = {lin1}
3. Homogenitas <k·u, v> = {hom1}
4. Positif-definit <v, v> = {vv}\n {pos}
"""
        except:
            self.ids.hasil.text = "[color=#ff0000]Input tidak valid! Gunakan angka dipisah spasi.[/color]"


