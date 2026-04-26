from libro import Libro
from estudiante import Estudiante
from biblioteca import Biblioteca

def main():
    print("==============================================")
    print(" SISTEMA DE GESTIÓN DE BIBLIOTECA UNEMI")
    print("==============================================")

    print("\nIntegrantes del grupo:")
    print("Andres Jesús Reyes Ayala")
    print("Marcos David Medina Lopez")
    print("Javier Israel Rodriguez Meza")
    print("Roddy Antonio Marcos Franco")
    print("Benjamin Jose Cabrera Yepe")

    biblioteca = Biblioteca("Biblioteca Grupo UNEMI")

    libro1 = Libro("001", "Interestelar", "Christopher Nolan")
    libro2 = Libro("002", "Hábitos Atómicos", "James Clear")
    libro3 = Libro("003", "Padre Rico Padre Pobre", "Robert Kiyosaki")

    biblioteca.registrar_libro(libro1)
    biblioteca.registrar_libro(libro2)
    biblioteca.registrar_libro(libro3)

    estudiante1 = Estudiante("0926400615", "Marcos David", "Medina Lopez", "Ingeniería en Sistemas")
    estudiante2 = Estudiante("0911111111", "Andres Jesús", "Reyes Ayala", "Ingeniería en Sistemas")

    biblioteca.registrar_estudiante(estudiante1)
    biblioteca.registrar_estudiante(estudiante2)

    print(biblioteca.prestar_libro("001", "0926400615", "26/04/2026", "03/05/2026"))
    print(biblioteca.prestar_libro("002", "0911111111", "26/04/2026", "03/05/2026"))

    print(biblioteca.devolver_libro("001", "0926400615"))

    
   #print(biblioteca.prestar_libro("001", "0911111111", "26/04/2026", "03/05/2026")) LIBRO NO ENCONTRADO 
   #print(biblioteca.devolver_libro("001", "0926400615")) DEVOLVER LIBRO 
 



if __name__ == "__main__":
    main()