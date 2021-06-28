import logging
from smtp_mailer import Smtp
from sms_sender import Sms
from models import Purchase, Customer
logging.basicConfig(filename='myapp.log', level=logging.DEBUG, 
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger=logging.getLogger(__name__)

purchases = [
    Purchase(id=1, product="Laptop ACER", total_price=200),
    Purchase(id=2, product="Laptop Asus", total_price=120),
    Purchase(id=3, product="Laptop HP", total_price=250),
    Purchase(id=4, product="Laptop Toshiba", total_price=230),
    Purchase(id=5, product="Laptop Mi Notebook 14", total_price=300)
]

customers = [
   Customer(uid=1, phone="+992501878849", email="test@tj.tj"),
   Customer(uid=2, phone="+992123456789", email="test1@tj.tj"),
   Customer(uid=3, phone="+992123456789", email="test2@tj.tj"),
   Customer(uid=4, phone="+992123456789", email="test3@tj.tj")
]


class SendNotification(object):
    def __init__(self, customer_id, purchase_id):
        self.customer_id = customer_id
        self.purchase_id = purchase_id
        self.__validation

    @property
    def _customer(self):
        customer = list(filter(lambda x: (x.u_id == int(self.customer_id)), customers))
        if(len(customer) > 0):
            mess_text = 'Пользователь с таким id={0} совершил покупку'.format(customer[0].u_id)
            logger.debug(mess_text)
            return customer[0]
        else:
            logger.error("Unknown user")
            return None

    @property
    def _purchase(self):
        purchase = list(filter(lambda x: (x.id == int(self.purchase_id)), purchases))
        if(len(purchase) > 0):
            mess_text = 'Товар {0} цена {1}'.format(purchase[0].product, purchase[0].price_str)
            logger.debug(mess_text)
            return purchase[0]
        else:
            logger.error("Unknown product")
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
                str = '\n Спасибо за пакупку!!!\n Номер вашей покупки: {0}\n Продукт: {1}\n Стоимость: {2}'.format(self._purchase.id, self._purchase.product, self._purchase.total_price)
                send_sms = Sms(str, self._customer.phone)
                if send_sms.send_sms=="SUCCESS":
                    success_text = '\n Успех,\n Вы отправили уведомление с помощью  SMS \n Номер заказа: {0}\n ID Клиента: {1}\n Номер телефона: {2}\n email-адресс: {3}'.format(self._purchase.id, self._customer.u_id, self._customer.phone, self._customer.email)
                    logger.debug(success_text)
                    return success_text
                elif send_sms.send_sms=="FAIL":
                    print("SMS не было отправлено")
                    print("Проблема с SMS verification Service")
                    print("------------------++++-------------")
                    success_text = '\n Успех,\n Вы отправили уведомление с помощью  SMS \n Номер заказа: {0}\n ID Клиента: {1}\n Номер телефона: {2}\n email-адресс: {3}'.format(self._purchase.id, self._customer.u_id, self._customer.phone, self._customer.email)
                    print("SUCCESS TEXT: \n"+success_text)
                    print("------------------++++-------------")
                else:
                    err_text = 'Ошибка при отправке уведомление по SMS на номер телефона {0}'.format(self._customer.phone)
                    logger.error(err_text)
                    return err_text
            
            elif flag.lower() == "mail":
                    str = '\n Спасибо за пакупку!!!\n Номер вашей покупки: {0}\n Продукт: {1}\n Стоимость: {2}'.format(self._purchase.id, self._purchase.product, self._purchase.total_price)
                    send_mail = Smtp(self._customer.email, str)
                    if send_mail.send_mail() =="SUCCESS":
                        success_text = '\n Успех,\n Вы отправили уведомление с помощью  EMAIL \n Номер заказа: {0}\n ID Клиента: {1}\n Номер телефона: {2}\n email-адресс: {3}'.format(self._purchase.id, self._customer.u_id, self._customer.phone, self._customer.email)
                        logger.debug(success_text)
                        return success_text
                    else:
                        err_text = 'Ошибка при отправке уведомление по EMAIL на почту {0}'.format(self._customer.email)
                        logger.error(err_text)
                        return err_text
            else:
                print("Unkcnown type of flag")
                logger.error("Unkcnown type of flag")