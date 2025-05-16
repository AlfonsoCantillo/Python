
from controller.cargarDatos import CargarDatos
from controller.respuestasApiController import RespuestasApiController
import pandas as pd

class GestionIngresosController:
  def __init__(self):
    self.cargar_datos = CargarDatos()
    self.respuesta = RespuestasApiController()  
    self.df_gestion_ingresos = self.cargar_datos.get_df_gestion_ingresos()
  
  def grabar_ingreso(self,placa,tipoVehiculo,fechaIngreso,fechaSalida,horas,totalPagar):
    try:
      nuevo_ingreso = pd.DataFrame([{
        'placa': placa,
        'tipoVehiculo': tipoVehiculo,
        'fechaIngreso': fechaIngreso,
        'fechaSalida': fechaSalida,
        'horas': horas,
        'totalPagar': totalPagar
      }])

      # Concatenar (o asignar si está vacío)
      if self.df_gestion_ingresos.empty:
          self.df_gestion_ingresos = nuevo_ingreso
      else:
          self.df_gestion_ingresos = pd.concat([self.df_gestion_ingresos, nuevo_ingreso], ignore_index=True)
      
      self.cargar_datos.guardar_df_gestion_ingresos(self.df_gestion_ingresos)      
      return self.respuesta.get_respuesta('200',f"Ingreso registrado con exito.",'')
    except Exception as e:
       return self.respuesta.get_respuesta('500',f"Error interno del servidor (GestionIngresosController/grabar_ingreso). {e}.",'')