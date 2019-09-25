# Ecotracker

## Concept

Ecotracker is a web app to be used in tracking fuel purchasing and fuel economy performance of motorized vehicles. Ecotracker was created to make the process organized and easy.

## Features

### Complete (as of 2019-09-25):
1. fuel-up (receipt) record keeping
2. per-vehicle fuel economy tracking (per receipt & overall)

### In development:
1. myGarage overall fuel economy tracking
2. per-vehicle fuel economy tracking (per month, per "trip")
3. XLS/CSV data export to file (download and Google Drive upload)

## How to use

### Intro

Let's start from the conclusion. To calculate fuel economy of your vehicle for any given distance (or, how many miles per gallon your car got) we will need the following pieces of data:
1. miles driven
2. how much fuel was burned (in gallons)

Generally speaking, the fuel gauges in cars are analog and don't output precise volume measurements. In other words, we can't check exactly how much fuel is in a car's tank at any given time. For this reason, accurate fuel consumption measurements must be recorded upon fill-ups. Fuel pumps at gas stations measure the volume of gas purchased down to the thousandths of a gallon.

Many people, when filling up their tanks, do not fill up their tanks completely. This can happen for a few different reasons:
1. payment is upfront, in cash (amount of fuel received depends on arbitrary cash payment)
2. automatic fuelling function of fuel pump does not exist or is out of surface.
3. the tank is manually "topped off" by driver after the automatic fuelling process completes

Whatever the case, the benefits of using Ecotracker are diminished (or possibly negated entirely) by such habits.

#### **Summary:** In order to receive accurate calculations from Ecotracker regarding fuel efficiency (how many miles per gallon your vehicle gets), you must:
1. allow fuel pumps to fill your tanks automatically
2. record during each fill-up the vehicle's number of miles driven since the last fill-up

#### This ensures that every time you fill up, the number of miles driven since your last fill-up corresponds consistently with the number of gallons purchased.
