def calculer_score(data: dict) -> tuple[int, str]:
    t_map = {"automobile": 10, "habitation": 15, "responsabilité civile": 20}
    T = t_map.get(data['type_sinistre'], 0)

    m = data['montant_estime_euros']
    M = 0 if m < 500 else 10 if m < 2000 else 20 if m < 5000 else 35

    a = data['anciennete_contrat_mois']
    A = 20 if a < 6 else 10 if a < 24 else 0

    s = data['nombre_sinistres_anterieurs']
    S = 0 if s == 0 else 10 if s == 1 else 20 if s == 2 else 30

    g = data['age_assure']
    G = 10 if g < 25 else 5 if g > 70 else 0

    score = min(100, max(0, T + M + A + S + G))
    
    if score < 35:
        decision = "Accepté"
    elif score <= 69:
        decision = "Analyse requise"
    else:
        decision = "Bloqué"
        
    return score, decision