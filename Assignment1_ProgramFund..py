from enum import Enum


# Enum for Payment Status
class PaymentStatus(Enum):
    PENDING = "Pending"
    COMPLETED = "Completed"
    FAILED = "Failed"


# Enum for Delivery Methods
class DeliveryMethod(Enum):
    STANDARD = "Standard"
    EXPRESS = "Express"


# Enum for Order Status
class OrderStatusType(Enum):
    PROCESSING = "Processing"
    SHIPPED = "Shipped"
    DELIVERED = "Delivered"
    DELAYED = "Delayed"


# Class Customer
class Customer:
    # Represents a customer placing an order.

    def __init__(self, customer_id, first_name, last_name, phone_number, email, address):
        self.__customer_id = customer_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__phone_number = phone_number
        self.__email = email
        self.__address = address

    # Getter and Setter methods
    def set_customerID(self, customer_id):
        self.__customer_id = customer_id

    def get_customerID(self):
        return self.__customer_id

    def set_firstName(self, first_name):
        self.__first_name = first_name

    def get_firstName(self):
        return self.__first_name

    def set_lastName(self, last_name):
        self.__last_name = last_name

    def get_lastName(self):
        return self.__last_name

    def set_phoneNumber(self, phone_number):
        self.__phone_number = phone_number

    def get_phoneNumber(self):
        return self.__phone_number

    def set_email(self, email):
        self.__email = email

    def get_email(self):
        return self.__email

    def validate_recipient_info(self):
        # Validates the customer's recipient information.
        pass

    def display_customerInfo(self):
        # Displays customer details.
        print(f"Customer: {self.__first_name} {self.__last_name}, Phone: {self.__phone_number}, Email: {self.__email}")


# Class Delivery Order
class DeliveryOrder:
    # Represents an order placed by a customer.

    def __init__(self, order_number, recipient_info, delivery_method, delivery_date, additional_order_details):
        self.__order_number = order_number
        self.__recipient_info = recipient_info
        self.__delivery_method = delivery_method
        self.__delivery_date = delivery_date
        self.__additional_order_details = additional_order_details

    # Getter and Setter methods
    def set_orderNumber(self, order_number):
        self.__order_number = order_number

    def get_orderNumber(self):
        return self.__order_number

    def set_recipientInfo(self, recipient_info):
        self.__recipient_info = recipient_info

    def get_recipientInfo(self):
        return self.__recipient_info

    def set_deliveryMethod(self, delivery_method):
        self.__delivery_method = delivery_method

    def get_deliveryMethod(self):
        return self.__delivery_method

    def set_deliveryDate(self, delivery_date):
        self.__delivery_date = delivery_date

    def get_deliveryDate(self):
        return self.__delivery_date

    def request_additional_order_info(self):
        # Requests additional details for the order if needed.
        pass

    def display_orderDetails(self):
        # Displays delivery order details.
        print(
            f"Order Number: {self.__order_number}, Delivery Date: {self.__delivery_date}, Method: {self.__delivery_method.value}")


# Class Payment
class Payment:
    # Represents payment details for an order.

    def __init__(self, payment_id, payment_method, payment_status, verification_status, transaction_date):
        self.__payment_id = payment_id
        self.__payment_method = payment_method
        self.__payment_status = payment_status
        self.__verification_status = verification_status
        self.__transaction_date = transaction_date

    # Getter and Setter methods
    def set_paymentID(self, payment_id):
        self.__payment_id = payment_id

    def get_paymentID(self):
        return self.__payment_id

    def set_paymentMethod(self, payment_method):
        self.__payment_method = payment_method

    def get_paymentMethod(self):
        return self.__payment_method

    def set_paymentStatus(self, payment_status):
        self.__payment_status = payment_status

    def get_paymentStatus(self):
        return self.__payment_status

    def validate_payment_info(self):
        # Validates payment details before processing.
        pass

    def display_paymentInfo(self):
        # Displays payment details.
        print(f"Payment ID: {self.__payment_id}, Status: {self.__payment_status.value}")


# Class Order Status
class OrderStatus:
    # Represents the tracking status of a delivery order.

    def __init__(self, tracking_number, current_status, expected_delivery_time, last_update_timestamp, delay_notified):
        self.__tracking_number = tracking_number
        self.__current_status = current_status
        self.__expected_delivery_time = expected_delivery_time
        self.__last_update_timestamp = last_update_timestamp
        self.__delay_notified = delay_notified

    # Getter and Setter methods
    def set_trackingNumber(self, tracking_number):
        self.__tracking_number = tracking_number

    def get_trackingNumber(self):
        return self.__tracking_number

    def set_currentStatus(self, current_status):
        self.__current_status = current_status

    def get_currentStatus(self):
        return self.__current_status

    def update_expected_delivery_time(self):
        # Updates the estimated delivery time based on tracking info.
        pass

    def display_deliveryStatus(self):
        # Displays order tracking status.
        print(f"Tracking: {self.__tracking_number}, Status: {self.__current_status.value}")


# Class Delivery Note
class DeliveryNote:
    # Represents the delivery note issued after payment confirmation.

    def __init__(self, delivery_note_id, order_reference, note_details, created_date, email_sent_status):
        self.__delivery_note_id = delivery_note_id
        self.__order_reference = order_reference
        self.__note_details = note_details
        self.__created_date = created_date
        self.__email_sent_status = email_sent_status

    # Getter and Setter methods
    def set_deliveryNoteID(self, delivery_note_id):
        self.__delivery_note_id = delivery_note_id

    def get_deliveryNoteID(self):
        return self.__delivery_note_id

    def generate_delivery_note(self):
        # Generates a unique delivery note for the order.
        pass

    def display_deliveryNote(self):
        # Displays delivery note details.
        print(
            f"Delivery Note ID: {self.__delivery_note_id}, Created: {self.__created_date}, Sent: {self.__email_sent_status}")


# Creating objects for each class
customer1 = Customer("C101", "John", "Doe", "1234567890", "john@example.com", "123 Street, City")
customer2 = Customer("C102", "Jane", "Smith", "9876543210", "jane@example.com", "456 Avenue, Town")

order1 = DeliveryOrder("O2025", "John Doe", DeliveryMethod.EXPRESS, "2025-03-01", "Fragile items")
order2 = DeliveryOrder("O2026", "Jane Smith", DeliveryMethod.STANDARD, "2025-03-02", "Handle with care")

payment1 = Payment("P555", "Credit Card", PaymentStatus.COMPLETED, True, "2025-02-28")
payment2 = Payment("P556", "Debit Card", PaymentStatus.PENDING, False, "2025-02-28")

status1 = OrderStatus("T98765", OrderStatusType.SHIPPED, "2025-03-01", "2025-02-28", False)
status2 = OrderStatus("T98766", OrderStatusType.PROCESSING, "2025-03-03", "2025-02-28", True)

note1 = DeliveryNote("N301", "O2025", "Package in transit", "2025-02-28", True)
note2 = DeliveryNote("N302", "O2026", "Pending dispatch", "2025-02-28", False)

# Display object information
customer1.display_customerInfo()
order1.display_orderDetails()
payment1.display_paymentInfo()
status1.display_deliveryStatus()
note1.display_deliveryNote()
