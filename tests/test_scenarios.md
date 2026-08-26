# UI Test Scenarios

## Test 1 - Successful Critical Dispatch

Input:
- Priority: Critical
- Resource: Ambulance + Doctor
- Specialist: Cardiologist

Expected:
- Dispatch result appears.
- Ambulance ID appears.
- Hospital ID appears.
- Distance and ETA appear.
- Route appears.

## Test 2 - High Priority Request

Input:
- Priority: High

Expected:
- Request is accepted.
- Dispatch result appears.

## Test 3 - Road Closure

Input:
- Road ID: R102
- Action: Close Road

Expected:
- Road closure message appears.

## Test 4 - Road Opening

Input:
- Road ID: R102
- Action: Open Road

Expected:
- Road opening message appears.

## Test 5 - Empty Road ID

Input:
- Road ID: empty

Expected:
- Warning asks for Road ID.
