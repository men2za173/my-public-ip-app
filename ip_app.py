"""
My Public IP App
Fetches and displays IPv4 and IPv6 information using the ipify.org API.
Team project — REST API + Git Collaboration
"""

import requests
import sys
import json


# ─── Constants ────────────────────────────────────────────────
API_URL_V4  = "https://api.ipify.org?format=json"
API_URL_V6  = "https://api6.ipify.org?format=json"
TIMEOUT_SEC = 10


# ─── Core Functions ───────────────────────────────────────────

def fetch_ip_info(url, timeout=TIMEOUT_SEC):
    """
    Fetch IP information from ipify.org.

    Args:
        url (str): The API endpoint to call.
        timeout (int): Seconds before the request times out.

    Returns:
        dict: Parsed JSON response from the API.

    Raises:
        requests.exceptions.Timeout: If the request times out.
        requests.exceptions.ConnectionError: If no internet connection.
        requests.exceptions.HTTPError: If the server returns an error.
    """
    response = requests.get(url, timeout=timeout)
    response.raise_for_status()
    return response.json()


def format_ip_info(ipv4_data, ipv6_data):
    """
    Format the API responses into a readable string.

    Args:
        ipv4_data (dict): JSON data from the IPv4 endpoint.
        ipv6_data (dict): JSON data from the IPv6 endpoint, or None if unavailable.

    Returns:
        str: A formatted, human-readable summary.
    """
    if not isinstance(ipv4_data, dict):
        return "Error: Invalid data format received."

    ipv6_address = "Not available on this network"
    if isinstance(ipv6_data, dict):
        ipv6_address = ipv6_data.get("ip", "Not available on this network")

    lines = [
        f"{'─' * 40}",
        f"  MY PUBLIC IP INFORMATION",
        f"{'─' * 40}",
        f"  IPv4 Address : {ipv4_data.get('ip', 'N/A')}",
        f"  IPv6 Address : {ipv6_address}",
        f"{'─' * 40}",
    ]
    return "\n".join(lines)


def run_app():
    """
    Main entry point. Calls both APIs, handles errors, and prints results.
    """
    print("\nFetching your IP information...\n")

    # ── Fetch IPv4 (required) ──────────────────────────────────
    try:
        ipv4_data = fetch_ip_info(API_URL_V4)
    except requests.exceptions.Timeout:
        print("Error: The request timed out. Check your internet connection.")
        sys.exit(1)
    except requests.exceptions.ConnectionError:
        print("Error: No internet connection. Please check your network.")
        sys.exit(1)
    except requests.exceptions.HTTPError as e:
        print(f"Error: HTTP error occurred — {e}")
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        print(f"Error: Unexpected network error — {e}")
        sys.exit(1)
    except (json.JSONDecodeError, KeyError) as e:
        print(f"Error: Failed to parse the API response — {e}")
        sys.exit(1)

    # ── Fetch IPv6 (optional — not all networks support it) ────
    ipv6_data = None
    try:
        ipv6_data = fetch_ip_info(API_URL_V6)
    except Exception:
        pass   # IPv6 silently falls back to "Not available on this network"

    # ── Display results ────────────────────────────────────────
    output = format_ip_info(ipv4_data, ipv6_data)
    print(output)


# ─── Script Entry Point ───────────────────────────────────────
if __name__ == "__main__":
    run_app()