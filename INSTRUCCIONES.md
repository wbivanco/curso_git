# Guía de Ejercicio: Flujo Completo Git + GitHub

Esta guía te llevará paso a paso a través de un flujo completo de trabajo profesional con Git y GitHub, utilizando el proyecto Python de este repositorio.

## 1. Introducción

En este ejercicio realizarás un flujo completo de trabajo profesional que incluye:

- ✅ Inicializar repositorio local
- ✅ Crear y trabajar en ramas
- ✅ Subir ramas al remoto
- ✅ Generar conflicto intencionalmente
- ✅ Resolver conflicto
- ✅ Crear Pull Request
- ✅ Merge final

## 2. Preparación

### Estructura del Proyecto

El proyecto tiene la siguiente estructura:

```
workshop_git/
├── app/
│   ├── __init__.py      # Hace que app sea un paquete Python
│   ├── main.py          # Aplicación principal
│   └── utils.py         # Funciones utilitarias (contiene greet)
├── tests/
│   └── test_app.py      # Tests con pytest
├── .github/
│   └── workflows/
│       └── ci.yml        # Workflow de CI con GitHub Actions
├── requirements.txt     # Dependencias del proyecto
├── README.md            # Documentación del proyecto
└── INSTRUCCIONES.md     # Guía completa del ejercicio
```

### Archivos Clave

- **`app/utils.py`**: Contiene la función `greet(name)` que retorna un saludo. Por defecto usa "mundo" si no se proporciona un nombre.
- **`app/main.py`**: Aplicación que solicita un nombre al usuario y muestra el saludo usando `greet()`.
- **`app/__init__.py`**: Archivo necesario para que Python reconozca `app` como un paquete.
- **`tests/test_app.py`**: Tests que validan el comportamiento de la función `greet()`.
- **`.github/workflows/ci.yml`**: Workflow de GitHub Actions que ejecuta automáticamente los tests en cada push y pull request.
- **`requirements.txt`**: Archivo que lista las dependencias del proyecto (pytest).

## 3. Inicializar Repositorio Local

Si el repositorio aún no está inicializado, ejecuta:

```bash
git init
```

Agrega todos los archivos al staging area:

```bash
git add .
```

Realiza el primer commit:

```bash
git commit -m "Primer commit del proyecto demo"
```

**Nota**: Si ya tienes un repositorio inicializado, puedes omitir `git init` y continuar con `git add` y `git commit`.

## 4. Crear Repositorio Remoto en GitHub

### Pasos en GitHub

