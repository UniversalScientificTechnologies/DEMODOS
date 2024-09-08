# SPACEDOS Dosimeter Simulator for Training Missions

This project was developed by [UST](https://www.ust.cz/) in collaboration with the [Institute of Nuclear Physics of the Czech Academy of Sciences](https://ujf.cas.cz) and the [Hydronaut H03 DeepLab](https://hydronaut.eu/). The primary goal is to create a sophisticated simulation system that functions as a remotely controlled [Personal Active Dosimeter (PAD)](https://en.wikipedia.org/wiki/Electronic_personal_dosimeter) and a Dosimeter Display Unit (DDU) designed as wearable wristwatch-like devices for astronauts.

![EOSR4434](https://github.com/user-attachments/assets/acbfe5dc-d8ca-4c22-b7dc-aa1cb41bda3a)

## Introduction

The SPACEDOS demo project is designed to support training and practice missions for space flights, specifically for the [Promise mission](https://www.vesmirprolidstvo.cz/cs/aktuality/PROMISE/), taking place in September 2024 at [Little Moon City Prague](https://www.littlemooncity.eu/). This simulator allows mission operators to set and simulate radiation levels that astronauts might encounter during their space missions.

The main goal of this simulator is to provide a comprehensive tool for complex radiation event exercises. The system is based on the real particle detector-spectrometer [SPACEDOS](https://github.com/UniversalScientificTechnologies/SPACEDOS02), enhancing realism during training. It enables multi-person exercises by simulating hotspots and areas with varying radiation exposure. Each individual sees their specific particle flux and total received dose on their DDU and PAD. This allows for detailed analysis of each participant's behavior in terms of optimizing overall radiation exposure during missions.

**Importantly, this system does not endanger the health of simulation participants, as there is no need to expose them to dangerous radiation. The remote operation ensures that trainees can safely experience realistic scenarios without any actual radiation exposure.**

## Flexibility and Modifiability

It is important to note that the system is highly adaptable and can be modified according to the user's specific requirements. Whether the mission space is large or small, the technology behind this simulator ensures it can be tailored to fit different training environments.

## Safety Considerations

One of the key advantages of this simulator is that it does not endanger the health of participants. Since the system simulates radiation exposure remotely, there is no need to expose trainees to actual dangerous radiation. This ensures that training exercises are safe while still providing realistic and effective learning experiences.

![PXL_20240906_104541024-EDIT](https://github.com/user-attachments/assets/503f4cfc-e8f6-4ec3-b39a-3f0ce3d34f56)


## Solution Description

### Components

1. **Personal Active Dosimeter (PAD)**: A simulated personal dosimeter that monitors and records radiation levels in real-time.
2. **Dosimeter Display Unit (DDU)**: A wristwatch-like display unit worn by astronauts, showing current radiation values measured by the PAD.
3. **Vibration Alert on DDU**: The DDU is equipped with a vibration motor that triggers alerts when preset radiation limits are exceeded. This feature ensures that astronauts are immediately informed of critical situations without distracting them from their mission tasks.
4. **Mission Messaging**: The DDU can also display important mission status messages, ensuring seamless communication with mission control in case of urgent events.

## Software

The control software is written in Python and utilizes the `rich` library to provide a clear and efficient interface for setting radiation values on the DDU watches. The mission operator can remotely control the displayed values on both the PAD and DDU, ensuring realistic and dynamic training scenarios.

![obrazek](https://github.com/user-attachments/assets/b746ed27-2748-4429-8d20-bde783a12b54)

### Noise Simulation

To enhance realism, the software adds noise to the simulated data, mimicking the typical behavior of real radiation detectors. This noise arises from the low number of particles detected during the exposure period, a common phenomenon in space radiation measurement.

### Remote Operation

The remote control of the dosimeter was chosen to ensure that trainees were not unnecessarily exposed to artificial radioactive sources during their training. This approach maximizes safety while maintaining the effectiveness of the training exercises.

The system for the **Promise mission** was designed to operate over a Wi-Fi network covering the entire training area. The system is highly flexible and can be adapted to other technologies depending on the complexity of the mission space.


## PAD - Personal Active Dosimeter 

![EOSR4449](https://github.com/user-attachments/assets/1ad55b66-e335-4a74-a256-f7421073e868)

## DDU - Dosimeter Display Unit

![PXL_20240904_150048028](https://github.com/user-attachments/assets/b3888b79-f818-4eb6-a282-9b013ce5907d)



# Missione Promise

The first application of the system took place during the successful PROMISE training mission in the Hydronaut SpaceLab, attended by Czech ESA reserve astronaut Major Aleš Svoboda, Miro Rozložník, and Matyáš Šanda. In the following photo, the members of the simulation can be seen, along with their training dosimeters and habitat.

![PXL_20240906_113316269](https://github.com/user-attachments/assets/1b40ea9f-2b88-410b-9eb6-cb28a5ac173e)

![obrazek](https://github.com/user-attachments/assets/577bf104-f723-4bd3-977e-e23b2fbb7165)
