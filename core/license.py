import os
from core.config import BASE_DIR

LICENSE_FILE = os.path.join(BASE_DIR, "license.key")
MOCK_PRO_KEY = "PRO_KEY_123"

def is_pro_active():
    """Check if the local license key is valid for Pro features."""
    if not os.path.exists(LICENSE_FILE):
        return False
    try:
        with open(LICENSE_FILE, 'r') as f:
            key = f.read().strip()
        # For now, evaluate against mock key for simplicity
        return key == MOCK_PRO_KEY
    except Exception:
        return False

def activate_license(key):
    """Save the license key string to disk and verify if it validates."""
    try:
        with open(LICENSE_FILE, 'w') as f:
            f.write(key.strip())
        return is_pro_active()
    except Exception as e:
        print(f"[License] Error saving license: {e}")
        return False

def deactivate_license():
    """Remove the license key file and revert to Free limits."""
    if os.path.exists(LICENSE_FILE):
        try:
            os.remove(LICENSE_FILE)
            return True
        except Exception:
            return False
    return True
