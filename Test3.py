import os
import bcrypt
import psycopg
from typing import Optional, Dict, Any

# Environment variable for secrets
STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY")

def verify_credentials(conn: psycopg.Connection, username: str, plain_password: str) -> Optional[Dict[str, Any]]:
    """Authenticate user with parameterized queries and bcrypt hash verification."""
    clean_username = username.strip().lower()
    
    with conn.cursor() as cur:
        # Secure: Parameterized query prevents SQL injection
        cur.execute(
            "SELECT user_id, hashed_password, role, is_active FROM accounts WHERE username = %s;",
            (clean_username,)
        )
        record = cur.fetchone()
        
        if not record:
            return None
            
        user_id, stored_hash, role, is_active = record
        
        if not is_active:
            return None

        # Secure: Bcrypt verification with salt
        if bcrypt.checkpw(plain_password.encode("utf-8"), stored_hash.encode("utf-8")):
            return {"user_id": user_id, "role": role}
            
        return None
