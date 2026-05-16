# app/cache.py
import sqlite3
import json
import time
import os

DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'cache.db')
TTL = 60 * 60 * 24  # 24 horas em segundos

def _conexao():
    conn = sqlite3.connect(DB_PATH)
    conn.execute('''
        CREATE TABLE IF NOT EXISTS cache (
            chave TEXT PRIMARY KEY,
            valor TEXT,
            timestamp REAL
        )
    ''')
    conn.commit()
    return conn

def get(chave: str):
    """Busca um valor no cache. Retorna None se não existir ou estiver expirado."""
    conn = _conexao()
    row = conn.execute(
        'SELECT valor, timestamp FROM cache WHERE chave = ?', (chave,)
    ).fetchone()
    conn.close()

    if row is None:
        return None

    valor, timestamp = row
    if time.time() - timestamp > TTL:
        return None  # expirado

    return json.loads(valor)

def set(chave: str, valor):
    """Salva um valor no cache."""
    conn = _conexao()
    conn.execute(
        'INSERT OR REPLACE INTO cache (chave, valor, timestamp) VALUES (?, ?, ?)',
        (chave, json.dumps(valor), time.time())
    )
    conn.commit()
    conn.close()