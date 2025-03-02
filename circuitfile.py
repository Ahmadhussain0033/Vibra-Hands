import schemdraw
from schemdraw import elements as elm

# Create a new drawing
with schemdraw.Drawing() as d:
    # Microcontroller (Arduino Nano 33 BLE)
    mcu = d.add(elm.IC(label='Arduino Nano 33 BLE', pins=[
        ('3.3V', '3.3V'), ('GND', 'GND'), ('SDA', 'A4/SDA'),
        ('SCL', 'A5/SCL'), ('MOSI', 'D11'), ('MISO', 'D12'), ('SCK', 'D13')
    ], anchor='W'))

    # IMU (MPU-9250)
    imu = d.add(elm.IC(label='MPU-9250', pins=[
        ('VCC', 'VCC'), ('GND', 'GND'), ('SDA', 'SDA'), ('SCL', 'SCL')
    ], anchor='E', at=(mcu.E[0], mcu.E[1] + 2)))
    d.add(elm.Line().right().at(mcu.E[2]).to(imu.W[2]))  # SDA
    d.add(elm.Line().right().at(mcu.E[3]).to(imu.W[3]))  # SCL

    # Haptic Motor (DRV2605L)
    haptic = d.add(elm.IC(label='DRV2605L', pins=[
        ('VCC', 'VCC'), ('GND', 'GND'), ('SDA', 'SDA'), ('SCL', 'SCL')
    ], anchor='E', at=(imu.E[0], imu.E[1] - 2)))
    d.add(elm.Line().right().at(mcu.E[2]).to(haptic.W[2]))  # SDA
    d.add(elm.Line().right().at(mcu.E[3]).to(haptic.W[3]))  # SCL

    # Wireless Module (NRF24L01)
    wireless = d.add(elm.IC(label='NRF24L01', pins=[
        ('VCC', 'VCC'), ('GND', 'GND'), ('MOSI', 'MOSI'),
        ('MISO', 'MISO'), ('SCK', 'SCK'), ('CSN', 'CSN')
    ], anchor='E', at=(haptic.E[0], haptic.E[1] - 3)))
    d.add(elm.Line().right().at(mcu.E[4]).to(wireless.W[2]))  # MOSI
    d.add(elm.Line().right().at(mcu.E[5]).to(wireless.W[3]))  # MISO
    d.add(elm.Line().right().at(mcu.E[6]).to(wireless.W[4]))  # SCK

    # Battery and Charger (TP4056)
    battery = d.add(elm.Battery(label='LiPo 3.7V', d='down').at(mcu.W[0]).left())
    charger = d.add(elm.IC(label='TP4056', pins=[
        ('B+', 'B+'), ('B-', 'B-'), ('OUT+', 'OUT+'), ('OUT-', 'OUT-')
    ], anchor='W', at=(battery.start[0], battery.start[1] - 3)))
    d.add(elm.Line().down().at(battery.start).to(charger.W[0]))  # B+
    d.add(elm.Line().down().at(battery.end).to(charger.W[1]))    # B-
    d.add(elm.Line().right().at(charger.E[2]).to(mcu.W[0]))      # OUT+ to VCC
    d.add(elm.Line().right().at(charger.E[3]).to(mcu.W[1]))      # OUT- to GND

    # Save the diagram
    d.save('vibra_hands_circuit_diagram.png')
