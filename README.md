# README

## Overview

This project provides a simple Python script to interact with a Supabase database. It demonstrates how to create a new user entry in a "users" table within the configured Supabase project. 

The script generates a random email and user ID, constructs a user record, and inserts it into the database.

## Features

- **Supabase Integration**: Uses the `supabase-python` library to connect to and interact with a Supabase instance.
- **Randomized User Data**: Generates a random email (using letters) and a unique user ID (UUID) for demonstration purposes.
- **Error Handling**: Includes basic error-handling logic to catch and report any issues during the database operation.

---

## Requirements

### Prerequisites
- Python 3.11.9 or later
- `pip` or other Python package managers

### Installed Python Packages
- Python libraries used in the code: 
  - `supabase`
  - `os`
  - `random`
  - `string`
  - `uuid`

To install the necessary dependencies, you can set up the environment with the following command:

```bash
pip install supabase os random string uuid
```

---

## Configuration

Ensure you configure the following environment variables to connect the script to your Supabase project:
- `SUPABASE_URL`: The Supabase project’s unique URL
- `SUPABASE_KEY`: The Supabase API Key for authenticating requests

Example configuration in your terminal:

```bash
export SUPABASE_URL="your-supabase-url"
export SUPABASE_KEY="your-supabase-key"
```

---

## How It Works

1. **Set Up Supabase Client**:
   The script initializes a Supabase `Client` instance using environment variables for the URL and key.

2. **Generate User Data**:
   Two random values are generated:
   - A random email address with a length of 10 lowercase letters + "@example.com".
   - A unique user ID using Python's `uuid` module.

3. **Insert User Record**:
   The user data is inserted into the `users` table of the connected Supabase database using the `supabase-python` library.

4. **Handle Success/Failure**:
   Once the record is inserted, the script:
   - Prints a success message along with the new user's ID if the operation succeeds.
   - Prints an error message if something goes wrong.

---

## Running the Script

To execute the script, simply run:

```bash
python main.py
```

---

## Example Output

On successful execution, you will receive an output like:
