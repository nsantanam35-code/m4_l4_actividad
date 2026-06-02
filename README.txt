=========================================================
PROYECTO: Sistema Educacional (POO)
=========================================================

DESCRIPCIÓN DEL PROYECTO
------------------------
Este proyecto tiene como objetivo modelar un sistema de gestión educacional 
utilizando el Paradigma Orientado a Objetos (POO) en Python. El sistema 
permite la creación de personas (Estudiantes y Profesores) y la gestión de 
cursos, facilitando la interacción entre entidades académicas.

CONCEPTOS DE POO APLICADOS
--------------------------
1. HERENCIA: Las clases 'Estudiante' y 'Profesor' heredan atributos y 
   comportamientos de la clase base 'Persona'.
   
2. POLIMORFISMO: Implementado en el método 'presentarse()', donde cada 
   clase hija (Estudiante y Profesor) sobrescribe el comportamiento para 
   ofrecer una respuesta específica según su rol.

3. SOBRECARGA DE MÉTODOS: Implementada en el método 'asignar_nota' de la clase 
   'Profesor', utilizando parámetros opcionales para permitir diferentes 
   firmas de llamado (con o sin comentario).

4. INTERACCIÓN ENTRE OBJETOS: El sistema demuestra la colaboración entre 
   instancias, permitiendo que un objeto 'Curso' gestione listas de objetos 
   'Estudiante' y asigne un 'Profesor' a su cargo.

ESTRUCTURA DE ARCHIVOS
----------------------
- main.py: Código fuente principal que contiene las definiciones de clase 
           y la ejecución de la lógica de interacción.
- README.TXT: Este archivo de documentación.

INSTRUCCIONES DE EJECUCIÓN
--------------------------
1. Asegúrese de tener instalado Python 3 en su terminal.
2. Navegue al directorio del proyecto: 
   cd poo_sistema_educacional
3. Ejecute el programa con el siguiente comando:
   python3 main.py


