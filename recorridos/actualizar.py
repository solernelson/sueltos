"""Copia el código actual de editor.html a todos los recorridos de esta carpeta.

Cada recorrido lleva su propia copia de la app. Cuando se corrige o mejora
editor.html, este script reemplaza el código de los demás .html y conserva
intactos sus datos (habitaciones, fotos, plano, ficha) y su título.

Uso:
    python actualizar.py            # actualiza todos los .html
    python actualizar.py casa.html  # solo los archivos indicados
"""
import re
import sys
from pathlib import Path

CARPETA = Path(__file__).resolve().parent
PLANTILLA = CARPETA / "editor.html"

# El JSON de los datos escapa "<", así que el primer </script> cierra el bloque.
DATOS = re.compile(r'<script id="tour-data" type="application/json">.*?</script>', re.S)
TITULO = re.compile(r"<title>.*?</title>", re.S)


def leer(p: Path) -> str:
    # newline="" conserva los saltos de línea tal como están en el archivo.
    with p.open(encoding="utf-8", newline="") as f:
        return f.read()


def main() -> int:
    # Algunas consolas de Windows no pueden mostrar ✓ o ✗: así no se cae el script.
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(errors="replace")
    plantilla = leer(PLANTILLA)
    if not DATOS.search(plantilla) or not TITULO.search(plantilla):
        print("editor.html no tiene el formato esperado; no se cambió nada.")
        return 1

    if len(sys.argv) > 1:
        archivos = [CARPETA / a for a in sys.argv[1:]]
    else:
        archivos = sorted(p for p in CARPETA.glob("*.html") if p.name != PLANTILLA.name)

    errores = 0
    for p in archivos:
        if not p.is_file():
            print(f"  ✗ {p.name}: no existe")
            errores += 1
            continue
        texto = leer(p)
        datos, titulo = DATOS.search(texto), TITULO.search(texto)
        if not datos or not titulo:
            print(f"  – {p.name}: no parece un recorrido, se omite")
            continue
        nuevo = TITULO.sub(lambda _: titulo.group(0), plantilla, count=1)
        nuevo = DATOS.sub(lambda _: datos.group(0), nuevo, count=1)
        if nuevo == texto:
            print(f"  = {p.name}: ya estaba al día")
            continue
        p.write_text(nuevo, encoding="utf-8", newline="")
        print(f"  ✓ {p.name}: actualizado")
    return 1 if errores else 0


if __name__ == "__main__":
    sys.exit(main())
