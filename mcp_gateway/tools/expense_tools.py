import os
from typing import Optional

import httpx
from dotenv import load_dotenv


load_dotenv()

EXPENSE_API_BASE_URL = os.getenv("EXPENSE_API_BASE_URL")

if not EXPENSE_API_BASE_URL:
    raise ValueError("EXPENSE_API_BASE_URL environment variable is not configured")

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("API_KEY environment variable is not configured")

HEADERS = {"X-API-Key": API_KEY}


def record_expense(
    user_id: str,
    amount: float,
    category: str,
    description: str | None,
    expense_date: str,
) -> dict:
    payload = {
        "user_id": user_id,
        "amount": amount,
        "category": category,
        "description": description,
        "expense_date": expense_date,
    }

    with httpx.Client(base_url=EXPENSE_API_BASE_URL, timeout=10.0) as client:
        response = client.post("/expenses", json=payload,headers=HEADERS)

    _raise_api_error(response)

    return response.json()


def fetch_expenses(
    user_id: str,
    categories: Optional[list[str]] = None,
) -> list[dict]:
    params = {}

    if categories:
        params["categories"] = categories

    with httpx.Client(base_url=EXPENSE_API_BASE_URL, timeout=10.0) as client:
        response = client.get(
            f"/users/{user_id}/expenses",
            params=params,headers=HEADERS
        )

    _raise_api_error(response)

    return response.json()


def fetch_expense_summary(user_id: str) -> dict:
    with httpx.Client(base_url=EXPENSE_API_BASE_URL, timeout=10.0) as client:
        response = client.get(
            f"/users/{user_id}/expenses/summary",headers=HEADERS
        )

    _raise_api_error(response)

    return response.json()


def remove_expenses(
    user_id: str,
    expense_ids: list[int],
) -> dict:
    payload = {
        "expense_ids": expense_ids,
    }

    with httpx.Client(base_url=EXPENSE_API_BASE_URL, timeout=10.0) as client:
        response = client.request(
            "DELETE",
            f"/users/{user_id}/expenses",
            json=payload,headers=HEADERS
        )

    _raise_api_error(response)

    return response.json()


def _raise_api_error(response: httpx.Response) -> None:
    if response.is_success:
        return

    try:
        detail = response.json().get("detail", response.text)
    except ValueError:
        detail = response.text

    raise ValueError(
        f"Expense API request failed with status "
        f"{response.status_code}: {detail}"
    )
