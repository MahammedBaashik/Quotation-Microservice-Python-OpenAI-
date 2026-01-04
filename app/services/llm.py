def generate_email(client_name, currency, total, delivery_terms, notes, lang):
    if lang == "ar":
        return f"""
عزيزي {client_name}،

يسعدنا تزويدكم بعرض السعر.
إجمالي العرض: {total} {currency}
شروط التسليم: {delivery_terms}

ملاحظات: {notes or "—"}

مع التحية،
Alrouf Lighting
"""
    return f"""
Dear {client_name},

Please find our quotation below.
Total Amount: {total} {currency}
Delivery Terms: {delivery_terms}

Notes: {notes or "—"}

Best regards,
Alrouf Lighting
"""
