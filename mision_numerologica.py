"""
Calculadora de Misión según Numerología Pitagórica
Muestra un número grande (1-9) y su significado.
Cumple con el desafío I/O 2026: "número grande entre 1 y 10"
"""

import sys
from datetime import datetime

# --------------------------------------------
# Significados de los números (1 al 9)
# --------------------------------------------
SIGNIFICADOS = {
    1: "🌟 MISIÓN 1: EL INICIADOR. Liderazgo, Independencia y Fuerza Creativa. Viniste a abrir caminos, inspirar a otros y manifestar ideas originales. Tu reto: confiar en tu intuición y actuar con valentía.",
    2: "🕊️ MISIÓN 2: EL PACIFICADOR. Cooperación, Diplomacia y Equilibrio. Tu propósito es construir puentes, fomentar la armonía y apoyar a los demás. Aprendes a escuchar, sanar y crear paz.",
    3: "🎨 MISIÓN 3: EL COMUNICADOR. Creatividad, Expresión y Alegría. Viniste a iluminar con tu voz, arte u optimismo. Enseñas a través de la celebración y la comunicación auténtica.",
    4: "🏛️ MISIÓN 4: EL CONSTRUCTOR. Estructura, Orden y Perseverancia. Tu alma anhela construir bases sólidas para la humanidad. Honradez, trabajo en equipo y legado duradero.",
    5: "🦋 MISIÓN 5: EL EXPLORADOR. Libertad, Aventura y Transformación. Viniste a experimentar cambios, expandir horizontes y abrazar la evolución constante. Maestría: adaptarte con sabiduría.",
    6: "❤️ MISIÓN 6: EL SANADOR. Responsabilidad, Amor Incondicional y Servicio. Tu misión es nutrir, proteger y restaurar la armonía familiar y comunitaria. Eres sostén y compasión.",
    7: "🔍 MISIÓN 7: EL SABIO. Análisis, Introspección y Conocimiento Esotérico. Viniste a buscar la verdad, estudiar los misterios y compartir perspectivas profundas. Discernimiento y espiritualidad.",
    8: "⚡ MISIÓN 8: EL MAESTRO MANIFESTADOR. Abundancia, Poder y logros Materiales. Tu propósito es materializar sueños y liderar con integridad. Aprendes equilibrio entre éxito y generosidad.",
    9: "🌍 MISIÓN 9: EL HUMANITARIO. Compasión Universal, Sabiduría y Culminación. Viniste a cerrar ciclos, perdonar y servir a la humanidad. Tu legado: expandir amor y conciencia global."
}

# --------------------------------------------
# Funciones de numerología
# --------------------------------------------
def reducir_a_digito(n: int) -> int:
    """Reduce un número a un dígito (1-9) sumando sus dígitos repetidamente."""
    if n == 0:
        return 0
    while n >= 10:
        suma = sum(int(d) for d in str(n))
        n = suma
    return n

def calcular_numero_mision(dia: int, mes: int, anio: int) -> int:
    """
    Calcula el número de misión según la numerología pitagórica.
    Suma todos los dígitos de la fecha (ddmmaaaa) y reduce hasta 1-9.
    """
    # Concatenar dígitos: día, mes, año como cadena
    fecha_str = f"{dia}{mes}{anio}"
    suma_total = sum(int(caracter) for caracter in fecha_str)
    return reducir_a_digito(suma_total)

def obtener_fecha_usuario():
    """Pide la fecha al usuario y la valida."""
    print("\n📅  CALCULADORA DE MISIÓN PITAGÓRICA  📅")
    print("Ingresa tu fecha de nacimiento.\n")
    
    while True:
        try:
            dia = int(input("  Día (1-31): "))
            mes = int(input("  Mes (1-12): "))
            anio = int(input("  Año (4 dígitos, ej: 1959): "))
            
            # Validar que sea una fecha real
            datetime(anio, mes, dia)
            return dia, mes, anio
        except ValueError:
            print("  ❌ Fecha inválida. Intenta de nuevo.\n")

# --------------------------------------------
# Mostrar número GIGANTE en ASCII (sin librerías externas)
# --------------------------------------------
def mostrar_numero_gigante(n: int):
    """Imprime el número en tamaño grande usando caracteres ASCII."""
    # Definimos dígitos del 0 al 9 en arte ASCII (5 líneas de alto)
    # Solo necesitamos 1-9, pero incluyo 0 por si acaso.
    ascii_digits = {
        0: [
            " █████ ",
            "██   ██",
            "██   ██",
            "██   ██",
            " █████ "
        ],
        1: [
            "   ██  ",
            "  ███  ",
            "   ██  ",
            "   ██  ",
            "  ████ "
        ],
        2: [
            " █████ ",
            "     ██",
            " █████ ",
            "██     ",
            " █████ "
        ],
        3: [
            " █████ ",
            "     ██",
            "  ███  ",
            "     ██",
            " █████ "
        ],
        4: [
            "██   ██",
            "██   ██",
            " █████ ",
            "     ██",
            "     ██"
        ],
        5: [
            " █████ ",
            "██     ",
            " █████ ",
            "     ██",
            " █████ "
        ],
        6: [
            " █████ ",
            "██     ",
            " █████ ",
            "██   ██",
            " █████ "
        ],
        7: [
            " █████ ",
            "     ██",
            "    ██ ",
            "   ██  ",
            "  ██   "
        ],
        8: [
            " █████ ",
            "██   ██",
            " █████ ",
            "██   ██",
            " █████ "
        ],
        9: [
            " █████ ",
            "██   ██",
            " █████ ",
            "     ██",
            " █████ "
        ]
    }
    
    digit_str = str(n)
    # Preparar 5 líneas de salida
    lines = ["" for _ in range(5)]
    for ch in digit_str:
        digit = int(ch)
        for i in range(5):
            lines[i] += ascii_digits[digit][i] + "  "
    
    # Imprimir con borde decorativo
    print("\n" + "=" * 50)
    for line in lines:
        print(line)
    print("=" * 50 + "\n")

# --------------------------------------------
# Programa principal
# --------------------------------------------
def main():
    dia, mes, anio = obtener_fecha_usuario()
    numero = calcular_numero_mision(dia, mes, anio)
    
    # Mostrar resultado
    print("\n✨ ¡TU NÚMERO DE MISIÓN ES...! ✨")
    mostrar_numero_gigante(numero)
    
    print(f"🔢 Número reducido: {numero}")
    print("\n📖 SIGNIFICADO:")
    print(SIGNIFICADOS.get(numero, "No hay definición para este número."))
    print("\n" + "💫" * 20)
    print("Este es tu propósito de vida según la numerología pitagórica.\n")

if __name__ == "__main__":
    main()