# Sistema de Gestión de Notas Estudiantiles

## Descripción
Aplicación de consola en Python para gestionar calificaciones de estudiantes de manera eficiente. Permite registrar, consultar y reportar el desempeño académico de los estudiantes.

## Características

✅ **Gestión de Estudiantes**
- Agregar nuevos estudiantes con cédula, nombre y email
- Eliminar estudiantes del sistema
- Listar todos los estudiantes registrados

✅ **Gestión de Calificaciones**
- Registrar múltiples calificaciones por estudiante y materia
- Validación automática de rangos (0-100)
- Almacenamiento con historial de fechas

✅ **Reportes y Análisis**
- Calcular promedios por materia y general
- Escala cualitativa (Excelente, Bueno, Satisfactorio, Aceptable, Deficiente)
- Generar reportes individuales detallados
- Exportar datos a CSV para análisis adicional

## Estructura del Proyecto

```
gestion_notas/
├── main.py                    # Código principal
├── requirements.txt           # Dependencias
├── README.md                  # Este archivo
├── .gitignore                 # Archivos ignorados por git
└── estudiantes.json           # Base de datos (se crea automáticamente)
```

## Requisitos

- Python 3.8 o superior
- Pip (gestor de paquetes de Python)
- Git (para control de versiones)

## Instalación

### 1. Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/gestion-notas.git
cd gestion-notas
```

### 2. Crear entorno virtual (recomendado)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

## Uso

### Ejecutar la aplicación
```bash
python main.py
```

### Menú Principal
```
1. Agregar estudiante
2. Eliminar estudiante
3. Registrar calificación
4. Ver reporte de estudiante
5. Listar todos los estudiantes
6. Exportar reporte CSV
7. Salir
```

## Ejemplos de Uso

### Agregar un estudiante
```
Selecciona una opción (1-7): 1
Cédula del estudiante: 1234567890
Nombre completo: Juan Pérez García
Email: juan.perez@ejemplo.com
✓ Estudiante Juan Pérez García agregado correctamente.
```

### Registrar una calificación
```
Selecciona una opción (1-7): 3
Cédula del estudiante: 1234567890
Nombre de la materia: Programación Python
Calificación (0-100): 85
✓ Calificación 85 registrada para Programación Python.
```

### Ver reporte de estudiante
```
Selecciona una opción (1-7): 4
Cédula del estudiante: 1234567890

============================================================
REPORTE ACADÉMICO - Juan Pérez García
============================================================
Cédula: 1234567890
Email: juan.perez@ejemplo.com
Fecha de registro: 2024-01-15

------------------------------------------------------------
CALIFICACIONES POR MATERIA
------------------------------------------------------------

Programación Python:
  Calificaciones: [85, 90, 88]
  Promedio: 87.67
  Escala: Excelente

------------------------------------------------------------
PROMEDIO GENERAL: 87.67
DESEMPEÑO: Excelente
============================================================
```

## Escala de Calificación

| Rango    | Escala          | Nota   |
|----------|-----------------|--------|
| 90-100   | Excelente       | 5.0    |
| 80-89    | Bueno           | 4.5    |
| 70-79    | Satisfactorio   | 4.0    |
| 60-69    | Aceptable       | 3.5    |
| < 60     | Deficiente      | < 3.5  |

## Estructura de Datos

### Formato JSON (estudiantes.json)
```json
{
  "1234567890": {
    "nombre": "Juan Pérez García",
    "email": "juan.perez@ejemplo.com",
    "calificaciones": {
      "Programación Python": [
        {
          "valor": 85,
          "fecha": "2024-01-15T10:30:00.000000"
        }
      ]
    },
    "fecha_creacion": "2024-01-15T10:25:00.000000"
  }
}
```

## Flujo de Git Workflow

Este proyecto sigue el modelo Git Flow:

### Ramas principales
- `main` - Código en producción, estable
- `develop` - Rama de desarrollo integrada

### Ramas de características
```bash
# Crear rama de feature
git checkout -b feature/agregar-export-pdf

# Hacer commits
git commit -m "feat: agregar exportación a PDF"

# Hacer push
git push origin feature/agregar-export-pdf

# Crear Pull Request en GitHub
```

### Commits
Usar convención Conventional Commits:
- `feat:` - Nueva característica
- `fix:` - Corrección de bug
- `docs:` - Cambios en documentación
- `style:` - Formateo de código
- `refactor:` - Refactorización de código

Ejemplo:
```bash
git commit -m "feat: agregar función de cálculo de promedio ponderado"
```

## Roles del Equipo

### Tech Lead
- Supervisar arquitectura del código
- Revisar Pull Requests
- Mantener estándares de calidad
- Resolver conflictos de merge

### Dev Backend
- Implementar funcionalidades principales
- Optimizar algoritmos
- Manejar persistencia de datos
- Escribir tests unitarios

### Dev Integration
- Integración continua
- Control de versiones
- Documentación del código
- Testing de integración

## Contribuir

1. Hacer fork del repositorio
2. Crear una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir un Pull Request

## Testing

Para ejecutar pruebas unitarias:
```bash
python -m pytest tests/
```

## Licencia
Este proyecto está bajo licencia MIT - ver archivo LICENSE para detalles.

## Soporte
Para reportar problemas o sugerencias, crear un issue en GitHub.

## Autores
- Equipo de Desarrollo
- Docente responsable

---
**Última actualización:** 2024