1. Ve a [GitHub](https://github.com) y crea un nuevo repositorio
2. **No** crees README, .gitignore ni licencia (ya los tenemos localmente)
3. Copia la URL del repositorio (SSH o HTTPS)

### Vincular Repositorio Local con Remoto

Agrega el remoto (reemplaza `TU_USUARIO` y `TU_REPO` con tus valores):

```bash
git remote add origin git@github.com:wbivanco/curso_git.git
```

O si usas HTTPS:

```bash
git remote add origin https://github.com/wbivanco/curso_git.git
```

### Configurar Autenticación SSH (Recomendado)

GitHub ya no acepta autenticación con contraseña para operaciones Git. Si usas SSH (recomendado), necesitas configurar una clave SSH.

#### Verificar si ya tienes una clave SSH

```bash
ls -la ~/.ssh/id_*.pub
```

Si no aparece ninguna clave, continúa con los siguientes pasos.

#### Generar una nueva clave SSH

```bash
ssh-keygen -t ed25519 -C "walterbivanco@gmail.com"
```

Presiona Enter para aceptar la ubicación por defecto (`~/.ssh/id_ed25519`). Opcionalmente, puedes agregar una frase de contraseña para mayor seguridad.

#### Agregar la clave al agente SSH

El agente SSH es un programa que mantiene tus claves privadas en memoria de forma segura, evitando que tengas que ingresar tu frase de contraseña cada vez que uses la clave.

```bash
eval "$(ssh-agent -s)"
```

Este comando:
- Inicia el agente SSH si no está corriendo
- `ssh-agent -s` genera comandos para configurar variables de entorno
- `eval` ejecuta esos comandos en la sesión actual
- Esto permite que otros programas (como Git) usen el agente SSH

```bash
ssh-add ~/.ssh/id_ed25519
```

Este comando:
- Agrega tu clave privada (`id_ed25519`) al agente SSH
- La clave queda cargada en memoria para uso inmediato
- Si tu clave tiene frase de contraseña, te la pedirá una sola vez
- A partir de ese momento, Git podrá usar la clave automáticamente sin pedirte la contraseña cada vez

#### Agregar la clave pública a GitHub

1. **Copiar tu clave pública:**
   ```bash
   cat ~/.ssh/id_ed25519.pub
   ```

2. **Agregar la clave en GitHub - Opción Recomendada (SSH Key de Usuario):**
   
   **Para uso general (recomendado):**
   - Ve a: https://github.com/settings/keys
   - Haz clic en "New SSH key"
   - Agrega un título descriptivo (ej: "Mi Mac")
   - Pega la clave completa que copiaste
   - Haz clic en "Add SSH key"
   
   Esta clave funcionará para **todos tus repositorios** y es la opción recomendada para desarrollo personal.

   **Alternativa - Deploy Key (solo para un repositorio específico):**
   - Ve a tu repositorio en GitHub
   - Settings → Deploy keys → Add deploy key
   - Pega la clave y marca "Allow write access" si necesitas hacer push
   
   ⚠️ **Nota**: Las deploy keys solo funcionan para un repositorio específico. Si vas a trabajar con múltiples repositorios, usa SSH keys de usuario.

3. **Verificar la conexión:**
   ```bash
   ssh -T git@github.com
   ```
   
   Deberías ver un mensaje como: `Hi TU_USUARIO! You've successfully authenticated...`

**Nota sobre HTTPS**: Si prefieres usar HTTPS, necesitarás crear un [Personal Access Token](https://github.com/settings/tokens) y usarlo como contraseña cuando Git te lo solicite.

### Verificar que el Remoto Use SSH

**⚠️ Importante**: Si cuando haces `git push` Git te pide usuario y contraseña, significa que el remoto está configurado con HTTPS en lugar de SSH. Las deploy keys **solo funcionan con SSH**.

Para verificar y cambiar a SSH:

```bash
# Ver la configuración actual del remoto
git remote -v
```

Si ves URLs que empiezan con `https://`, cámbialas a SSH:

```bash
# Cambiar de HTTPS a SSH
git remote set-url origin git@github.com:wbivanco/curso_git.git

# Verificar que el cambio se aplicó
git remote -v
```

Ahora deberías ver URLs que empiezan con `git@github.com:` en lugar de `https://`.

### Subir la Rama Main al Remoto

Una vez configurada la autenticación y verificado que el remoto usa SSH, sube la rama main:

```bash
git push -u origin main
```

Si todo está configurado correctamente, **no debería pedirte usuario ni contraseña** y el push se completará automáticamente usando tu deploy key.

## 5. Crear Rama Feature

Crea y cambia a una nueva rama para trabajar en una funcionalidad:

```bash
git checkout -b feature/saludo
```

### Editar el Código

Abre el archivo `app/utils.py` y modifica la función `greet()` para cambiar el saludo por defecto de "mundo" a "GitHub".

**Antes:**
```python
def greet(name: str) -> str:
    name = name.strip() or "mundo"
    return f"Hola, {name}!"
```

**Después:**
```python
def greet(name: str) -> str:
    name = name.strip() or "GitHub"
    return f"Hola, {name}!"
```

### Actualizar el Test

**⚠️ Importante**: Cuando cambias el código, también debes actualizar el test para que coincida. Abre `tests/test_app.py` y actualiza el test:

**Antes:**
```python
def test_greet_empty():
    assert greet("") == "Hola, mundo!"
```

**Después:**
```python
def test_greet_empty():
    assert greet("") == "Hola, GitHub!"
```

Esto asegura que el test valide el comportamiento correcto del código modificado.

### Commit y Push

Agrega los archivos modificados:

```bash
git add app/utils.py tests/test_app.py
```

Realiza el commit:

```bash
git commit -m "feat: cambia saludo por defecto a GitHub"
```

Sube la rama al remoto:

```bash
git push -u origin feature/saludo
```

## 6. Crear Conflicto desde Main

Ahora vamos a crear un conflicto intencionalmente. Cambia a la rama main:

```bash
git checkout main
```

### Editar el Mismo Archivo en Main

Abre `app/utils.py` y realiza una modificación diferente e incompatible. Por ejemplo, cambia el saludo por defecto a "Python":

**Modificación en main:**
```python
def greet(name: str) -> str:
    name = name.strip() or "Python"
    return f"Hola, {name}!"
```

### Actualizar el Test en Main

**⚠️ Importante**: También debes actualizar el test en `tests/test_app.py` para que coincida con el cambio:

**Antes:**
```python
def test_greet_empty():
    assert greet("") == "Hola, mundo!"
```

**Después:**
```python
def test_greet_empty():
    assert greet("") == "Hola, Python!"
```

### Commit y Push en Main

Agrega y commitea los cambios:

```bash
git add app/utils.py tests/test_app.py
git commit -m "feat: cambia saludo por defecto en main"
```

Sube los cambios:

```bash
git push
```

**Resultado**: Ahora tenemos dos versiones diferentes del mismo archivo en dos ramas diferentes, lo que generará un conflicto al intentar mergear.

## 7. Crear Pull Request

### En GitHub

1. Ve a tu repositorio en GitHub
2. Verás una notificación sugiriendo crear un Pull Request para la rama `feature/saludo`
3. Haz clic en "Compare & pull request"

### Propósito del Pull Request

Explica que los PRs sirven para:
- **Revisión**: Otros desarrolladores pueden revisar tus cambios
- **Integración**: Validar que los cambios funcionan correctamente
- **Validación**: Ejecutar tests y verificaciones automáticas
- **Acciones automáticas**: GitHub Actions puede ejecutar CI/CD

### Conflicto Detectado

GitHub mostrará que hay un conflicto que debe resolverse antes de poder mergear el PR. Verás un mensaje como:

> "This branch has conflicts that must be resolved"

## 8. Resolver Conflicto

### Cambiar a la Rama Feature

```bash
git checkout feature/saludo
```

### Traer Cambios de Main

```bash
git pull origin main --no-rebase
```

**Nota**: El flag `--no-rebase` le dice a Git que haga un merge (no un rebase) cuando hay ramas divergentes. Esto es lo que queremos para este ejercicio.

#### ¿Qué es Merge vs Rebase?

**Merge (Fusión):**
- Combina las ramas creando un **commit de merge** que une ambas historias
- Mantiene el historial completo de ambas ramas
- Crea un "punto de unión" visible en el historial
- Es más seguro y no reescribe el historial
- **Ejemplo visual:**
  ```
  main:     A---B---C---F (merge commit)
                    \   /
  feature:           D---E
  ```

**Rebase (Reaplicar):**
- Toma tus commits y los "re-aplica" encima de la otra rama
- Reescribe el historial para que parezca lineal
- No crea commits de merge
- El historial queda más limpio pero se modifica
- **Ejemplo visual:**
  ```
  main:     A---B---C
                      \
  feature:             D'---E' (commits reaplicados)
  ```

**Para este ejercicio usamos merge** porque:
- Es más seguro y no modifica el historial existente
- Permite ver claramente cuándo se integraron los cambios
- Es la práctica más común en equipos de trabajo

Git te mostrará que hay un conflicto en `app/utils.py` y el merge quedará en estado pendiente hasta que resuelvas el conflicto.

### Abrir el Archivo con Conflicto

Abre `app/utils.py` y verás marcadores de conflicto:

```python
def greet(name: str) -> str:
<<<<<<< HEAD
    name = name.strip() or "GitHub"
=======
    name = name.strip() or "Python"
>>>>>>> main
    return f"Hola, {name}!"
```

### Explicación de los Marcadores

- `<<<<<<< HEAD`: Inicio del cambio en tu rama actual (feature/saludo)
- `=======`: Separador entre las dos versiones
- `>>>>>>> main`: Fin del cambio que viene de main

### Resolver Manualmente

Elige una de las versiones o combina ambas. Por ejemplo, si queremos mantener "GitHub":

```python
def greet(name: str) -> str:
    name = name.strip() or "GitHub"
    return f"Hola, {name}!"
```

**Elimina todos los marcadores de conflicto** (`<<<<<<<`, `=======`, `>>>>>>>`).

### Finalizar la Resolución

Agrega el archivo resuelto:

```bash
git add app/utils.py
```

Realiza el commit de resolución:

```bash
git commit -m "fix: resuelve conflicto"
```

Sube los cambios:

```bash
git push
```

## 9. Merge Final del PR

### Verificar en GitHub

1. Regresa al Pull Request en GitHub
2. Verifica que:
   - Los checks de GitHub Actions estén verdes ✅ (el workflow de CI ejecutará los tests automáticamente)
   - No haya más conflictos
   - Los cambios se vean correctamente
   
**Nota**: El workflow de CI (`.github/workflows/ci.yml`) se ejecutará automáticamente cuando crees o actualices el Pull Request. Verás los resultados en la pestaña "Checks" del PR. Los tests deben pasar en todas las versiones de Python (3.9, 3.10, 3.11) para que el check esté verde.

### Realizar el Merge

1. Haz clic en "Merge pull request"
2. Confirma el merge
3. Opcionalmente, borra la rama `feature/saludo` desde la interfaz de GitHub

### Actualizar Local

Actualiza tu rama main local:

```bash
git checkout main
git pull origin main
```

Opcionalmente, borra la rama local:

```bash
git branch -d feature/saludo
```

## 10. Cierre y Conceptos Clave

### Conceptos Reforzados

- **Ramas como líneas de trabajo**: Permiten trabajar en funcionalidades de forma aislada
- **Conflictos como parte normal del desarrollo**: Son esperables cuando múltiples personas trabajan en el mismo código
- **Pull Requests como mecanismo de colaboración**: Facilitan la revisión y discusión antes de integrar cambios
- **GitHub Actions como automatización**: Ejecutan tests, linting y otras verificaciones automáticamente en cada push y PR
  - El workflow de CI incluido (`ci.yml`) prueba el código con Python 3.9, 3.10 y 3.11
  - Los checks aparecen en los Pull Requests y deben estar verdes antes de hacer merge

### Verificación Final

Ejecuta los tests para asegurarte de que todo funciona:

**Si usas pyenv**, asegúrate de tener configurada la versión de Python:

```bash
# Configurar Python 3.10.14 para este proyecto (si usas pyenv)
pyenv local 3.10.14

# Ejecutar tests
python -m pytest tests/
```

O simplemente:

```bash
pytest tests/
```

**Nota**: Si obtienes un error de que pytest no se encuentra, asegúrate de tenerlo instalado:

```bash
pip install pytest
```

O ejecuta la aplicación:

```bash
python -m app.main
```

## Resumen de Comandos

```bash
# Inicialización
git init
git add .
git commit -m "chore: primer commit del proyecto demo"

# Configurar remoto
git remote add origin <URL>
git push -u origin main

# Trabajar en feature
git checkout -b feature/saludo
# Editar app/utils.py (cambiar "mundo" a "GitHub")
# Editar tests/test_app.py (cambiar "mundo" a "GitHub" en el test)
git add app/utils.py tests/test_app.py
git commit -m "feat: cambia saludo por defecto a GitHub"
git push -u origin feature/saludo

# Crear conflicto
git checkout main
# Editar app/utils.py con cambio diferente (cambiar "mundo" a "Python")
# Editar tests/test_app.py (cambiar "mundo" a "Python" en el test)
git add app/utils.py tests/test_app.py
git commit -m "feat: cambia saludo por defecto en main"
git push

# Resolver conflicto
git checkout feature/saludo
git pull origin main
# Resolver conflicto en app/utils.py
git add app/utils.py
git commit -m "fix: resuelve conflicto"
git push

# Merge final (desde GitHub)
git checkout main
git pull origin main
```

---

**¡Felicitaciones!** Has completado un flujo completo de trabajo profesional con Git y GitHub. 🎉

