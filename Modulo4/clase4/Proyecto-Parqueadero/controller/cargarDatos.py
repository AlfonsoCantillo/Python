import pandas as pd

class CargarDatos:
  def __init__(self):
    self.df_vehiculos = pd.read_csv('controller/data/vehiculos.csv', sep=';')
    self.df_gestion_ingresos = pd.read_csv('controller/data/gestionIngresos.csv', sep=';')
    self.df_parametros_generales = pd.read_csv('controller/data/parametrosGenerales.csv', sep=';')

  def get_df_vehiculos(self):
    return self.df_vehiculos
  
  def get_df_gestion_ingresos(self):
    return self.df_gestion_ingresos
  
  def get_df_parametros_generales(self):
    return self.df_parametros_generales
  
  def guardar_df_vehiculos(self,df_vehiculos):
    df_vehiculos.to_csv('controller/data/vehiculos.csv',sep=";",index=False)
  
  def guardar_df_gestion_ingresos(self,df_gestion_ingresos):
    df_gestion_ingresos.to_csv('controller/data/gestionIngresos.csv',sep=";",index=False)

  def guardar_df_parametros_generales(self,df_parametros_generales):
    df_parametros_generales.to_csv('controller/data/parametrosGenerales.csv',sep=";",index=False)