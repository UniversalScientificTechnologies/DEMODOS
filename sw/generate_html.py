from rich.console import Console
from rich.panel import Panel
from rich.layout import Layout
from rich.live import Live
from rich.text import Text
import random
import time
import json
import os
import keyboard


class Dozimetr:
    def __init__(self, id, name="Dozimetr"):
        self.id = id
        self.name = name
        self.cps = 95
        self.threshold = 300
        self.noise = True
        self.cluster_counter = 0
        self.total_dose = 0
        self.last_above_threshold = time.time() - 180
        self.last_update_time = time.time()
        self.file_prefix = f"dozimetr_{self.id}"
        self.data = {}
        self.update_required = False

        # Načtení dat ze souboru, pokud existuje
        if os.path.exists(f"{self.file_prefix}.json"):
            with open(f"{self.file_prefix}.json", "r") as f:
                self.data = json.load(f)
                print("Nacitam data z JSON souboru:", self.data)
                self.total_dose = self.data.get("total_dose", 0)
        
        print(self.file_prefix, self.total_dose)

    def generate_data(self):
        heartrate = random.randint(60, 120)

        data =  {
            "cps": self.cps,
            "dose_rate": 0,
            "alert": 0,
            "level": 0,
            "total_dose": 0
        }

        if self.cluster_counter > 0:
            data['cps'] += random.randint(10, 50)
            self.cluster_counter -= 1
        else:
            if random.random() > 0.95:
                self.cluster_counter = random.randint(3, 10)

        data['cps'] = max(0, min(data['cps'], 1000))

        dose_rate = data['cps'] * (0.1 + random.uniform(-0.05,0.05))
        data['alert'] = data['cps'] > self.threshold

        data["total_dose"] += dose_rate / 0.36

        return data

    def update(self, force_update=False):
        """Aktualizace dat, pokud je vyžadována nebo pokud uplynulo 10 sekund."""
        current_time = time.time()
        if current_time - self.last_update_time >= 10 or self.update_required or force_update:
            self.data = self.generate_data()

            if self.noise:
                self.data['cps'] += random.randint(-10, 10)
                self.data['cps'] = max(0, min(self.data['cps'], 1000))

            if self.data['cps'] > self.threshold:
                self.last_above_threshold = time.time()
            elif time.time() - self.last_above_threshold > 180:
                self.data['alert'] = False

            # Uložení aktuálního stavu do JSON souboru
            with open(f"{self.file_prefix}.json", "w") as f:
                json.dump(self.data, f)

            self.last_update_time = current_time
            self.update_required = False  # Reset příznaku aktualizace

    def reset(self):
        """Vynuluje kumulativní dávku."""
        self.total_dose = 0
        self.update_required = True  # Příznak pro vyžádání aktualizace

    def render(self, selected=False):
        title = f" {self.name} {'[bold](Selected)[/bold]' if selected else ''} "
        content_upper = (
            f"[bold]CPS:[/bold] {self.cps}\n"
            f"[bold]Threshold:[/bold] {self.threshold}\n"
            f"[bold]Noise:[/bold] {'On' if self.noise else 'Off'}"
        )

        # Zobrazení všech hodnot, které jsou ukládány do JSON souboru
        content_lower = (
            f"[bold]CPS:[/bold] {self.data.get('cps', 0):.2f} CPS\n"
            f"[bold]Total Dose:[/bold] {self.data.get('total_dose', 0)/10:.2f} mSv\n"
            f"[bold]Dose rate:[/bold] {self.data.get('dose_rate', 0):.2f} uSv/h\n"
            f"[bold]Alert:[/bold] {'Yes' if self.data.get('alert', False) else 'No'}\n"
        )

        separator = "-" * 20
        panel_content = f"{content_upper}\n{separator}\n{content_lower}"

        return Panel(panel_content, title=title, border_style="bold green" if selected else "white")

def main():
    console = Console()
    # Pojmenované dozimetry
    dozimeters = [
        Dozimetr(1, "PAD Aleš"),
        Dozimetr(2, "PAD Matyáš"),
        Dozimetr(3, "PAD Miro")
    ]
    selected_dozimeter = 0

    layout = Layout()

    layout.split_column(
        Layout(name="top", size=4),
        Layout(name="upper"),
        Layout(name="lower", size=4),
    )

    info_text = (
        "Use UP/DOWN to adjust CPS, LEFT/RIGHT to adjust threshold. "
        "'n' to toggle noise, 'r' to reset all, 'Tab' to switch, 'q' to quit."
    )

    with Live(layout, console=console, refresh_per_second=10):
        while True:
            layout["top"].update(
                Panel(
                    Text("SPACEDOS training set", justify="center"), 
                    border_style="bold red"
                )
            )
            
            layout["upper"].split_row(
                Layout(dozimeters[0].render(selected_dozimeter == 0)),
                Layout(dozimeters[1].render(selected_dozimeter == 1)),
                Layout(dozimeters[2].render(selected_dozimeter == 2)),
            )

            layout["lower"].update(
                Panel(
                    Text(info_text, justify="center"),
                    border_style="bold blue",
                )
            )

            # Kontrola klávesových vstupů
            if keyboard.is_pressed("q"):
                break
            elif keyboard.is_pressed("tab"):
                selected_dozimeter = (selected_dozimeter + 1) % len(dozimeters)
                time.sleep(0.1)
            elif keyboard.is_pressed("r"):
                for dozimetr in dozimeters:
                    dozimetr.reset()
                time.sleep(0.2)
            elif keyboard.is_pressed("n"):
                dozimeters[selected_dozimeter].noise = not dozimeters[selected_dozimeter].noise
                dozimeters[selected_dozimeter].update_required = True
                time.sleep(0.2)
            elif keyboard.is_pressed("up"):
                dozimeters[selected_dozimeter].cps += 5
                dozimeters[selected_dozimeter].update_required = True
                time.sleep(0.1)
            elif keyboard.is_pressed("down"):
                dozimeters[selected_dozimeter].cps -= 5
                dozimeters[selected_dozimeter].update_required = True
                time.sleep(0.1)
            elif keyboard.is_pressed("right"):
                dozimeters[selected_dozimeter].threshold += 10
                dozimeters[selected_dozimeter].update_required = True
                time.sleep(0.1)
            elif keyboard.is_pressed("left"):
                dozimeters[selected_dozimeter].threshold -= 10
                dozimeters[selected_dozimeter].update_required = True
                time.sleep(0.1)

            for dozimetr in dozimeters:
                dozimetr.update()

if __name__ == "__main__":
    main()
