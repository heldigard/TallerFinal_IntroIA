import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

reparaciones = ctrl.Antecedent(np.array([2, 5, 6, 8, 10, 11, 13, 15, 18, 20]), 'reparaciones')
monto_reparacion = ctrl.Antecedent(np.array([750, 1235, 2427, 3625, 4500, 8105, 12300, 20125, 32250]), 'monto_reparacion')
calificacion = ctrl.Antecedent(np.array([15,19,23,42,55,59,53,81,85]), 'calificacion')

valores_prima = np.linspace(1700, 6200, 10)
print(valores_prima)

prima = ctrl.Consequent(np.array(valores_prima), 'prima')
print(prima.universe)
reparaciones.automf(number=3, names=['bajas', 'medias', 'altas'])
monto_reparacion.automf(number=3, names=['bajo', 'medio', 'alto'])
calificacion.automf(number=3, names=['baja', 'media', 'alta'])

prima['baja']=fuzz.trimf(prima.universe,[1700,1700,3950])
prima['media']=fuzz.trimf(prima.universe,[1700,3950,6200])
prima['alta']=fuzz.trimf(prima.universe,[3950,6200,6200])
prima.view()

#reparaciones.view()
#monto_reparacion.view()

rule1=ctrl.Rule(reparaciones['altas'] | monto_reparacion['alto'] & calificacion['alta'],prima['baja'])
rule2=ctrl.Rule(reparaciones['medias'] | monto_reparacion['medio'] & calificacion['alta'],prima['baja'])
rule3=ctrl.Rule(reparaciones['bajas'] | monto_reparacion['bajo'] & calificacion['baja'],prima['media'])
rule4=ctrl.Rule(reparaciones['medias'] | monto_reparacion['medio'] & calificacion['media'],prima['media'])
rule5=ctrl.Rule(reparaciones['altas'] | monto_reparacion['alto'] & calificacion['baja'],prima['alta'])
rule6=ctrl.Rule(reparaciones['altas'] | monto_reparacion['alto'] & calificacion['media'],prima['alta'])

control_system=ctrl.ControlSystem([rule3,rule2,rule1,rule4,rule5,rule6])
fuzzy_system=ctrl.ControlSystemSimulation(control_system)
fuzzy_system.input['reparaciones']=1
fuzzy_system.input['monto_reparacion']=1
fuzzy_system.input['calificacion']=1
fuzzy_system.compute()
print(fuzzy_system.output['prima'])
prima.view(sim=fuzzy_system)

#pip install scikit-fuzzy
#pip install matplotlib
#pip install mpld3

#CON GAUSS

