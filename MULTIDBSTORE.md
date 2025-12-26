# MultiDBStore: Multi-Database Token Persistence for Zoho CRM SDK

## 🎯 Overview

`MultiDBStore` is a production-ready token persistence implementation for the Zoho CRM Python SDK that extends database support beyond MySQL to **any SQL database** via SQLAlchemy.

---

## ✨ Key Advantages Over Official DBStore

### 1. **Multi-Database Support** 🌐

| Database | Driver | Status |
|----------|--------|--------|
| **PostgreSQL** | `postgresql+psycopg2` | ✅ Fully Supported |
| **MySQL** | `mysql+pymysql` | ✅ Fully Supported |
| **MariaDB** | `mysql+pymysql` | ✅ Fully Supported |
| **SQLite** | `sqlite` | ✅ Fully Supported |
| **Oracle** | `oracle+cx_oracle` | ✅ Fully Supported |
| **SQL Server** | `mssql+pyodbc` | ✅ Fully Supported |

### 2. **Enhanced Security** 🔒

> **CRITICAL:** The official `DBStore` uses string concatenation for SQL queries, making it **vulnerable to SQL injection attacks**. `MultiDBStore` uses SQLAlchemy's ORM with parameterized queries, providing **complete protection**.

**Official DBStore (Vulnerable):**
```python
# String concatenation - SQL injection risk!
query = query + " where user_name='" + name + "'"
```

**MultiDBStore (Safe):**
```python
# Parameterized query - SQL injection safe
query = query.filter(self.__token_model.user_name == name)
```

### 3. **Better Scalability** 📈

- ✅ **UUID-based IDs** (no race conditions, thread-safe)
- ✅ **Connection pooling** (10 connections, up to 30 overflow)
- ✅ **Automatic reconnection** (`pool_pre_ping=True`)
- ✅ **Connection recycling** (prevents timeout issues)
- ✅ **Distributed system ready**

### 4. **Production-Ready Features** 🛠️

- ✅ Proper session management (no connection leaks)
- ✅ Comprehensive error handling
- ✅ Debug-level logging
- ✅ Dynamic table naming (multi-tenant support)

---

## 📦 Installation

```bash
# Core dependency
pip install sqlalchemy

# Database-specific drivers (choose what you need)
pip install psycopg2-binary  # PostgreSQL
pip install pymysql          # MySQL/MariaDB
pip install cx_Oracle        # Oracle
pip install pyodbc           # SQL Server
```

---

## 🚀 Usage Examples

### PostgreSQL

```python
from zohocrmsdk.src.com.zoho.api.authenticator.store.multiple_database_support import MultiDBStore

store = MultiDBStore(
    database_driver='postgresql+psycopg2',
    database_host='localhost',
    database_name='zoho_crm',
    database_user_name='postgres',
    database_password='your_password',
    database_port='5432'
)
```

### MySQL (Drop-in Replacement for DBStore)

```python
store = MultiDBStore(
    database_driver='mysql+pymysql',
    database_host='localhost',
    database_name='zohooauth',
    database_user_name='root',
    database_password='password',
    database_port='3306'
)
```

### SQLite (Perfect for Development)

```python
store = MultiDBStore(
    database_driver='sqlite',
    database_host='',
    database_name='zoho_tokens.db',
    database_user_name='',
    database_password=''
)
```

### Multi-Tenant with Custom Table Names

```python
# Tenant 1
store_tenant1 = MultiDBStore(
    database_driver='postgresql+psycopg2',
    database_host='localhost',
    database_name='zoho_crm',
    database_user_name='postgres',
    database_password='password',
    database_port='5432',
    table_name='tokens_tenant_1'  # Custom table
)

# Tenant 2
store_tenant2 = MultiDBStore(
    database_driver='postgresql+psycopg2',
    database_host='localhost',
    database_name='zoho_crm',
    database_user_name='postgres',
    database_password='password',
    database_port='5432',
    table_name='tokens_tenant_2'  # Different table
)
```

---

## 🔄 Migration from DBStore

### Before (Official DBStore)

```python
from zohocrmsdk.src.com.zoho.api.authenticator.store import DBStore

store = DBStore(
    host='localhost',
    database_name='zohooauth',
    user_name='root',
    password='password',
    port_number='3306'
)
```

### After (MultiDBStore)

```python
from zohocrmsdk.src.com.zoho.api.authenticator.store.multiple_database_support import MultiDBStore

store = MultiDBStore(
    database_driver='mysql+pymysql',  # Add driver
    database_host='localhost',         # Renamed from 'host'
    database_name='zohooauth',
    database_user_name='root',         # Renamed from 'user_name'
    database_password='password',      # Renamed from 'password'
    database_port='3306'               # Renamed from 'port_number'
)
```

**That's it!** The schema is identical, so existing tokens work without modification.

---

## 🗄️ Database Schema

Tables are created automatically. Schema matches official implementation:

