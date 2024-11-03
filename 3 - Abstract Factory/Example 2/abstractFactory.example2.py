from abc import ABC, abstractmethod

class IPaymentGateway(ABC): 
    @abstractmethod
    def process_payment(self, amount):
        pass

class ITransactionLogger(ABC):
    @abstractmethod
    def log_transaction(self, message):
        pass

class IPaymentGatewayFactory(ABC):
    @abstractmethod
    def create_payment_gateway(self):
        pass

    @abstractmethod
    def create_transaction_logger(self):
        pass

class PayPalGateway(IPaymentGateway):
    def process_payment(self, amount):
        print(f"Processing payment of {amount} with PayPal")
        return True

class PayPalTransactionLogger(ITransactionLogger):
    def log_transaction(self, message):
        print(f"Registering transaction in PayPal: {message}")

class StripeGateway(IPaymentGateway): 
    def process_payment(self, amount): 
        print(f"Processing payment of {amount} with Stripe")
        return True  

class StripeTransactionLogger(ITransactionLogger):
    def log_transaction(self, message):
        print(f"Registering transaction in Stripe: {message}")

class PayPalGatewayFactory(IPaymentGatewayFactory):
    def create_payment_gateway(self):
        return PayPalGateway()
    
    def create_transaction_logger(self):
        return PayPalTransactionLogger()

class StripeGatewayFactory(IPaymentGatewayFactory):
    def create_payment_gateway(self):
        return StripeGateway()
    
    def create_transaction_logger(self):
        return StripeTransactionLogger()
    
class PaymentService:
    def __init__(self, payment_gateway_factory):
        self._payment_gateway = payment_gateway_factory.create_payment_gateway()
        self._transaction_logger = payment_gateway_factory.create_transaction_logger()

    def process_payment(self, amount):
            if self._payment_gateway.process_payment(amount):
                self._transaction_logger.log_transaction(f"Payment of {amount} was successful")
            else:
                self._transaction_logger.log_transaction(f"Payment of {amount} failed")


payment_gateway_factory = PayPalGatewayFactory()
payment_service = PaymentService(payment_gateway_factory)

amount = 100.00
payment_service.process_payment(amount)

another_payment_gateway_factory = StripeGatewayFactory()
another_payment_service = PaymentService(another_payment_gateway_factory)
another_payment_service.process_payment(amount)