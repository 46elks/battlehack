CREATE TABLE currencies (
    id VARCHAR(3) PRIMARY KEY,
    name VARCHAR
);

INSERT INTO currencies (id, name) VALUES
    ('SEK', 'svenska kronor'),
    ('USD', 'united states dollars'),
    ('EUR', 'euros');

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    number VARCHAR UNIQUE,
    braintree_id VARCHAR UNIQUE
);

CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    uri VARCHAR NOT NULL UNIQUE,
    datetime TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    currency VARCHAR(3) references currencies (id) DEFAULT 'SEK',
    amount INTEGER NOT NULL,
    sender VARCHAR(15),
    recipient INTEGER references users(id) NOT NULL,
    is_payed BOOLEAN DEFAULT False
);