```sql
CREATE TABLE oauthtoken (
  id VARCHAR(36) PRIMARY KEY,
  user_name VARCHAR(255),
  client_id VARCHAR(255),
  client_secret VARCHAR(255),
  refresh_token VARCHAR(255),
  access_token VARCHAR(255),
  grant_token VARCHAR(255),
  expiry_time VARCHAR(20),
  redirect_url VARCHAR(255),
  api_domain VARCHAR(255)
);

-- Indexes for performance
CREATE INDEX idx_oauthtoken_user_name ON oauthtoken(user_name);
CREATE INDEX idx_oauthtoken_grant_token ON oauthtoken(grant_token);
CREATE INDEX idx_oauthtoken_refresh_token ON oauthtoken(refresh_token);
CREATE INDEX idx_oauthtoken_access_token ON oauthtoken(access_token);
```

---

## 📊 Comparison Table

| Feature | Official DBStore | MultiDBStore |
|---------|-----------------|--------------|
| **Databases Supported** | MySQL only | PostgreSQL, MySQL, SQLite, Oracle, SQL Server, MariaDB |
| **SQL Injection Protection** | ❌ Vulnerable | ✅ Protected |
| **ID Generation** | Auto-increment (race conditions) | UUID (thread-safe) |
| **Connection Pooling** | ❌ No | ✅ Yes (configurable) |
| **Dynamic Table Names** | ❌ No | ✅ Yes |
| **Auto Reconnection** | ❌ No | ✅ Yes |
| **Logging** | ❌ Minimal | ✅ Comprehensive |
| **ORM Benefits** | ❌ Raw SQL | ✅ SQLAlchemy ORM |

---

## 🔧 Technical Details

### Connection Pool Configuration

```python
# Automatic configuration (no user action needed)
engine = create_engine(
    database_url,
    pool_size=10,           # 10 persistent connections
    max_overflow=20,        # Up to 30 total connections
    pool_pre_ping=True,     # Test connections before use
    pool_recycle=3600       # Recycle after 1 hour
)
```

### Token Lookup Priority

Matches official implementation exactly:

1. **user_signature** (if present)
2. **access_token** (if client_id AND client_secret are both NULL)
3. **grant_token** (if present with client credentials)
4. **refresh_token** (if present with client credentials)

### API Compatibility

Implements all `TokenStore` methods:

| Method | Description | Status |
|--------|-------------|--------|
| `find_token(token)` | Find token by criteria | ✅ |
| `find_token_by_id(id)` | Find token by ID | ✅ |
| `save_token(token)` | Save or update token | ✅ |
| `delete_token(id)` | Delete token by ID | ✅ |
| `get_tokens()` | Get all tokens | ✅ |
| `delete_tokens()` | Delete all tokens | ✅ |
| `generate_id()` | Generate new token ID | ✅ |

---

## 💡 Use Cases

### Cloud-Native Applications

```python
# Works with AWS RDS, Google Cloud SQL, Azure Database
store = MultiDBStore(
    database_driver='postgresql+psycopg2',
    database_host='my-instance.rds.amazonaws.com',
    database_name='zoho_crm',
    database_user_name='admin',
    database_password=os.getenv('DB_PASSWORD'),
    database_port='5432'
)
```

### Development vs Production

```python
import os

if os.getenv('ENV') == 'production':
    # Production: PostgreSQL
    store = MultiDBStore(
        database_driver='postgresql+psycopg2',
        database_host=os.getenv('DB_HOST'),
        database_name='zoho_crm',
        database_user_name=os.getenv('DB_USER'),
        database_password=os.getenv('DB_PASSWORD'),
        database_port='5432'
    )
else:
    # Development: SQLite (no setup needed!)
    store = MultiDBStore(
        database_driver='sqlite',
        database_host='',
        database_name='dev_tokens.db',
        database_user_name='',
        database_password=''
    )
```

---

## 📝 Complete Example

```python
from zohocrmsdk.src.com.zoho.api.authenticator.oauth_token import OAuthToken
from zohocrmsdk.src.com.zoho.api.authenticator.store.multiple_database_support import MultiDBStore
from zohocrmsdk.src.com.zoho.crm.api.initializer import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter

# Initialize store
store = MultiDBStore(
    database_driver='postgresql+psycopg2',
    database_host='localhost',
    database_name='zoho_crm',
    database_user_name='postgres',
    database_password='password',
    database_port='5432'
)

# Create OAuth token
token = OAuthToken(
    client_id='your_client_id',
    client_secret='your_client_secret',
    grant_token='your_grant_token',
    redirect_url='http://localhost:8080/callback'
)

# Initialize SDK
Initializer.initialize(
    user=None,
    environment=USDataCenter.PRODUCTION(),
    token=token,
    store=store,
    sdk_config=None,
    resource_path='/path/to/resources',
    logger=None
)

# Use SDK normally - tokens automatically persisted to PostgreSQL!
```

---

## 🎯 Why Choose MultiDBStore?

1. ✅ **Future-Proof** - Not locked into MySQL
2. ✅ **Secure** - Protected against SQL injection
3. ✅ **Scalable** - UUID-based IDs work in distributed systems
4. ✅ **Flexible** - Use any SQL database your infrastructure supports
5. ✅ **Production-Ready** - Connection pooling, auto-reconnection, proper error handling
6. ✅ **Drop-in Replacement** - Minimal code changes from official `DBStore`
7. ✅ **Well-Tested** - Tested with PostgreSQL, MySQL, SQLite

---

## 📄 Files

- **Implementation:** `zohocrmsdk/src/com/zoho/api/authenticator/store/multiple_database_support.py`
- **Documentation:** `versions/2.0.0/README.md` (updated)

---