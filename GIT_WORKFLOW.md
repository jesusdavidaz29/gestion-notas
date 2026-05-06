# Guía de Git Workflow - Sistema de Gestión de Notas

## Configuración Inicial

### 1. Configurar Git localmente

```bash
# Configurar nombre de usuario
git config --global user.name "Tu Nombre"

# Configurar email
git config --global user.email "tu.email@ejemplo.com"

# Verificar configuración
git config --list
```

### 2. Crear el repositorio en GitHub

1. Ir a https://github.com/new
2. Nombre del repo: `gestion-notas`
3. Descripción: "Sistema de Gestión de Notas Estudiantiles"
4. Seleccionar "Public" o "Private" según necesidad
5. Crear repositorio

### 3. Inicializar repositorio local

```bash
cd gestion-notas
git init
git add .
git commit -m "feat: proyecto inicial del sistema de gestión de notas"
```

### 4. Conectar repositorio remoto

```bash
# Reemplazar TU_USUARIO con tu usuario de GitHub
git remote add origin https://github.com/TU_USUARIO/gestion-notas.git

# Renombrar rama main (si es necesario)
git branch -M main

# Hacer push inicial
git push -u origin main
```

---

## Flujo de Trabajo Colaborativo

### Roles y Responsabilidades

#### Tech Lead
- Responsable de la arquitectura del proyecto
- Revisa y aprueba Pull Requests
- Mantiene estándares de código
- Maneja las ramas principales (main, develop)

#### Dev Backend
- Implementa las funcionalidades principales
- Crea y ejecuta tests unitarios
- Optimiza algoritmos y persistencia de datos

#### Dev Integration
- Mantiene continuidad entre ramas
- Documenta cambios importantes
- Realiza testing de integración
- Coordina merges complejos

---

## Workflow Estándar

### Rama Principal
```bash
main (rama de producción - código estable)
  ↓
develop (rama de integración - desarrollo)
  ↓
feature/* (ramas de características)
bug/* (ramas de correcciones)
docs/* (ramas de documentación)
```

### Crear una rama de feature

```bash
# 1. Actualizar la rama develop
git checkout develop
git pull origin develop

# 2. Crear rama de feature con nombre descriptivo
# Nombre: feature/[tipo-descripcion]
git checkout -b feature/agregar-exportacion-pdf

# Ejemplos válidos:
# feature/agregar-busqueda-estudiantes
# feature/mejorar-calculo-promedio
# feature/implementar-autenticacion
```

### Hacer cambios y commits

```bash
# Ver estado
git status

# Agregar archivos (opción 1: archivo específico)
git add main.py

# Agregar archivos (opción 2: todos)
git add .

# Hacer commit con mensaje descriptivo
# Formato: [tipo]: [descripción]
git commit -m "feat: agregar exportación a PDF de reportes"

# Otros ejemplos:
git commit -m "fix: corregir cálculo de promedio ponderado"
git commit -m "docs: actualizar README con nuevas funcionalidades"
git commit -m "refactor: optimizar búsqueda de estudiantes"
git commit -m "test: agregar tests para validación de calificaciones"
```

### Convención de Commits

```
feat:      Nueva característica
fix:       Corrección de bug
docs:      Cambios en documentación
style:     Formateo, cambios menores de código
refactor:  Refactorización sin cambiar funcionalidad
perf:      Mejora de rendimiento
test:      Agregar o actualizar tests
chore:     Cambios de compilación, dependencias, etc.
```

### Push a rama remota

```bash
# Primer push de la rama
git push -u origin feature/agregar-exportacion-pdf

# Pushes posteriores
git push
```

---

## Pull Request (PR)

### Crear Pull Request en GitHub

1. Ir a https://github.com/TU_USUARIO/gestion-notas
2. Ver notificación "Compare & pull request"
3. Seleccionar:
   - Base: `develop` (¡NO main!)
   - Compare: `feature/tu-rama`

4. Completar el template:

```markdown
## Descripción
Describe los cambios realizados brevemente

## Tipo de cambio
- [ ] Nueva característica
- [ ] Corrección de bug
- [ ] Documentación

## Testing
- [ ] He testeado los cambios localmente
- [ ] He ejecutado pytest con éxito

## Checklist
- [ ] Mi código sigue el estilo del proyecto
- [ ] He actualizado la documentación
- [ ] He agregado tests cuando es necesario
```

5. Hacer click en "Create pull request"

### Revisión de PR (Tech Lead)

