def calculate_lines(items):
    lines = []
    grand_total = 0.0

    for item in items:
        unit_price = item.unit_cost * (1 + item.margin_pct / 100)
        total = unit_price * item.qty
        grand_total += total

        lines.append({
            "sku": item.sku,
            "qty": item.qty,
            "unit_price": round(unit_price, 2),
            "line_total": round(total, 2)
        })

    return lines, round(grand_total, 2)
