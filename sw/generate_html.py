import curses
import random
import json
import time
import os

threshold = 300


def generate_data(cps, threshold, cluster_counter, total_dose):
    heartrate = random.randint(60, 120)
    
    if cluster_counter > 0:
        cps += random.randint(10, 50)
        cluster_counter -= 1
    else:
        if random.random() > 0.95:
            cluster_counter = random.randint(3, 10)

    cps = max(0, min(cps, 1000))

    dose_rate = cps * (0.1 + random.uniform(-0.05,0.05))

    alert = cps > threshold

    total_dose += dose_rate/3.6

    return {"cps": cps, "dose_rate": dose_rate, "alert": alert, "level": 3, "heartrate": heartrate, "total_dose": total_dose}, cluster_counter

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.timeout(10000)

    global threshold
    cps = 95
    dose_rate = 0
    #threshold = 120
    last_above_threshold = time.time() - 180
    noise = True
    cluster_counter = 0
    last_update_time = time.time()

    # Načtení dat ze souboru, pokud existuje
    if os.path.exists("watchy.json"):
        with open("watchy.json", "r") as f:
            data = json.load(f)
            total_dose = data.get("total_dose", 0)
    else:
        total_dose = 0

    # Inicializace proměnné data s výchozími hodnotami
    data = {"cps": cps, "alert": False, "level": 3, "heartrate": 0, "total_dose": total_dose}
    
    while True:
        key = stdscr.getch()

        if key == curses.KEY_UP:
            cps += 5
        elif key == curses.KEY_DOWN:
            cps -= 5
        elif key == ord('n'):
            noise = not noise
        elif key == ord('q'):
            break

        current_time = time.time()
        if current_time - last_update_time >= 10:
            # Generování dat každých 10 sekund
            data, cluster_counter = generate_data(cps, threshold, cluster_counter, total_dose)
            total_dose = data['total_dose']

            if noise:
                data['cps'] += random.randint(-10, 10)
                data['cps'] = max(0, min(data['cps'], 1000))

            # Hystereze pro alert
            if data['cps'] > threshold:
                last_above_threshold = time.time()
            elif time.time() - last_above_threshold > 180:
                data['alert'] = False

            # Uložení aktuálního stavu do souboru
            with open("watchy.json", "w") as f:
                f.write(json.dumps(data))

            data2 = data
            data2['total_dose'] = int(data2['total_dose'])
            data2['dose_rate'] = int(data2['dose_rate']*10)
            with open("watchy.html", "w") as f:
                f.write(json.dumps(data2))

            last_update_time = current_time
            dose_rate = data['dose_rate']/10.0
        stdscr.clear()
        stdscr.addstr(0, 0, f"CPS: {cps}")
        stdscr.addstr(1, 0, f"Threshold: {threshold}")
        stdscr.addstr(2, 0, f"Noise: {'On' if noise else 'Off'}")
        stdscr.addstr(4, 0, f"Total Dose: {(total_dose/10000):.2f} mSv")
        stdscr.addstr(6, 0, f"Dose rate: {dose_rate:.2f} uSv/h")
        stdscr.addstr(8, 0, f"Data: {json.dumps(data)}")
        stdscr.addstr(10, 0, "Use UP/DOWN to adjust CPS, 'n' to toggle noise, 'q' to quit.")
        stdscr.refresh()

        time.sleep(0.1)

if __name__ == "__main__":
    curses.wrapper(main)
