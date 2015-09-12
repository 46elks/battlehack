CREATE TABLE currencies (
    id SERIAL PRIMARY KEY,
    shortname VARCHAR UNIQUE NOT NULL,
    longname VARCHAR
);

INSERT INTO currencies (shortname, longname) VALUES
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
    currency INTEGER references currencies (id),
    amount INTEGER NOT NULL,
    sender VARCHAR(15),
    recipient INTEGER references users(id)
);
