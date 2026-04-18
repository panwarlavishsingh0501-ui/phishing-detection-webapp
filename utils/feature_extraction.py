def extract_features(url):
    # Example features for phishing detection
    features = {
        "url_length": len(url),
        "has_https": 1 if url.startswith("https") else 0,
        "contains_at_symbol": 1 if "@" in url else 0,
        "suspicious_words": 1 if any(word in url.lower() for word in ["login", "secure", "bank", "update", "free", "verify"]) else 0
    }
    # Return dict (for template) — model will use values list
    return features
