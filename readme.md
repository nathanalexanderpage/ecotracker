# Ecotracker


## Concept

A web app to organize and simplify the process of tracking fuel purchases and fuel economy performance of motorized vehicless.


## Features

### Complete (as of 2019-09-25):
1. fuel-up (receipt) record keeping
2. per-vehicle fuel economy tracking (per receipt & overall)

### In development:
1. myGarage overall fuel economy tracking
2. per-vehicle fuel economy tracking (per month, overall for user-defined subset of fill-ups such as roadtrip-related)
3. XLS/CSV data export to file (download and Google Drive upload)


## How to use

### Intro

This intro section explains how to ensure the numbers you record will produce accurate measurements for your vehicles' fuel efficiency statistics.

***Warning: without abiding by the guidelines set forth in this section, accurate fuel efficiency statistics can't be obtained!***

In order to calculate fuel economy of your vehicle (how many miles per gallon your car got) for any given distance we will need the following pieces of data:
1. miles driven
2. how much fuel was burned (in gallons)

Generally speaking, the fuel gauges in cars are analog and don't output precise volume measurements. In other words, we can't check exactly how much fuel is in a car's tank at any given time. For this reason, accurate fuel consumption measurements must be recorded upon fill-up. Fuel pumps at gas stations measure the volume of gas purchased down to thousandths of a gallon.

Many people, when filling up their tanks, do not fill up their tanks to a consistent volume level. This can happen for a few different reasons:
1. payment is upfront, in cash (amount of fuel received determined by arbitrary cash payment amount)
2. automatic fuelling function of fuel pump does not exist (pretty unlikely at this point, hopefully)
3. tank is manually "topped off" by driver after the pump's automatic fuelling process completes

*These and similar circumstances severely diminish the benefits of using Ecotracker.*

#### **Summary:** In order to receive accurate calculations from Ecotracker regarding fuel efficiency (how many miles per gallon your vehicle gets), you must:
1. allow fuel pumps to fill your tanks automatically - they will stop pumping when the appropriate amount has been replenished
2. record during each fill-up the vehicle's number of miles driven since its last fill-up

This ensures that every time you fill up, the number of miles driven since your last fill-up corresponds consistently with the number of gallons purchased.

### Record keeping for fuel purchases

For new users, perform the following tasks in order to start keeping track of fuel purchases:
1. Add a vehicle for which you want to keep fuel purchase records
2. Add a fuel station to the system if necessary (fill-up records must be assigned to a fuel station)
3. Add a fill-up record
4. Repeat #2-3 every time you fill up
5. View statistics anytime from your profile to see how fuel-efficient your vehicles are

Instructions for each of the above steps are below.

#### Add vehicle
Use the "add vehicle" form in the 'Vehicle' section

#### Add fuel station (if necessary)
If your fuel station is not present in the list of fuel stations, use the "add fuel station" form in the 'Fuel Station' section

#### Add fill-up (fuel purchase) records
Use the "add fill-up" form in the 'Fill-Up' section

### Fuel economy and other statistics tracking

As a by-product of keeping fuel purchase records, vehicles' fuel efficiency statistics will be automatically calculated -- all you have to do is view them!

#### Viewing statistics

##### Per Vehicle:
Navigate to 'Vehicles'. Choose one of your existing vehicles. Statistics will be present on that vehicle's page once it has fill-up records.

##### Per Fill-Up:
Navigate to 'Fill-Ups'. Choose one of your existing fill-up records. Statistics will be present on that fill-up record's page.