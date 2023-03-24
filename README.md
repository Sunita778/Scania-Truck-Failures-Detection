**Project Title:**

*Scania Truck Failures*

**Technologies**

*Machine Learning Technology*

**Domain**

*Transportation*

## Problem Statement:

The Air Pressure System (APS) is a critical component of a heavy-duty vehicle that
uses compressed air to force a piston to provide pressure to the brake pads, slowing
the vehicle down. The benefits of using an APS instead of a hydraulic system are the
easy availability and long-term sustainability of natural air.
This is a Binary Classification problem, in which the affirmative class indicates that the
failure was caused by a certain component of the APS, while the negative class
indicates that the failure was caused by something else.

- *Approach:* The classical machine learning tasks like Data Exploration, Data Cleaning,
Feature Engineering, Model Building and Model Testing. Try out different machine
learning algorithms that’s best fit for the above case.

- *Results:* You have to build a solution that should able to predict whether a failure of a
Scania Truck component is related to the air pressure system (APS) or not.

### Step 1 - Install the requirements

```bash
pip install -r requirements.txt
```

### Step 2 - Run main.py file

```bash
python main.py
```

### Git version

```bash
git -- version
```

To download dataset

```
wget https://raw.githubusercontent.com/Sunita778/aps-fault-detection/main/aps_failure_training_set1.csv
```

## Git commands

If you are starting a project and you want to use git in your project
```
git init
```
Note: This is going to initalize git in your source code.

OR

You can clone exiting github repo
```
git clone <github_url>
```
Note: Clone/ Downlaod github repo in your system

Add your changes made in file to git stagging are
```
git add file_name
```
Note: You can given file_name to add specific file or use "." to add everything to staging are

Create commits
```
git commit -m "message"
```
```
git push origin main
```
Note: origin--> contains url to your github repo main--> is your branch name

To push your changes forcefully.
```
git push origin main -f
```

To pull changes from github repo
```
git pull origin main
```
Note: origin--> contains url to your github repo main--> is your branch name




