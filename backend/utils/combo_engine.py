def suggest_combos(recognized):
    combos = []
    names = [a["name"] for a in recognized]

    # Example logic
    if "Chronosphere" in names and "Macropyre" in names:
        combos.append({
            "combo": ["Chronosphere", "Macropyre"],
            "synergy": "High AoE damage"
        })

    if "Laguna Blade" in names and "Magic Missile" in names:
        combos.append({
            "combo": ["Magic Missile", "Laguna Blade"],
            "synergy": "Single-target burst"
        })

    if "Ravage" in names and "Electric Vortex" in names:
        combos.append({
            "combo": ["Ravage", "Electric Vortex"],
            "synergy": "AOE Stun"
        })
    
    if "Dream Coil" in names and "Poison Attack" in names:
        combos.append({
            "combo": ["Dream Coil", "Poison Attack"],
            "synergy": "AOE DMG"
        })
        
    if "Dream Coil" in names and "Shadow Realm" in names:
        combos.append({
            "combo": ["Dream Coil", "Shadow Realm"],
            "synergy": "AOE DMG"
        })

    if "Dream Coil" in names and "Flak Cannon" in names:
        combos.append({
            "combo": ["Dream Coil", "Flak Cannon"],
            "synergy": "AOE DMG"
        })

    return combos
