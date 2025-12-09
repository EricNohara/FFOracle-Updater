"# FFOracle-Updater

## Overview
The FFOracle-Updater is an automated backend service that manages weekly updates for the FFOracle system. It exposes multiple endpoints that are triggered by AWS timer events to keep the database synchronized with the current NFL season week.

- **Frontend Repository:** https://github.com/EricNohara/Fantasy-Football-Assistant-Manager-Frontend
- **Backend Repository** https://github.com/EricNohara/FFOracle-Backend/
- **Production:** Deployed on AWS Lambda

## Features

### Automated Week Increment
- **Weekly Updates**: Automatically increments the current week in the database
- **Example**: Week 12 → Week 13
- Ensures the system always reflects the current NFL season week

### Architecture

#### Endpoints
The updater exposes **4 different endpoints** on the backend, each designed for specific update operations.

#### AWS Timer Triggers
- Multiple timer triggers are configured in AWS
- Each endpoint has its own dedicated timer trigger
- AWS automatically calls the appropriate timer trigger based on the route
- Enables scheduled, autonomous updates without manual intervention

## How It Works

1. AWS CloudWatch Events (or EventBridge) triggers are set up for each endpoint
2. At scheduled intervals, AWS invokes the corresponding Lambda function endpoint
3. The updater processes the request and updates the database accordingly
4. The system maintains current week information automatically throughout the NFL season" 
