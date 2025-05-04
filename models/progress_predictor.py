from datetime import datetime, timedelta

def estimate_goal_date(current_weight, target_weight, maintenance_cal, ideal_cal):
    # Total calories needed to lose or gain the weight (1 kg ≈ 7700 kcal)
    weight_change = target_weight - current_weight
    total_kcal_change = abs(weight_change) * 7700

    # Daily difference in calorie intake
    daily_diff = abs(maintenance_cal - ideal_cal)

    if daily_diff == 0:
        return "You are maintaining your weight — no change expected."

    days_needed = total_kcal_change / daily_diff
    target_date = datetime.today() + timedelta(days=int(days_needed))

    return target_date.strftime("%B %d, %Y")
