
from controller.cargarDatos import CargarDatos
from controller.gestionIngresosController import GestionIngresosController
from controller.parametrosGeneralesController import ParametrosGeneralesController
from controller.respuestasApiController import RespuestasApiController
import pandas as pd
from datetime import datetime
import math
from controller.excepciones import (
    VehiculoYaExisteException,
    VehiculoNoEncontradoException,
    TipoVehiculoInvalidoException,
    ErrorTarifaException,
    ParametroNoEncontradoException
)

class vehiculosController():
  def __init__(self):
    self.cargar_datos = CargarDatos()
    self.parametros_generales = ParametrosGeneralesController()
    self.respuesta = RespuestasApiController()  
    self.df_vehiculos = self.cargar_datos.get_df_vehiculos()
    self.gestion_ingresos = GestionIngresosController()
  
  def grabar_vehiculo(self, placa, tipoVehiculo, fechaIngreso):
    try:      
      if self.df_vehiculos['placa'].str.contains(placa).any():
        raise VehiculoYaExisteException(placa)
      
      llave = 'consecutivoIdVehiculos'
      resultado= self.parametros_generales.buscar_parametro(llave)
      if resultado['estado'] != '200':
        return resultado
      
      id_consecutivo = resultado['valor'] #Obtener el consecutivo          
      #Grabar el registro en el DataSet
      nuevo_vehiculo = pd.DataFrame([{
                    'id': id_consecutivo,
                    'placa': placa.upper(),
                    'tipoVehiculo': tipoVehiculo.upper(),
                    'fechaIngreso': fechaIngreso.strftime("%Y-%m-%d %H:%M:%S"),
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
    
    except VehiculoYaExisteException as e:
      return self.respuesta.get_respuesta('400',str(e),'')
    except Exception as e:
      return self.respuesta.get_respuesta('500',f"Error interno del servidor realizar el ingreso del vehículo. {e}.",'')
  
  def obtener_vehiculos_todos(self):
    return self.df_vehiculos
  
  def obtener_vehiculos_uno(self,placa):
    try:
      if placa not in self.df_vehiculos['placa'].values:
        raise VehiculoNoEncontradoException(placa)      
      
      vehiculo = self.df_vehiculos.loc[self.df_vehiculos['placa'] == placa].iloc[0].to_dict()
      return self.respuesta.get_respuesta("200","",vehiculo)      
    except VehiculoNoEncontradoException as e:
      return self.respuesta.get_respuesta('400',str(e),'')
    except Exception as e:
      return self.respuesta.get_respuesta('500',f"Error interno del servidor (vehiculosController/obtener_vehiculos_uno). {e}.",'')
  
  def existe_vehiculo(self,placa):
    if placa in self.df_vehiculos['placa'].values:
      return True
    return False

  def modificar_vehiculo(self, placa, tipoVehiculo, fechaIngreso):
    try:
      if not self.existe_vehiculo(placa):      
        raise VehiculoNoEncontradoException(placa)(placa)
      
      self.df_vehiculos.loc[self.df_vehiculos['placa'] == placa, 'tipoVehiculo'] = tipoVehiculo
      self.df_vehiculos.loc[self.df_vehiculos['placa'] == placa, 'fechaIngreso'] = fechaIngreso
      self.cargar_datos.guardar_df_vehiculos(self.df_vehiculos)
      return self.respuesta.get_respuesta('200',f"Vehiculo con placas {placa}, actualizado con éxito.",'')
      
    except VehiculoNoEncontradoException(placa) as e:
      return self.respuesta.get_respuesta('400',str(e),'')
    except Exception as e:
      return self.respuesta.get_respuesta("500",f"Error interno del servidor (modificar_vehiculo). {e}.","")

  def eliminar_vehiculo(self, placa):
    try:
      if not self.existe_vehiculo(placa):      
        raise VehiculoNoEncontradoException(placa)
      
      self.df_vehiculos = self.df_vehiculos[self.df_vehiculos['placa'] != placa]
      self.cargar_datos.guardar_df_vehiculos(self.df_vehiculos)
      return self.respuesta.get_respuesta('200',f"Vehiculo con placas {placa}, eliminado con éxito.",'')
    
    except VehiculoNoEncontradoException(placa) as e:
      return self.respuesta.get_respuesta('400',str(e),'')
    except Exception as e:
      return self.respuesta.get_respuesta("500",f"Error interno del servidor (eliminar_vehiculo). {e}.","") 

  def liquidar_vehiculo(self, placa, fecha_salida):    
    try:
      if not self.existe_vehiculo(placa):      
        raise VehiculoNoEncontradoException(placa)        
      
      vehiculo= self.obtener_vehiculos_uno(placa)
      tipo_vehiculo= vehiculo['valor']['tipoVehiculo'].upper()
      if tipo_vehiculo not in['CARRO','MOTO']:
        raise TipoVehiculoInvalidoException(tipo_vehiculo) 
      
      llave = f"valorTarifa{tipo_vehiculo.capitalize()}"
      resultado= self.parametros_generales.buscar_parametro(llave)
      if resultado['estado'] != '200':
        return resultado
      
      valor_tarifa = resultado['valor']   
      fecha_ingreso = datetime.strptime(vehiculo['valor']['fechaIngreso'], "%Y-%m-%d %H:%M:%S")
      fecha_salida  = datetime.strptime(fecha_salida,"%Y-%m-%d %H:%M:%S")
      tiempo_transcurrido = math.ceil(((fecha_salida - fecha_ingreso).total_seconds() / 3600))
      total_pagar = math.ceil(tiempo_transcurrido*valor_tarifa)
      
      resultado= self.eliminar_vehiculo(placa)
      if resultado['estado'] != '200':
        return resultado
      
      resultado= self.gestion_ingresos.grabar_ingreso(placa,tipo_vehiculo,fecha_ingreso,fecha_salida,tiempo_transcurrido,total_pagar)
      if resultado['estado'] != '200':
        return resultado

      return self.respuesta.get_respuesta('200',f"Vehiculo con placas {placa}, liquidado con éxito. Horas totales: {tiempo_transcurrido} / Total cancelado: ${total_pagar:,.0f}",'')
      
        
    except (TipoVehiculoInvalidoException,VehiculoNoEncontradoException,ErrorTarifaException) as e:
      return self.respuesta.get_respuesta('400',str(e),'')
    except Exception as e:
      return self.respuesta.get_respuesta("500",f"Error interno del servidor (liquidar_vehiculo). {e}.","") 