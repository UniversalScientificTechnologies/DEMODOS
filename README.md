# Dosimeter Simulator for Space Missions

This project was developed by [UST](https://www.ust.cz/) in collaboration with the [Institute of Nuclear Physics of the Czech Academy of Sciences](https://ujf.cas.cz) and the [Hydronaut H03 DeepLab](https://hydronaut.eu/). The primary goal is to create a simulator for a remotely controlled Personal Active Dosimeter (PAD) and a Dosimeter Display Unit (DDU) in the form of wristwatches for astronauts.

![EOSR4434](https://github.com/user-attachments/assets/acbfe5dc-d8ca-4c22-b7dc-aa1cb41bda3a)


## Introduction

The Dosimeter Simulator project is designed to support training and practice missions for space flights, specifically for the [Promise mission](https://www.vesmirprolidstvo.cz/cs/aktuality/PROMISE/), taking place in September 2024 at [Little Moon City Prague](https://www.littlemooncity.eu/). This simulator allows mission operators to set and simulate radiation levels that astronauts might encounter during their space missions.

## Solution Description

### Components

1. **Personal Active Dosimeter (PAD)**: A simulated personal dosimeter that monitors and records radiation levels in real-time.
2. **Dosimeter Display Unit (DDU)**: A wristwatch-like display unit worn by astronauts, showing current radiation values measured by the PAD.

## Software

The control software is written in Python and utilizes the `rich` library to provide a clear and efficient interface for setting radiation values on the DDU watches. The mission operator can remotely control the displayed values on both the PAD and DDU, ensuring realistic and dynamic training scenarios.

![obrazek](https://github.com/user-attachments/assets/b746ed27-2748-4429-8d20-bde783a12b54)

### Noise Simulation

To enhance realism, the software adds noise to the simulated data, mimicking the typical behavior of real radiation detectors. This noise arises from the low number of particles detected during the exposure period, a common phenomenon in space radiation measurement.

### Remote Operation

The remote control of the dosimeter was chosen to ensure that trainees are not unnecessarily exposed to artificial radioactive sources during their training. This approach maximizes safety while maintaining the effectiveness of the training exercises.

## PAD - Personal active dosimeter 

![EOSR4449](https://github.com/user-attachments/assets/1ad55b66-e335-4a74-a256-f7421073e868)



## DDU - Dosimeter display unit

![PXL_20240904_150048028](https://github.com/user-attachments/assets/b3888b79-f818-4eb6-a282-9b013ce5907d)
