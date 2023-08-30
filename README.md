# Bank OLTP

Bank simulator where you can execute common actions around users, accounts, and cards.

## Requirements

Python3 is expected to be installed on the machine. Install the project depedencies with the following command ``pip install -r requirements.txt``.

## Packages

``peewee==3.16.3``


## Usage
---

1. Run the program with the following command
```shell
python main.py
```

2. Predetermined examples of the functionality will run



## Entities
---

The following are entities handled in this system:

### User Entity


```yaml
    id: AutoField
    name: CharField
    email: CharField
    phone: CharField
    age: IntegerField
```

### Account Entity

```yaml
    id: AutoField
    balance: DecimalField
    user_id: ForeignKeyField(User)
```

### Card Entity

```yaml
    card_number: CharField
    account: ForeignKeyField(Account)
    balance: DecimalField
    cvv: CharField
```
