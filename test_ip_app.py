"""
Unit tests for ip_app.py
Run with:  python -m pytest test_ip_app.py -v
       or: python -m unittest test_ip_app -v
"""

import unittest
from unittest.mock import patch, MagicMock
import requests

from ip_app import fetch_ip_info, format_ip_info


# ─── Sample data to use in tests ──────────────────────────────
SAMPLE_IPV4 = {
    "ip": "203.0.113.42",
}

SAMPLE_IPV6 = {
    "ip": "2001:db8::1",
}


class TestFetchIpInfo(unittest.TestCase):
    """Tests for the fetch_ip_info() function."""

    @patch("ip_app.requests.get")
    def test_successful_fetch_ipv4(self, mock_get):
        """fetch_ip_info() should return a dict on a successful IPv4 call."""
        mock_response = MagicMock()
        mock_response.json.return_value = SAMPLE_IPV4
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        result = fetch_ip_info("https://api.ipify.org?format=json")

        self.assertIsInstance(result, dict)
        self.assertEqual(result["ip"], "203.0.113.42")

    @patch("ip_app.requests.get")
    def test_successful_fetch_ipv6(self, mock_get):
        """fetch_ip_info() should return a dict on a successful IPv6 call."""
        mock_response = MagicMock()
        mock_response.json.return_value = SAMPLE_IPV6
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        result = fetch_ip_info("https://api6.ipify.org?format=json")

        self.assertIsInstance(result, dict)
        self.assertEqual(result["ip"], "2001:db8::1")

    @patch("ip_app.requests.get")
    def test_timeout_raises_exception(self, mock_get):
        """fetch_ip_info() should raise Timeout when the request times out."""
        mock_get.side_effect = requests.exceptions.Timeout

        with self.assertRaises(requests.exceptions.Timeout):
            fetch_ip_info("https://api.ipify.org?format=json")

    @patch("ip_app.requests.get")
    def test_connection_error_raises_exception(self, mock_get):
        """fetch_ip_info() should raise ConnectionError when offline."""
        mock_get.side_effect = requests.exceptions.ConnectionError

        with self.assertRaises(requests.exceptions.ConnectionError):
            fetch_ip_info("https://api.ipify.org?format=json")

    @patch("ip_app.requests.get")
    def test_http_error_raises_exception(self, mock_get):
        """fetch_ip_info() should raise HTTPError on a bad status code."""
        mock_response = MagicMock()
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError
        mock_get.return_value = mock_response

        with self.assertRaises(requests.exceptions.HTTPError):
            fetch_ip_info("https://api.ipify.org?format=json")


class TestFormatIpInfo(unittest.TestCase):
    """Tests for the format_ip_info() function."""

    def test_output_contains_ipv4_address(self):
        """format_ip_info() output should contain the IPv4 address."""
        output = format_ip_info(SAMPLE_IPV4, SAMPLE_IPV6)
        self.assertIn("203.0.113.42", output)

    def test_output_contains_ipv6_address(self):
        """format_ip_info() output should contain the IPv6 address."""
        output = format_ip_info(SAMPLE_IPV4, SAMPLE_IPV6)
        self.assertIn("2001:db8::1", output)

    def test_output_is_string(self):
        """format_ip_info() should always return a string."""
        output = format_ip_info(SAMPLE_IPV4, SAMPLE_IPV6)
        self.assertIsInstance(output, str)

    def test_ipv6_unavailable_shows_fallback(self):
        """format_ip_info() should show fallback message when IPv6 is None."""
        output = format_ip_info(SAMPLE_IPV4, None)
        self.assertIn("Not available", output)

    def test_invalid_ipv4_data_returns_error_string(self):
        """format_ip_info() should handle non-dict IPv4 input gracefully."""
        output = format_ip_info(None, None)
        self.assertIn("Error", output)

    def test_missing_ipv4_field_shows_na(self):
        """format_ip_info() should show N/A for missing IPv4 field."""
        output = format_ip_info({}, None)
        self.assertIn("N/A", output)


if __name__ == "__main__":
    unittest.main()
