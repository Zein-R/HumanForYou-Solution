# ======================================================================
# SOLUTION TEMPORAIRE POUR LA CELLULE 30
# ======================================================================
# Remplacez le contenu de la cellule 30 par ce code :

# Visualisation: Taux d'attrition par BusinessTravel
if 'BusinessTravel' in df.columns:
    travel_attrition = calculate_attrition_rate(df, 'BusinessTravel')
    
    # Essayer d'abord avec Plotly (graphique interactif)
    try:
        fig = px.bar(x=travel_attrition.index, y=travel_attrition.values,
                     labels={'x': 'Type de déplacement professionnel', 'y': 'Taux d\'attrition (%)'},
                     title='Taux d\'Attrition par Type de Déplacement Professionnel',
                     color=travel_attrition.values,
                     color_continuous_scale='Reds')
        fig.update_layout(showlegend=False, height=400)
        fig.show()
    except Exception as e:
        # Alternative avec matplotlib (graphique statique)
        print("⚠️ Plotly non disponible, utilisation de matplotlib")
        plt.figure(figsize=(10, 6))
        colors = plt.cm.Reds(travel_attrition.values / travel_attrition.values.max())
        plt.bar(travel_attrition.index, travel_attrition.values, color=colors)
        plt.xlabel('Type de déplacement professionnel', fontsize=12)
        plt.ylabel('Taux d\'attrition (%)', fontsize=12)
        plt.title('Taux d\'Attrition par Type de Déplacement Professionnel', fontsize=14, fontweight='bold')
        plt.xticks(rotation=15)
        plt.grid(axis='y', alpha=0.3)
        plt.tight_layout()
        plt.show()
