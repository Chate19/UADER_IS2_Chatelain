"""
Análisis Financiero de Proyecto de Software
"""

def calcular_vp_anualidad(cuota: float, tasa: float, periodos: int) -> float:
    """Calcula el valor presente de una serie de pagos uniformes (anualidad vencida)."""
    return cuota * ((1 - (1 + tasa) ** -periodos) / tasa)

def calcular_vp_futuro(monto_futuro: float, tasa: float, periodos: int) -> float:
    """Calcula el valor presente de un monto único a recibir en el futuro."""
    return monto_futuro / ((1 + tasa) ** periodos)

# Variables iniciales del proyecto
tasa_efectiva_mensual = 0.01
costo_mensual = 1000.0

# -------------------------------------------------------------------
# a. VPN si la ejecución ocurre según los planes (12 meses)
# -------------------------------------------------------------------
meses_plan = 12
flujo_esperado_mes_12 = 18000.0

vp_inversion_a = calcular_vp_anualidad(costo_mensual, tasa_efectiva_mensual, meses_plan)
vp_beneficios_a = calcular_vp_futuro(flujo_esperado_mes_12, tasa_efectiva_mensual, meses_plan)
vpn_a = vp_beneficios_a - vp_inversion_a

print(f"a. Valor Presente Neto (12 meses): ${vpn_a:.2f}")

# -------------------------------------------------------------------
# b. VPN si se extiende a 15 meses
# -------------------------------------------------------------------
meses_ext = 15
flujo_esperado_mes_15 = 18000.0

vp_inversion_b = calcular_vp_anualidad(costo_mensual, tasa_efectiva_mensual, meses_ext)
vp_beneficios_b = calcular_vp_futuro(flujo_esperado_mes_15, tasa_efectiva_mensual, meses_ext)
vpn_b = vp_beneficios_b - vp_inversion_b

print(f"b. Valor Presente Neto (15 meses): ${vpn_b:.2f}")

# -------------------------------------------------------------------
# c. Rentabilidad en ambos casos (VPN / VP Inversión)
# -------------------------------------------------------------------
rentabilidad_a = vpn_a / vp_inversion_a
rentabilidad_b = vpn_b / vp_inversion_b

print(f"c. Rentabilidad Caso A (12 meses): {rentabilidad_a:.2%}")
print(f"c. Rentabilidad Caso B (15 meses): {rentabilidad_b:.2%}")

# -------------------------------------------------------------------
# d. Impacto del retraso de 6 meses (total 18 meses)
# -------------------------------------------------------------------
meses_retraso_6 = 18
vp_inversion_d = calcular_vp_anualidad(costo_mensual, tasa_efectiva_mensual, meses_retraso_6)
vp_beneficios_d = calcular_vp_futuro(18000, tasa_efectiva_mensual, meses_retraso_6)
vpn_d = vp_beneficios_d - vp_inversion_d

print(f"d. Valor Presente Neto (18 meses): ${vpn_d:.2f}")

# -------------------------------------------------------------------
# e. Gestión profesional (Costo + 5%, garantiza 12 meses)
# -------------------------------------------------------------------
costo_mensual_profesional = costo_mensual * 1.05
vp_inversion_e = calcular_vp_anualidad(costo_mensual_profesional, tasa_efectiva_mensual, meses_plan)
vpn_e = vp_beneficios_a - vp_inversion_e

print(f"e. Valor Presente Neto (Gestión Profesional): ${vpn_e:.2f}")

# -------------------------------------------------------------------
# f. [Desafío] Costo mensual máximo aceptable para 15 meses manteniendo el VPN_A
# -------------------------------------------------------------------
# Ecuación: VPN_A = VP_Beneficios_15 - VP_Inversion_15_Nueva
vp_inversion_15_maxima = vp_beneficios_b - vpn_a
# Sabiendo que: vp_inversion = cuota_max * factor_anualidad
factor_anualidad_15 = calcular_vp_anualidad(1, tasa_efectiva_mensual, meses_ext)
costo_max_mensual_15 = vp_inversion_15_maxima / factor_anualidad_15

print(f"f. Costo mensual máximo para 15 meses manteniendo VPN de 12 meses: ${costo_max_mensual_15:.2f}")