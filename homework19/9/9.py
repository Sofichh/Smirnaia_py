from сrossnull import Field, Cross, Null
field = Field()
field.show()
vin = 0
while vin != 1:
    null1 = Null()
    cross1 = Cross()
    null1.null(field)
    cross1.cross(field)
    vin += field.check()

