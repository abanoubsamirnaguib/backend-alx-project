#!/usr/bin/env python
"""
Generate a Django SECRET_KEY for production use.
Run this script to generate a new secure SECRET_KEY.
"""

from django.core.management.utils import get_random_secret_key

if __name__ == "__main__":
    secret_key = get_random_secret_key()
    print("=" * 60)
    print("Django SECRET_KEY Generated")
    print("=" * 60)
    print("\nCopy this key to your environment variables:")
    print("-" * 60)
    print(secret_key)
    print("-" * 60)
    print("\nUse this in:")
    print("- Railway environment variables")
    print("- .env file (for local development)")
    print("- Never commit .env to Git!")
    print("=" * 60)
