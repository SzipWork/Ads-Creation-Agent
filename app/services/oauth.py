def validate_oauth(token: str):
    if token == "invalid":
        return {
            "error": True,
            "explanation": "Invalid client ID or secret.",
            "action": "Verify OAuth credentials."
        }

    if token == "missing_scope":
        return {
            "error": True,
            "explanation": "Missing Ads permission scope.",
            "action": "Re-authorize with ads scope."
        }

    if token == "expired":
        return {
            "error": True,
            "explanation": "OAuth token expired or revoked.",
            "action": "Re-authenticate."
        }

    if token == "geo_blocked":
        return {
            "error": True,
            "explanation": "TikTok Ads API is geo-restricted.",
            "action": "Use mock API or allowed region."
        }

    return {"error": False}
