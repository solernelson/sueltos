# Recorridos virtuales

Recorridos virtuales de casas hechos con fotos panorámicas del celular. Cada recorrido es **un solo archivo HTML**, con las fotos incluidas, que se publica gratis con GitHub Pages.

## Archivos

| Archivo | Para qué sirve |
|---|---|
| `editor.html` | Editor vacío. Ábrelo en tu computadora para crear un recorrido nuevo. |
| `index.html` | Recorrido de ejemplo: la portada del sitio. |

## Crear un recorrido nuevo

1. Abre `editor.html` con doble clic en Chrome o Edge.
2. Toca **Añadir panorámicas** y elige tus fotos, una por habitación.
3. En cada habitación:
   - Ponle nombre y ajusta el **Ángulo** hasta que las paredes se vean rectas (360° si diste la vuelta completa).
   - **+ Punto de paso**: toca una puerta y elige a qué habitación lleva.
   - **+ Etiqueta**: toca algo de la foto y escribe una explicación.
   - **Fotos de detalle**: agrega fotos normales del baño, los acabados, la vista…
   - **Usar esta vista al entrar**: define hacia dónde mira la persona al llegar.
4. Opcional:
   - **Plano de la casa**: sube una imagen del plano y usa **Ubicar en el plano** en cada habitación.
   - **Ficha de la propiedad**: precio, ubicación, m², habitaciones, baños y WhatsApp.
5. Cambia el nombre del recorrido arriba y toca **Descargar HTML**.
6. El archivo se guarda en *Descargas*. Muévelo a esta carpeta con un nombre corto y sin espacios, por ejemplo `casa-heredia.html`.

> El editor local no guarda solo: si cierras la pestaña sin descargar, pierdes los cambios.

## Editar un recorrido ya descargado

Los recorridos descargados se abren en modo visitante. Para editarlos, ábrelos con `#editar` al final de la dirección, por ejemplo:

```
file:///C:/MyRepos/sueltos/recorridos/casa-heredia.html#editar
```

Haz los cambios, descarga de nuevo y reemplaza el archivo.

## Publicar en GitHub Pages

Este proyecto vive en el repositorio [solernelson/sueltos](https://github.com/solernelson/sueltos), dentro de la carpeta `recorridos/`.

Para activar Pages la primera vez, entra en GitHub a **Settings → Pages**, elige **Source: Deploy from a branch** y luego **main** y **/(root)**. En 1 o 2 minutos quedan listos los enlaces:

- `https://solernelson.github.io/sueltos/recorridos/`: el ejemplo (`index.html`)
- `https://solernelson.github.io/sueltos/recorridos/editor.html`: el editor en línea
- `https://solernelson.github.io/sueltos/recorridos/casa-heredia.html`: cada recorrido

Para agregar o actualizar un recorrido:

```bash
cd C:\MyRepos\sueltos
git add recorridos/casa-heredia.html
git commit -m "Recorrido casa Heredia"
git push
```

> En el plan gratis de GitHub, Pages solo funciona con repositorios **públicos**. Cualquiera con el enlace puede ver los recorridos.

## Cómo tomar las fotos

- Párate en el centro de la habitación y usa el modo **Panorámica** de la cámara.
- Gira el celular sobre sí mismo, no tu cuerpo, a la altura del pecho y despacio.
- Procura que salgan las **puertas**: ahí van los puntos para pasar de una habitación a otra.
- Enciende las luces, abre las cortinas y evita que haya gente moviéndose.

## Notas

- El visor usa [three.js](https://threejs.org), que se carga desde internet: el recorrido necesita conexión para abrirse.
- **Mirar moviendo el celular** (giroscopio) funciona en la versión publicada en GitHub Pages, porque se sirve por HTTPS. En iPhone pide permiso la primera vez.
- Las fotos se reducen automáticamente al subirlas, para que el recorrido cargue rápido en el celular.
