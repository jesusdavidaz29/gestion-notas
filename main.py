"""
Sistema de Gestión de Notas
Aplicación de consola para gestionar calificaciones estudiantiles
"""

import json
import os
from datetime import datetime
from pathlib import Path


class GestorNotas:
    """Clase principal para gestionar estudiantes y sus calificaciones"""
    
    def __init__(self, archivo_datos="estudiantes.json"):
        self.archivo_datos = archivo_datos
        self.estudiantes = self._cargar_datos()
    
    def _cargar_datos(self):
        """Carga los datos desde el archivo JSON"""
        if os.path.exists(self.archivo_datos):
            try:
                with open(self.archivo_datos, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                print("⚠️  Archivo corrupto. Iniciando con datos vacíos.")
                return {}
        return {}
    
    def _guardar_datos(self):
        """Guarda los datos en el archivo JSON"""
        try:
            with open(self.archivo_datos, 'w', encoding='utf-8') as f:
                json.dump(self.estudiantes, f, ensure_ascii=False, indent=2)
            print("✓ Datos guardados correctamente.")
        except IOError as e:
            print(f"✗ Error al guardar datos: {e}")
    
    def agregar_estudiante(self, cedula, nombre, email):
        """Agrega un nuevo estudiante"""
        if cedula in self.estudiantes:
            print(f"✗ El estudiante con cédula {cedula} ya existe.")
            return False
        
        self.estudiantes[cedula] = {
            "nombre": nombre,
            "email": email,
            "calificaciones": {},
            "fecha_creacion": datetime.now().isoformat()
        }
        self._guardar_datos()
        print(f"✓ Estudiante {nombre} agregado correctamente.")
        return True
    
    def eliminar_estudiante(self, cedula):
        """Elimina un estudiante"""
        if cedula not in self.estudiantes:
            print(f"✗ Estudiante con cédula {cedula} no encontrado.")
            return False
        
        nombre = self.estudiantes[cedula]["nombre"]
        del self.estudiantes[cedula]
        self._guardar_datos()
        print(f"✓ Estudiante {nombre} eliminado correctamente.")
        return True
    
    def registrar_calificacion(self, cedula, materia, calificacion):
        """Registra una calificación para un estudiante en una materia"""
        if cedula not in self.estudiantes:
            print(f"✗ Estudiante con cédula {cedula} no encontrado.")
            return False
        
        if not (0 <= calificacion <= 100):
            print("✗ La calificación debe estar entre 0 y 100.")
            return False
        
        if materia not in self.estudiantes[cedula]["calificaciones"]:
            self.estudiantes[cedula]["calificaciones"][materia] = []
        
        self.estudiantes[cedula]["calificaciones"][materia].append({
            "valor": calificacion,
            "fecha": datetime.now().isoformat()
        })
        self._guardar_datos()
        print(f"✓ Calificación {calificacion} registrada para {materia}.")
        return True
    
    def obtener_promedio(self, cedula, materia=None):
        """Obtiene el promedio de un estudiante (por materia o general)"""
        if cedula not in self.estudiantes:
            print(f"✗ Estudiante con cédula {cedula} no encontrado.")
            return None
        
        calificaciones_dict = self.estudiantes[cedula]["calificaciones"]
        
        if materia:
            if materia not in calificaciones_dict:
                print(f"✗ No hay calificaciones para {materia}.")
                return None
            valores = [c["valor"] for c in calificaciones_dict[materia]]
        else:
            valores = []
            for cal_list in calificaciones_dict.values():
                valores.extend([c["valor"] for c in cal_list])
        
        if not valores:
            return None
        
        return sum(valores) / len(valores)
    
    def obtener_escala(self, promedio):
        """Convierte un promedio numérico a escala cualitativa"""
        if promedio >= 90:
            return "Excelente"
        elif promedio >= 80:
            return "Bueno"
        elif promedio >= 70:
            return "Satisfactorio"
        elif promedio >= 60:
            return "Aceptable"
        else:
            return "Deficiente"
    
    def generar_reporte_estudiante(self, cedula):
        """Genera un reporte completo de un estudiante"""
        if cedula not in self.estudiantes:
            print(f"✗ Estudiante con cédula {cedula} no encontrado.")
            return
        
        est = self.estudiantes[cedula]
        print(f"\n{'='*60}")
        print(f"REPORTE ACADÉMICO - {est['nombre']}")
        print(f"{'='*60}")
        print(f"Cédula: {cedula}")
        print(f"Email: {est['email']}")
        print(f"Fecha de registro: {est['fecha_creacion'][:10]}")
        print(f"\n{'-'*60}")
        print("CALIFICACIONES POR MATERIA")
        print(f"{'-'*60}")
        
        if not est["calificaciones"]:
            print("Sin calificaciones registradas.")
        else:
            for materia, notas in sorted(est["calificaciones"].items()):
                valores = [n["valor"] for n in notas]
                promedio_materia = sum(valores) / len(valores)
                escala = self.obtener_escala(promedio_materia)
                
                print(f"\n{materia}:")
                print(f"  Calificaciones: {valores}")
                print(f"  Promedio: {promedio_materia:.2f}")
                print(f"  Escala: {escala}")
        
        promedio_general = self.obtener_promedio(cedula)
        if promedio_general:
            escala_general = self.obtener_escala(promedio_general)
            print(f"\n{'-'*60}")
            print(f"PROMEDIO GENERAL: {promedio_general:.2f}")
            print(f"DESEMPEÑO: {escala_general}")
            print(f"{'='*60}\n")
    
    def listar_estudiantes(self):
        """Lista todos los estudiantes registrados"""
        if not self.estudiantes:
            print("No hay estudiantes registrados.")
            return
        
        print(f"\n{'='*80}")
        print(f"{'Cédula':<12} {'Nombre':<25} {'Email':<30} {'Promedio':<10}")
        print(f"{'='*80}")
        
        for cedula, datos in sorted(self.estudiantes.items()):
            promedio = self.obtener_promedio(cedula)
            promedio_str = f"{promedio:.2f}" if promedio else "N/A"
            print(f"{cedula:<12} {datos['nombre']:<25} {datos['email']:<30} {promedio_str:<10}")
        
        print(f"{'='*80}\n")
    
    def exportar_reporte_csv(self, archivo_salida="reporte_estudiantes.csv"):
        """Exporta un reporte en formato CSV"""
        try:
            with open(archivo_salida, 'w', encoding='utf-8') as f:
                f.write("Cédula,Nombre,Email,Promedio General,Desempeño\n")
                
                for cedula, datos in sorted(self.estudiantes.items()):
                    promedio = self.obtener_promedio(cedula)
                    promedio_str = f"{promedio:.2f}" if promedio else "N/A"
                    desempeño = self.obtener_escala(promedio) if promedio else "N/A"
                    
                    f.write(f"{cedula},{datos['nombre']},{datos['email']},{promedio_str},{desempeño}\n")
            
            print(f"✓ Reporte exportado a {archivo_salida}")
        except IOError as e:
            print(f"✗ Error al exportar reporte: {e}")


def mostrar_menu():
    """Muestra el menú principal"""
    print("\n" + "="*60)
    print("SISTEMA DE GESTIÓN DE NOTAS ESTUDIANTILES")
    print("="*60)
    print("1. Agregar estudiante")
    print("2. Eliminar estudiante")
    print("3. Registrar calificación")
    print("4. Ver reporte de estudiante")
    print("5. Listar todos los estudiantes")
    print("6. Exportar reporte CSV")
    print("7. Salir")
    print("="*60)


def main():
    """Función principal - Loop de la aplicación"""
    gestor = GestorNotas()
    
    while True:
        mostrar_menu()
        opcion = input("\nSelecciona una opción (1-7): ").strip()
        
        if opcion == "1":
            cedula = input("Cédula del estudiante: ").strip()
            nombre = input("Nombre completo: ").strip()
            email = input("Email: ").strip()
            gestor.agregar_estudiante(cedula, nombre, email)
        
        elif opcion == "2":
            cedula = input("Cédula del estudiante a eliminar: ").strip()
            confirmar = input("¿Estás seguro? (s/n): ").strip().lower()
            if confirmar == 's':
                gestor.eliminar_estudiante(cedula)
        
        elif opcion == "3":
            cedula = input("Cédula del estudiante: ").strip()
            materia = input("Nombre de la materia: ").strip()
            try:
                calificacion = float(input("Calificación (0-100): "))
                gestor.registrar_calificacion(cedula, materia, calificacion)
            except ValueError:
                print("✗ Calificación inválida. Debe ser un número.")
        
        elif opcion == "4":
            cedula = input("Cédula del estudiante: ").strip()
            gestor.generar_reporte_estudiante(cedula)
        
        elif opcion == "5":
            gestor.listar_estudiantes()
        
        elif opcion == "6":
            gestor.exportar_reporte_csv()
        
        elif opcion == "7":
            print("\n✓ Hasta luego!")
            break
        
        else:
            print("✗ Opción inválida. Intenta de nuevo.")


if __name__ == "__main__":
    main()
