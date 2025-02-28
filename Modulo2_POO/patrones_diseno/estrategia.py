# 1. Estrategia abstracta
class MetodoPago:
    def pagar(self, monto):
        pass
# 2. Estrategias concretas
class PagoConTarjeta(MetodoPago):
    def pagar(self, monto):
        print(f"Pagando ${monto} con tarjeta de crédito.")
class PagoConPaypal(MetodoPago):
    def pagar(self, monto):
        print(f"Pagando ${monto} con PayPal.")
# 3. Contexto
class Pedido:
    def __init__(self, monto, metodo_pago: MetodoPago):
        self.monto = monto
        self.metodo_pago = metodo_pago
    
    def realizar_pago(self):
        self.metodo_pago.pagar(self.monto)
    
    def cambiar_metodo_pago(self, nuevo_metodo_pago: MetodoPago):
        self.metodo_pago = nuevo_metodo_pago
        print("Método de pago cambiado.")

# Uso del patrón Strategy con cambio dinámico de estrategia
# Crear métodos de pago
pago_con_tarjeta = PagoConTarjeta()
pago_con_paypal = PagoConPaypal()
# Crear un pedido con un método de pago inicial
pedido1 = Pedido(100, pago_con_tarjeta)
# Realizar el pago con el primer método
pedido1.realizar_pago()  # Pago con tarjeta
# Cambiar el método de pago en tiempo de ejecución
pedido1.cambiar_metodo_pago(pago_con_paypal)
# Realizar el pago con el nuevo método
pedido1.realizar_pago()  # Pago con PayPal