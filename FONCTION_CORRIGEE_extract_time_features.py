# ======================================================================
# FONCTION CORRIGÉE : extract_time_features
# ======================================================================
# Remplacez le contenu de la cellule 42 par ce code :

def extract_time_features(in_time_df, out_time_df):
    """
    Extrait des features à partir des horaires d'arrivée et de départ
    
    Features créées:
    - AvgDailyHours: Heures de travail moyennes par jour
    - HoursVariance: Variance des heures de travail
    - AvgArrivalTime: Heure moyenne d'arrivée
    - AvgDepartureTime: Heure moyenne de départ
    - LateArrivals: Nombre d'arrivées tardives (après 9h30)
    - EarlyDepartures: Nombre de départs précoces (avant 17h)
    - WorkdaysPresent: Nombre de jours travaillés
    """
    
    features = []
    
    # Détecter automatiquement le nom de la colonne ID (première colonne)
    id_col_name = in_time_df.columns[0]
    print(f"📋 Colonne ID détectée: '{id_col_name}'")
    
    # Colonnes de dates (toutes sauf la première)
    date_cols = in_time_df.columns[1:]
    print(f"📅 Nombre de dates à analyser: {len(date_cols)}")
    
    # Itérer sur chaque employé
    for idx in range(len(in_time_df)):
        # Récupérer l'ID employé
        employee_id = in_time_df.iloc[idx, 0]  # Première colonne = ID
        
        # Récupérer les données de l'employé (toutes les colonnes sauf la première)
        in_times = in_time_df.iloc[idx, 1:].values
        out_times = out_time_df.iloc[idx, 1:].values
        
        # Initialisation
        daily_hours = []
        arrival_times = []
        departure_times = []
        late_arrivals = 0
        early_departures = 0
        workdays = 0
        
        for in_t, out_t in zip(in_times, out_times):
            # Vérifier si les valeurs existent (pas NaN ou NaT)
            if pd.notna(in_t) and pd.notna(out_t):
                try:
                    # Convertir en datetime
                    in_dt = pd.to_datetime(in_t, errors='coerce')
                    out_dt = pd.to_datetime(out_t, errors='coerce')
                    
                    if pd.notna(in_dt) and pd.notna(out_dt):
                        # Calculer les heures travaillées
                        hours_worked = (out_dt - in_dt).total_seconds() / 3600
                        
                        if 0 < hours_worked < 24:  # Validation
                            daily_hours.append(hours_worked)
                            workdays += 1
                            
                            # Heure d'arrivée et de départ
                            arrival_hour = in_dt.hour + in_dt.minute / 60
                            departure_hour = out_dt.hour + out_dt.minute / 60
                            
                            arrival_times.append(arrival_hour)
                            departure_times.append(departure_hour)
                            
                            # Comptage des arrivées tardives (après 9h30)
                            if arrival_hour > 9.5:
                                late_arrivals += 1
                            
                            # Comptage des départs précoces (avant 17h)
                            if departure_hour < 17:
                                early_departures += 1
                except:
                    continue
        
        # Calcul des statistiques
        avg_hours = np.mean(daily_hours) if daily_hours else 0
        hours_variance = np.var(daily_hours) if len(daily_hours) > 1 else 0
        avg_arrival = np.mean(arrival_times) if arrival_times else 0
        avg_departure = np.mean(departure_times) if departure_times else 0
        
        # Ajouter les features pour cet employé
        # IMPORTANT: Utiliser 'EmployeeID' comme nom standardisé
        features.append({
            'EmployeeID': employee_id,
            'AvgDailyHours': avg_hours,
            'HoursVariance': hours_variance,
            'AvgArrivalTime': avg_arrival,
            'AvgDepartureTime': avg_departure,
            'LateArrivals': late_arrivals,
            'EarlyDepartures': early_departures,
            'WorkdaysPresent': workdays
        })
    
    print(f"✓ {len(features)} employés traités")
    return pd.DataFrame(features)

print("✓ Fonction d'extraction de features temporelles définie (VERSION CORRIGÉE)")





# =======================================================================================
# =======================================================================================
# =======================================================================================

# Fonction pour extraire les features temporelles
def extract_time_features(in_time_df, out_time_df):
    """
    Extrait des features à partir des horaires d'arrivée et de départ
    
    Features créées:
    - AvgDailyHours: Heures de travail moyennes par jour
    - HoursVariance: Variance des heures de travail
    - AvgArrivalTime: Heure moyenne d'arrivée
    - AvgDepartureTime: Heure moyenne de départ
    - LateArrivals: Nombre d'arrivées tardives (après 9h30)
    - EarlyDepartures: Nombre de départs précoces (avant 17h)
    - WorkdaysPresent: Nombre de jours travaillés
    """
    
    features = []
    
    # Détecter automatiquement le nom de la colonne ID (première colonne)
    id_col_name = in_time_df.columns[0]
    print(f"📋 Colonne ID détectée: '{id_col_name}'")
    
    # Colonnes de dates (toutes sauf la première)
    date_cols = in_time_df.columns[1:]
    print(f"📅 Nombre de dates à analyser: {len(date_cols)}")
    
    for idx, employee_id in enumerate(in_time_df[id_col_name]):
        # Récupérer les données de l'employé
        in_times = in_time_df.iloc[idx, 1:].values
        out_times = out_time_df.iloc[idx, 1:].values
        
        # Initialisation
        daily_hours = []
        arrival_times = []
        departure_times = []
        late_arrivals = 0
        early_departures = 0
        workdays = 0
        
        for in_t, out_t in zip(in_times, out_times):
            # Vérifier si les valeurs existent (pas NaN ou NaT)
            if pd.notna(in_t) and pd.notna(out_t):
                try:
                    # Convertir en datetime
                    in_dt = pd.to_datetime(in_t, errors='coerce')
                    out_dt = pd.to_datetime(out_t, errors='coerce')
                    
                    if pd.notna(in_dt) and pd.notna(out_dt):
                        # Calculer les heures travaillées
                        hours_worked = (out_dt - in_dt).total_seconds() / 3600
                        
                        if 0 < hours_worked < 24:  # Validation
                            daily_hours.append(hours_worked)
                            workdays += 1
                            
                            # Heure d'arrivée et de départ
                            arrival_hour = in_dt.hour + in_dt.minute / 60
                            departure_hour = out_dt.hour + out_dt.minute / 60
                            
                            arrival_times.append(arrival_hour)
                            departure_times.append(departure_hour)
                            
                            # Comptage des arrivées tardives (après 9h30)
                            if arrival_hour > 9.5:
                                late_arrivals += 1
                            
                            # Comptage des départs précoces (avant 17h)
                            if departure_hour < 17:
                                early_departures += 1
                except:
                    continue
        
        # Calcul des statistiques
        avg_hours = np.mean(daily_hours) if daily_hours else 0
        hours_variance = np.var(daily_hours) if len(daily_hours) > 1 else 0
        avg_arrival = np.mean(arrival_times) if arrival_times else 0
        avg_departure = np.mean(departure_times) if departure_times else 0
        
        features.append({
            'EmployeeID': employee_id,
            'AvgDailyHours': avg_hours,
            'HoursVariance': hours_variance,
            'AvgArrivalTime': avg_arrival,
            'AvgDepartureTime': avg_departure,
            'LateArrivals': late_arrivals,
            'EarlyDepartures': early_departures,
            'WorkdaysPresent': workdays
        })
    
    return pd.DataFrame(features)

print("✓ Fonction d'extraction de features temporelles définie")