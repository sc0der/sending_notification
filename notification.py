import logging
from smtp_mailer import Smtp
from sms_sender import Sms
from data import *
logging.basicConfig(filename='myapp.log', level=logging.DEBUG, 
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger=logging.getLogger(__name__)

purchases = [
    Purchase(id=1, product="Laptop", total_price=200)
]

customers = [
   Customer(uid=1, phone="992123456789", email="test@tj.tj")
]


class SendNotification(object):
    def __init__(self, customer_id, purchase_id):
        self.customer_id = customer_id
        self.purchase_id = purchase_id
        self.__validation

    @property
    def _customer(self):
        for customer in customers:
            if customer.u_id == self.customer_id:
                # str = 'Пользователь с таким id={0} совершил покупку'.format(customer.u_id)
                # print(str)
                return customer
            else:
                logger.error("Unknown user")
                print("Unknown user")
                return None

    @property
    def _purchase(self):
        for purchase in purchases:
            if purchase.id == self.purchase_id:
                # str = 'Товар {0} цена {1}'.format(purchase.product, purchase.price_str )
                # print(str)
                return purchase
            else:
                logger.error("Unknown product")
                print("Unknown product")
                return None

    @property
    def __validation(self):
        if self._customer != None and self._purchase != None:
            return True
        else:
            return False

    def send_nofication(self, flag):
        if self.__validation:
            if flag.lower() == "sms":
                print(self._customer.u_id)
                str = '\n Спасибо за пакупку!!!\n Номер вашего покупки: {0}\n Продукт: {1}\n Стоимость: {2}'.format(self._purchase.id, self._purchase.product, self._purchase.total_price)
                send_sms = Sms(str, self._customer.phone)
                if send_sms=="SUCCESS":
                    success_text = '\n Успех,\n Вы отправили уведомление с помощью  SMS \n Номер заказа: {0}\n ID Клиента: {1}\n Номер телефона: {2}\n email-адресс: {3}'.format(self._purchase.id, self._customer.u_id, self._customer.phone, self._customer.email)
                    print(success_text)
                    return success_text
                else:
                    err_text = 'Ошибка при отправке уведомление по SMS на номер телефона {0}'.format(self._customer.phone)
                    logger.error(err_text)
                    print(err_text)
                    return err_text
            
            elif flag.lower() == "mail":
                    str = '\n Спасибо за пакупку!!!\n Номер вашего покупки: {0}\n Продукт: {1}\n Стоимость: {2}'.format(self._purchase.id, self._purchase.product, self._purchase.total_price)
                    send_mail = Smtp(self._customer.email, str)
                    if send_mail.send_mail() =="SUCCESS":
                        success_text = '\n Успех,\n Вы отправили уведомление с помощью  EMAIL \n Номер заказа: {0}\n ID Клиента: {1}\n Номер телефона: {2}\n email-адресс: {3}'.format(self._purchase.id, self._customer.u_id, self._customer.phone, self._customer.email)
                        return success_text
                    else:
                        err_text = 'Ошибка при отправке уведомление по EMAIL на почту {0}'.format(self._customer.email)
                        logger.error(err_text)
                        print(err_text)
                        return err_text
            else:
                print("Unkcnown type of flag")
                logger.error("Unkcnown type of flag")