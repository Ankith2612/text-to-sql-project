-- transactions table
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY,
    card_number TEXT,
    merchant_id TEXT,
    acquirer_id TEXT,
    issuer_id TEXT,
    amount REAL,
    currency TEXT,
    status TEXT,
    timestamp DATETIME,
    network TEXT
);

-- merchants table
CREATE TABLE IF NOT EXISTS merchants (
    id TEXT PRIMARY KEY,
    name TEXT,
    category TEXT,
    location TEXT
);

-- acquirers table
CREATE TABLE IF NOT EXISTS acquirers (
    id TEXT PRIMARY KEY,
    name TEXT,
    country TEXT
);

-- issuers table
CREATE TABLE IF NOT EXISTS issuers (
    id TEXT PRIMARY KEY,
    name TEXT,
    card_type TEXT
);

-- merchants
INSERT OR IGNORE INTO merchants VALUES ('1HNUHY001LUNMN', 'Walmart', 'Retail', 'Arkansas');
INSERT OR IGNORE INTO merchants VALUES ('2HNUYIOK00OIMM', 'Amazon', 'E-commerce', 'Washington');

-- acquirers
INSERT OR IGNORE INTO acquirers VALUES ('P00001', 'Chase Paymentech', 'USA');
INSERT OR IGNORE INTO acquirers VALUES ('P00002', 'Bank of America Merchant Services', 'USA');

-- issuers
INSERT OR IGNORE INTO issuers VALUES ('B00001', 'Wells Fargo', 'Credit');
INSERT OR IGNORE INTO issuers VALUES ('B00002', 'Citi Bank', 'Debit');

-- transactions
INSERT OR IGNORE INTO transactions VALUES
(1, '****1234', '1HNUHY001LUNMN', 'P00001', 'B00001', 120.50, 'USD', 'approved', '2024-06-01 10:30:00', 'Visa'),
(2, '****5678', '2HNUYIOK00OIMM', 'P00002', 'B00002', 250.00, 'USD', 'declined', '2024-06-02 15:15:00', 'Mastercard');

