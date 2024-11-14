
class ticket_booking:
    def ticket():
        print('book Ticket')
class w_metro(ticket_booking):
    def trip1():
        print('Water metro trip')
class t_metro(ticket_booking):
    def trip2():
        print('Metro Train Trip')
obj=t_metro
obj.trip2()