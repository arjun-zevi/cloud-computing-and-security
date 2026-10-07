# Program 6: Simulate a cloud scenario using CloudSim and run a scheduling algorithm not present in CloudSim


## Aim
To simulate a cloud scenario using CloudSim and run a scheduling algorithm (Shortest Job First) that is not part of CloudSim.

## Prerequisites
- JDK 8+ and Eclipse
- CloudSim 3.0.3 (download from the CloudSim GitHub releases) unzipped

## Repository contents
```
06-cloudsim-sjf-scheduling/
├── .gitignore
├── README.md
├── code.txt
├── output/output_screenshot.png
├── src/CloudSimExample1_baseline_output.txt
├── src/SJFSchedulingExample.java
```
`code.txt` contains every program/command used, in one plain-text file.

## Procedure
1. Download and unzip CloudSim; open Eclipse and create a new Java project.
2. Import the unpacked CloudSim project / add the `cloudsim-3.0.3.jar` to the build path.
3. Run the bundled `CloudSimExample1` once (baseline - output in `src/CloudSimExample1_baseline_output.txt`).
4. Copy `src/SJFSchedulingExample.java` into package `org.cloudbus.cloudsim.examples` and run it.
5. The program: `CloudSim.init` -> create Datacenter -> create Broker -> create 3 VMs -> create 6 cloudlets -> **sort cloudlets by length (SJF)** -> bind round-robin to VMs -> `CloudSim.startSimulation()` -> print results.

## Expected output
A table of cloudlet ID / status / data-centre / VM / time / start / finish, with shorter cloudlets finishing first on each VM.


## Result
A cloud scenario was simulated and the SJF scheduling algorithm was executed in CloudSim.

