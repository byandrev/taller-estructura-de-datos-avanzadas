def generar_archivos():
    # Datos de entrada
    n = int(input("Ingrese el número de registros: "))
    operations = []
    heap = set()
    output = []

    for _ in range(n):
        record = input("Ingrese el registro: ").split()
        operations.append(record)

    for record in operations:
        if record[0] == "insert":
            x = int(record[1])
            output.append(record)
            heap.add(x)
        elif record[0] == "getMin":
            x = int(record[1])
            output.append(record)
            if len(heap) == 0 or min(heap) != x:
                output.append(["removeMin"])
                output.append(["insert", str(x)])
                heap.add(x)
        elif record[0] == "removeMin":
            output.append(record)
            if len(heap) == 0:
                output.append(["insert", "1"])
            heap.remove(min(heap))

    # Generar archivo de entrada
    with open("datos_entrada.txt", "w") as archivo_entrada:
        archivo_entrada.write(str(n) + "\n")
        for record in operations:
            archivo_entrada.write(" ".join(record) + "\n")

    # Generar archivo de salida
    with open("datos_salida.txt", "w") as archivo_salida:
        archivo_salida.write(str(len(output)) + "\n")
        for record in output:
            archivo_salida.write(" ".join(record) + "\n")


# Ejecutar la función para generar los archivos
generar_archivos()
