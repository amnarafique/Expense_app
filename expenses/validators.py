class TopUpValidator:

    @classmethod
    def validate_balance(cls, balance: float) -> bool:
       if not balance:
           return False

       try:
           float(balance)
       except ValueError:
           return False
       return True
