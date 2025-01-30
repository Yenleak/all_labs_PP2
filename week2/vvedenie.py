class Car:
    def __init__(audi,model, year, engine):
        audi.model = model
        audi.engine = engine
        audi.year = year
    
    def start_car(audi):
        print(f"{audi.model} with {audi.engine} engine of {audi.year} is started")

    def stop_car(audi):
        print(f"{audi.model} with {audi.engine} engine of {audi.year} is stopped")


audi = Car("Audi A4", 2011, "1.8-litre 20v")

audi.start_car()
audi.stop_car()