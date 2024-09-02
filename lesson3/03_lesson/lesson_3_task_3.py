from address import Address
from mailing import Mailing

to_address = Address(
    index="123456", city="Moscow", street="Lyublino", house="10", room="12"
)
from_address = Address(
    index="654321", city="St.Petersburg", street="Lenina", house="9", room="66"
)

mailing = Mailing(
    to_address=to_address,
    from_address=from_address,
    cost=1000,
    track="987654321"
)

print(
    f"Отправление {mailing.track} из {mailing.from_address.index}, "
    f"{mailing.from_address.city}, {mailing.from_address.street}, "
    f"{mailing.from_address.house} - {mailing.from_address.room} в "
    f"{mailing.to_address.index}, {mailing.to_address.city}, "
    f"{mailing.to_address.street}, {mailing.to_address.house} - "
    f"{mailing.to_address.room}. Стоимость {mailing.cost} рублей."
)
