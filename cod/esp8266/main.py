import time, gc, machine, framebuf, ssd1306, bme280_float
from machine import Pin, SoftI2C
import icons as ic
import wxicons as wi
import tv, network
import net

SWITCH_MS = 15000     # Bildwechsel
OFF_MS = 120000       # 2 min -> Display aus
DEEP_MS = 3600000     # 1 h -> Tiefschlaf
WEATHER_MS = 600000   # Wetter alle 10 min
LONG_MS = 700         # ab hier "lang gedrueckt"
DAYS = ("Mo", "Di", "Mi", "Do", "Fr", "Sa", "So")

oled = ssd1306.SSD1306_I2C(128, 64, SoftI2C(scl=Pin(5), sda=Pin(4)))
bme = bme280_float.BME280(i2c=SoftI2C(scl=Pin(14), sda=Pin(13)))
btn = Pin(12, Pin.IN, Pin.PULL_UP)
bufA = framebuf.FrameBuffer(bytearray(1024), 128, 64, framebuf.MONO_VLSB)
bufB = framebuf.FrameBuffer(bytearray(1024), 128, 64, framebuf.MONO_VLSB)
temp = hum = pres = out = fc = None
scr = 0
hit = False
_last = 0

def _irq(p):
    global hit, _last
    if not hit:
        n = time.ticks_ms()
        if time.ticks_diff(n, _last) > 50:
            hit = True
            _last = n

btn.irq(trigger=Pin.IRQ_FALLING, handler=_irq)

def gesture():
    # 0 = nichts, 1 = kurz (vor), 2 = lang (zurueck)
    global hit
    if not hit:
        return 0
    if btn.value() == 0:
        if time.ticks_diff(time.ticks_ms(), _last) > LONG_MS:
            while btn.value() == 0:
                time.sleep_ms(10)
            time.sleep_ms(30)
            hit = False
            return 2
        return 0
    time.sleep_ms(30)
    hit = False
    return 1

def since(t0):
    return time.ticks_diff(time.ticks_ms(), t0)

def read_sensor():
    global temp, hum, pres
    try:
        t, p, h = bme.read_compensated_data()
        temp, pres, hum = t, p / 100, h
    except OSError:
        pass

def get_weather():
    global out, fc
    r = net.weather() if net.sta.isconnected() else None
    if r:
        out, fc = r
    return r is not None

def mood(tp, hp):
    if hp > 70:
        return "feucht"
    if tp < 18:
        return "kalt"
    if tp > 26:
        return "warm"
    return "angenehm"

def dayname(i, s):
    if i == 0:
        return "Heute"
    y, m, d = int(s[:4]), int(s[5:7]), int(s[8:10])
    return DAYS[time.localtime(time.mktime((y, m, d, 0, 0, 0, 0, 0)))[6]]

def right(d, tp, hp, l2):
    s = str(round(tp))
    k = 3 if len(s) <= 2 else 2
    w = ic.big(d, s, 46, 14, k)
    d.ellipse(46 + w + 3, 15, 2, 2, 1)
    ic.big(d, "C", 46 + w + 8, 14, k)
    d.text("Luft %d%%" % hp, 46, 42)
    d.text(l2, 46, 53)

def inside(d, t):
    d.fill(0)
    d.text("INNEN", 0, 0)
    d.hline(0, 10, 128, 1)
    if temp is None:
        d.text("Sensor?", 36, 30)
        return
    m = mood(temp, hum)
    d.text(m, 128 - len(m) * 8, 0)
    f = {"feucht": ic.drop, "kalt": ic.flake, "warm": ic.sun}.get(m, ic.smile)
    f(d, 22, 36, t)
    right(d, temp, hum, "%d hPa" % pres)

def outside(d, t):
    d.fill(0)
    d.text("OCHSENHAUSEN", 0, 0)
    d.hline(0, 10, 128, 1)
    if out is None:
        d.text("kein Wetter", 24, 30)
        return
    wi.wx(d, out[2], 22, 36, t)
    right(d, out[0], out[1], wi.wx_name(out[2]))

def forecast(d, t):
    d.fill(0)
    d.text("VORSCHAU", 0, 0)
    d.text("max/min", 72, 0)
    d.hline(0, 10, 128, 1)
    if not fc:
        d.text("kein Wetter", 24, 30)
        return
    for i, (ds, c, hi, lo) in enumerate(fc):
        cx = 21 + i * 43
        n = dayname(i, ds)
        d.text(n, cx - len(n) * 4, 14)
        wi.mini(d, c, cx, 33)
        a = "%d" % round(hi)
        b = "%d" % round(lo)
        d.text(a, cx - len(a) * 4, 47)
        d.text(b, cx - len(b) * 4, 56)
    d.vline(42, 13, 50, 1)
    d.vline(85, 13, 50, 1)

