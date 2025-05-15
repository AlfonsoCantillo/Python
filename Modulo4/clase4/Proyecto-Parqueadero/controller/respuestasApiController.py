
class RespuestasApiController():
  def __init__(self):
    pass

  def get_respuesta(self,estado,mensaje,valor):
    respuesta = {
      'estado' : estado,
      'mensaje': mensaje,
      'valor'  : valor
    }
    return respuesta