```bash
# Descargar la rama para revisar
git fetch origin
git checkout feature/agregar-exportacion-pdf

# Ejecutar tests
python -m pytest test_gestion_notas.py

# Si todo está bien:
# Aprobar en GitHub y hacer merge
```

---

## Manejo de Conflictos

### Si hay conflicto de merge

```bash
# 1. Actualizar rama develop
git checkout develop
git pull origin develop

# 2. Rebase la rama de feature
git checkout feature/agregar-exportacion-pdf
git rebase develop

# 3. Resolver conflictos manualmente
# - Editar archivos con conflictos
# - Buscar marcadores: <<<<<<<, =======, >>>>>>>
# - Elegir versión correcta
# - git add [archivo]

# 4. Continuar rebase
git rebase --continue

# 5. Force push (solo en rama de feature)
git push --force
```

---

## Actualizar rama local

```bash
# Traer todos los cambios del remoto
git fetch origin

# Actualizar tu rama actual
git pull origin develop

# O equivalente
git pull
```

---

## Revertir cambios

```bash
# Descartar cambios en archivo específico
git checkout -- nombre_archivo.py

# Descartar todos los cambios no staged
git checkout -- .

# Deshacer último commit (mantener cambios)
git reset --soft HEAD~1

# Deshacer último commit (descartar cambios)
git reset --hard HEAD~1

# Ver historial para encontrar commit anterior
git log --oneline
```

---

## Comandos Útiles

```bash
# Ver estado actual
git status

# Ver historial de commits
git log --oneline -n 10

# Ver cambios sin stagear
git diff

# Ver cambios stagedos
git diff --cached

# Ver ramas locales
git branch

# Ver ramas remotas
git branch -r

# Ver todas las ramas
git branch -a

# Cambiar de rama
git checkout nombre-rama

# Crear y cambiar a rama nueva
git checkout -b nombre-rama

# Eliminar rama local
git branch -d nombre-rama

# Eliminar rama remota
git push origin --delete nombre-rama

# Ver quién modificó cada línea
git blame archivo.py

# Buscar en historial
git log --grep="palabra clave"
```

---

## Ejemplo Completo de Flujo

```bash
# 1. Clonar repositorio
git clone https://github.com/TU_USUARIO/gestion-notas.git
cd gestion-notas

# 2. Crear rama de feature
git checkout develop
git pull origin develop
git checkout -b feature/validar-email

# 3. Hacer cambios
# (Editar archivos en el editor)

# 4. Verificar cambios
git status
git diff

# 5. Agregar y comitear
git add .
git commit -m "feat: agregar validación de email para estudiantes"

# 6. Push
git push -u origin feature/validar-email

# 7. Crear Pull Request en GitHub
# (Ir a GitHub y hacer click en "Create pull request")

# 8. Esperar revisión del Tech Lead
# (Hacer cambios si es necesario)
git commit -m "fix: mejorar validación de email según feedback"
git push

# 9. Merge a develop (por Tech Lead)
# 10. Delete rama en GitHub

# 11. Limpiar localmente
git checkout develop
git pull origin develop
git branch -d feature/validar-email
```

---

## Buenas Prácticas

✅ **HACER:**
- Hacer commits pequeños y frecuentes
- Escribir mensajes de commit claros y descriptivos
- Pullear antes de hacer push
- Revisar el código antes de comitear
- Ejecutar tests localmente
- Mantener ramas actualizadas con develop

❌ **NO HACER:**
- Hacer commits muy grandes
- Comitear sin mensaje (vacío o genérico)
- Trabajar directamente en main o develop
- Hacer force push en ramas compartidas
- Comitear archivos innecesarios (venv/, __pycache__)
- Ignorar advertencias del linter

---

## Resolución de Problemas

### "fatal: The current branch develop has no upstream branch"
```bash
git push -u origin develop
```

### "Your local changes to 'archivo.py' would be overwritten"
```bash
git stash           # Guardar cambios temporalmente
git pull
git stash pop       # Recuperar cambios
```

### "The branch has unresolved merge conflicts"
```bash
# Editar archivos con conflictos y resolver manualmente
git add .
git commit -m "fix: resolver conflictos de merge"
git push
```

---

## Recursos Útiles

- [Git Documentation](https://git-scm.com/doc)
- [GitHub Guides](https://guides.github.com/)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [Git Flow](https://nvie.com/posts/a-successful-git-branching-model/)

---

**Última actualización:** 2024
**Responsable:** Tech Lead
