
from controller.cargarDatos import CargarDatos
from controller.parametrosGeneralesController import ParametrosGeneralesController
from controller.respuestasApiController import RespuestasApiController
import pandas as pd

class vehiculosController():
  def __init__(self):
    self.cargar_datos = CargarDatos()
    self.parametros_generales = ParametrosGeneralesController()
    self.respuesta = RespuestasApiController()  
    self.df_vehiculos = self.cargar_datos.get_df_vehiculos()
    self.df_gestion_ingresos = self.cargar_datos.get_df_gestion_ingresos()
  
  def grabar_vehiculo(self, placa, tipoVehiculo, fechaIngreso):
    try:      
      if self.df_vehiculos.empty or not self.df_vehiculos['placa'].str.contains(placa).any():
        llave = 'consecutivoIdVehiculos'
        resultado= self.parametros_generales.buscar_parametro(llave)
        if resultado['estado'] == '200':
          id_consecutivo = resultado['valor'] #Obtener el consecutivo          
          #Grabar el registro en el DataSet
          nuevo_vehiculo = pd.DataFrame([{
                        'id': id_consecutivo,
                        'placa': placa,
                        'tipoVehiculo': tipoVehiculo,
                        'fechaIngreso': fechaIngreso,
                        'estado': True
                    }])          
          # Concatenar (o asignar si está vacío)
          if self.df_vehiculos.empty:
              self.df_vehiculos = nuevo_vehiculo
          else:
              self.df_vehiculos = pd.concat([self.df_vehiculos, nuevo_vehiculo], ignore_index=True)
          
          self.cargar_datos.guardar_df_vehiculos(self.df_vehiculos)
          self.parametros_generales.actualizar_parametro(llave,(id_consecutivo+1))
          return self.respuesta.get_respuesta('200',f"Vehiculo con placas {placa}, ingresado al parqueadero.",'')
        else:
          return resultado
      else:
        return self.respuesta.get_respuesta('400',f"El vehículo con placa {placa}, ya se encuentra al interior del parqueadero.",'')
    except Exception as e:
      return self.respuesta.get_respuesta('500',f"Error interno del servidor realizar el ingreso del vehículo. {e}.",'')
  
  def obtener_vehiculos_todos(self):
    return self.df_vehiculos
  
  def obtener_vehiculos_uno(self,placa):
    if placa in self.df_vehiculos['placa'].values:
      return True
    return False

  def modificar_vehiculo(self, placa, tipoVehiculo, fechaIngreso):
    try:
      if self.obtener_vehiculos_uno(placa):      
        self.df_vehiculos.loc[self.df_vehiculos['placa'] == placa, 'tipoVehiculo'] = tipoVehiculo
        self.df_vehiculos.loc[self.df_vehiculos['placa'] == placa, 'fechaIngreso'] = fechaIngreso
        self.cargar_datos.guardar_df_vehiculos(self.df_vehiculos)
        return self.respuesta.get_respuesta('200',f"Vehiculo con placas {placa}, actualizado con éxito.",'')
      else:
        return self.respuesta.get_respuesta('400',f"El vehículo con placa {placa}, no se encuentra al interior del parqueadero.",'')      
    except Exception as e:
      return self.respuesta.get_respuesta("500",f"Error interno del servidor (modificar_vehiculo). {e}.","")

  def eliminar_vehiculo(self, placa):
    try:
      if self.obtener_vehiculos_uno(placa):      
        self.df_vehiculos = self.df_vehiculos[self.df_vehiculos['placa'] != placa]
        self.cargar_datos.guardar_df_vehiculos(self.df_vehiculos)
        return self.respuesta.get_respuesta('200',f"Vehiculo con placas {placa}, eliminado con éxito.",'')
      else:
        return self.respuesta.get_respuesta('400',f"El vehículo con placa {placa}, no se encuentra al interior del parqueadero.",'')      
    except Exception as e:
      return self.respuesta.get_respuesta("500",f"Error interno del servidor (eliminar_vehiculo). {e}.","")    
