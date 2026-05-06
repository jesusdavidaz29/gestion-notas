# Contribuyendo al Sistema de Gestión de Notas

¡Gracias por tu interés en contribuir! Sigue estas directrices para una contribución efectiva.

## Proceso de Contribución

### 1. Fork y Clone
```bash
# Fork en GitHub (botón en la esquina superior derecha)
git clone https://github.com/TU_USUARIO/gestion-notas.git
cd gestion-notas
```

### 2. Crear Rama de Feature
```bash
git checkout develop
git pull origin develop
git checkout -b feature/descripcion-corta
```

### 3. Desarrollar con Estándares

#### Código Python
- Seguir PEP 8
- Usar nombres descriptivos para variables y funciones
- Agregar docstrings a todas las funciones
- Máximo 100 caracteres por línea

#### Ejemplo de función bien documentada
```python
def obtener_promedio(self, cedula, materia=None):
    """
    Obtiene el promedio de un estudiante.
    
    Args:
        cedula (str): Cédula del estudiante
        materia (str, optional): Si se especifica, calcula promedio por materia
        
    Returns:
        float: Promedio calculado, o None si no hay calificaciones
        
    Raises:
        ValueError: Si la cédula no existe
    """
    # Implementación...
```

### 4. Escribir Tests
```bash
# Agregar tests para nueva funcionalidad
python -m pytest test_gestion_notas.py -v

# Ver cobertura
python -m pytest --cov=main test_gestion_notas.py
```

### 5. Commit y Push
```bash
git add .
git commit -m "feat: descripción clara del cambio"
git push -u origin feature/descripcion-corta
```

### 6. Crear Pull Request
- Ir a https://github.com/TU_USUARIO/gestion-notas
- Completar template de PR
- Describir cambios y motivación
- Enlazar issues si corresponde (#123)

### 7. Responder Feedback
- Hacer cambios sugeridos
- Comitear nuevamente si es necesario
- Responder comentarios

### 8. Esperar Merge
- Tech Lead revisará y aprobará
- Tu rama se mergeará a `develop`
- Festejar! 🎉

---

## Estándares de Código

### Nombres
```python
# ✅ BIEN
def calcular_promedio_general(cedula):
    promedio_total = sum(calificaciones) / len(calificaciones)
    
# ❌ MAL
def calc(c):
    p = sum(x) / len(x)
```

### Documentación
```python
# ✅ BIEN
class GestorNotas:
    """Gestor central para operaciones con estudiantes y calificaciones."""
    
    def agregar_estudiante(self, cedula, nombre, email):
        """
        Agrega un nuevo estudiante al sistema.
        
        Args:
            cedula: Identificador único del estudiante
            nombre: Nombre completo
            email: Dirección de correo
            
        Returns:
            bool: True si éxito, False si ya existe
        """

# ❌ MAL
def agregar_estudiante(self, cedula, nombre, email):
    # Agregar estudiante
    ...
```

### Comentarios
```python
# ✅ BIEN - Explica el "por qué"
if promedio < 60:
    # Estudiante requiere seguimiento especial por bajo desempeño
    self.marcar_para_seguimiento(cedula)

# ❌ MAL - Explica lo obvio
if promedio < 60:
    # Aumentar promedio a 60
    promedio = 60
```

---

## Tipos de Contribuciones

### 🎯 Nuevas Características
```bash
git checkout -b feature/nombre-caracteristica
```
- Agregar funcionalidad completamente nueva
- Debe tener tests
- Actualizar README

### 🐛 Bug Fixes
```bash
git checkout -b fix/descripcion-bug
```
- Corregir comportamiento incorrecto
- Incluir test que falle antes del fix
- Incluir test que pase después

### 📚 Documentación
```bash
git checkout -b docs/tema
```
- Mejorar README
- Agregar ejemplos
- Documentar APIs
- Sin cambios de código

### ♻️ Refactoring
```bash
git checkout -b refactor/descripcion
```
- Mejorar código existente
- No cambia funcionalidad
- Debe mantener todos los tests pasando

### 🧪 Tests
```bash
git checkout -b test/cobertura-area
```
- Aumentar cobertura de tests
- Tests para casos edge
- Sin cambios de lógica

---

## Checklist Antes de PR

- [ ] Código sigue PEP 8
- [ ] Todas las funciones tienen docstrings
- [ ] Tests escritos y pasando: `pytest -v`
- [ ] Sin warnings o errores
- [ ] README actualizado si es necesario
- [ ] Git commits con mensaje descriptivo
- [ ] Rama creada desde `develop` (no `main`)
- [ ] 0 conflictos de merge

---

## Reportar Issues

### Formato de Issue
```markdown
## Descripción del problema
Describe claramente qué está sucediendo.

## Comportamiento esperado
¿Qué debería suceder?

## Pasos para reproducir
1. Paso 1
2. Paso 2
3. Paso 3

## Entorno
- Python: 3.9
- OS: Windows/Mac/Linux
- Versión Git: 2.33

## Información adicional
Capturas de pantalla, mensajes de error, etc.
```

---

## Sugerencias de Características

Para sugerir una nueva característica:

1. Crear un issue con etiqueta `enhancement`
2. Describir el caso de uso
3. Proponer una solución
4. Esperar feedback antes de implementar

---

## Comunidad

- Se respetuoso con otros contribuyentes
- Proporciona feedback constructivo
- Ayuda a otros reviendo código
- Comparte tu conocimiento

---

## Contacto

- **Tech Lead:** [nombre del tech lead]
- **Email:** [email de contacto]
- **Slack/Discord:** [canal del proyecto]

---

¡Gracias por contribuir! 🙏
