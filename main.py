import click
from notification import SendNotification

@click.command()
@click.option("--send_by", default="mail", prompt="Укажите способ отправки уведомление", help="Укажите способ отправки уведомление о совершении покупки 'mail' по почте и 'sms' по номеру телефона и 'product'-номер продукта & 'customer'-номер клиента")
@click.option("--customer", default="1", prompt="Укажите номер клиента", help="Укажите способ отправки уведомление о совершении покупки 'mail' по почте и 'sms' по номеру телефона и 'product'-номер продукта & 'customer'-номер клиента")
@click.option("--product", default="1", prompt="Укажите номер продукта", help="Укажите способ отправки уведомление о совершении покупки 'mail' по почте и 'sms' по номеру телефона и 'product'-номер продукта & 'customer'-номер клиента ")

def main(send_by, customer, product):
    notify = SendNotification(customer_id=customer, purchase_id=product)
    purch = notify.send_nofication(send_by)
    click.echo(purch)

if __name__ == '__main__':
    main()