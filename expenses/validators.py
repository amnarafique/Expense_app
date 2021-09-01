class TopUpValidator:

    @classmethod
    def validate_balance(cls, balance: float) -> bool:
       return False if not balance else True
