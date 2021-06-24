import click
from notification import SendNotification

@click.command()
@click.option("--send_by", default="mail", prompt="Укажите способ отправки уведомление",help="Укажите способ отправки уведомление о совершении покупки 'mail' по почте и 'sms' по номеру телефона ")
# @click.option("--/help", help="Укажите способ отправки уведомление о совершении покупки")

def main(send_by):
    notify = SendNotification(customer_id=1, purchase_id=1)
    mess = notify.send_nofication(send_by)
    click.echo(mess)

if __name__ == '__main__':
    main()