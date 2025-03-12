def division_segura(n1,n2):
  try:
    print(f"{n1} / {n2} = {n1/n2}")
  except ZeroDivisionError:
    print("No es posible realizar la división. Divisor debe se diferente de cero")
    return None

division_segura(10,2)