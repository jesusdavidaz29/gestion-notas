# Configuración del Equipo - Sistema de Gestión de Notas

## Información General del Proyecto
- **Nombre:** Sistema de Gestión de Notas Estudiantiles
- **Descripción:** Aplicación de consola en Python para gestionar calificaciones
- **Lenguaje:** Python 3.8+
- **Repositorio:** https://github.com/TU_USUARIO/gestion-notas.git
- **Duración:** 1 semestre
- **Docente:** [Nombre del docente]

---

## Equipo - 3 Integrantes

### Integrante 1: TECH LEAD
**Responsabilidades:**
- Supervisar la arquitectura general del proyecto
- Revisar y aprobar Pull Requests
- Mantener estándares de calidad de código
- Resolver conflictos de merge
- Comunicación con docente/stakeholders
- Gestionar timeline y entregas

**Tareas Iniciales:**
- [ ] Crear repositorio en GitHub
- [ ] Configurar permisos y acceso del equipo
- [ ] Establecer reglas de protección en rama main
- [ ] Crear milestone y labels en GitHub
- [ ] Hacer setup inicial del proyecto
- [ ] Revisar que todos los miembros tengan acceso

**Ramas a Gestionar:**
```
main (producción) - ← Solo Tech Lead puede hacer merge desde develop
develop (integración) - ← Punto de merge de todas las features
```

---

### Integrante 2: DEV BACKEND
**Responsabilidades:**
- Implementar funcionalidades principales
- Crear tests unitarios
- Optimizar lógica de negocio
- Manejar persistencia de datos
- Documentar funciones y módulos

**Tareas Iniciales:**
- [ ] Entender arquitectura de GestorNotas
- [ ] Implementar pruebas unitarias
- [ ] Crear datos de prueba
- [ ] Optimizar algoritmos de cálculo
- [ ] Implementar exportación a CSV
- [ ] Documentar cada función

**Features Asignadas (Ejemplos):**
```
feature/validar-emails
feature/calcular-promedio-ponderado
feature/exportar-csv
feature/buscar-estudiante
feature/estadisticas-grupo
```

**Testing:**
```bash
# Ejecutar tests regularmente
python -m pytest test_gestion_notas.py -v

# Ver cobertura
python -m pytest --cov=main test_gestion_notas.py

# Tests específicos
python -m pytest test_gestion_notas.py::TestGestorNotas::test_agregar_estudiante
```

---

### Integrante 3: DEV INTEGRATION
**Responsabilidades:**
- Integración continua entre ramas
- Documentación de cambios
- Testing de integración
- Mantener flujo de Git limpio
- Coordinar merges complejos
- Control de versiones

**Tareas Iniciales:**
- [ ] Documentar workflow de Git
- [ ] Crear templates de PR
- [ ] Documentar funcionalidades finales
- [ ] Realizar testing de integración
- [ ] Crear guía de despliegue
- [ ] Mantener historial limpio

**Documentación a Crear:**
```
GIT_WORKFLOW.md ✓
CONTRIBUTING.md ✓
API_DOCUMENTATION.md
DEPLOYMENT_GUIDE.md
CHANGELOG.md
```

---

## Reuniones

### Scrum Diario (5-10 min)
**Frecuencia:** Lunes a Viernes
**Horario:** [Define horario]

**Preguntas a responder:**
1. ¿Qué hice ayer?
2. ¿Qué haré hoy?
3. ¿Hay algún bloqueante?

### Reunión de Retrospectiva
**Frecuencia:** Fin de cada semana o milestone
**Duración:** 30 min

**Temas:**
- ¿Qué salió bien?
- ¿Qué no salió bien?
- ¿Qué podemos mejorar?

---

## Milestones y Entregas

### Fase 1: Setup (Semana 1)
- [ ] Repositorio creado y configurado
- [ ] Todos tienen acceso
- [ ] Estructura de proyecto lista
- [ ] Entorno local configurado

**Fecha límite:** [Definir]

### Fase 2: Core (Semanas 2-4)
- [ ] Clase GestorNotas implementada
- [ ] CRUD de estudiantes
- [ ] Gestión de calificaciones
- [ ] Cálculo de promedios
- [ ] Tests unitarios >80%

**Fecha límite:** [Definir]

### Fase 3: Features (Semanas 5-6)
- [ ] Exportación a CSV
- [ ] Reportes avanzados
- [ ] Validaciones completas
- [ ] Manejo de errores robusto

**Fecha límite:** [Definir]

