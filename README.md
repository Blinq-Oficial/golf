# Smart Meeting — Ryder Golf Business Trip España 2026

Landing page de alta conversión para el evento **Smart Meeting Ryder Golf Business Trip**, un viaje de negocios premium que combina golf, networking, gastronomía y cultura por España (Madrid → Sevilla → Ronda → Málaga).

## Stack Técnico

| Componente | Tecnología |
|---|---|
| Estructura | HTML5 semántico |
| Estilos | CSS3 vanilla (oklch, clamp, grid, custom properties) |
| Interactividad | JavaScript vanilla (IntersectionObserver, parallax) |
| Iconos | Phosphor Icons (CDN) |
| Fuentes | Google Fonts (Inter + Playfair Display) |

## Paleta de Diseño

- **Negro Carbón** `oklch(0.10 0.005 260)` — fondo principal
- **Negro Profundo** `oklch(0.07 0.005 260)` — secciones deep
- **Dorado** `oklch(0.74 0.14 85)` — acentos, CTAs, bordes
- **Blanco / Gris claro** — textos sobre fondo oscuro

> ⚠️ **No se usa rojo ni azul marino.** La paleta es estrictamente Negro + Dorado para mantener coherencia de estatus premium.

## Estructura del Proyecto

```
golf/
├── index.html
├── style.css
├── main.js
├── assets/
│   ├── bg_golf_spain.png
│   ├── gastronomy.png
│   └── video/
│       ├── destinos-bg.mp4
│       └── golf-bg.mp4
└── README.md
```

## Secciones de la Landing

1. **Hero** — CTA principal "Asegure su Lugar"
2. **Ruta del Viaje** — 4 destinos con video de fondo
3. **Experiencia Gastronómica** — Video + copy premium
4. **Networking Exclusivo** — Tarjetas con imagen de fondo
5. **Servicios VIP Incluidos** — Tabla sin bordes
6. **Nuestra Esencia + Perfil del Grupo** — Layout 2 columnas
7. **Cierre CTA** — Último empujón de conversión
8. **Modal de Solicitud** — Formulario de captura

---

## Protocolo Git — LEER ANTES DE TOCAR CÓDIGO

### Regla #1: UNA SOLA RAMA

Este proyecto opera **exclusivamente en `main`**. No se crean ramas. No se hacen merges. No hay conflictos.

### Flujo de Trabajo Diario

#### Antes de empezar a trabajar:
```bash
git pull origin main
```
Esto trae los últimos cambios. **Siempre** hacer esto antes de editar cualquier archivo.

#### Después de hacer cambios:
```bash
git add -A
git commit -m "descripción breve del cambio"
git push origin main
```

#### Formato de commits:
- `feat: nueva sección de testimonios`
- `fix: corregir espaciado en mobile`
- `refactor: paleta de colores actualizada`
- `content: actualizar textos del itinerario`

### Comandos que SÍ debes usar

| Comando | Cuándo |
|---|---|
| `git pull origin main` | **Siempre** antes de empezar a trabajar |
| `git add -A` | Después de hacer cambios |
| `git commit -m "mensaje"` | Para guardar cambios localmente |
| `git push origin main` | Para subir cambios al repo |
| `git status` | Para ver qué archivos cambiaste |
| `git log -n 5` | Para ver los últimos 5 commits |

### Comandos que NO debes usar

| Comando | Por qué NO |
|---|---|
| `git checkout -b rama` | No creamos ramas |
| `git merge` | No hay ramas que mergear |
| `git rebase` | Innecesario y peligroso aquí |
| `git force push` | Destruye historial |

### Si hay conflicto (no debería pasar)

1. **No entres en pánico**
2. Abre el archivo conflictivo
3. Busca las marcas `<<<<<<< HEAD` y `>>>>>>>`
4. Decide cuál versión conservar
5. Borra las marcas de conflicto
6. `git add -A`, `git commit -m "fix: resolver conflicto"` y push

### Configurar el repo por primera vez

```bash
git clone https://github.com/Blinq-Oficial/golf.git
cd golf
```

---

## Placeholders Pendientes

- `[correo@delcliente.com]` → Email real del cliente
- `[sitioweb-del-cliente.com]` → URL del sitio web
- `[Nombre del Cliente]` → Razón social para el copyright
- Formulario → Conectar a WhatsApp o backend real

## Contacto

Proyecto desarrollado por **Blinq** · [@Blinq-Oficial](https://github.com/Blinq-Oficial)
