import time
import board
import threading
import busio
import adafruit_bme280
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import RPi.GPIO as GPIO
from blink import blink, off

i2c = busio.I2C(board.SCL, board.SDA)
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)
bme280.sea_level_pressure = 1013.25

# Parameters
x_len = 200         # Number of points to display

y1_range = [0, 50]
y2_range = [0, 100]
y3_range = [1000, 1200]

# Create figure for plotting
fig = plt.figure()

# axes
ax1 = fig.add_subplot(3, 1, 1)
ax2 = fig.add_subplot(3, 1, 2)
ax3 = fig.add_subplot(3, 1, 3)

xs = list(range(0, 200))

y1 = [0] * x_len
y2 = [0] * x_len
y3 = [0] * x_len

ax1.set_ylim(y1_range)
ax2.set_ylim(y2_range)
ax3.set_ylim(y3_range)

ax1.set_title("Temperature")
ax2.set_title("Humidity")
ax3.set_title("Pressure")

# Create a blank line. We will update the line in animate
line1, = ax1.plot(xs, y1)
line2, = ax2.plot(xs, y2)
line3, = ax3.plot(xs, y3)

# This function is called periodically from FuncAnimation
def animate(i, y1, y2, y3):

    # Add y to list
    y1.append(bme280.temperature)
    y2.append(bme280.humidity)
    y3.append(bme280.pressure)

    # Limit y list to set number of items
    y1 = y1[-x_len:]
    y2 = y2[-x_len:]
    y3 = y3[-x_len:]

    # Update line with new Y values
    line1.set_ydata(y1)
    line2.set_ydata(y2)
    line3.set_ydata(y3)

    return line1,line2,line3

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig,
    animate,
    fargs=(y1,y2,y3,),
    interval=50,
    blit=True)

def main():
    thread = threading.Thread(target=blink, args=())
    thread.daemon = True
    thread.start()
    plt.show()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        off()