### Fase 4: QA y Deployment (Semana 7)
- [ ] Testing integral
- [ ] Documentación completa
- [ ] Merge final a main
- [ ] Release v1.0

**Fecha límite:** [Definir]

---

## Convenciones de Código

### Formato de Rama
```
[tipo]/[descripcion-corta-con-guiones]

feature/     Nueva característica
fix/         Corrección de bug
docs/        Documentación
refactor/    Refactorización
test/        Pruebas

Ejemplos:
feature/validar-emails
fix/promedio-negativo
docs/actualizar-readme
refactor/optimizar-busqueda
test/cobertura-calificaciones
```

### Formato de Commit
```
[tipo]: [descripción imperativa]

feat:     Nueva característica
fix:      Corrección de bug
docs:     Cambios en documentación
style:    Formateo de código
refactor: Refactorización sin cambiar funcionalidad
test:     Agregar tests
perf:     Mejora de rendimiento

Ejemplos:
git commit -m "feat: agregar validación de emails"
git commit -m "fix: corregir cálculo de promedio general"
git commit -m "docs: actualizar README con ejemplos"
git commit -m "test: agregar tests para clase GestorNotas"
```

### Estilo Python (PEP 8)
```python
# Indentación: 4 espacios
def mi_funcion():
    pass

# Línea máxima: 100 caracteres
resultado = calcular_algo_muy_largo_que_requiere_muchos_parametros(
    param1, param2, param3
)

# Docstrings: Google style
def obtener_promedio(cedula):
    """Obtiene el promedio de un estudiante.
    
    Args:
        cedula: Cédula del estudiante
        
    Returns:
        float: Promedio calculado o None
    """
    pass
```

---

## Flujo de Revisión de Código

### Checklist de Reviewer (Tech Lead)

- [ ] Código sigue PEP 8
- [ ] Tests escritos y pasando
- [ ] Documentación actualizada
- [ ] Sin conflictos de merge
- [ ] Commits tienen buen mensaje
- [ ] Cobertura de tests > 80%
- [ ] No hay prints de debug
- [ ] Manejo de errores adecuado

### Feedback en PR

**Formato recomendado:**
```markdown
## Cambios Solicitados

### Crítico
- [ ] Agregar validación de entrada

### Importante
- [ ] Mejorar nombre de variable

### Sugerencia
- Considerar refactorizar esta función
```

---

## Recursos y Herramientas

### Desarrollo
- **IDE Recomendado:** VS Code, PyCharm, o similar
- **Python:** 3.8+
- **Git:** Última versión estable
- **GitHub:** Acceso a repositorio

### Testing
```bash
# Instalar pytest
pip install pytest pytest-cov

# Ejecutar tests
pytest test_gestion_notas.py -v

# Con cobertura
pytest --cov=main test_gestion_notas.py
```

### Linting (Opcional pero Recomendado)
```bash
# Instalar flake8
pip install flake8

# Verificar código
flake8 main.py --max-line-length=100
```

---

## Contacto y Comunicación

- **Tech Lead:** [Nombre] - [Email] - [Teléfono]
- **Canal Slack/Discord:** [Link]
- **Email Equipo:** [Email grupal]
- **Docente:** [Nombre] - [Email]

---

## Problemas Frecuentes

### "Mi rama tiene conflictos"
```bash
git fetch origin
git rebase origin/develop
# Resolver conflictos en editor
git add .
git rebase --continue
git push --force
```

### "Necesito traer cambios de otro miembro"
```bash
git fetch origin
git pull origin develop
git merge origin/feature/otra-rama
```

### "Cometí un error y necesito revertir"
```bash
# Ver commits
git log --oneline -n 10

# Deshacer último commit
git reset --soft HEAD~1

# O especificar commit
git revert [hash-commit]
git push
```

---

## Criterios de Aceptación - Entrega Final

✅ **DEBE TENER:**
- [ ] Código funcional y probado
- [ ] Todos los tests pasando
- [ ] Documentación completa
- [ ] README actualizado
- [ ] Git workflow limpio
- [ ] Sin errores en ejecución
- [ ] Código con estándar PEP 8

✅ **BUENA PRÁCTICA:**
- [ ] Más de 80% cobertura de tests
- [ ] Commits con mensajes claros
- [ ] Documentación de APIs
- [ ] Guía de uso de la aplicación
- [ ] Ejemplos de funcionalidad

---

**Última actualización:** 2024
**Aprobado por:** [Tech Lead]
