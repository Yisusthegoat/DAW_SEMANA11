# Nexo - Catálogo de productos (Semana 11)

Aplicación educativa con Django 5.x que presenta un catálogo empresarial sencillo. Incluye una página de resumen (FBV), un listado de productos (CBV `ListView`), plantillas Django y persistencia SQLite con el modelo `Producto`.

## Requisitos

- Python 3.11 o superior
- PowerShell (terminal integrada de Visual Studio Code)

## Instalación y ejecución en Windows

Desde la carpeta del proyecto:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py check
python manage.py makemigrations
python manage.py migrate
```

Para agregar los productos de demostración, ejecuta este comando una vez:

```powershell
python manage.py shell -c "from app.models import Producto; datos=[('Laptop Pro 14','Equipo portátil para productividad y trabajo diario.',4299.90,8),('Monitor Studio 27','Monitor IPS de alta resolución con soporte ergonómico.',1249.00,15),('Teclado Mecánico K2','Teclado compacto con switches táctiles.',289.90,24),('Mouse Inalámbrico Air','Mouse ergonómico recargable para oficina.',139.50,0),('Base USB-C Hub','Hub multipuerto para conectar periféricos y pantallas.',219.00,11),('Audífonos Focus','Audífonos cómodos con micrófono integrado.',349.90,6)]; [Producto.objects.get_or_create(nombre=n, defaults={'descripcion':d,'precio':p,'stock':s}) for n,d,p,s in datos]; print('Productos:', Producto.objects.count()); print('Disponibles:', Producto.objects.filter(stock__gt=0).count())"
```

Inicia el servidor:

```powershell
python manage.py runserver
```

Abre <http://127.0.0.1:8000/> para el resumen y <http://127.0.0.1:8000/catalogo/> para el catálogo. Detén el servidor con `Ctrl+C`.

## Consultas ORM y QuerySets

Entra al shell con `python manage.py shell` y prueba:

```python
from app.models import Producto

productos = Producto.objects.all()
print(productos)  # La consulta se evalúa al iterar/imprimir el QuerySet.

disponibles = Producto.objects.filter(stock__gt=0)
print(list(disponibles))  # La conversión a lista fuerza la consulta.
```

`all()` y `filter()` construyen QuerySets. Django retrasa normalmente la consulta a SQLite hasta que se necesitan los resultados, por ejemplo al iterar, convertir a lista o pedir su longitud. Así puede encadenar filtros antes de leer filas.

## Arquitectura

- **Modelo:** `app/models.py` define `Producto`; Django crea la tabla SQLite a partir de las migraciones.
- **Vistas:** `home` es una vista basada en función y `CatalogoListView` es una vista basada en clase. La CBV amplía el contexto con `get_context_data()`.
- **URLs:** `app/urls.py` nombra las rutas; `project/urls.py` incluye las rutas de la app.
- **Plantillas:** `templates/base.html` contiene estructura y navegación común; `home.html` y `catalogo.html` heredan mediante `{% extends %}`. Los enlaces usan `{% url %}`.
- **Ciclo Request/Response:** Django resuelve la URL de una solicitud, invoca su vista, obtiene datos del ORM, renderiza la plantilla con contexto y devuelve una respuesta HTTP al navegador.

## Validación

```powershell
python --version
python -m django --version
python manage.py check
python manage.py makemigrations
python manage.py migrate
python manage.py test
python manage.py runserver
```

La base `db.sqlite3` se genera localmente y está excluida de Git. No subas el entorno `.venv` al repositorio.

## Evidencias sugeridas

1. Terminal con `python --version` y `python -m django --version`.
2. Estructura del proyecto en el explorador de VS Code.
3. `python manage.py check`, creación de la migración y salida de `migrate`.
4. Shell de Django mostrando `Producto.objects.all()` y `filter()`.
5. Página de resumen en `/` y tabla completa en `/catalogo/`.
6. `python manage.py test` con el resultado de las pruebas.

## GitHub

El workspace no tiene un remoto GitHub configurado. Crea un repositorio vacío en tu cuenta y enlázalo con:

```powershell
git remote add origin https://github.com/USUARIO/REPOSITORIO.git
git add .
git commit -m "Implementa práctica Django Semana 11"
git push -u origin main
```
