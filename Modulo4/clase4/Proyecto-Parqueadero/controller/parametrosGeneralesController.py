from controller.cargarDatos import CargarDatos
from controller.respuestasApiController import RespuestasApiController

class ParametrosGeneralesController():
  def __init__(self):
    self.cargar_datos = CargarDatos()
    self.respuesta = RespuestasApiController()     
    self.df_parametros_generales = self.cargar_datos.get_df_parametros_generales()
  
  def buscar_parametro(self,llave):
    try:
      if llave in self.df_parametros_generales['llave'].values:    
        valor = self.df_parametros_generales.loc[self.df_parametros_generales['llave'] == llave,'valor'].values[0]
        return self.respuesta.get_respuesta("200","",valor)
      
      return self.respuesta.get_respuesta("400",f"Parametro {llave}, no registrado en sistema. Consulte con el administrador del sistema.","")
    except Exception as e:
      return self.respuesta.get_respuesta("500",f"Error interno del servidor (buscar_parametro). {e}.","")
    
  def actualizar_parametro(self,llave,valor):
    try:
      resultado = self.buscar_parametro(llave)
      if resultado['estado'] == '200':
        #self.df_parametros_generales = self.df_parametros_generales.loc[self.df_parametros_generales['llave'] == llave, 'valor'] = valor
        #self.cargar_datos.guardar_df_parametros_generales(self.df_parametros_generales)
        self.df_parametros_generales.loc[self.df_parametros_generales['llave'] == llave, 'valor'] = valor
        self.cargar_datos.guardar_df_parametros_generales(self.df_parametros_generales)


        return self.respuesta.get_respuesta("200","Parametro actualizado con éxito",valor)
      
      return resultado
    except Exception as e:
      return self.respuesta.get_respuesta("500",f"Error interno del servidor (actualizar_parametro). {e}.","")
  