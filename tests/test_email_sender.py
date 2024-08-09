import sys
import os
import pytest
import pytest_asyncio

from app.email_sender import send_email


@pytest.mark.asyncio
async def test_send_email():
    response = await send_email("test@example.com", "recipient@example.com", "Test Subject", "Test Body")
    assert response == "Email sent successfully"
