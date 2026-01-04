from fastapi import FastAPI
from app.models import QuoteRequest
from app.services.pricing import calculate_lines
from app.services.llm import generate_email

app = FastAPI(title="Quotation Microservice")

@app.post("/quote")
def create_quote(payload: QuoteRequest):
    lines, total = calculate_lines(payload.items)

    email = generate_email(
        client_name=payload.client.name,
        currency=payload.currency,
        total=total,
        delivery_terms=payload.delivery_terms,
        notes=payload.notes,
        lang=payload.client.lang
    )

    return {
        "client": payload.client.name,
        "currency": payload.currency,
        "lines": lines,
        "grand_total": total,
        "email_draft": email.strip()
    }
