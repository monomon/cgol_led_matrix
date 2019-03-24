import time
import RPi.GPIO as GPIO
import cgol

SDI = 17
RCLK = 18
SRCLK = 27

clock_interval = 6e-7
shift_interval = 1e-4
frame_interval = 0.04


def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SDI, GPIO.OUT)
    GPIO.setup(RCLK, GPIO.OUT)
    GPIO.setup(SRCLK, GPIO.OUT)
    GPIO.output(SDI, GPIO.LOW)
    GPIO.output(RCLK, GPIO.LOW)
    GPIO.output(SRCLK, GPIO.LOW)


def send_byte(dat):
    for b in range(0, 8):
        GPIO.output(SDI, 0x80 & (dat << b))
        GPIO.output(SRCLK, GPIO.HIGH)
        time.sleep(clock_interval)
        GPIO.output(SRCLK, GPIO.LOW)


def flush():
    GPIO.output(RCLK, GPIO.HIGH)
    time.sleep(shift_interval)
    GPIO.output(RCLK, GPIO.LOW)


def make_row_string(row):
    return reduce(lambda a, c: a + str(c), row, "")

def convert_image_to_788bs_mask(image):
    mask = []
    for i, row in enumerate(image):
        row_bin = int(make_row_string(row), 2)
        mask.append((
            (1 << i) ^ 0xff if row_bin > 0 else 0xff,
            row_bin
        ))
    return mask


def play_leds(initial_grid, count):
    next_grid = initial_grid

    repetitions = int(
            round(frame_interval/float(8*(2*clock_interval + shift_interval))))

    for i in range(count):
        next_grid = cgol.get_next_grid(next_grid)
        next_frame = convert_image_to_788bs_mask(next_grid)
        for j in range(repetitions):
            for line in next_frame:
                send_byte(line[0])
                send_byte(line[1])
                flush()


setup()
grid_size = (8, 8)
if __name__ == "__main__":
    for i in range(3):
        play_leds(cgol.acorn, 30)
    play_leds(cgol.beacon, 30)
    play_leds(cgol.glider, 100)