def draw(d, s, t):
    (inside, outside, forecast)[s](d, t)

def slide(a, b, k):
    for x in (16, 40, 72, 100, 120, 128):
        oled.fill(0)
        oled.blit(a, -x * k, 0)
        oled.blit(b, (128 - x) * k, 0)
        oled.show()

def go(k):
    global scr
    draw(bufA, scr, 0)
    scr = (scr + k) % 3
    draw(bufB, scr, 0)
    slide(bufA, bufB, k)

def connect_anim():
    n = [0]
    err = [0]
    def frame():
        st = net.sta.status()
        if st == network.STAT_NO_AP_FOUND or st == network.STAT_WRONG_PASSWORD:
            err[0] = st
        oled.fill(0)
        ic.wifi(oled, 64, 40, n[0] % 4)
        oled.text("Verbinde...", 20, 54)
        oled.show()
        n[0] += 1
    ok = net.connect(frame)
    oled.fill(0)
    if ok:
        for i in range(1, 6):
            oled.line(50, 24, 50 + 2 * i, 24 + 2 * i, 1)
            oled.line(51, 24, 51 + 2 * i, 24 + 2 * i, 1)
            oled.show()
            time.sleep_ms(30)
        for i in range(1, 9):
            oled.line(60, 34, 60 + 3 * i, 34 - 3 * i, 1)
            oled.line(61, 34, 61 + 3 * i, 34 - 3 * i, 1)
            oled.show()
            time.sleep_ms(30)
        oled.text("Verbunden!", 24, 54)
    else:
        for i in range(1, 9):
            oled.line(52, 8, 52 + 3 * i, 8 + 3 * i, 1)
            oled.line(53, 8, 53 + 3 * i, 8 + 3 * i, 1)
            oled.show()
            time.sleep_ms(25)
        for i in range(1, 9):
            oled.line(76, 8, 76 - 3 * i, 8 + 3 * i, 1)
            oled.line(77, 8, 77 - 3 * i, 8 + 3 * i, 1)
            oled.show()
            time.sleep_ms(25)
        if err[0] == network.STAT_NO_AP_FOUND:
            a, b = "Netzwerk nicht", "gefunden"
        elif err[0] == network.STAT_WRONG_PASSWORD:
            a, b = "Passwort", "falsch"
        else:
            a, b = "Keine", "Verbindung"
        oled.text(a, 64 - len(a) * 4, 40)
        oled.text(b, 64 - len(b) * 4, 52)
    oled.show()
    time.sleep_ms(800 if ok else 2500)

def deep_sleep():
    global hit
    oled.poweroff()
    net.sta.disconnect()
    net.sta.active(False)
    hit = False
    while not hit:
        machine.idle()
    while btn.value() == 0:
        time.sleep_ms(10)
    time.sleep_ms(50)
    hit = False
    oled.poweron()
    connect_anim()
    read_sensor()
    tv.on(oled, lambda d: draw(d, scr, 0))

connect_anim()
read_sensor()
touch = sw = sens = rec = wea = time.ticks_ms()
wea_wait = 0
off = False
fr = 0

while True:
    g = gesture()
    if g:
        touch = sw = time.ticks_ms()
        if off:
            off = False
            tv.on(oled, lambda d: draw(d, scr, 0))
        elif g == 1:
            go(1)
        else:
            go(-1)
    if since(touch) > DEEP_MS:
        deep_sleep()
        touch = sw = sens = rec = wea = time.ticks_ms()
        wea_wait = 0
        off = False
        continue
    if not off and since(touch) > OFF_MS:
        tv.off(oled, lambda d: draw(d, scr, 0))
        off = True
    if since(sens) > 5000:
        read_sensor()
        sens = time.ticks_ms()
    if since(wea) > wea_wait:
        wea_wait = WEATHER_MS if get_weather() else 60000
        wea = time.ticks_ms()
    if not net.sta.isconnected() and since(rec) > 30000:
        net.reconnect()
        rec = time.ticks_ms()
    if not off:
        if since(sw) > SWITCH_MS:
            go(1)
            sw = time.ticks_ms()
        draw(oled, scr, fr)
        oled.show()
        fr += 1
    gc.collect()
    time.sleep_ms(80)
