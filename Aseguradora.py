import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

reparaciones = ctrl.Antecedent(np.array([2, 5, 6, 8, 10, 11, 13, 15, 18, 20]), 'reparaciones')
monto_reparacion = ctrl.Antecedent(np.array([750, 1235, 2427, 3625, 4500, 8105, 12300, 20125, 32250]), 'monto_reparacion')
calificacion = ctrl.Antecedent(np.array([15,19,23,42,55,59,53,81,85]), 'calificacion')

print(calificacion.universe)

propina = ctrl.Consequent(np.arange(0, 21), 'propina')
reparaciones.automf(number=3, names=['bajas', 'medias', 'altas'])
monto_reparacion.automf(number=3, names=['bajo', 'medio', 'alto'])
calificacion.automf(number=3, names=['baja', 'media', 'alta'])

print(calificacion.view())

#pip install matplotlib
#pip install mpld3
