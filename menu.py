import logica

def mostrar_menu():
    print("\n" + "="*40)
    print("   TIENDA DE HARDWARE - MENÚ PRINCIPAL   ")
    print("="*40)
    print("1. Ver catálogo de productos")
    print("2. Agregar producto al carrito")
    print("3. Ver detalle del carrito")
    print("4. Ver total a pagar (CLP y USD)")
    print("5. Vaciar carrito")
    print("6. Guardar y Salir")
    print("="*40)

def main():
    print("Iniciando sistema...")
    # Carga de datos persistentes al arrancar
    mi_carrito = logica.cargar_carrito()
    if mi_carrito:
        print("¡Se ha recuperado una sesión de carrito anterior!")
    
    while True:
        mostrar_menu()
        
        try:
            opcion = int(input("Seleccione una opción (1-6): "))
            
            if opcion == 1:
                print("\n--- CATÁLOGO DISPONIBLE ---")
                catalogo = logica.obtener_catalogo()
                # Uso de bucle for obligatorio para mostrar datos
                for prod in catalogo:
                    print(f"ID: {prod['id']} | {prod['nombre']} | Precio: ${prod['precio']} CLP")
                    
            elif opcion == 2:
                try:
                    id_ingresado = int(input("Ingrese el ID del producto: "))
                    cant_ingresada = int(input("Ingrese la cantidad: "))
                    
                    # Llamada a lógica, atrapando posibles errores
                    logica.agregar_al_carrito(mi_carrito, id_ingresado, cant_ingresada)
                    print(" Producto agregado correctamente al carrito.")
                except ValueError as e:
                    print(f" Error de ingreso: {e} (Asegúrese de ingresar números válidos).")
                except KeyError as e:
                    print(f" Error: {e}")
                    
            elif opcion == 3:
                print("\n--- MI CARRITO ---")
                if not mi_carrito:
                    print("El carrito está vacío.")
                else:
                    # Uso de bucle for obligatorio para iterar el diccionario compuesto
                    for p_id, datos in mi_carrito.items():
                        subtotal = datos['precio'] * datos['cantidad']
                        print(f"- {datos['nombre']} (x{datos['cantidad']}) | Subtotal: ${subtotal} CLP")
                        
            elif opcion == 4:
                if not mi_carrito:
                    print("\nNo hay productos en el carrito para calcular.")
                else:
                    total_clp = logica.calcular_total_clp(mi_carrito)
                    print("\nObteniendo valor del dólar actual...")
                    valor_usd_actual = logica.obtener_valor_dolar()
                    
                    total_usd = total_clp / valor_usd_actual
                    
                    print(f"\n--- TOTAL A PAGAR ---")
                    print(f"Total en Pesos Chilenos: ${total_clp:,} CLP")
                    print(f"Total en Dólares (API):  ${total_usd:.2f} USD")
                    print(f"(Tasa de cambio usada: $1 USD = ${valor_usd_actual} CLP)")
                    
            elif opcion == 5:
                mi_carrito = logica.vaciar_carrito()
                print("\n El carrito ha sido vaciado.")
                
            elif opcion == 6:
                # Persistencia al salir
                logica.guardar_carrito(mi_carrito)
                print("\n Datos guardados exitosamente. ¡Gracias por su visita!")
                break # Rompe el ciclo while, terminando el programa
                
            else:
                print("\n Por favor, seleccione una opción válida entre 1 y 6.")
                
        except ValueError:
            print("\n Error: Entrada inválida. Debe ingresar un número.")

if __name__ == "__main__":
    main()