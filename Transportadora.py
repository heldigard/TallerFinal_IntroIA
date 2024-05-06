class Transportadora:
    def __init__(self):
        # Datos de las tiendas
        self.tiendas = {
            '1': {'ventas': 1200, 'precio_unitario': 15000, 'distancia': 1500, 'costo': 400},
            '2': {'ventas': 2300, 'precio_unitario': 18000, 'distancia': 2500, 'costo': 600},
            '3': {'ventas': 700, 'precio_unitario': 17000, 'distancia': 800, 'costo': 1200},
            '4': {'ventas': 1800, 'precio_unitario': 12000, 'distancia': 1600, 'costo': 500},
            '5': {'ventas': 2000, 'precio_unitario': 16000, 'distancia': 300, 'costo': 300},
        }

    # Función de utilidad
    def utilidad(self, individuo):
        utilidad_total = 0
        distancia_total = 0

        for i in range(len(individuo)):
            if individuo[i] == 1:
                tienda = self.tiendas[str(i + 1)]
                utilidad_total += (
                        (tienda['precio_unitario'] * tienda['ventas']) -
                        (tienda['distancia'] * tienda['costo'])
                )
                distancia_total += tienda['distancia']

        if distancia_total > 4000:
            return 0

        return utilidad_total
